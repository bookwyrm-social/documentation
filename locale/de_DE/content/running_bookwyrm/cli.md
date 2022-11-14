- - -
Title: Command Line Tool Date: 2021-11-11 Order: 9
- - -

Bookwyrm-Entwickler und Instanz-Manager können das `bw-dev`-Skript für gemeinsame Aufgaben verwenden. Dies macht deine Befehle kürzer, leichter zu merken und schwieriger durcheinander zu bringen.

Sobald Sie Bookwyrm [in Produktion](installing-in-production.html) oder [in Entwicklung](https://docs.joinbookwyrm.com/developer-environment.html#setting_up_the_developer_environment)installiert haben, können Sie das Skript von der Kommandozeile aus mit `./bw-dev` ausführen, gefolgt von dem Unterbefehl, den Sie ausführen wollen.

## Docker Kurzbefehle

### bash

Öffne eine interaktive `bash`-Sitzung im Docker-`Web`-Container.

### build

Äquivalent zu `docker-compose build`.

### dbshell

Öffnen Sie eine interaktive Postgres-Datenbank-Shell. Ich hoffe, Sie wissen, was Sie tun.

### runweb args

Führe einen beliebigen Befehl (oben durch `args` repräsentiert) im `web`-Container aus.

Äquivalent zu `docker-compose run --rm web`.

### service_ports_web args

Führen Sie einen beliebigen Befehl im `Web`-Container (oben dargestellt durch `args`) mit exponierten Ports aus. Dies ist nützlich, wenn du `pdb`-Tests ausführen möchtest, da `runweb` nicht die `pdb`-Prompt freigibt.

Äquivalent zu `docker-compose run --rm --service-ports web`.

### shell

Öffne eine interaktive Django-Shell im Docker-`Web`-Container. Sie würden dies verwenden, wenn Sie Django Shell-Befehle direkt ausführen möchten.

### up [args]

Docker-Container starten oder neustarten, optional inklusive aller Argumente (oben dargestellt durch `args`). Äquivalent zu `docker-compose up --build [args]`

## Datenbank verwalten

### initdb

Eine Datenbank initialisieren.

### makemigrations [appname migration number]

_Dieser Befehl ist nicht verfügbar im `Produktion`szweig_.

Führt Djangos `makemigrations`-Befehl im Docker-Container aus. Wenn Sie die Datenbankstruktur in einem Entwicklungszweig geändert haben, müssen Sie dies ausführen, damit Ihre Änderungen wirksam werden. Optional können Sie eine bestimmte Migration angeben, z.B. `./bw-dev makemigrations bookwyrm 0108`

### migrate

Führt Djangos `migrate`-Kommando im Docker-Container aus. Sie müssen dies immer nach `makemigrations` ausführen.

### resetdb

_Dieser Befehl ist nicht verfügbar im `Produktion`szweig_.

Setzt die Datenbank zurück. **Dieser Befehl löscht Ihre gesamte Bookwyrm-Datenbank**und initiiert dann eine neue Datenbank und führt alle Migrationen aus. Sie sollten alle aktuellen Migrationsdateien löschen, die Sie nicht ausführen möchten, _bevor_ das `resetdb` ausgeführt wird.

## Eine Bookwyrm-Instanz verwalten

### collectstatic

Migrieren Sie statische Assets in einen Docker-Container oder in einen S3-kompatiblen "Bucket", abhängig vom Kontext.

### generate_preview_images

Erzeugen von Vorschaubildern für Webseiten, Benutzer und Bücher. Dies kann eine Weile dauern, wenn Sie eine große Datenbank haben.

### generate_thumbnails

Erzeugt Miniaturbilder für Buchtitelbilder.

### populate_streams args

Baut den Redis Stream (Benutzer-Feeds) neu auf. Sie müssen dies normalerweise nicht ausführen, es sei denn, es gibt einen Fehler, der die Feeds Ihrer Benutzer aus irgendeinem Grund löscht. Sie können mit dem Argument `--stream` den Stream angeben.

### populate_list_streams

Redis-Cache der Listen wieder befüllen. Sie müssen dies normalerweise nicht ausführen, es sei denn, es gibt einen Fehler, der die Listen Ihrer Benutzer aus irgendeinem Grund löscht.

### populate_suggestions

Empfohlene Benutzer für alle Benutzer befüllen. Sie können dies manuell ausführen wollen, um Vorschläge zu aktualisieren.

### restart_celery

Startet den `celery_worker`-Docker-Container neu.

### update

Wenn es Änderungen im `-Produktions`zweig gibt, können Sie Ihre Instanz ohne Ausfallzeit aktualisieren.

Dieser Befehl `git pull`t die neuesten `Produktion`szweigaktualisierungen, baut Docker Images falls nötig, führt Django-Migrationen aus, aktualisiert statische Dateien und startet alle Docker Container neu.

### admin_code

Ruft den geheimen Admin-Code ab, der verwendet wird, um den initalen Admin-Benutzer in einer neuen BookWyrm-Instanz zu registrieren.

## S3 kompatiblen Speicher einrichten

Standardmäßig verwendet BookWyrm lokalen Speicher für statische Assets (Favicon, Standard-Avatar, etc.) und Medien (Benutzer-Avatare, Buchtitelbilder usw.), aber Sie können einen externen Speicherdienst verwenden, um diese Dateien zu bereitzustellen. BookWyrm verwendet django-storages, um externen Speicher wie S3-kompatible Dienste, Apache Libcloud oder SFTP anzubinden.

Siehe [Externer Speicher](/external-storage.html) für weitere Informationen.

### copy_media_to_s3

Migrieren Sie alle hochgeladenen Medien von einer bestehenden Bookwrym-Installation in einen S3-kompatiblen "Bucket". Für den ersten Upload in einen leeren Bucket verwenden.

### sync_media_to_s3

Synchronisieren Sie neue oder geänderte Medien von einer existierenden Bookwrym-Installation zu einem S3-kompatiblen "Bucket". Nutzen, um sicherzustellen, dass alle lokalen Dateien in den existierenden Bucket hochgeladen sind.

### set_cors_to_s3 filename

Kopieren Sie eine CORS-Regel-JSON-Datei in Ihren S3-Bucket, wobei der `Dateiname` der Name Ihrer JSON-Datei ist (z.B. `./bw-dev set_cors_to_s3 cors.json`)

## Entwicklung und Test

_Diese Befehle sind nicht verfügbar im `Produktionszweig`_.

### black

BookWyrm verwendet den [Black](https://github.com/psf/black) Code-Formatierer, um die Python Codebase konsistent zu gestalten. Führen Sie `black` aus, bevor Sie Ihre Änderungen übertragen, so dass die `pylint` Aufgabe für ihre Pull-Anfrage nicht fehlschlägt und Sie traurig macht.

### prettier

BookWyrm verwendet [Prettier](https://prettier.io/) um die JavaScript-Codebasis konsistent zu gestalten. Führen Sie `prettier` aus, bevor Sie Änderungen an Skripten übertragen, um Ihren Code automatisch zu formatieren.

### stylelint

BookWyrm verwendet [Stylelint](uhttps://stylelint.io/), um die CSS-Dateien einheitlich zu gestalten. Führen Sie `stylelintprettier` aus, bevor Sie Änderungen an Skripten übertragen, um Ihren Code automatisch zu formatieren.

### formatters

Dieser Befehl führt alle Code-Formatierer (`black`, `prettier`, und `stylelint`) auf einmal aus.

### clean

Entferne alle gestoppten Docker-Container.

Äquivalent zu:

```shell
docker-compose stop
docker-compose rm -f
```

### makemessages

Erstellt Nachrichtendateien für alle Übersetzungstexte. Nachdem Sie `makemessages` ausgeführt haben, müssen Sie `compilemessages` ausführen, um die Übersetzungen zu kompilieren. Siehe [Djangos makemessages](https://docs.djangoproject.com/en/3.2/ref/django-admin/#makemessages).

### compilemessages

Kompiliert Übersetzungsdateien. Siehe [Djangos compilemessages](https://docs.djangoproject.com/en/3.2/ref/django-admin/#compilemessages).

### pytest args

Tests mit `pytest` ausführen.
