---
Title: Installation ohne Docker
Date: 2023-8-19
Order: 2
---

This project is still young and isn't, at the moment, very stable, so please proceed with caution when running in production.

This method of installation is more involved, and therefore is for more experienced admins. **Docker install is the recommended method** as there may not be much support available for Dockerless installation. If you have expertise in this area, we would love your help to improve this documentation!

This install method assumes you already have ssl configured with certificates available.

## Servereinrichtung
- Hole dir eine Domain und konfiguriere DNS für deinen Server. Du musst die Nameserver Deiner Domain bei Deinem DNS-Provider auf den Server verweisen, auf dem du BookWyrm betreibst. Hier sind Anweisungen für [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Setze Deiner Server mit geeigneter Firewall für den Betrieb einer Web-Anwendung auf (dieser Befehlssatz ist mit Ubuntu 20.04 getestet). Hier ist eine Anleitung für [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Richte einen E-Mail-Dienst (wie [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) und die entsprechenden SMTP/DNS-Einstellungen ein. Benutze die Dokumentation des Dienstes für die Konfiguration deines DNS
- Abhängigkeiten installieren. On debian this could look like `apt install postgresql redis nginx python3-venv python3-pip python3-dev libpq-dev gunicorn gettext-base`

## BookWyrm installieren und konfigurieren

Die `-Produktion` Zweig von BookWyrm enthält eine Reihe von Werkzeugen die nicht auf dem `Haupt-` -Zweig sind, die für den Betrieb in der Produktion geeignet sind zum Beispiel `docker-compose` Änderungen, um die Standardbefehle oder die Konfiguration von Containern zu aktualisieren und individuelle Änderungen an der Container-Konfiguration, um Dinge wie SSL oder regelmäßige Sicherungen zu aktivieren. Nicht alle diese Änderungen wirken sich auf die Installation ohne Docker aus, aber der `-production`-Zweig wird immer noch empfohlen

Anleitung für das Ausführen von BookWyrm in Produktion ohne Docker:

- Erstelle und betrete das Verzeichnis, in das Du  BookWyrm installieren willst. Für das Beispiel: `/opt/bookwyrm`: `mkdir /opt/bookwyrm && cd /opt/bookwyrm`
- Get the application code, note that this only clones the `production` branch: `git clone https://github.com/bookwyrm-social/bookwyrm.git --branch production --single-branch ./`
- Create your environment variables file, `cp .env.example .env`, and update the following. Passwords should generally be enclosed in "quotation marks". You can use `bw-dev create_secrets` to generate passwords in `.env`-file:
    - `SECRET_KEY` | A difficult to guess, secret string of characters.
    - `DOMAIN` | Deine Web-Domain
    - `POSTGRES_PASSWORD` | Setze ein sicheres Passwort für die Datenbank
    - `POSTGRES_HOST` | Auf `localhost` (setzen die Maschine auf der Deine Datenbank läuft)
    - `POSTGRES_USER` | Auf `bookwyrm` setzen (empfohlen) oder etwas Eigenes. (später konfiguriert)
    - `POSTGRES_DB` | Auf `Bookwyrm` setzen
    - `REDIS_ACTIVITY_PASSWORD` | Auf nichts setzen (auf einem lokalen Rechner mit einer Firewall)
    - `REDIS_ACTIVITY_HOST` | Auf  `localhost` setzen (die Maschine, auf der  redis läuft)
    - `REDIS_BROKER_PASSWORD` | Auf nichts setzen (auf einem lokalen Rechner mit einer Firewall)
    - `REDIS_BROKER_HOST` | Auf  `localhost` setzen (die Maschine, auf der  redis läuft)
    - `EMAIL_HOST_USER` | Die "von"-Adresse, die deine App beim Senden von E-Mails verwendet
    - `EMAIL_HOST_PASSWORD` | Das Passwort von deinem E-Mail-Dienst
- If you are on Debian and some other operating systems, you may need to create the `/var/cache/nginx` directory:
``` { .sh }
mkdir /var/cache/nginx
chown www-data:www-data /var/cache/nginx
```
- Nginx konfigurieren
    - Copy the server_config to nginx's conf.d: `cp nginx/locations /etc/nginx/conf.d/locations`
    - Update nginx `/etc/nginx/conf.d/locations`:
        - Replace `/app` with your install directory `/opt/bookwyrm` everywhere in the file (including commented out)
    - Make a copy of the production template config and set it for use in nginx:
        - Set env-variables for DOMAIN and MAX_UPLOAD_MiB so envsubst can populate nginx templates. For example `export DOMAIN=your-web-domain MAX_UPLOAD_MiB=100`
        - `envsubst '$DOMAIN,$MAX_UPLOAD_MiB' < nginx/server_config > /etc/nginx/conf.d/server_config`
        - `envsubst '$DOMAIN,$MAX_UPLOAD_MiB' < nginx/server_name > /etc/nginx/conf.d/server_name`
        - `envsubst '$DOMAIN,$MAX_UPLOAD_MiB' < nginx/https.conf > /etc/nginx/sites-available/bookwyrm.conf`
    - If you are running another web-server on your host machine, you should use following command to use nginx as reverse-proxy: `envsubst '$DOMAIN,$MAX_UPLOAD_MiB' < nginx/reverse_proxy.conf > /etc/nginx/sites-available/bookwyrm.conf`
    - Update nginx `/etc/nginx/sites-available/bookwyrm.conf`:
        - Change the `ssl_certificate` and `ssl_certificate_key` paths to your fullchain and privkey locations if you are not using nginx as reverse-proxy
        - Change upstream addresses in lines 4 and 7 to `server localhost:8000` and `server localhost:8888`. Du kannst hier einen anderen Port wählen, wenn du magst
    - Enable the nginx config: `ln -s /etc/nginx/sites-available/bookwyrm.conf /etc/nginx/sites-enabled/bookwyrm.conf`
     - Lade Nginx neu: `systemctl reload nginx`
- Einrichtung der virtuellen Python-Umgebung
    - Make the python venv directory in your install dir: `python3 -m venv ./venv`
    - Installiere die Python-Abhängigkeiten für Bookwyrm via pip mit folgendem Befehl: `./venv/bin/pip3 install -r requirements.txt`
- Erstelle die Bookwyrm PostgreSQL-Datenbank. Make sure to change the password to what you set in the `.env` config: `sudo -i -u postgres psql`

``` { .sql }
CREATE USER bookwyrm WITH PASSWORD 'securedbypassword123';

CREATE DATABASE bookwyrm TEMPLATE template0 ENCODING 'UNICODE';

ALTER DATABASE bookwyrm OWNER TO bookwyrm;

GRANT ALL PRIVILEGES ON DATABASE bookwyrm TO bookwyrm;

\q
```

- Migriere das Datenbankschema, indem du `venv/bin/python3 manage.py migrate`
- Initialisiere die Datenbank, indem du folgenden Befehl ausführst `venv/bin/python3 manage.py initdb`
- Compile the themes by running `venv/bin/python3 manage.py compile_themes`
- Create the static files by running `venv/bin/python3 manage.py collectstatic --no-input`
- Wenn du einen externen Speicher für statische Assets und Mediendateien verwenden möchtest (z. B. einen S3-kompatiblen Dienst), [befolge die Anweisungen](/external-storage.html) bis es dir mitteilt, wieder hierherzukommen
- Erstelle und richte deinen `Bookwyrm` Account ein
    - Erstelle den System-Bookwyrm-Account: `useradd bookwyrm -r`
    - Ändere den Eigentümer deines Installationsverzeichnisses auf bookwyrm: `chown -R bookwyrm:bookwyrm /opt/bookwyrm`
    - Du solltest nun die Befehle welche mit Bookwyrm zu tun haben mit dem Bookwyrm-Benutzer ausführen:   `sudo -u bookwyrm echo I am the $(whoami) user`
- Configure, enable, and start BookWyrm's `systemd` services:
    - Copy the service configurations by running `cp contrib/systemd/*.service /etc/systemd/system/`
    - Enable and start the services with `systemctl enable bookwyrm bookwyrm-worker bookwyrm-scheduler`

- Erstelle den Admin-Code mit `sudo -u bookwyrm venv/bin/python3 manage. y admin_code`, und kopieren Sie den Admin-Code, der beim Erstellen Ihres Admin-Kontos verwendet werden soll.
- Du kannst deinen Code jederzeit erhalten, indem du diesen Befehl erneut ausführst. Hier ist eine Beispielausgabe:

```  { .sh }
*******************************************
Verwende diesen Code um deinen Administratoraccount zu erstellen:
c6c35779-af3a-4091-b330-c026610920d6
*******************************************
```
- The application should now be running at your domain. When you load the domain, you should get a configuration page to confirm your instance settings, and a form to create an admin account. Benutze deinen Admin-Code um dich zu registrieren.

Congrats! You did it!! Configure your instance however you'd like.

## Finding log files

Like all software, BookWyrm can contain bugs, and often these bugs are in the Python code and easiest to reproduce by getting more context from the logs.

If you use the provided `systemd` service configurations from `contrib/systemd` you will be able to read the logs with `journalctl`:

``` { .sh }
# viewing logs of the web process
journalctl -u bookwyrm

# viewing logs of the worker process
journalctl -u bookwyrm-worker

# viewing logs of the scheduler process
journalctl -u bookwyrm-scheduler
```
Feel free to explore additional ways of slicing and dicing logs with flags documented in `journalctl --help`.

While BookWyrm's application logs will most often be enough, you can find logs for other services like Nginx, PostgreSQL, or Redis are usually in `.log` files located somewhere in `/var/logs`.

## Mitmachen

Siehe [Mitmachen](https://joinbookwyrm.com/get-involved/) für Details.
