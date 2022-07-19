- - -
Title: Django Debug-Symbolleiste Date: 2022-05-16 Order: 5
- - -

BookWyrm hat einen Branch, der konfiguriert ist, um die [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) auszuführen. Dieser Branch wird niemals in `main` zusammengeführt und hat ein paar Optimierungen, die ihn mit der Symbolleiste funktionieren lassen, aber unsicher ist in allem, was einer Produktionsumgebung ähnelt. Um diesen Branch zu verwenden, müssen Sie einige Schritte gehen, um ihn zum Laufen zu bringen.

## Einrichtung

- Mit Git den [`debug-toolbar`](https://github.com/bookwyrm-social/bookwyrm/tree/debug-toolbar)-Branch auschecken
- Aktualisieren Sie den Branch relativ zum `main` mit `git merge main`. Der Branch wird periodisch aktualisiert, aber wird wahrscheinlich hinterher sein.
- Erstellen Sie die Docker-Images mit `docker-compose up --build` neu, um sicherzustellen, dass die Debug-Toolbar-Bibliothek von `requirements.txt` installiert ist
- Access the application `web` image directly (instead of via `nginx`) using port `8000`
