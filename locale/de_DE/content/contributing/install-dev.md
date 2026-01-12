- - -
Title: Entwicklungsumgebung Date: 2025-05-12 Order: 5
- - -

## Voraussetzungen

Diese Anleitung geht davon aus, dass du BookWyrm mit Docker entwickelst. Du musst [Docker](https://docs.docker.com/engine/install/) und [docker-compose](https://docs.docker.com/compose/install/) installieren, bevor Du loslegst.

## Entwicklungsumgebung einrichten

### Den Quellcode erhalten

1. Kopiere den [BookWyrm-Quellcode von GitHub](https://github.com/bookwyrm-social/bookwyrm). Du kannst [einen Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) des Projekts erstellen und [dann `git clone` ausführen, um den Quellcode](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) auf deinen Computer herunterzuladen.
2. Gehe in das Verzeichnis, das den Quellcodeode auf Ihrem Computer enthält. Von jetzt an arbeitest Du aus diesem Verzeichnis heraus.
3. Die Entwicklung wird auf dem `main`-Branch durchgeführt. Stelle also sicher, dass du diesen Branch ausgecheckt hast: `git checkout main`
4. Erstelle eine Datei für Umgebungsvariablen für die Entwicklung durch Kopieren der Beispieldatei für Umgebungsvariablen (`.env.example`) in eine neue Datei namens `.env` ein. Falls Du die Kommandozeile nutzt, kannst du das wie folgt tun:
``` { .sh }
cp .env.example .env
```

### Configure your environment settings

In `.env`:

4. change `DEBUG` to `true`
5. If you use a tunneling/proxy service like [ngrok](https://ngrok.com), set `DOMAIN` to to the domain name you are using (e.g. `abcd-1234.ngrok-free.app`). Otherwise, set `DOMAIN` to `localhost`
6. change `NGINX_SETUP` to `reverse_proxy` (this prevents BookWyrm trying to set up https certificates on your development machine)
7. If you need to use a particular port (e.g. if you are tunneling via ngrok), uncomment `PORT` and set it (e.g. `PORT=1333`). If using `localhost` this is optional.

Check that you have [all the required settings configured](/environment.html#required-environment-settings) before proceeding.

If you try to register your admin account and see a message that `CSRF verification failed` you may have set your domain or port incorrectly.

### Email (optional)

If you want to test sending emails, you will need to [set up appropriate real values](/environment.html#email-configuration) in the "Email config" section. You do not need to change anything for [the separate `EMAIL` setting](/environment.html#email).

### Build and run

8. Führe Folgendes über die Kommandozeile aus:

``` { .sh }
./bw-dev build            # Build the docker images
./bw-dev setup            # Initialize the database and run migrations. Note the ADMIN key at the end of this output. You'll need it to register the first admin user.
./bw-dev up               # Start the docker containers
```

9. Once the build is complete, you can access the instance at `http://localhost`, your ngrok domain, or `http://localhost:{PORT}`, depending on you domain and port configuration.
10. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

Wenn du neugierig bist: das `./bw-dev` Kommando ist ein simples Shell-Script, das verschiedene Tools ansteuert: darüber hinaus könntest du es überspringen und direk `docker-compose build` oder `docker-compose up` laufen lassen, wenn du magst. `./bw-dev` sammelt sie einfach an einem gemeinsamen Ort zur Bequemlichkeit. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Modelle editieren oder erstellen

Wenn du ein Modell änderst oder erstellst, wird sich wahrscheinlich die Datenbankstruktur ändern. Damit diese Änderungen wirksam werden, musst du Djangos `makemigrations`-Befehl ausführen, um eine neue [Django Migrationsdatei](https://docs.djangoproject.com/en/3.2/topics/migrations)zu erstellen und dann diese `migrieren`:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

## Statische Dateien editieren
Jedes Mal, wenn du CSS oder JavaScript bearbeitest, musst du Djangos `collectstatic`-Befehl erneut ausführen, damit deine Änderungen wirksam werden:
``` { .sh }
./bw-dev collectstatic
```

Wenn du [yarn installierstt](https://yarnpkg.com/getting-started/install) haben, kannst du `yarn watch:static` ausführen, um das vorherige Skript bei jeder Änderung automatisch im Verzeichnis `bookwyrm/static` auszuführen.
