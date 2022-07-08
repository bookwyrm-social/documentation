- - -
Title: Developer Environment Date: 2021-04-12 Order: 3
- - -

## Prérequis

Ces instructions supposent que vous développez BookWyrm en utilisant Docker. Vous devrez [installer Docker](https://docs.docker.com/engine/install/) et [docker-compose](https://docs.docker.com/compose/install/) avant toute chose.

## Mise en place de l'environnement de développement

- Obtenez une copie de [la base code de BookWyrm depuis GitHub](https://github.com/bookwyrm-social/bookwyrm). Vous pouvez [créer un fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) du dépôt, puis [utiliser `git clone` pour télécharger le code](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) sur votre ordinateur.
- Allez dans le répertoire qui contient le code sur votre ordinateur, vous travaillerez désormais à partir de ce répertoire.
- Configurez votre fichier de variables d'environnement de développement en copiant le fichier d'environnement d'exemple (`.env.example`) dans un nouveau fichier nommé `.env`. En ligne de commande, vous pouvez le faire en tapant :
``` { .sh }
cp .env.example .env
```
- Dans `.env`, modifiez la valeur de `DEBUG` en `true`
- En option, vous pouvez utiliser un service comme [ngrok](https://ngrok.com/) pour configurer un nom de domaine, définissez ensuite dans votre fichier `.env` la valeur de `DOMAIN` en utilisant le nom de domaine généré par ngrok.

- Configurez nginx pour le développement en copiant le fichier de configuration nginx pour le développement (`nginx/development`) vers un nouveau fichier nommé `nginx/default.conf` :
``` { .sh }
cp nginx/development nginx/default.conf
```

- Lancez l'application. En ligne de commande, exécutez :
``` { .sh }
./bw-dev build  # Construit les images docker
./bw-dev setup  # Initialise la base de données et lance les migrations
./bw-dev up     # Démarre les conteneurs docker
```
- Une fois la compilation terminée, vous pouvez accéder à l'instance sur `http://localhost:1333` et créer un utilisateur admin.

Pour les curieux·ses : la commande `./bw-dev` est un simple script shell qui exécute divers autres outils ; au lieu des commandes ci-dessus, vous auriez pu exécuter `docker-compose build` ou `docker-compose up` directement si vous le souhaitez. `./bw-dev` les rassemble dans un seul endroit pour plus de commodité. Exécutez la commande sans argument pour obtenir une liste des commandes disponibles, lisez la [page de documentation](/command-line-tool.html) dédiée, ou ouvrez le fichier et examinez exactement ce que chaque commande fait !

### Édition ou création du modèle de données

Si vous créez ou modifiez un modèle, vous changerez probablement la structure de la base de données. Pour que ces changements aient des effets, vous devrez utiliser la commande `makemigrations` de Django pour créer un nouveau [fichier de migration Django](https://docs.djangoproject.com/en/3.2/topics/migrations), puis la commande `migrate` pour le migrer :

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

### Édition des fichiers statiques
Chaque fois que vous éditez du CSS ou du JavaScript, vous devrez exécuter la commande `collectstatic` de Django pour que vos changements aient un effet :
``` { .sh }
./bw-dev collectstatic
```

Si vous avez [installé yarn](https://yarnpkg.com/getting-started/install), vous pouvez exécuter `yarn watch:static` qui va exécuter automatiquement le script précédent à chaque fois qu'un changement se produit dans le répertoire `bookwyrm/static`.
