---
Title: Installation ohne Docker
Date: 2022-10-02
Order: 2
---

Dieses Projekt ist noch jung und, im Moment, nicht sehr stabil. Bitte verwende es nur mit Vorsicht in Produktion. Diese Methode der Installation benötigt mehr Können und ist daher für erfahrene Administrator*innen. Docker Installation wird empfohlen Diese Installationsmethode geht davon aus, dass du bereits SSL mit verfügbaren Zertifikaten konfiguriert hast

## Servereinrichtung
- Hole dir eine Domain und konfiguriere DNS für deinen Server. Du musst die Nameserver Deiner Domain bei Deinem DNS-Provider auf den Server verweisen, auf dem du BookWyrm betreibst. Hier sind Anweisungen für [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Setze Deiner Server mit geeigneter Firewall für den Betrieb einer Web-Anwendung auf (dieser Befehlssatz ist mit Ubuntu 20.04 getestet). Hier ist eine Anleitung für [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Richte einen E-Mail-Dienst (wie [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) und die entsprechenden SMTP/DNS-Einstellungen ein. Benutze die Dokumentation des Dienstes für die Konfiguration deines DNS
- Abhängigkeiten installieren. Auf Debian könnte das wie `apt install postgresql redis nginx python3-venv libpq-dev` aussehen.

## BookWyrm installieren und konfigurieren

Die `-Produktion` Zweig von BookWyrm enthält eine Reihe von Werkzeugen die nicht auf dem `Haupt-` -Zweig sind, die für den Betrieb in der Produktion geeignet sind zum Beispiel `docker-compose` Änderungen, um die Standardbefehle oder die Konfiguration von Containern zu aktualisieren und individuelle Änderungen an der Container-Konfiguration, um Dinge wie SSL oder regelmäßige Sicherungen zu aktivieren. Nicht alle diese Änderungen wirken sich auf die Installation ohne Docker aus, aber der `-production`-Zweig wird immer noch empfohlen

Anleitung für das Ausführen von BookWyrm in Produktion ohne Docker:

- Erstelle und betrete das Verzeichnis, in das Du  BookWyrm installieren willst. Für das Beispiel: `/opt/bookwyrm`: `mkdir /opt/bookwyrm && cd /opt/bookwyrm`
- Hole den Quelltext: `git clone git@github.com:bookwyrm-social/bookwyrm.git ./`
- Wechsel in den `production`-zweig: `git checkout production`
- Erstelle deine Umgebungsvariablendatei `cp .env.example .env` und aktualisiere Folgendes:
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
    - `EMAIL_HOST_USER` | Die "von"-Adresse, die deine App beim Senden von E-Mails verwendet
    - `EMAIL_HOST_PASSWORD` | Das Passwort von deinem E-Mail-Dienst
- Nginx konfigurieren
    - Kopiere die server_config nach nginx's conf.d: `cp nginx/server_config /etc/nginx/conf.d/server_config`
    - Erstelle eine Kopie der Konfiguration der Produktionsvorlage und setze sie für die Verwendung in nginx `cp nginx/production nginx/bookwyrm.conf`
    - Aktualisiere nginx `bookwyrm.conf`:
        - Ersetze `your-domain.com` mit deinem Domainnamen überall in der Datei (inklusive der aktuell auskommentierten Zeilen)
        - Ersetze in der Datei überall (inklusive der auskommentierten Zeilen) `/app/` mit deinem Installationsverzeichnis `/opt/bookwyrm/`
        - Zeilen 18 bis 67 auskommentieren, um die Weiterleitung zu HTTPS zu ermöglichen. Du solltest zwei `Server`-Blöcke aktiviert haben
        - Ändere die `ssl_certificate` und `ssl_certificate_key` Pfade an Ihre volle Kette und Privkey Positionen
        - Ändere die Zeile 4 zu folgendem Inhalt: `server localhost:8000`. Du kannst hier einen anderen Port wählen, wenn du magst
        - Wenn du einen anderen Webserver auf deinem Host-Rechner betreibst, musst du den [Reverse-Proxy-Anweisungen](/reverse-proxy.html) folgen
    - Aktiviere die nginx-Konfigurationsdatei mit folgendem Befehl: `ln -s /etc/nginx/sites-available/bookwyrm.conf /etc/nginx/sites-enabled/bookwyrm.conf`
     - Lade Nginx neu: `systemctl reload nginx`
- Einrichtung der virtuellen Python-Umgebung
    - Erstelle den Python venv-Ordner in deinem Installationsverzeichnis: `mkdir venv` `python3 -m venv ./venv`
    - Installiere die Python-Abhängigkeiten für Bookwyrm via pip mit folgendem Befehl: `./venv/bin/pip3 install -r requirements.txt`
- Erstelle die Bookwyrm PostgreSQL-Datenbank. Ändere das Passwort zu dem, welches du in der `.env` Konfiguration gesetzt hast:

    `sudo -i -u postgres psql`

```
CREATE USER bookwyrm WITH PASSWORD 'securedbypassword123';

CREATE DATABASE bookwyrm TEMPLATE template0 ENCODING 'UNICODE';

ALTER DATABASE bookwyrm OWNER TO bookwyrm;

GRANT ALL PRIVILEGES ON DATABASE bookwyrm TO bookwyrm;

\q
```

- Migriere das Datenbankschema, indem du `venv/bin/python3 manage.py migrate`
- Initialisiere die Datenbank, indem du folgenden Befehl ausführst `venv/bin/python3 manage.py initdb`
- Erstelle die Statische durch Ausführen von `venv/bin/python3 manage.py collectstatic --no-input`
- Wenn du einen externen Speicher für statische Assets und Mediendateien verwenden möchtest (z. B. einen S3-kompatiblen Dienst), [befolge die Anweisungen](/external-storage.html) bis es dir mitteilt, wieder hierherzukommen
- Erstelle und richte deinen `Bookwyrm` Account ein
    - Erstelle den System-Bookwyrm-Account: `useradd bookwyrm -r`
    - Ändere den Eigentümer deines Installationsverzeichnisses auf bookwyrm: `chown -R bookwyrm:bookwyrm /opt/bookwyrm`
    - Du solltest nun die Befehle welche mit Bookwyrm zu tun haben mit dem Bookwyrm-Benutzer ausführen:   `sudo -u bookwyrm echo I am the $(whoami) user`

- Erstelle den Admin-Code mit `sudo -u bookwyrm venv/bin/python3 manage. y admin_code`, und kopieren Sie den Admin-Code, der beim Erstellen Ihres Admin-Kontos verwendet werden soll.
- Du kannst deinen Code jederzeit erhalten, indem du diesen Befehl erneut ausführst. Hier ist eine Beispielausgabe:

``` { .sh }
*******************************************
Verwende diesen Code um deinen Administratoraccount zu erstellen:
c6c35779-af3a-4091-b330-c026610920d6
*******************************************
```

- Erstelle und konfiguriere das Startskript
    - Erstelle eine Datei mit dem Namen dockerless-run.sh und füge die folgenden Inhalte ein

``` { .sh }
#!/bin/bash

# Stoppen falls ein Prozess fehlschlägt.
set -e

# bookwyrm
/opt/bookwyrm/venv/bin/gunicorn bookwyrm.wsgi:application --bind 0.0.0.0:8000 &

# celery
/opt/bookwyrm/venv/bin/celery -A celerywyrm worker -l info -Q high_priority,medium_priority,low_priority &
/opt/bookwyrm/venv/bin/celery -A celerywyrm beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler &
# /opt/bookwyrm/venv/bin/celery -A celerywyrm flower &
```
    - Ersetze `/opt/bookwyrm` durch dein Installationsverzeichnis
    - Ändere `8000` auf deine eigene Portnummer
    - Flower wurde hier deaktiviert, da es nicht automatisch mit dem Passwort in der `.env` Datei konfiguriert ist
- Du kannst nun BookWyrm mit folgendem Befehl ausführen: `sudo -u bookwyrm bash /opt/bookwyrm/dockerless-run.sh`
- Die Anwendung sollte auf deiner Domain laufen. Wenn du die Domain lädst, siehst du eine Konfigurationsseite, die deine Instanzeinstellungen bestätigt und ein Formular zum Erstellen eines Administratorkontos. Benutze deinen Admin-Code um dich zu registrieren.
- Möglicherweise möchtest du BookWyrm so konfigurieren, dass es mit einem System-Dienst automatisch ausgeführt wird. Hier ist ein Beispiel:
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
Du musst einen Cron-Job einrichten, damit der Dienst beim Neustart automatisch starten kann.

Glückwunsch! Du hast es geschafft!! Konfigure deine Instanz wie es dir gefällt.

## Mitmachen

Siehe [Mitmachen](https://joinbookwyrm.com/get-involved/) für Details.
