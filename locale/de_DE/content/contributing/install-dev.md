- - -
Title: Entwicklungsumgebung Date: 2021-04-12 Order: 3
- - -

## Voraussetzungen

Diese Anweisungen gehen davon aus, dass du BookWyrm mit Docker entwickelst. Du musst [Docker](https://docs.docker.com/engine/install/) und [docker-compose](https://docs.docker.com/compose/install/) installieren, um loszulegen.

## Entwicklungsumgebung einrichten

- Kopiere die [der BookWyrm-Codebasis von GitHub](https://github.com/bookwyrm-social/bookwyrm). Du kannst [einen Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) des Projekts erstellen und [verwende dann `git clone`, um den Code](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) auf deinen Computer herunterzuladen.
- Gehe in das Verzeichnis, das den Code auf Ihrem Computer enthält. Du arbeitest von hier aus.
- Richte deine Datei für Entwicklungsumgebungsvariablen durch Kopieren der Beispielumgebungsdatei (`.env.example`) in eine neue Datei namens `.env` ein. In der Kommandozeile kannst du das wie folgt tun:
``` { .sh }
cp .env.example .env
```
- In `.env`ändere `DEBUG` zu `true`
- Optional kannst du einen Dienst wie [ngrok](https://ngrok.com/) verwenden, um eine Domain einzurichten und setze die `DOMAIN`-Variable in Ihrer `.env`-Datei auf den von ngrok-generierten Domainnamen.

- Richte nginx für die Entwicklung ein, indem du die Entwicklerkonfigurationsdatei für nginx (`nginx/development`) in eine neue Datei mit dem Namen `nginx/default.conf` kopierst:
``` { .sh }
cp nginx/development nginx/default.conf
```

- Starte die Applikation. Führe Folgendes über die Kommandozeile aus:
``` { .sh }
./bw-dev build            # Baut die Docker-Images
./bw-dev setup            # Initialisiert die Datenbank und führt die Migrationen aus
./bw-dev up               # Start die Docker-Container
```
- Sobald die Erstellung abgeschlossen ist, kannst du auf die Instanz unter `http://localhost:1333` zugreifen und einen Admin erstellen.

Wenn du neugierig bist: das `./bw-dev` Kommando ist ein simples Shell-Script, das verschiedene Tools ansteuert: darüber hinaus könntest du es überspringen und direk `docker-compose build` oder `docker-compose up` laufen lassen, wenn du magst. `./bw-dev` sammelt sie einfach an einem gemeinsamen Ort zur Bequemlichkeit. Führe es ohne Argumente aus, um eine Liste der verfügbaren Befehle zu erhalten, lese die [Dokumentationsseite](/command-line-tool.html) dafür oder öffne es und schaue dich um, um genau zu sehen, was jeder Befehl tut!

### Modelle editieren oder erstellen

Wenn du ein Modell änderst oder erstellst, wird sich wahrscheinlich die Datenbankstruktur ändern. Damit diese Änderungen wirksam werden, musst du Djangos `makemigrations`-Befehl ausführen, um eine neue [Django Migrationsdatei](https://docs.djangoproject.com/en/3.2/topics/migrations)zu erstellen und dann diese `migrieren`:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

### Statische Dateien editieren
Jedes Mal, wenn du CSS oder JavaScript bearbeitest, musst du Djangos `collectstatic`-Befehl erneut ausführen, damit deine Änderungen wirksam werden:
``` { .sh }
./bw-dev collectstatic
```

Wenn du [yarn installierstt](https://yarnpkg.com/getting-started/install) haben, kannst du `yarn watch:static` ausführen, um das vorherige Skript bei jeder Änderung automatisch im Verzeichnis `bookwyrm/static` auszuführen.
