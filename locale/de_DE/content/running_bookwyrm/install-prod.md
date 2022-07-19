- - -
Titel: Installation in Produktion Datum: 2021-05-18 Bestellung: 1
- - -

Dieses Projekt ist noch jung und im Moment nicht sehr stabil und deshalb sollten Sie bei der Verwendung in Produktion mit Vorsicht vorgehen.

## Servereinrichtung
- Holen Sie sich einen Domänennamen und konfigurieren Sie DNS für Ihren Server. Sie müssen die Nameserver Ihrer Domain auf Ihren DNS-Provider auf den Server verweisen, auf dem Sie BookWyrm betreiben. Hier sind Anweisungen für [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Setzen Sie Ihren Server mit geeigneten Firewalls für den Betrieb einer Web-Anwendung auf (dieser Befehlssatz ist mit Ubuntu 20.04 getestet). Hier sind Anweisungen für [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Richten Sie einen E-Mail-Dienst (wie [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) und die entsprechenden SMTP/DNS-Einstellungen ein. Benutzen Sie die Dokumentation des Dienstes für die Konfiguration Ihres DNS
- [Docker und docker-compose installieren](https://docs.docker.com/compose/install/)

## BookWyrm installieren und konfigurieren

Der `-Produktionszweig` von BookWyrm enthält eine Reihe von Werkzeugen die nicht auf dem `main`-Zweig sind, die für den Betrieb in der Produktion geeignet sind zum Beispiel `docker-compose`-Änderungen, um die Standardbefehle oder die Konfiguration von Containern zu aktualisieren und individuelle Änderungen an der Container-Konfiguration, um Dinge wie SSL oder regelmäßige Sicherungen zu aktivieren.

Anleitung für das Ausführen von BookWyrm in der Produktion:

- Erhalten Sie den Anwendungsquellcode: `git clone git@github.com:bookwyrm-social/bookwyrm.git`
- Wechseln Sie zum `Produktionszweig`: `git checkout production`
- Erstellen Sie Ihre Umgebungsvariablendatei `cp .env.example .env` und aktualisieren Sie Folgendes:
    - `SECRET_KEY` | Eine schwer zu erratende geheime Zeichenfolge
    - `DOMAIN` | Ihre Webdomain
    - `EMAIL` | E-Mail-Adresse für die Verifizierung der certbot-Domain
    - `POSTGRES_PASSWORD` | Setzen Sie ein sicheres Passwort für die Datenbank
    - `REDIS_ACTIVITY_PASSWORD` | Setzen Sie ein sicheres Passwort für das Redis Activity Subsystem
    - `REDIS_BROKER_PASSWORD` | Setzen Sie ein sicheres Passwort für das Redis Queue Broker Subsystem
    - `FLOWER_USER` | Ihr eigener Benutzername für den Zugriff auf den Flower Queue Monitor
    - `FLOWER_PASSWORD` | Ihr eigenes sicheres Passwort für den Zugriff auf Flower Queue Monitor
    - `EMAIL_HOST_USER` | Die "von"-Adresse, die Ihre App beim Senden von E-Mails verwendet
    - `EMAIL_HOST_PASSWORD` | Das von Ihrem E-Mail-Dienst bereitgestellte Passwort
- Nginx konfigurieren
    - Erstellen Sie eine Kopie der Konfiguration der Produktionsvorlage und setzen Sie sie für die Verwendung in nginx `cp nginx/production nginx/default.conf`
    - Aktualisiere `nginx/default.conf`:
        - Ersetzen Sie `your-domain.com` mit Ihrem Domain-Namen überall in der Datei (einschließlich der Zeilen, die derzeit auskommentiert sind)
        - Wenn Sie die `www`-Subdomain nicht verwenden, entfernen Sie die www.your-domain.com-Version der Domain aus dem `server_name` im ersten Serverblock in `nginx/default.conf` und entfernen Sie das `-d www.${DOMAIN}`-Flag am Ende des Befehls `certbot` in `docker-compose.yml`.
        - Wenn Sie einen anderen Webserver auf Ihrem Host-Rechner betreiben, müssen Sie den [Reverse-Proxy-Anweisungen](/using-a-reverse-proxy.html) folgen
- Initialisieren Sie die Datenbank durch Ausführen von `./bw-dev migrate`
- Führen Sie die Anwendung aus (dies sollte auch ein Certbot-SSL-Zertifikat für Ihre Domain einrichten) mit `docker-compose up --build` und stellen Sie sicher, dass alle Images erfolgreich erstellt werden
    - Wenn Sie andere Dienste auf Ihrem Host-Rechner betreiben, können Sie auf Fehler stoßen, dass Dienste fehlschlagen, wenn Sie versuchen, sich an einen Port zu binden. See the [troubleshooting guide](#port_conflicts) for advice on resolving this.
- Wenn Docker erfolgreich gebaut wurde, stoppen Sie den Prozess mit `STRG-C`
- HTTPS-Weiterleitung einrichten
    - In `docker-compose.yml` kommentieren Sie den aktiven certbot-Befehl, der das Zertifikat installiert und entfernen Sie die Kommentarzeile unten, die automatische Erneuerungen einstellt.
    - In `nginx/default.conf`entfernen Sie die Kommentarzeilen 18 bis 50, um die Weiterleitung zu HTTPS zu aktivieren. Sie sollten zwei `Server`-Blöcke aktiviert haben
- Richten Sie einen `cron`-Job ein, um Ihre Zertifikate aktuell zu halten (Lets Encrypt-Zertifikate laufen nach 90 Tagen ab)
    - Geben Sie `crontab -e` ein, um Ihre cron-Datei im Host zu bearbeiten
    - fügen Sie eine Zeile zum Erneuern einmal am Tag hinzu: `5 0 * * * cd /path/to/your/bookwyrm && docker-compose run --rm certbot`
- Wenn Sie einen externen Speicher für statische Assets und Mediendateien verwenden möchten (z. B. einen S3-kompatiblen Dienst), [befolgen Sie die Anweisungen](/external-storage.html) bis es Ihnen mitteilt, wieder hierher zu kommen
- Initialisieren Sie die Anwendung mit `./bw-dev setup` und kopieren Sie den Admin-Code, der beim Erstellen Ihres Admin-Kontos verwendet werden soll.
    - Die Ausgabe von `./bw-dev setup` sollte mit Ihrem Admin-Code abgeschlossen werden. Sie können Ihren Code jederzeit erhalten, indem Sie `./bw-dev admin_code` auf der Befehlszeile ausführen. Hier ist eine Beispielausgabe:

``` { .sh }
*******************************************
Use this code to create your admin account:
c6c35779-af3a-4091-b330-c026610920d6
*******************************************
```

- Starten Sie Docker-Compose im Hintergrund mit: `docker-compose up -d`
- Die Anwendung sollte auf Ihrer Domain laufen. Wenn Sie die Domain laden, erhalten Sie eine Konfigurationsseite, die Ihre Instanzeinstellungen bestätigt und ein Formular zum Erstellen eines Administratorkontos. Benutzen Sie Ihren Admin-Code, um sich zu registrieren.

Glückwunsch! Sie haben es geschafft! Konfigurieren Sie Ihre Instanz wie Sie möchten.


## Sicherungskopien

BookWyrms db Service speichert täglich um Mitternacht UTC eine Sicherungskopie seiner Datenbank in sein `/backups`-Verzeichnis. Sicherungen heißen `backup__%Y-%m-%d.sql`.

Der Datenbankdienst hat ein optionales Skript zum periodischen Beschneiden des Backup-Verzeichnisses, so dass alle aktuellen täglichen Sicherungen beibehalten werden, aber für ältere Backups werden nur wöchentliche oder monatliche Backups aufbewahrt. Um dieses Skript zu aktivieren:

- Kommentieren Sie die letzte Zeile in `postgres-docker/cronfile` aus
- bauen Sie Ihre Instanz erneut mit `docker-compose up --build`

Sie können mit `docker cp` Backups aus dem Backup-Volume auf Ihren Host-Rechner kopieren:

- Führen Sie `docker-compose ps` aus, um den vollständigen Namen des Datenbankdienstes zu bestätigen (es ist wahrscheinlich `bookwyrm_db_1`).
- Führen Sie `docker cp <container_name>:/backups <host machine path>` aus

## Port-Konflikte

BookWyrm hat mehrere Dienste, die auf ihren Standard-Ports laufen. Dies bedeutet, dass, je nachdem, was Sie auf Ihrem Host-Rechner laufen haben, können Sie auf Fehler beim Erstellen oder Ausführen von BookWyrm stoßen, wenn Versuche fehlschlagen, sich an diese Ports zu binden.

Wenn dies geschieht, müssen Sie Ihre Konfiguration ändern, um Dienste auf verschiedenen Ports auszuführen. Dies kann eine oder mehrere Änderungen der folgenden Dateien erfordern:

- `docker-compose.yml`
- `nginx/default.conf`
- `.env` (Sie erstellen diese Datei selbst während des Setups)

Wenn Sie bereits einen Webserver auf Ihrem Rechner betreiben, müssen Sie einen Reverse-Proxy einrichten.

## Verbinden Sie sich

Da BookWyrm ein junges Projekt ist, arbeiten wir noch immer an einem stabilen Veröffentlichungsplan und es gibt viele Fehler und große Änderungen. Es gibt ein GitHub Team, das markiert werden kann, wenn es etwas Wichtiges über ein Update gibt und dem du beitreten kannst, indem du deinen GitHub Benutzernamen teilst. Es gibt einige Möglichkeiten, sich mit uns in Kontakt zu setzen:

 - Öffnen Sie ein Problem oder eine Pull-Anfrage, um Ihre Instanz zur [offiziellen Liste](https://github.com/bookwyrm-social/documentation/blob/main/content/using_bookwyrm/instances.md) hinzuzufügen
 - Erreiche das Projekt auf [Mastodon](https://tech.lgbt/@bookwyrm) oder [maile den Betreuern](mailto:mousereeve@riseup.net) direkt deinen GitHub-Benutzernamen
 - Treten Sie dem [Matrix](https://matrix.to/#/#bookwyrm:matrix.org) Chatraum bei
