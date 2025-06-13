- - -
Títol: Actualitzant la teva instància Data: 2022-11-17 Ordre: 3
- - -

Quan hi ha canvis disponibles a la branca de producció, els pots instal·lar i fer funcionar a la teva instància mitjançant la comanda `./bw-dev update`. Això fa les següents coses:

- `git pull` retorna el codi actualitzat des del repositori de git. Si hi ha conflictes, podries necessitar executar  `git pull` de manera separada i resoldre els conflictes abans d'intentar l'script `./bw-dev update` de nou.
- `docker-compose build` reconstrueix les imatges, cosa que garanteix que els paquets correctes s'instal·lin. Els passos requereixen temps i només són necessaris quan les dependències (incloent els paquets pip `requirements.txt`) han canviat, així que ho pots comentar si vols una actualització més ràpida i no et fa res descomentar si fes falta.
- `docker-compose run --rm web python manage.py migrate` executa les migracions de la base de dades amb Django fent ús de les noves imatges Docker construïdes
- `docker-compose run --rm web python manage.py collectstatic --no-input` carrega qualsevol fitxer estàtic actualitzat (així com el JavaScript i CSS)
- `docker-compose down; docker-compose up -d` reiniciarà tots els contenidors docker i farà ús de les noves imatges construïdes (Atenció: temps inoperatiu durant el reinici)

## Reconstruint els fluxos d'activitat

La informació de la qual es nodreix cada usuari queda emmagatzemada a Redis. Per tal de recrear un flux, utilitza la comanda de gestió:

``` { .sh }
./bw-dev populate_streams
# O utilitza docker-compose directament
docker-compose run --rm web python manage.py populate_streams
```

Si alguna cosa ha anat molt malament, el flux de dades es pot eliminar.

``` { .sh }
docker-compose run --rm web python manage.py erase_streams
```
