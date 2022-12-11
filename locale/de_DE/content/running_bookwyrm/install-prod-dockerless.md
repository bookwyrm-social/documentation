---
Title: Installation ohne Docker
Date: 2022-10-02
Order: 2
---

Dieses Projekt ist noch jung und, im Moment, nicht sehr stabil. Bitte verwende es nur mit Vorsicht in Produktion. Diese Methode der Installation benötigt mehr Können und ist daher für erfahrene Administrator*innen. Docker Installation wird empfohlen Diese Installationsmethode geht davon aus, dass Du bereits SSL mit verfügbaren Zertifikaten konfiguriert hast

## Servereinrichtung
- Holen Dir eine Domain und konfiguriere DNS für Deinen Server. Du musst die Nameserver Deiner Domain bei Deinem DNS-Provider auf den Server verweisen, auf dem Du BookWyrm betreibst. Hier sind Anweisungen für [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Setze Deiner Server mit geeigneter Firewall für den Betrieb einer Web-Anwendung auf (dieser Befehlssatz ist mit Ubuntu 20.04 getestet). Hier ist eine Anleitung für [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Richte einen E-Mail-Dienst (wie [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) und die entsprechenden SMTP/DNS-Einstellungen ein. Benutze die Dokumentation des Dienstes für die Konfiguration Deines DNS
- Abhängigkeiten installieren. On debian this could look like `apt install postgresql redis nginx python3-venv python3-pip python3-dev libpq-dev`

## BookWyrm installieren und konfigurieren

Die `-Produktion` Zweig von BookWyrm enthält eine Reihe von Werkzeugen die nicht auf dem `Haupt-` -Zweig sind, die für den Betrieb in der Produktion geeignet sind zum Beispiel `docker-compose` Änderungen, um die Standardbefehle oder die Konfiguration von Containern zu aktualisieren und individuelle Änderungen an der Container-Konfiguration, um Dinge wie SSL oder regelmäßige Sicherungen zu aktivieren. Nicht alle diese Änderungen wirken sich auf die Installation ohne Docker aus, aber der `-production`-Zweig wird immer noch empfohlen

Anleitung für das Ausführen von BookWyrm in Produktion ohne Docker:

- Erstelle und betrete das Verzeichnis, in das Du  BookWyrm installieren willst. Für das Beispiel: `/opt/bookwyrm`: `mkdir /opt/bookwyrm && cd /opt/bookwyrm`
- Hole den Quelltext: `git clone git@github.com:bookwyrm-social/bookwyrm.git ./`
- Wechsel in den `production`-zweig: `git checkout production`
- Create your environment variables file, `cp .env.example .env`, and update the following:
    - `SECRET_KEY` | Eine schwer zu erratende geheime Zeichenfolge
    - `DOMAIN` | Deine Web-Domain
    - `POSTGRES_PASSWORD` | Setze ein sicheres Passwort für die Datenbank
    - `POSTGRES_HOST` | Auf `localhost` (setzen die Maschine auf der Deine Datenbank läuft)
    - `POSTGRES_USER` | Auf `bookwyrm` setzen (empfohlen) oder etwas Eigenes. (später konfiguriert)
    - `POSTGRES_DB` | Auf `Bookwyrm` setzen
    - `REDIS_ACTIVITY_PASSWORD` | Auf nichts setzen (auf einem lokalen Rechner mit einer Firewall)
    - `REDIS_ACTIVITY_HOST` | Auf  `localhost` setzen (die Maschine, auf der  redis läuft)
    - `REDIS_BROKER_PASSWORD` | Auf nichts setzen (auf einem lokalen Rechner mit einer Firewall)
    - `REDIS_BROKER_HOST` | Auf  `localhost` setzen (die Maschine, auf der  redis läuft)
    - `EMAIL_HOST_USER` | Die "von"-Adresse, die Deine App beim Senden von E-Mails verwendet
    - `EMAIL_HOST_PASSWORD` | Das Passwort von Deinem E-Mail-Dienst
- Nginx konfigurieren
    - Copy the server_config to nginx's conf.d: `cp nginx/server_config /etc/nginx/conf.d/server_config`
    - Make a copy of the production template config and set it for use in nginx: `cp nginx/production /etc/nginx/sites-available/bookwyrm.conf`
    - Aktualisiere nginx `bookwyrm.conf`:
        - Replace `your-domain.com` with your domain name everywhere in the file (including the lines that are currently commented out)
        - Replace `/app/` with your install directory `/opt/bookwyrm/` everywhere in the file (including commented out)
        - Uncomment lines 18 to 67 to enable forwarding to HTTPS. You should have two `server` blocks enabled
        - Change the `ssl_certificate` and `ssl_certificate_key` paths to your fullchain and privkey locations
        - Change line 4 so that it says `server localhost:8000`. Sie können hier einen anderen Port wählen, wenn Sie möchten
        - If you are running another web-server on your host machine, you will need to follow the [reverse-proxy instructions](/reverse-proxy.html)
    - Enable the nginx config: `ln -s /etc/nginx/sites-available/bookwyrm.conf /etc/nginx/sites-enabled/bookwyrm.conf`
     - Reload nginx: `systemctl reload nginx`
- Einrichtung der virtuellen Python-Umgebung
    - Make the python venv directory in your install dir: `mkdir venv` `python3 -m venv ./venv`
    - Install bookwyrm python dependencies with pip: `./venv/bin/pip3 install -r requirements.txt`
- Make the bookwyrm postgresql database. Make sure to change the password to what you set in the `.env` config:

    `sudo -i -u postgres psql`

```
CREATE USER bookwyrm WITH PASSWORD 'securedbypassword123';

CREATE DATABASE bookwyrm TEMPLATE template0 ENCODING 'UNICODE';

ALTER DATABASE bookwyrm OWNER TO bookwyrm;

GRANT ALL PRIVILEGES ON DATABASE bookwyrm TO bookwyrm;

\q
```

- Migrate the database schema by running `venv/bin/python3 manage.py migrate`
- Initialize the database by running `venv/bin/python3 manage.py initdb`
- Create the static by running `venv/bin/python3 manage.py collectstatic --no-input`
- If you wish to use an external storage for static assets and media files (such as an S3-compatible service), [follow the instructions](/external-storage.html) until it tells you to come back here
- Create and setup your `bookwyrm` user
    - Make the system bookwyrm user: `useradd bookwyrm -r`
    - Change the owner of your install directory to bookwyrm: `chown -R bookwyrm:bookwyrm /opt/bookwyrm`
    - You should now run bookwyrm related commands as the bookwyrm user: `sudo -u bookwyrm echo I am the $(whoami) user`

- Generate the admin code with `sudo -u bookwyrm venv/bin/python3 manage.py admin_code`, and copy the admin code to use when you create your admin account.
- You can get your code at any time by re-running that command. Hier ist eine Beispielausgabe:

``` { .sh }
*******************************************
Use this code to create your admin account:
c6c35779-af3a-4091-b330-c026610920d6
*******************************************
```

- Make and configure the run script
    - Make a file called dockerless-run.sh and fill it with the following contents

``` { .sh }
#!/bin/bash

# stop if one process fails
set -e

# bookwyrm
/opt/bookwyrm/venv/bin/gunicorn bookwyrm.wsgi:application --bind 0.0.0.0:8000 &

# celery
/opt/bookwyrm/venv/bin/celery -A celerywyrm worker -l info -Q high_priority,medium_priority,low_priority &
/opt/bookwyrm/venv/bin/celery -A celerywyrm beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler &
# /opt/bookwyrm/venv/bin/celery -A celerywyrm flower &
```
    - Replace `/opt/bookwyrm` with your install dir
    - Ändere `8000` auf deine eigene Portnummer
    - Flower wurde hier deaktiviert, da es nicht automatisch mit dem Passwort in der `.env` Datei konfiguriert ist
- You can now run BookWyrm with: `sudo -u bookwyrm bash /opt/bookwyrm/dockerless-run.sh`
- The application should be running at your domain. When you load the domain, you should get a configuration page which confirms your instance settings, and a form to create an admin account. Use your admin code to register.
- You may want to configure BookWyrm to autorun with a systemd service. Hier ist ein Beispiel:
```
# /etc/systemd/system/bookwyrm.service
[Unit]
Description=Bookwyrm Server
After=network.target
After=systemd-user-sessions.service
After=network-online.target

[Service]
User=bookwyrm
Type=simple
Restart=always
ExecStart=/bin/bash /opt/bookwyrm/dockerless-run.sh
WorkingDirectory=/opt/bookwyrm/

[Install]
WantedBy=multi-user.target
```
You will need to set up a Cron job for the service to start automatically on a server restart.

Glückwunsch! Du hast es geschafft!! Configure your instance however you'd like.

## Mitmachen

Siehe [Mitmachen](https://joinbookwyrm.com/get-involved/) für Details.
