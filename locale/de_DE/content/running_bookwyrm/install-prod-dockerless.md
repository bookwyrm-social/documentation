---
Title: Installation ohne Docker
Date: 2023-8-19
Order: 2
---

Dieses Projekt ist noch jung und im Moment nicht sehr stabil und deshalb solltest du bei der Verwendung in Produktion mit Vorsicht vorgehen.

Diese Installationsmethode ist komplexer und daher nur für erfahrenere Administrator*innen gedacht. **Die Docker-Installation ist die empfohlene Methode**, weil Unterstützung für die Installation ohne Docker nur eingeschränkt verfügbar ist. Wenn du Expertise in diesem Bereich hast, fänden wir deine Hilfe beim Verbessern dieser Dokumentation großartig!

Diese Installationsmethode setzt voraus, dass du bereits SSL mit gültigen Zertifikaten eingerichtet hast.

## Servereinrichtung
- Hole dir eine Domain und konfiguriere DNS für deinen Server. Du musst die Nameserver deiner Domain bei deinem DNS-Provider auf den Server verweisen lassen, auf dem du BookWyrm betreibst. Hier sind Anweisungen für [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Setze deinen Server mit geeigneter Firewall für den Betrieb einer Web-Anwendung auf (diese Anleitung wurde mit Ubuntu 20.04 getestet). Hier ist eine Anleitung für [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Richte einen E-Mail-Dienst (wie [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) und die entsprechenden SMTP/DNS-Einstellungen ein. Benutze die Dokumentation des Dienstes für die Konfiguration deines DNS
- Installiere die Abhängigkeiten. Unter Debian könnte das so aussehen: `apt install postgresql redis nginx python3-venv python3-pip python3-dev libpq-dev gunicorn gettext-base`

## BookWyrm installieren und konfigurieren

Der `production`-Branch von BookWyrm enthält eine Reihe von Werkzeugen, die nicht auf dem `main`-Branch sind, aber für den Betrieb in der Produktion geeignet sind. Beispiele sind die `docker-compose`-Änderungen, um die Standardbefehle oder die Konfiguration von Containern zu aktualisieren, und individuelle Änderungen an der Container-Konfiguration, um Dinge wie SSL oder regelmäßige Sicherungen zu aktivieren. Nicht alle diese Änderungen wirken sich auf die Installation ohne Docker aus, aber der `production`-Branch wird immer noch empfohlen

Anleitung für das Ausführen von BookWyrm in Produktion ohne Docker:

- Erstelle und betrete das Verzeichnis, in das du BookWyrm installieren willst. Für das Beispiel: `/opt/bookwyrm`: `mkdir /opt/bookwyrm && cd /opt/bookwyrm`
- Lade den Anwendungscode herunter. Bedenke, dass dies nur den `production`-Branch klont: `git clone https://github.com/bookwyrm-social/bookwyrm.git --branch production --single-branch ./`
- Erstelle die Datei mit deinen Umgebungsvariablen mittels `cp .env.example .env`, und ändere folgende Einstellungen. Passwörter sollten generell in "Anführungszeichen" gesetzt werden. Du kannst `bw-dev create_secrets` verwenden, um Passwörter in der `.env`-Datei zu generieren:
    - `SECRET_KEY` | Eine schwer zu erratende, geheime Zeichenkette.
    - `DOMAIN` | Deine Web-Domain
    - `POSTGRES_PASSWORD` | Setze ein sicheres Passwort für die Datenbank
    - `POSTGRES_HOST` | Auf `localhost` setzen (die Maschine, auf der deine Datenbank läuft)
    - `POSTGRES_USER` | Auf `bookwyrm` setzen (empfohlen) oder etwas Eigenes. (später konfiguriert)
    - `POSTGRES_DB` | Auf `Bookwyrm` setzen
    - `REDIS_ACTIVITY_PASSWORD` | Auf nichts setzen (auf einem lokalen Rechner mit einer Firewall)
    - `REDIS_ACTIVITY_HOST` | Auf  `localhost` setzen (die Maschine, auf der  redis läuft)
    - `REDIS_BROKER_PASSWORD` | Auf nichts setzen (auf einem lokalen Rechner mit einer Firewall)
    - `REDIS_BROKER_HOST` | Auf  `localhost` setzen (die Maschine, auf der  redis läuft)
    - `EMAIL_HOST_USER` | Die "von"-Adresse, die deine App beim Senden von E-Mails verwendet
    - `EMAIL_HOST_PASSWORD` | Das Passwort von deinem E-Mail-Dienst
- Wenn du auf Debian oder einigen anderen Betriebssystemen unterwegs bist, kann es sein, dass du das Verzeichnis `/var/cache/nginx` anlegen musst:
``` { .sh }
mkdir /var/cache/nginx
chown www-data:www-data /var/cache/nginx
```
- Nginx konfigurieren
    - Kopiere die `server_config` in Nginx' `conf.d`: `cp nginx/locations /etc/nginx/conf.d/locations`
    - Aktualisiere Nginx' `/etc/nginx/conf.d/locations`:
        - Ersetze `/app` überall in der Datei durch dein Installationsverzeichnis `/opt/bookwyrm` (auskommentierte Bereiche eingeschlossen)
    - Erstelle eine Kopie der Beispiel-Konfiguration für die Produktion und konfiguriere die Verwedung in Nginx:
        - Setze die Umgebungsvariablen für `DOMAIN` und `MAX_UPLOAD_MiB`, damit `envsubst` Nginx-Vorlagen erstellen kann. Beispielsweise `export DOMAIN=your-web-domain MAX_UPLOAD_MiB=100`
        - `envsubst '$DOMAIN,$MAX_UPLOAD_MiB' < nginx/server_config > /etc/nginx/conf.d/server_config`
        - `envsubst '$DOMAIN,$MAX_UPLOAD_MiB' < nginx/server_name > /etc/nginx/conf.d/server_name`
        - `envsubst '$DOMAIN,$MAX_UPLOAD_MiB' < nginx/https.conf > /etc/nginx/sites-available/bookwyrm.conf`
    - Wenn du noch einen anderen Web-Server auf deiner Host-Maschine ausführst, solltest du folgenden Befehl verwenden, um Nginx als deinen Reverse Proxy zu nutzen: `envsubst '$DOMAIN,$MAX_UPLOAD_MiB' < nginx/reverse_proxy.conf > /etc/nginx/sites-available/bookwyrm.conf`
    - Aktualisiere Nginx' `/etc/nginx/sites-available/bookwyrm.conf`:
        - Ändere die Pfade in `ssl_certificate` und `ssl_certificate_key` zu den Orten, an denen deine volle Zertifikatskette und dein privater Schlüssel gespeichert worden sind, wenn du Nginx nicht als Reverse Proxy einsetzt
        - Ändere die Upstream-Adressen in den Zeilen 4 und 7 zu `server localhost:8000` und `server localhost:8888`. Du kannst hier einen anderen Port wählen, wenn du magst
    - Aktiviere die nginx-Konfiguration: `ln -s /etc/nginx/sites-available/bookwyrm.conf /etc/nginx/sites-enabled/bookwyrm.conf`
     - Lade Nginx neu: `systemctl reload nginx`
- Einrichtung der virtuellen Python-Umgebung
    - Lege das Python-venv-Verzeichnis in deinem Installationsverzechnis an: `python3 -m venv ./venv`
    - Installiere die Python-Abhängigkeiten von BookWyrm mit pip: `./venv/bin/pip3 install --upgrade "pip>=25.1.0"` `./venv/bin/pip3 install --group main`
- Erstelle die Bookwyrm-PostgreSQL-Datenbank. Stelle sicher, dass du das Passwort zu dem änderst, das du in deiner `.env`-Konfiguration angegeben hast: `sudo -i -u postgres psql`

``` { .sql }
CREATE USER bookwyrm WITH PASSWORD 'securedbypassword123';

CREATE DATABASE bookwyrm TEMPLATE template0 ENCODING 'UNICODE';

ALTER DATABASE bookwyrm OWNER TO bookwyrm;

GRANT ALL PRIVILEGES ON DATABASE bookwyrm TO bookwyrm;

\q
```

- Migriere das Datenbankschema, indem du `venv/bin/python3 manage.py migrate` ausführst
- Initialisiere die Datenbank, indem du folgenden Befehl ausführst: `venv/bin/python3 manage.py initdb`
- Kompiliere die Themes mit dem Befehl `venv/bin/python3 manage.py compile_themes`
- Erstelle die statischen Dateien mit dem Befehl `venv/bin/python3 manage.py collectstatic --no-input`
- Wenn du einen externen Speicher für statische Assets und Mediendateien verwenden möchtest (z. B. einen S3-kompatiblen Dienst), [befolge diese Anweisungen](/external-storage.html), bis sie dir mitteilen, wieder hierherzukommen
- Erstelle und richte deinen `Bookwyrm`-Account ein
    - Erstelle den System-Bookwyrm-Account: `useradd bookwyrm -r`
    - Ändere den Eigentümer deines Installationsverzeichnisses auf bookwyrm: `chown -R bookwyrm:bookwyrm /opt/bookwyrm`
    - Du solltest nun die Befehle, welche mit Bookwyrm zu tun haben, mit dem Bookwyrm-Konto ausführen:   `sudo -u bookwyrm echo I am the $(whoami) user`
- Konfiguriere, aktiviere und starte BookWyrms `systemd`-Dienste:
    - Kopiere die Dienstkonfigurationen durch folgenden Befehlt: `cp contrib/systemd/*.service /etc/systemd/system/`
    - Aktiviere und starte den Dienst mit `systemctl enable bookwyrm bookwyrm-worker bookwyrm-scheduler`

- Erstelle den Admin-Code mit `sudo -u bookwyrm venv/bin/python3 manage. y admin_code`, und kopiere den Admin-Code, der beim Erstellen deines Admin-Kontos verwendet werden soll.
- Du kannst deinen Code jederzeit erhalten, indem du diesen Befehl erneut ausführst. Hier ist eine Beispielausgabe:

```  { .sh }
*******************************************
Verwende diesen Code um deinen Administratoraccount zu erstellen:
c6c35779-af3a-4091-b330-c026610920d6
*******************************************
```
- Die Anwendung sollte nun unter deiner Domain laufen. Wenn du die Domain aufrufst, solltest du eine Konfigurationsseite sehen, um deine Instanz-Einstellungen zu bestätigen, sowie ein Formular für das Anlegen eines Administrations-Accounts. Benutze deinen Admin-Code, um dich zu registrieren.

Gratulation! Du hast es geschafft!! Richte deine Instanz ganz nach deinen Wünschen ein.

## Log-Dateien finden

Wie alle Software kann BookWyrm Bugs enthalten, und oft verstecken sich diese Bugs im Python-Code. Sie sind am einfachsten zu reproduzieren, wenn wir mehr Kontext aus den Log-Dateien erhalten.

Wenn du die vorgegebenen `systemd`-Dienstkonfigurationen aus `contrib/systemd` verwendest, wirst du die Logs mit `journalctl` auslesen können:

``` { .sh }
# Log-Dateien des Web-Prozesses ansehen
journalctl -u bookwyrm

# Log-Dateien des Worker-Prozesses ansehen
journalctl -u bookwyrm-worker

# Log-Dateien des Scheduler-Prozesses ansehen
journalctl -u bookwyrm-scheduler
```
Erkunde gern weitere Wege, um die Logs mit den Flags aufzuteilen, die in `journalctl --help` angegeben sind.

Auch wenn BookWyrms Anwendungs-Logs oft genügen, kannst du die Logs anderer Dienste wie Nginx, PostgreSQL oder Redis normalerweise in `.log`-Dateien irgendwo in `/var/logs` finden.

## Mitmachen

Siehe [Mitmachen](https://joinbookwyrm.com/get-involved/) für Details.
