- - -
Title: Updating Your Instance Date: 2021-04-13 Order: 2
- - -

When there are changes available in the production branch, you can install and get them running on your instance using the command `./bw-dev update`. This does a number of things:

- `git pull` obține codul actualizat de pe depozitul git. Dacă sunt conflicte, s-ar putea să aveți nevoie să rulați `git pull` separat și să rezolvați conflictele înainte de a reîncerca scriptul `./bw-dev update`.
- `docker-compose build` recompilează imaginile, ceea ce asigură că pachetele corecte au fost instalate. Acest pas durează mult timp și este necesar numai dacă dependențele (inclusiv pachetele pip `requirements.txt`) s-au schimbat, deci puteți să-l comentați dacă vreți o cale de actualizare mai rapidă și nu vă deranjează să-l decomentați când este necesar.
- `docker-compose exec web python manage.py migrate` rulează migrările bazei de date în Django
- `docker-compose exec web python manage.py collectstatic --no-input` încarcă orice fișier static actualizat (precum JavaScript și CSS)
- `docker-compose restart` reîncarcă containerele Docker

## Recompilați fluxurile de activitate

Feeds for each user are stored in Redis. To re-populate a stream, use the management command:

``` { .sh }
./bw-dev populate_streams
# Sau folosiți direct docker-compose
docker-compose run --rm web python manage.py populate_streams
```

If something has gone terribly awry, the stream data can be deleted.

``` { .sh }
docker-compose run --rm web python manage.py erase_streams
```
