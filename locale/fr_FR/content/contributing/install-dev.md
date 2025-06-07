- - -
Title: Developer Environment Date: 2025-05-26 Order: 5
- - -

## Prérequis

Ces instructions supposent que vous développez BookWyrm en utilisant Docker. Vous devrez [installer Docker](https://docs.docker.com/engine/install/) et [docker-compose](https://docs.docker.com/compose/install/) avant toute chose.

## Mise en place de l'environnement de développement

### Get the code

1. Obtenez une copie de [la base code de BookWyrm depuis GitHub](https://github.com/bookwyrm-social/bookwyrm). Vous pouvez [créer un fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) du dépôt, puis [utiliser `git clone` pour télécharger le code](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) sur votre ordinateur.
2. Allez dans le répertoire qui contient le code sur votre ordinateur, vous travaillerez désormais à partir de ce répertoire.
3. Configurez votre fichier de variables d'environnement de développement en copiant le fichier d'environnement d'exemple (`.env.example`) dans un nouveau fichier nommé `.env`. En ligne de commande, vous pouvez le faire en tapant :
``` { .sh }
cp .env.example .env
```

### Configure your environment settings

In `.env`:

4. change `DEBUG` to `true`
5. If you use a tunneling/proxy service like [ngrok](https://ngrok.com), set `DOMAIN` to to the domain name you are using (e.g. `abcd-1234.ngrok-free.app`). Otherwise, set `DOMAIN` to `localhost`
6. change `NGINX_SETUP` to `reverse_proxy` (this prevents BookWyrm trying to set up https certificates on your development machine)
7. If you need to use a particular port (e.g. if you are tunneling via ngrok), uncomment `PORT` and set it (e.g. `PORT=1333`). If using `localhost` this is optional.

If you try to register your admin account and see a message that `CSRF verification failed`, you should check these settings, as you may have set your domain or port incorrectly.

### Email (optional)

If you want to test sending emails, you will need to [set up appropriate values](/environment.html#email-configuration) in the "Email config" section. You do not need to change anything for [the separate `EMAIL` setting](/environment.html#email).

### Build and run

8. En ligne de commande, exécutez :

``` { .sh }
./bw-dev build            # Build the docker images
./bw-dev setup            # Initialize the database and run migrations. Note the ADMIN key at the end of this output. You'll need it to register the first admin user.
./bw-dev up               # Start the docker containers
```

9. Once the build is complete, you can access the instance at `http://localhost`, your ngrok domain, or `http://localhost:{PORT}`, depending on you domain and port configuration.
10. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

Pour les curieux·ses : la commande `./bw-dev` est un simple script shell qui exécute divers autres outils ; au lieu des commandes ci-dessus, vous auriez pu exécuter `docker-compose build` ou `docker-compose up` directement si vous le souhaitez. `./bw-dev` les rassemble dans un seul endroit pour plus de commodité. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Édition ou création du modèle de données

Si vous créez ou modifiez un modèle, vous changerez probablement la structure de la base de données. Pour que ces changements aient des effets, vous devrez utiliser la commande `makemigrations` de Django pour créer un nouveau [fichier de migration Django](https://docs.djangoproject.com/en/3.2/topics/migrations), puis la commande `migrate` pour le migrer :

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

## Édition des fichiers statiques
Chaque fois que vous éditez du CSS ou du JavaScript, vous devrez exécuter la commande `collectstatic` de Django pour que vos changements aient un effet :
``` { .sh }
./bw-dev collectstatic
```

Si vous avez [installé yarn](https://yarnpkg.com/getting-started/install), vous pouvez exécuter `yarn watch:static` qui va exécuter automatiquement le script précédent à chaque fois qu'un changement se produit dans le répertoire `bookwyrm/static`.
