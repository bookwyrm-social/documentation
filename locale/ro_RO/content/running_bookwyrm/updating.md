- - -
Title: Updating Your Instance Date: 2022-11-17 Order: 3
- - -

Când sunt schimbări disponibile în ramura de producție, puteți să le instalați și rula utilizând comanda `./bw-dev update` pe instanța dvs. Aceasta face mai multe de lucruri:

- `git pull` obține codul actualizat de pe depozitul git. Dacă sunt conflicte, s-ar putea să aveți nevoie să rulați `git pull` separat și să rezolvați conflictele înainte de a reîncerca scriptul `./bw-dev update`.
- `docker-compose build` recompilează imaginile, ceea ce asigură că pachetele corecte au fost instalate. Acest pas durează mult timp și este necesar numai dacă dependențele (inclusiv pachetele pip `requirements.txt`) s-au schimbat, deci puteți să-l comentați dacă vreți o cale de actualizare mai rapidă și nu vă deranjează să-l decomentați când este necesar.
- `docker-compose run --rm web python manage.py migrate` runs the database migrations in Django using the newly built Docker images
- `docker-compose run --rm web python manage.py collectstatic --no-input` loads any updated static files (such as the JavaScript and CSS)
- `docker-compose down; docker-compose up -d` will restart all the docker containers and make use of the newly built images (Attention: downtime during the restart)

## Recompilați fluxurile de activitate

Fluxurile pentru fiecare utilizator sunt stocate în Redis. Pentru a repopula un flux, folosiți comanda de gestionare:

``` { .sh }
./bw-dev populate_streams
# Sau folosiți direct docker-compose
docker-compose run --rm web python manage.py populate_streams
```

Dacă ceva a mers groaznic, datele fluxului pot fi șterse.

``` { .sh }
docker-compose run --rm web python manage.py erase_streams
```
