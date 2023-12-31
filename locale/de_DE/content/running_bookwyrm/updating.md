- - -
Title: Deine Instanz updaten Date: 2022-11-17 Order: 3
- - -

Wenn Änderungen im Produktionszweig verfügbar sind, kannst du sie mit dem Befehl `./bw-dev update` installieren und auf deine Instanz übertragen. Das macht eine Reihe von Dingen:

- `git pull` holt den aktualisierten Code aus dem git Repository. Wenn es Konflikte gibt, musst du möglicherweise `git pull` separat ausführen und die Konflikte lösen, bevor du das `./bw-dev update`-Skript erneut probieren kannst.
- `docker-compose build` baut die Images neu auf, was sicherstellt, dass die richtigen Pakete installiert sind. Dieser Schritt dauert lange und wird nur benötigt, wenn die Abhängigkeiten (einschließlich pip `requirements.txt` Pakete) geändert wurden, daher kannst du es auskommentieren, wenn du einen schnelleren Updatepfad haben möchten und es nicht stört, ihn bei Bedarf zu kommentieren.
- `docker-compose run --rm web python manage.py migrate` startet die Django-Datenbankmigrationund verwendet die neu gebrauten Docker Images.
- `Docker-Compose führen --rm web python manage.py collectstatic --no-input` lädt alle aktualisierten statischen Dateien (wie JavaScript und CSS)
- `Docker komponieren; docker-compose up -d` startet alle Docker Container neu und nutzt die neu erstellten Images (Achtung: Ausfallzeit beim Neustart)

## Aktivitätsstreams neu erstellen

Feeds für alle Benutzer*innen werden in Redis gespeichert. Um einen Stream erneut zu befüllen, benutze den Verwaltungsbefehl:

``` { .sh }
./bw-dev populate_streams
# oder verwenden Sie docker-compose direkt
docker-compose run --rm web python manage.py populate_streams
```

Wenn etwas furchtbar schief gelaufen ist, können die Streamdaten gelöscht werden.

``` { .sh }
docker-compose run --rm web python manage.py erase_streams
```
