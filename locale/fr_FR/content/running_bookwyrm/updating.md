- - -
Title: Updating Your Instance Date: 2022-11-17 Order: 3
- - -

Quand des changements sont disponibles sur la branche de production, il est possible de les installer et les faire fonctionner sur l'instance en utilisant la commande `./bw-dev update`. Cela fait plusieurs choses :

- `git pull` récupère le code à jour depuis le dépôt git. S'il y a des conflits, vous pourriez avoir besoin de lancer `git pull` indépendamment et résoudre les conflits avant d'essayer le script `./bw-dev update` à nouveau.
- `docker-compose build` reconstruit les images, ce qui permet de s'assurer que les bons paquets sont installés. Cette étape prend beaucoup de temps et est nécessaire uniquement lorsque les dépendances (incluant les paquets pip `requirements.txt`) ont changées, il est donc possible de la commenter si on souhaite une mise à jour plus rapide et ne pas être gêné de la décommenter si nécessaire.
- `docker-compose run --rm web python manage.py migrate` runs the database migrations in Django using the newly built Docker images
- `docker-compose run --rm web python manage.py collectstatic --no-input` loads any updated static files (such as the JavaScript and CSS)
- `docker-compose down; docker-compose up -d` will restart all the docker containers and make use of the newly built images (Attention: downtime during the restart)

## Reconstruire les flux d'activité

Les flux de chaque utilisateur·ice sont stockés dans Redis. Pour repeupler un flux, il faut utiliser la commande de gestion :

``` { .sh }
./bw-dev populate_streams
# Ou en utilisant directement docker-compose
docker-compose run --rm web python manage.py populate_streams
```

Si quelque chose s'est terriblement mal passé, le flux de donnée peut être supprimé.

``` { .sh }
docker-compose run --rm web python manage.py erase_streams
```
