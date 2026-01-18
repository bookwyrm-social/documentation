- - -
Title: Entwicklungsumgebung Date: 2025-05-12 Order: 5
- - -

## Voraussetzungen

Diese Anleitung geht davon aus, dass du BookWyrm mit Docker entwickelst. Du musst [Docker](https://docs.docker.com/engine/install/) und [docker-compose](https://docs.docker.com/compose/install/) installieren, bevor du loslegst.

_Wenn du zu BookWyrm beiträgst, ohne Docker zu verwenden, würden wir uns freuen, wenn du uns helfen würdest, [diese Anleitung zu aktualisieren](/documentation.html), damit sie auch eine Hilfestellung enthält, wie eine Entwicklungsumgebung ohne Docker aufgesetzt werden kann_.

## Entwicklungsumgebung einrichten

### Quellcode erhalten

1. Kopiere den [BookWyrm-Quellcode von GitHub](https://github.com/bookwyrm-social/bookwyrm). Du kannst [einen Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) des Projekts erstellen und [dann `git clone` ausführen, um den Quellcode](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) auf deinen Computer herunterzuladen.
2. Gehe in das Verzeichnis auf deinem Computer, das den Quellcode enthält. Von jetzt an arbeitest du in diesem Verzeichnis.
3. Die Entwicklung wird auf dem `main`-Branch durchgeführt. Stelle also sicher, dass du diesen Branch ausgecheckt hast: `git checkout main`
4. Erstelle eine Datei mit Umgebungsvariablen für die Entwicklung, indem du die Beispieldatei (`.env.example`) kopierst und als neue Datei namens `.env` einfügst. In der Kommandozeile kannst du das wie folgt tun:
``` { .sh }
cp .env.example .env
```

### Umgebung konfigurieren

In der Datei `.env`:

4. Ändere `DEBUG` zu `true`
5. Wenn du einen Tunneling-Dienst oder Proxy wie [ngrok](https://ngrok.com) verwendest, ändere die `DOMAIN` zu der Domain, die du verwendest (z. B. `abcd-1234.ngrok-free.app`). Andernfalls, ändere `DOMAIN` zu `localhost`
6. Ändere `NGINX_SETUP` zu `reverse_proxy` (dies verhindert, dass BookWyrm versucht, HTTPS-Zertifikate auf deinem Entwicklungsgerät zu erstellen)
7. Wenn du einen bestimmten Port verwenden möchtest (z. B. wenn du Anfragen durch ngrok tunnelst), entferne den Kommentar vor `PORT` und gib den Port an (z. B. `PORT=1333`). Wenn du `localhost` nutzt, ist dieser Schritt optional.

Prüfe, ob du [alle notwendigen Einstellungen getroffen hast](/environment.html#required-environment-settings), bevor du fortfährst.

Wenn du versuchst, deinen Administrations-Account anzulegen, und eine Nachricht siehst, die `CSRF verification failed` lautet, kann es sein, dass du die Domain oder den Port falsch angegeben hast.

### E-Mail (optional)

Wenn du ausprobieren möchtest, E-Mails zu versenden, wirst du [passende, echte Werte](/environment.html#email-configuration) im Bereich "E-Mail-Konfiguration" angeben müssen. Du musst nichts an der [separaten Einstellung `EMAIL`](/environment.html#email) ändern.

### Bauen und ausführen

8. Führe Folgendes über die Kommandozeile aus:

``` { .sh }
./bw-dev build            # Docker-Images bauen
./bw-dev setup            # Datenbank initialisieren und Migrationen ausführen. Notiere dir den Administrations-Schlüssel am Ende der Ausgabe. Du wirst ihn brauchen, um einen Administrations-Account anzulegen.
./bw-dev up               # Docker-Container starten
```

9. Sobald der Build abgeschlossen ist, kannst du die Instanz unter `http://localhost`, unter deiner ngrok-Domain oder unter `http://localhost:{PORT}` erreichen, abhängig von deiner Domain- und Port-Einstellung.
10. Du kannst nun deinen Administrations-Schlüssel eingeben und einen Administrations-Account anlegen. Ab hier funktioniert alles so, wie es in "BookWyrm betreiben" beschrieben ist.

Wenn du neugierig bist: Das `./bw-dev`-Kommando ist ein simples Shell-Script, das verschiedene andere Tools ansteuert. Du könntest es überspringen und direkt `docker-compose build` oder `docker-compose up` laufen lassen, wenn du möchtest. `./bw-dev` kombiniert diese Aufrufe der Einfachheit halber an einem gemeinsamen Ort. Führe das Skript ohne Argumente aus, um eine Liste der verfügbaren Kommandos zu erhalten, lies die [zugehörige Seite in der Dokumentation](/cli.html) oder öffne das Skript und sieh genau, was jedes Kommando tut!

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

Wenn du [yarn installiert](https://yarnpkg.com/getting-started/install) hast, kannst du `yarn watch:static` ausführen, um das vorherige Skript bei jeder Änderung automatisch im Verzeichnis `bookwyrm/static` ausführen zu lassen.
