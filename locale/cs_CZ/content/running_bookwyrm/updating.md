- - -
Název: Aktualizace instance Datum: 2022-11-17 Pořadí: 3
- - -

When there are changes available in the production branch, you can install and get them running on your instance using the command `./bw-dev update`. This does a number of things:

- `git pull` gets the updated code from the git repository. If there are conflicts, you may need to run `git pull` separately and resolve the conflicts before trying the `./bw-dev update` script again.
- `docker-compose build` rebuilds the images, which ensures that the correct packages are installed. This step takes a long time and is only needed when the dependencies (including pip `requirements.txt` packages) have changed, so you can comment it out if you want a quicker update path and don't mind un-commenting it as needed.
- `docker-compose run --rm web python manage.py migrate` spouští migrace databáze v Django pomocí nově sestavených Docker obrazů
- `docker-compose run --rm web python manage.py collectstatic --no-input` načte všechny aktualizované statické soubory (například JavaScript a CSS)
- `dokové složení; docker-compose -d` restartuje všechny Docker kontejnery a použije nově sestavené obrazy (upozornění: výpadek během restartu)

## Re-building activity streams

Feeds for each user are stored in Redis. To re-populate a stream, use the management command:

``` { .sh }
./bw-dev populate_streams
# Or use docker-compose directly
docker-compose run --rm web python manage.py populate_streams
```

If something has gone terribly awry, the stream data can be deleted.

``` { .sh }
docker-compose run --rm web python manage.py erase_streams
```
