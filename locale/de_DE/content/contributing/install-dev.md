- - -
Title: Entwicklungsumgebung Date: 2021-04-12 Order: 3
- - -

## Voraussetzungen

Diese Anweisungen gehen davon aus, dass Sie BookWyrm mit Docker entwickeln. Sie müssen [Docker](https://docs.docker.com/engine/install/) und [docker-compose](https://docs.docker.com/compose/install/) installieren, um loszulegen.

## Entwicklungsumgebung einrichten

- Holen Sie sich eine Kopie von [der BookWyrm-Codebasis von GitHub](https://github.com/bookwyrm-social/bookwyrm). Sie können [einen Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) des Projekts erstellen und dann [verwenden Sie `git clone`, um den Code](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) auf Ihren Computer herunterzuladen.
- Gehen Sie in das Verzeichnis, das den Code auf Ihrem Computer enthält, Sie arbeiten von hier aus.
- Richten Sie Ihre Datei für Entwicklungsumgebungsvariablen durch Kopieren der Beispielumgebungsdatei (`.env.example`) in eine neue Datei namens `.env` ein. In der Kommandozeile können Sie dies tun mit:
``` { .sh }
cp .env.example .env
```
- In `.env`ändern Sie `DEBUG` zu `true`
- Optional können Sie einen Dienst wie [ngrok](https://ngrok.com/) verwenden, um eine Domain einzurichten und setzen Sie die `DOMAIN`-Variable in Ihrer `.env`-Datei auf den von ngrok-generierten Domainnamen.

- Richten Sie nginx für die Entwicklung ein, indem Sie die Entwicklerkonfigurationsdatei für nginx (`nginx/development`) in eine neue Datei mit dem Namen `nginx/default.conf` kopieren:
``` { .sh }
cp nginx/development nginx/default.conf
```

- Starte die Applikation. Führen sie folgendes über die Kommandozeile aus:
``` { .sh }
./bw-dev build            # Baut die Docker-Images
./bw-dev setup            # Initialisiert die Datenbank und führt die Migrationen aus
./bw-dev up               # Start die Docker-Container
```
- Sobald die Erstellung abgeschlossen ist, können Sie auf die Instanz unter `http://localhost:1333` zugreifen und einen Administrator erstellen.

Wenn du neugierig bist: das `./bw-dev` Kommando ist ein simples Shell-Script, das verschiedene Tools ansteuert: darüber hinaus könntest du es überspringen und direk `docker-compose build` oder `docker-compose up` laufen lassen, wenn du magst. `./bw-dev` sammelt sie einfach an einem gemeinsamen Ort zur Bequemlichkeit. Führen Sie es ohne Argumente aus, um eine Liste der verfügbaren Befehle zu erhalten, lesen Sie die [Dokumentationsseite](/command-line-tool.html) dafür oder öffnen Sie es und schauen Sie sich um, um genau zu sehen, was jeder Befehl tut!

### Modelle editieren oder erstellen

Wenn Sie ein Modell ändern oder erstellen, werden Sie wahrscheinlich die Datenbankstruktur ändern. Damit diese Änderungen wirksam werden, müssen Sie Djangos `makemigrations`-Befehl ausführen, um eine neue [Django Migrationsdatei](https://docs.djangoproject.com/en/3.2/topics/migrations)zu erstellen und dann diese `migrieren`:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

### Statische Dateien editieren
Jedes Mal, wenn Sie CSS oder JavaScript bearbeiten, müssen Sie Djangos `collectstatic`-Befehl erneut ausführen, damit Ihre Änderungen wirksam werden:
``` { .sh }
./bw-dev collectstatic
```

Wenn Sie [yarn installiert](https://yarnpkg.com/getting-started/install) haben, können Sie `yarn watch:static` ausführen, um das vorherige Skript bei jeder Änderung automatisch im Verzeichnis `bookwyrm/static` auszuführen.
