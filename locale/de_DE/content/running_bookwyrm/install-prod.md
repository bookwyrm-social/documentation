- - -
Title: Installing in Production Date: 2025-04-01 Order: 1
- - -

Dieses Projekt ist noch jung und im Moment nicht sehr stabil und deshalb solltest du bei der Verwendung in Produktion mit Vorsicht vorgehen.

## Servereinrichtung
- Hole einen Domänennamen und konfiguriere DNS für deinen Server. Du musst die Nameserver Ihrer Domain auf deinen DNS-Provider auf den Server verweisen, auf dem BookWyrm läuft. Hier sind Anweisungen für [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Setze den Server mit geeigneten Firewalls für den Betrieb einer Web-Anwendung auf (dieser Befehlssatz ist mit Ubuntu 20.04 getestet). Hier sind Anweisungen für [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Richte einen E-Mail-Dienst (wie [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) und die entsprechenden SMTP/DNS-Einstellungen ein. Benutze die Dokumentation des Dienstes für die Konfiguration des DNS
- [Docker und docker-compose installieren](https://docs.docker.com/compose/install/)

## BookWyrm installieren und konfigurieren

There are several repos in the BookWyrm org, including documentation, a static landing page, and the actual Bookwyrm code. To run BookWyrm, you want the actual app code which is in [bookwyrm-social/bookwyrm](https://github.com/bookwyrm-social/bookwyrm).

Der `-Produktionszweig` von BookWyrm enthält eine Reihe von Werkzeugen die nicht auf dem `main`-Zweig sind, die für den Betrieb in der Produktion geeignet sind zum Beispiel `docker-compose`-Änderungen, um die Standardbefehle oder die Konfiguration von Containern zu aktualisieren und individuelle Änderungen an der Container-Konfiguration, um Dinge wie SSL oder regelmäßige Sicherungen zu aktivieren.

Anleitung für das Ausführen von BookWyrm in der Produktion:

- Hole den Code: `git clone git@github.com:bookwyrm-social/bookwyrm.git`
- Wechsel zum `Produktionszweig`: `git checkout production`
- Erstelle deine Umgebungsvariablendatei `cp .env.example .env` und aktualisiere Folgendes:
    - `DOMAIN` | Deine Webdomain
    - `EMAIL` | E-Mail-Adresse für die Verifizierung der certbot-Domain
    - `FLOWER_USER` | Dein eigener Benutzername für den Zugriff auf den Flower Queue Monitor
    - `EMAIL_HOST_USER` | Die "von"-Adresse, die die App beim Senden von E-Mails verwendet
    - `EMAIL_HOST_PASSWORD` | Das von deinem E-Mail-Dienst bereitgestellte Passwort
- Initialize secrets by running `bw-dev create_secrets` or manually update following in `.env`:
    - `SECRET_KEY` | Eine schwer zu erratende geheime Zeichenfolge
    - `POSTGRES_PASSWORD` | Setze sicheres Passwort für die Datenbank
    - `REDIS_ACTIVITY_PASSWORD` | Setze ein sicheres Passwort für das Redis Activity Subsystem
    - `REDIS_BROKER_PASSWORD` | Setze ein sicheres Passwort für das Redis Queue Broker Subsystem
    - `FLOWER_PASSWORD` | Dein eigenes sicheres Passwort für den Zugriff auf Flower Queue Monitor
    - Wenn du einen anderen Webserver auf deinem Host-Rechner betreibst, musst du den [Reverse-Proxy-Anweisungen](/reverse-proxy.html) folgen
- Setup ssl certificate via letsencrypt by running `./bw-dev init_ssl`
- Initialisiere die Datenbank durch Ausführen von `./bw-dev migrate`
- Run the application with `docker-compose up --build`, and make sure all the images build successfully
    - Wenn du andere Dienste auf deinem Host-Rechner betreibst, kannst du auf Fehler stoßen, dass Dienste fehlschlagen, wenn du versuchst, sich an einen Port zu binden. Siehe die [Fehlerbehebungsanleitung](#port_conflicts) für Hinweise dies zu beheben.
- Wenn Docker erfolgreich gebaut wurde, stoppe den Prozess mit `STRG-C`
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
- `nginx/production.conf` or `nginx/reverse_proxy.conf` depending on NGINX_SETUP in .env-file
- `.env` (Sie erstellen diese Datei selbst während des Setups)

Wenn du bereits einen Webserver auf deinem Rechner betreibst, musst du einen Reverse-Proxy einrichten.

## Verbinde dich

Da BookWyrm ein junges Projekt ist, arbeiten wir noch immer an einem stabilen Veröffentlichungsplan und es gibt viele Fehler und große Änderungen. Es gibt ein GitHub Team, das markiert werden kann, wenn es etwas Wichtiges über ein Update gibt und dem du beitreten kannst, indem du deinen GitHub-Namen teilst. Es gibt einige Möglichkeiten, sich mit uns in Kontakt zu setzen:

 - Open an issue or pull request to add your instance to the [official list](https://joinbookwyrm.com/instances/)
 - Erreiche das Projekt auf [Mastodon](https://tech.lgbt/@bookwyrm) oder [maile den Betreuern](mailto:mousereeve@riseup.net) direkt deinen GitHub-Benutzernamen
 - Trete dem [Matrix](https://matrix.to/#/#bookwyrm:matrix.org) Chatraum bei
