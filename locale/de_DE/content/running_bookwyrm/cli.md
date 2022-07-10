- - -
Titel: Befehlszeilenwerkzeug Datum: 2021-11-11 Bestellung: 6
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

Setzt die Datenbank zurück. **This command will delete your entire Bookwyrm database**, and then initiate a fresh database and run all migrations. You should delete any recent migration files you do not want to run, _before_ running `resetdb`.

## Eine Bookwyrm-Instanz verwalten

### collectstatic

Migrate static assets to either a Docker container or to an S3-compatible "bucket", depending on the context.

### generate_preview_images

Generate preview images for site, users, and books. This can take a while if you have a large database.

### generate_thumbnails

Generates thumbnail images for book covers.

### populate_streams args

Re-populates Redis streams (user feeds). You will not usually need to run this unless there is an error that wipes out your user feeds for some reason. Sie können mit dem Argument `--stream` den Stream angeben.

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

Migrate all uploaded media from an existing Bookwrym installation to an S3-compatible "bucket". Für den ersten Upload in einen leeren Bucket verwenden.

### sync_media_to_s3

Sync new or changed uploaded media from an existing Bookwrym installation to an S3-compatible "bucket". Nutzen, um sicherzustellen, dass alle lokalen Dateien in den existierenden Bucket hochgeladen sind.

### set_cors_to_s3 filename

Copy a CORS rules JSON file to your S3 bucket, where `filename` is the name of your JSON file (e.g. `./bw-dev set_cors_to_s3 cors.json`)

## Entwicklung und Test

_These commands are not available on the `production` branch_.

### black

BookWyrm verwendet den [Black](https://github.com/psf/black) Code-Formatierer, um die Python Codebase konsistent zu gestalten. Run `black` before committing your changes so the `pylint` task does not fail for your pull request and make you sad.

### prettier

BookWyrm verwendet [Prettier](https://prettier.io/) um die JavaScript-Codebasis konsistent zu gestalten. Führen Sie `prettier` aus, bevor Sie Änderungen an Skripten übertragen, um Ihren Code automatisch zu formatieren.

### stylelint

BookWyrm uses [Stylelint](uhttps://stylelint.io/) to keep the CSS files consistently styled. Run `stylelintprettier` before committing changes to scripts to automatically format your code.

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

Erstellt Nachrichtendateien für alle Übersetzungstexte. After you have run `makemessages` you need to run `compilemessages` to compile the translations. Siehe [Djangos makemessages](https://docs.djangoproject.com/en/3.2/ref/django-admin/#makemessages).

### compilemessages

Kompiliert Übersetzungsdateien. Siehe [Djangos compilemessages](https://docs.djangoproject.com/en/3.2/ref/django-admin/#compilemessages).

### pytest args

Tests mit `pytest` ausführen.
