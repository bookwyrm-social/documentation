- - -
Title : Mise à jour de votre instance Date : 2021-04-13 Order : 3
- - -

Quand des changements sont disponibles sur la branche de production, il est possible de les installer et les faire fonctionner sur l'instance en utilisant la commande `./bw-dev update`. Cela fait plusieurs choses :

- `git pull` récupère le code à jour depuis le dépôt git. S'il y a des conflits, vous pourriez avoir besoin de lancer `git pull` indépendamment et résoudre les conflits avant d'essayer le script `./bw-dev update` à nouveau.
- `docker-compose build` reconstruit les images, ce qui permet de s'assurer que les bons paquets sont installés. Cette étape prend beaucoup de temps et est nécessaire uniquement lorsque les dépendances (incluant les paquets pip `requirements.txt`) ont changées, il est donc possible de la commenter si on souhaite une mise à jour plus rapide et ne pas être gêné de la décommenter si nécessaire.
- `docker-compose exec web python manage.py migrate` lance la migration de la base de données dans Django
- `docker-compose exec web python manage.py collectstatic --no-input` charge tous les fichiers statiques mis à jour (comme les fichiers JavaScript et CSS)
- `docker-compose restart` relance les conteneurs docker

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
