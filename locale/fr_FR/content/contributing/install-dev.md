- - -
Title: Developer Environment Date: 2021-04-12 Order: 3
- - -

## Prérequis

These instructions assume you are developing BookWyrm using Docker. You'll need to [install Docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/) to get started.

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

If you're curious: the `./bw-dev` command is a simple shell script runs various other tools: above, you could skip it and run `docker-compose build` or `docker-compose up` directly if you like. `./bw-dev` just collects them into one common place for convenience. Run it without arguments to get a list of available commands, read the [documentation page](/command-line-tool.html) for it, or open it up and look around to see exactly what each command is doing!

### Édition ou création du modèle de données

If you change or create a model, you will probably change the database structure. For these changes to have effect you will need to run Django's `makemigrations` command to create a new [Django migrations file](https://docs.djangoproject.com/en/3.2/topics/migrations), and then `migrate` it:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

### Édition des fichiers statiques
Any time you edit the CSS or JavaScript, you will need to run Django's `collectstatic` command again in order for your changes to have effect:
``` { .sh }
./bw-dev collectstatic
```

If you have [installed yarn](https://yarnpkg.com/getting-started/install), you can run `yarn watch:static` to automatically run the previous script every time a change occurs in `bookwyrm/static` directory.
