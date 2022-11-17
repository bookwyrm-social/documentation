- - -
Title: Updating Your Instance Date: 2022-11-17 Order: 3
- - -

Wenn Änderungen im Produktionszweig verfügbar sind, kannst du sie mit dem Befehl `./bw-dev update` installieren und auf deine Instanz übertragen. Das macht eine Reihe von Dingen:

- `git pull` holt den aktualisierten Code aus dem git Repository. Wenn es Konflikte gibt, müssen Sie möglicherweise `git pull` separat ausführen und die Konflikte lösen, bevor Sie das `./bw-dev update`-Skript erneut probieren.
- `docker-compose build` baut die Images neu auf, was sicherstellt, dass die richtigen Pakete installiert sind. Dieser Schritt dauert lange und wird nur benötigt, wenn die Abhängigkeiten (einschließlich pip `requirements.txt` Pakete) geändert wurden, daher können Sie es auskommentieren, wenn Sie einen schnelleren Updatepfad haben möchten und es nicht stört, ihn bei Bedarf zu kommentieren.
- `docker-compose run --rm web python manage.py migrate` runs the database migrations in Django using the newly built Docker images
- `docker-compose run --rm web python manage.py collectstatic --no-input` loads any updated static files (such as the JavaScript and CSS)
- `docker-compose down; docker-compose up -d` will restart all the docker containers and make use of the newly built images (Attention: downtime during the restart)

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
