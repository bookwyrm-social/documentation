- - -
Title: Command Line Tool Date: 2021-11-11 Order: 7
- - -

Les développeur·ses de BookWyrm et les gestionnaires d'une instance peuvent utiliser le script `bw-dev` pour des tâches courantes. Cela peut simplifier vos commandes en les rendant plus courtes, plus faciles à mémoriser et diminuer le risque d'erreur.

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

Par défaut, BookWyrm stocke localement les fichiers statiques (favicon, avatar par défaut, etc.) et les médias (avatars, couvertures de livres, etc.), mais vous pouvez utiliser un service de stockage externe. BookWyrm utilise django-storages pour gérer le stockage externe, comme les services compatibles S3, Apache Libcloud ou SFTP.

Voir [Stockage externe](/external-storage.html) pour plus d'informations.

### copy_media_to_s3

Migrer tous les médias téléversés depuis une installation existante de Bookwrym vers un « seau » S3 compatible. Utiliser pour l'envoi initial vers un seau vide.

### sync_media_to_s3

Synchroniser les médias téléversés neufs ou modifiés depuis une installation existante de Bookwrym vers un « seau » S3 compatible. À utiliser pour s’assurer que tous les fichiers locaux soient téléversés dans un seau existant.

### set_cors_to_s3 filename

Copiez un fichier JSON de règles CORS dans votre seau S3, où `filename` est le nom de votre fichier JSON (ex : `./bw-dev set_cors_to_s3 cors.json`)

## Développement et test

_Ces commandes ne sont pas disponibles sur la branche de `production`_.

### black

BookWyrm utilise le formateur de code [Black](https://github.com/psf/black) pour assurer la cohérence du code Python. Exécutez `black` avant de valider vos modifications afin que la tâche `pylint` n’échoue pas pour votre pull request et vous rend triste.

### prettier

BookWyrm utilise [Prettier](https://prettier.io/) pour assurer la cohérence du code JavaScript. Exécutez `prettier` avant de valider les modifications aux scripts pour formater automatiquement votre code.

### stylelint

BookWyrm utilise [Stylelint](uhttps://stylelint.io/) pour assurer la cohérence des fichiers CSS. Exécutez `stylelintprettier` avant de valider les modifications aux scripts pour formater automatiquement votre code.

### formatters

Cette commande exécute tous les formateurs de code (`black`, `prettier`, et `stylelint`) en une seule fois.

### clean

Supprimer tous les conteneurs Docker arrêtés.

Équivalent de :

```shell
docker-compose stop
docker-compose rm -f
```

### makemessages

Crée des fichiers de messages pour tous les segments de traduction. Après avoir exécuté `makemessages` , vous devez exécuter `compilemessages` pour compiler les traductions. Voir [les makemessages Django](https://docs.djangoproject.com/en/3.2/ref/django-admin/#makemessages).

### compilemessages

Compile les fichiers de traduction. Voir [la doc de Django pour compilemessages](https://docs.djangoproject.com/en/3.2/ref/django-admin/#compilemessages).

### Arguments de pytest

Exécutez des tests avec `pytest`.
