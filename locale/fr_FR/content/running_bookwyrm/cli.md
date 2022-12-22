- - -
Title: Outils en ligne de commande Date: 2021-11-11 Order: 9
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

### compile_themes

Compile tous les thèmes BookWyrm, qui sont des fichiers `*.scss` répertoriés dans `bookwyrm/static/css/themes`.

### collectstatic

Migre les ressources statiques vers un conteneur Docker ou un compartiment compatible S3, selon le contexte.

### generate_preview_images

Génère des images de prévisualisation pour le site, les utilisateur-ice-s et les livres. Si vous avez une grande base de données, cela peut prendre un temps conséquent. Voir [Optional features : Générer les images de prévisualisation](/optional_features.html)

### remove_remote_user_preview_images

Supprime les images de prévisualisation pour les comptes externes. Voir [Optional Features : Supprimer les images de prévisualisation pour les comptes externes](/optional_features.html)

### generate_thumbnails

Génère les miniatures pour les couvertures de livres.

### populate_streams args

Rafraîchit les flux Redis (flux utilisateurs). Vous n'aurez généralement pas besoin d'exécuter cela à moins qu'une erreur n'efface vos flux utilisateurs pour une raison ou une autre. Vous pouvez préciser quel flux en particulier en utilisant l'argument `--stream`.

### populate_list_streams

Rafraîchit le cache Redis des listes. Vous n'aurez généralement pas besoin d'exécuter cela à moins qu'une erreur n'efface les listes de vos utilisateur-ice-s pour une raison ou une autre.

### populate_suggestions

Rafraîchit la liste des comptes suggérés pour tous-tes les utilisateur-ice-s. Vous pouvez exécuter cela afin d'actualiser les suggestions.

### restart_celery

Redémarre le conteneur Docker `celery_worker`.

### update

Lors de changements sur la branche `production`, vous pouvez mettre à jour votre instance sans la rendre indisponible.

Cette commande `git pull` les dernières mises à jour de la branche `production` , construit des images docker si nécessaire, exécute les migrations Django, met à jour les fichiers statiques et redémarre tous les conteneurs Docker.

### admin_code

Récupère le code admin utilisé pour enregistrer l'admin initial sur une nouvelle instance BookWyrm.

## Configuration du stockage compatible S3

Par défaut, BookWyrm stocke localement les ressources statiques (favicon, avatar par défaut, etc.) et les médias (avatars, couvertures de livres, etc.), mais vous pouvez utiliser un service de stockage externe pour ces fichiers. BookWyrm utilise django-storages pour gérer le stockage externe, tel que les services compatibles S3, Apache Libcloud ou SFTP.

Voir [External Storage](/external-storage.html) pour plus d'informations.

### copy_media_to_s3

Migre tous les médias téléchargés d'une instance Bookwyrm existante vers un compartiment compatible S3. À utiliser pour un premier téléchargement vers un compartiment vide.

### sync_media_to_s3

Syncronise les médias nouvellement créés ou modifiés d'une instance Bookwyrm existante vers un compartiment compatible S3. À utiliser pour s'assurer que tous les fichiers locaux ont été téléchargés vers un compartiment existant.

### set_cors_to_s3 filename

Copie un fichier JSON de règles CORS vers un compartiment S3, où `filename` est le nom de votre fichier JSON (e.g. `./bw-dev set_cors_to_s3 cors.json`)

## Développement et test

_Ces commandes ne sont pas disponibles sur la branche `production`_.

### black

BookWyrm utilise le formateur de code [Black](https://github.com/psf/black) pour assurer la cohérence du code Python. Exécutez `black` avant de valider vos modifications afin d'éviter que la tâche `pylint` pour votre pull request n'échoue et ne vous rende triste.

### prettier

BookWyrm utilise [Prettier](https://prettier.io/) pour assurer la cohérence du code JavaScript. Exécutez `prettier` avant de valider vos modifications de scripts afin de formater automatiquement votre code.

### stylelint

BookWyrm utilise [Stylelint](uhttps://stylelint.io/) pour assurer la cohérence des fichiers CSS. Exécutez `stylelintprettier` avant de valider vos modifications de scripts afin de formater automatiquement votre code.

### formatters

Cette commande exécute tous les formateurs de code (`black`, `prettier`, et `stylelint`) à la suite.

### clean

Supprime tous les conteneurs Docker arrêtés.

Correspond à :

```shell
docker-compose stop
docker-compose rm -f
```

### makemessages

Génère les fichiers de messages pour toutes les chaînes de traduction. Après avoir exécuté `makemessages`, vous devez exécuter `compilemessages` pour compiler les traductions. Voir [makemessages dans Django](https://docs.djangoproject.com/en/3.2/ref/django-admin/#makemessages).

### compilemessages

Compile les fichiers de traduction. Voir [compilemessages dans Django](https://docs.djangoproject.com/en/3.2/ref/django-admin/#compilemessages).

### pytest args

Exécute les tests avec `pytest`.

### deactivate_2fa

Désactive l'authentification à deux facteurs pour un utilisateur donné.

### manual_confirm

Confirme l'adresse e-mail d'un-e utilisateur-ice et l'active.
