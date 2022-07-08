Când sunt schimbări disponibile în ramura de producție, puteți să le instalați și rula utilizând comanda `./bw-dev update` pe instanța dvs. Aceasta face mai multe de lucruri:

- `git pull` obține codul actualizat de pe depozitul git. Dacă sunt conflicte, s-ar putea să aveți nevoie să rulați `git pull` separat și să rezolvați conflictele înainte de a reîncerca scriptul `./bw-dev update`.
- `docker-compose build` recompilează imaginile, ceea ce asigură că pachetele corecte au fost instalate. Acest pas durează mult timp și este necesar numai dacă dependențele (inclusiv pachetele pip `requirements.txt`) s-au schimbat, deci puteți să-l comentați dacă vreți o cale de actualizare mai rapidă și nu vă deranjează să-l decomentați când este necesar.
- `docker-compose exec web python manage.py migrate` rulează migrările bazei de date în Django
- `docker-compose exec web python manage.py collectstatic --no-input` încarcă orice fișier static actualizat (precum JavaScript și CSS)
- `docker-compose restart` reîncarcă containerele Docker

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
