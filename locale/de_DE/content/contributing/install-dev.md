- - -
Titel: Entwicklungsumgebung Datum: 2021-04-12 Bestellung: 3
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

If you're curious: the `./bw-dev` command is a simple shell script runs various other tools: above, you could skip it and run `docker-compose build` or `docker-compose up` directly if you like. `./bw-dev` just collects them into one common place for convenience. Run it without arguments to get a list of available commands, read the [documentation page](/command-line-tool.html) for it, or open it up and look around to see exactly what each command is doing!

### Modelle editieren oder erstellen

If you change or create a model, you will probably change the database structure. For these changes to have effect you will need to run Django's `makemigrations` command to create a new [Django migrations file](https://docs.djangoproject.com/en/3.2/topics/migrations), and then `migrate` it:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

### Statische Dateien editieren
Any time you edit the CSS or JavaScript, you will need to run Django's `collectstatic` command again in order for your changes to have effect:
``` { .sh }
./bw-dev collectstatic
```

If you have [installed yarn](https://yarnpkg.com/getting-started/install), you can run `yarn watch:static` to automatically run the previous script every time a change occurs in `bookwyrm/static` directory.
