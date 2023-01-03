- - -
Title: Installation in Produktion Date: 2021-05-18 Order: 1
- - -

Dieses Projekt ist noch jung und im Moment nicht sehr stabil und deshalb solltest du bei der Verwendung in Produktion mit Vorsicht vorgehen.

## Servereinrichtung
- Hole einen Domänennamen und konfiguriere DNS für deinen Server. Du musst die Nameserver Ihrer Domain auf deinen DNS-Provider auf den Server verweisen, auf dem BookWyrm läuft. Hier sind Anweisungen für [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Setze den Server mit geeigneten Firewalls für den Betrieb einer Web-Anwendung auf (dieser Befehlssatz ist mit Ubuntu 20.04 getestet). Hier sind Anweisungen für [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Richte einen E-Mail-Dienst (wie [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) und die entsprechenden SMTP/DNS-Einstellungen ein. Benutze die Dokumentation des Dienstes für die Konfiguration des DNS
- [Docker und docker-compose installieren](https://docs.docker.com/compose/install/)

## BookWyrm installieren und konfigurieren

Der `-Produktionszweig` von BookWyrm enthält eine Reihe von Werkzeugen die nicht auf dem `main`-Zweig sind, die für den Betrieb in der Produktion geeignet sind zum Beispiel `docker-compose`-Änderungen, um die Standardbefehle oder die Konfiguration von Containern zu aktualisieren und individuelle Änderungen an der Container-Konfiguration, um Dinge wie SSL oder regelmäßige Sicherungen zu aktivieren.

Anleitung für das Ausführen von BookWyrm in der Produktion:

- Hole den Code: `git clone git@github.com:bookwyrm-social/bookwyrm.git`
- Wechsel zum `Produktionszweig`: `git checkout production`
- Erstelle deine Umgebungsvariablendatei `cp .env.example .env` und aktualisiere Folgendes:
    - `SECRET_KEY` | Eine schwer zu erratende geheime Zeichenfolge
    - `DOMAIN` | Deine Webdomain
    - `EMAIL` | E-Mail-Adresse für die Verifizierung der certbot-Domain
    - `POSTGRES_PASSWORD` | Setze sicheres Passwort für die Datenbank
    - `REDIS_ACTIVITY_PASSWORD` | Setze ein sicheres Passwort für das Redis Activity Subsystem
    - `REDIS_BROKER_PASSWORD` | Setze ein sicheres Passwort für das Redis Queue Broker Subsystem
    - `FLOWER_USER` | Dein eigener Benutzername für den Zugriff auf den Flower Queue Monitor
    - `FLOWER_PASSWORD` | Dein eigenes sicheres Passwort für den Zugriff auf Flower Queue Monitor
    - `EMAIL_HOST_USER` | Die "von"-Adresse, die die App beim Senden von E-Mails verwendet
    - `EMAIL_HOST_PASSWORD` | Das von deinem E-Mail-Dienst bereitgestellte Passwort
- Nginx konfigurieren
    - Erstelle eine Kopie der Konfiguration der Produktionsvorlage und setze sie für die Verwendung in nginx `cp nginx/production nginx/default.conf`
    - Aktualisiere `nginx/default.conf`:
        - Ersetze `your-domain.com` mit deinem Domain-Namen überall in der Datei (einschließlich der Zeilen, die derzeit auskommentiert sind)
        - Wenn du die `www`-Subdomain nicht verwendest, entferne die www.your-domain.com-Version der Domain aus dem `server_name` im ersten Serverblock in `nginx/default.conf` und entferne das `-d www.${DOMAIN}`-Flag am Ende des Befehls `certbot` in `docker-compose.yml`.
        - Wenn du einen anderen Webserver auf deinem Host-Rechner betreibst, musst du den [Reverse-Proxy-Anweisungen](/reverse-proxy.html) folgen
- Initialisiere die Datenbank durch Ausführen von `./bw-dev migrate`
- Führe die Anwendung aus (dies sollte auch ein Certbot-Ssl-Zertifikat für deine Domain einrichten) mit `docker-compose up --build` und stelle sicher, dass alle Images erfolgreich erstellt werden
    - Wenn du andere Dienste auf deinem Host-Rechner betreibst, kannst du auf Fehler stoßen, dass Dienste fehlschlagen, wenn du versuchst, sich an einen Port zu binden. Siehe die [Fehlerbehebungsanleitung](#port_conflicts) für Hinweise dies zu beheben.
- Wenn Docker erfolgreich gebaut wurde, stoppe den Prozess mit `STRG-C`
- HTTPS-Weiterleitung einrichten
    - In `docker-compose.yml` kommentiere den aktiven certbot-Befehl, der das Zertifikat installiert und entfernen die Kommentarzeile unten, die automatische Erneuerungen einstellt.
    - In `nginx/default.conf`entferne die Kommentarzeilen 18 bis 50, um die Weiterleitung zu HTTPS zu aktivieren. Du solltest zwei `Server`-Blöcke aktiviert haben
- Richte einen `cron`-Job ein, um deine Zertifikate aktuell zu halten (Lets Encrypt-Zertifikate laufen nach 90 Tagen ab)
    - Gebe `crontab -e` ein, um die cron-Datei im Host zu bearbeiten
    - fügen eine Zeile zum Erneuern einmal am Tag hinzu: `5 0 * * * cd /path/to/your/bookwyrm && docker-compose run --rm certbot`
- Wenn du einen externen Speicher für statische Assets und Mediendateien verwenden möchtest (z. B. einen S3-kompatiblen Dienst), [befolge die Anweisungen](/external-storage.html) bis es dir mitteilt, wieder hierherzukommen
- Initialisieren die Anwendung mit `./bw-dev setup` und kopiere den Admin-Code, der beim Erstellen deines Admin-Kontos verwendet werden soll.
    - Die Ausgabe von `./bw-dev setup` sollte mit deinem Admin-Code abgeschlossen werden. Du kannst den Code jederzeit erhalten, indem du `./bw-dev admin_code` auf der Befehlszeile ausführst. Hier ist eine Beispielausgabe:

``` { .sh }
*******************************************
Use this code to create your admin account:
c6c35779-af3a-4091-b330-c026610920d6
*******************************************
```

- Starte Docker-Compose im Hintergrund mit: `docker-compose up -d`
- Die Anwendung sollte auf deiner Domain laufen. Wenn du die Domain lädst, erhälst du eine Konfigurationsseite, die deine Instanzeinstellungen bestätigt und ein Formular zum Erstellen eines Administratorkontos. Benutze deinen Admin-Code, um dich zu registrieren.

Glückwunsch! Du hast es geschafft!! Konfigurieren deine Instanz, wie du möchtest.


## Sicherungskopien

BookWyrms db Service speichert täglich um Mitternacht UTC eine Sicherungskopie seiner Datenbank in sein `/backups`-Verzeichnis. Sicherungen heißen `backup__%Y-%m-%d.sql`.

Der Datenbankdienst hat ein optionales Skript zum periodischen Beschneiden des Backup-Verzeichnisses, so dass alle aktuellen täglichen Sicherungen beibehalten werden, aber für ältere Backups werden nur wöchentliche oder monatliche Backups aufbewahrt. Um dieses Skript zu aktivieren:

- Kommentiere die letzte Zeile in `postgres-docker/cronfile` aus
- baue deine Instanz erneut mit `docker-compose up --build`

Du kannst mit `docker cp` Backups aus dem Backup-Volume auf deinen Host-Rechner kopieren:

- Führe `docker-compose ps` aus, um den vollständigen Namen des Datenbankdienstes zu bestätigen (es ist wahrscheinlich `bookwyrm_db_1`.
- Führe `docker cp <container_name>:/backups <host machine path>` aus

## Port-Konflikte

BookWyrm hat mehrere Dienste, die auf ihren Standard-Ports laufen. Dies bedeutet, dass, je nachdem, was auf deinem Host-Rechner läuft, können Sie auf Fehler beim Erstellen oder Ausführen von BookWyrm stoßen, wenn Versuche fehlschlagen, sich an diese Ports zu binden.

Wenn dies geschieht, musst du deine Konfiguration ändern, um Dienste auf verschiedenen Ports auszuführen. Dies kann eine oder mehrere Änderungen der folgenden Dateien erfordern:

- `docker-compose.yml`
- `nginx/default.conf`
- `.env` (Sie erstellen diese Datei selbst während des Setups)

Wenn du bereits einen Webserver auf deinem Rechner betreibst, musst du einen Reverse-Proxy einrichten.

## Verbinde dich

Da BookWyrm ein junges Projekt ist, arbeiten wir noch immer an einem stabilen Veröffentlichungsplan und es gibt viele Fehler und große Änderungen. Es gibt ein GitHub Team, das markiert werden kann, wenn es etwas Wichtiges über ein Update gibt und dem du beitreten kannst, indem du deinen GitHub-Namen teilst. Es gibt einige Möglichkeiten, sich mit uns in Kontakt zu setzen:

 - Öffne ein Issue oder einen Pull Request, um deine Instanz zur [offiziellen Liste](https://github.com/bookwyrm-social/documentation/blob/main/content/using_bookwyrm/instances.md) hinzuzufügen
 - Erreiche das Projekt auf [Mastodon](https://tech.lgbt/@bookwyrm) oder [maile den Betreuern](mailto:mousereeve@riseup.net) direkt deinen GitHub-Benutzernamen
 - Trete dem [Matrix](https://matrix.to/#/#bookwyrm:matrix.org) Chatraum bei
