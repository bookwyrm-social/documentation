- - -
Title: Outils en ligne de commande Date: 11/11/2021 Order: 6
- - -

Les développeur-e-s de BookWyrm et les gestionnaires d'une instance peuvent utiliser le script `bw-dev` pour des tâches courantes. Cela peut simplifier vos commandes en les rendant plus courtes, plus faciles à mémoriser et diminuer le risque d'erreur.

Une fois que vous avez installé Bookwyrm [en production](installing-in-production.html) ou [en développement](https://docs.joinbookwyrm.com/developer-environment.html#setting_up_the_developer_environment), vous pouvez exécuter le script à partir de la ligne de commande avec `./bw-dev` suivi de la sous-commande que vous voulez exécuter.

## Raccourcis Docker

### bash

Ouvez une session interactive `bash` dans le conteneur docker `web`.

### build

Équivalent à `docker-compose build`.

### dbshell

Ouvrir un shell de base de donnée Postgres interactif. On espère que vous savez ce que vous faites.

### runweb args

Exécuter une commande arbitraire (représentée ci-dessus par `args`) dans le conteneur `web`.

Équivalent à `docker-compose run --rm web`.

### service_ports_web args

Exécuter une commande arbitraire dans le conteneur `web` (représenté ci-dessus par `args`) avec les ports exposés. Ceci est utile si vous voulez exécuter des tests `pdb` parce que `runweb` n'affiche pas l'invite de commande `pdb`.

Équivalent à `docker-compose run --rm web`.

### shell

Ouvrir un shell Django interactif à l'intérieur du conteneur docker `web`. Cela sert à exécuter directement des commandes Django.

### up [args]

Démarrer ou redémarrer des conteneurs Docker, en incluant optionnellement des arguments (représentés ci-dessus par `args`). Équivalent à `docker-compose up --build [args]`

## Gérer la base de données

### initdb

Initialiser une base de données.

### makemigrations [appname migration number]

_Cette commande n'est pas disponible sur la branche de `production`_.

Exécute la commande Django `makemigrations` à l'intérieur du conteneur Docker. Si vous avez changé la structure de la base de donnée dans une branche de développement, vous allez devoir exécuter cette commande pour que vos changements s'appliquent. Facultativement, vous pouvez préciser quelle migration exécuter, par exemple `./bw-dev makemigrations bookwyrm 0108`

### migrate

Exécute la commande Django `migrate` à l'intérieur de votre conteneur Docker. Il faut toujours faire ceci après `makemigrations`.

### resetdb

_Cette commande n'est pas disponible sur la branche de `production`_.

Réinitialise la base de données. **Cette commande va supprimer votre base de données Bookwyrm en entier**, et va ensuite initialiser une nouvelle base de donnée et effectuer toutes les migrations. Vous devriez supprimer tous les fichiers de migration récents que vous ne voulez pas exécuter _avant_ d'exécuter `resetdb`.

## Gérer une instance de Bookwyrm

### collectstatic

Migre les ressources statiques soit vers un conteneur Docker, soit vers un "compartiment" S3-compatible, dépendamment du contexte.

### generate_preview_images

Génère un aperçu pour le site, les utilisateur-ice-s et les livres. Si vous avez une grande base de données, cela peut prendre un certain temps.

### generate_thumbnails

Génère des vignettes pour les couvertures des livres.

### populate_streams args

Rafraîchit les flux Redis. Vous n’aurez généralement pas besoin de ceci à moins qu’une erreur efface votre flux Redis. Vous pouvez spécifier quel flux en utilisant l’argument `--stream`.

### populate_list_streams

Rafraîchit le cache Redis des listes. Vous n’aurez généralement pas besoin de ceci à moins qu’une erreur efface vos listes.

### populate_suggestions

Rafraîchir la liste de personnes recommandées pour tout le monde. Vous pouvez exécuter cela manuellement pour actualiser les suggestions.

### restart_celery

Redémarre le conteneur Docker `celery_worker`.

### mise à jour

Lors de changements sur la branche `production`, vous pouvez mettre à jour votre instance sans temps d’arrêt.

Cette commande `git pull` les dernières mises à jour de la branche `production` , construit des images docker si nécessaire, exécute les migrations Django, met à jour les fichiers statiques et redémarre tous les conteneurs Docker.

### admin_code

Récupère le code admin utilisé pour enregistrer l'admin initial sur une nouvelle instance BookWyrm.

## Configuration du stockage S3 compatible

By default, BookWyrm uses local storage for static assets (favicon, default avatar, etc.), and media (user avatars, book covers, etc.), but you can use an external storage service to serve these files. BookWyrm uses django-storages to handle external storage, such as S3-compatible services, Apache Libcloud or SFTP.

See [External Storage](/external-storage.html) for more information.

### copy_media_to_s3

Migrate all uploaded media from an existing Bookwrym installation to an S3-compatible "bucket". Use for initial upload to an empty bucket.

### sync_media_to_s3

Sync new or changed uploaded media from an existing Bookwrym installation to an S3-compatible "bucket". Use to ensure all local files are uploaded to an existing bucket.

### set_cors_to_s3 filename

Copy a CORS rules JSON file to your S3 bucket, where `filename` is the name of your JSON file (e.g. `./bw-dev set_cors_to_s3 cors.json`)

## Development and testing

_These commands are not available on the `production` branch_.

### black

BookWyrm uses the [Black](https://github.com/psf/black) code formatter to keep the Python codebase consistent styled. Run `black` before committing your changes so the `pylint` task does not fail for your pull request and make you sad.

### prettier

BookWyrm uses [Prettier](https://prettier.io/) to keep the JavaScript codebase consistently styled. Run `prettier` before committing changes to scripts to automatically format your code.

### stylelint

BookWyrm uses [Stylelint](uhttps://stylelint.io/) to keep the CSS files consistently styled. Run `stylelintprettier` before committing changes to scripts to automatically format your code.

### formatters

This command runs all code formatters (`black`, `prettier`, and `stylelint`) in one go.

### clean

Remove all stopped Docker containers.

Equivalent to:

```shell
docker-compose stop
docker-compose rm -f
```

### makemessages

Creates message files for all translation strings. After you have run `makemessages` you need to run `compilemessages` to compile the translations. See [Django's makemessages](https://docs.djangoproject.com/en/3.2/ref/django-admin/#makemessages).

### compilemessages

Compiles translation files. See [Django's compilemessages](https://docs.djangoproject.com/en/3.2/ref/django-admin/#compilemessages).

### pytest args

Run tests with `pytest`.
