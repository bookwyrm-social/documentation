- - -
Title: Updating Your Instance Date: 2021-04-13 Order: 3
- - -

Wenn Änderungen im Produktionszweig verfügbar sind, kannst du sie mit dem Befehl `./bw-dev update` installieren und auf deine Instanz übertragen. Das macht eine Reihe von Dingen:

- `git pull` holt den aktualisierten Code aus dem git Repository. Wenn es Konflikte gibt, müssen Sie möglicherweise `git pull` separat ausführen und die Konflikte lösen, bevor Sie das `./bw-dev update`-Skript erneut probieren.
- `docker-compose build` baut die Images neu auf, was sicherstellt, dass die richtigen Pakete installiert sind. Dieser Schritt dauert lange und wird nur benötigt, wenn die Abhängigkeiten (einschließlich pip `requirements.txt` Pakete) geändert wurden, daher können Sie es auskommentieren, wenn Sie einen schnelleren Updatepfad haben möchten und es nicht stört, ihn bei Bedarf zu kommentieren.
- `docker-compose exec web python manage.py migrate` führt Datenbankmigrationen in Django aus
- `docker-compose exec web python manage.py collectstatic --no-input` lädt alle aktualisierten statischen Dateien (wie JavaScript und CSS)
- `docker-compose restart` lädt die Docker-Container neu

## Aktivitätsstreams neu erstellen

Feeds für jeden Benutzer werden in Redis gespeichert. Um einen Stream erneut zu befüllen, benutzen Sie den Verwaltungsbefehl:

``` { .sh }
./bw-dev populate_streams
# oder verwenden Sie docker-compose direkt
docker-compose run --rm web python manage.py populate_streams
```

Wenn etwas furchtbar schief gelaufen ist, können die Streamdaten gelöscht werden.

``` { .sh }
docker-compose run --rm web python manage.py erase_streams
```
