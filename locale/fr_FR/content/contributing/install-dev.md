- - -
Title: Developer Environment Date: 2026-02-22 Order: 5
- - -

## Prérequis

Ces instructions supposent que vous développez BookWyrm en utilisant Docker. Vous devrez [installer Docker](https://docs.docker.com/engine/install/) et [docker-compose](https://docs.docker.com/compose/install/) avant toute chose.

_If you are contributing to BookWyrm in a dockerless development environment we would love for you to [help us update this guide](/documentation.html) to include instructions for setting up a dockerless development environment_.

## Mise en place de l'environnement de développement

### Get the code

1. Obtenez une copie de [la base code de BookWyrm depuis GitHub](https://github.com/bookwyrm-social/bookwyrm). Vous pouvez [créer un fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) du dépôt, puis [utiliser `git clone` pour télécharger le code](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) sur votre ordinateur.
2. Allez dans le répertoire qui contient le code sur votre ordinateur, vous travaillerez désormais à partir de ce répertoire.
3. Development occurs on the `main` branch, so ensure that is the branch you have checked out: `git checkout main`
4. Configurez votre fichier de variables d'environnement de développement en copiant le fichier d'environnement d'exemple (`.env.example`) dans un nouveau fichier nommé `.env`. En ligne de commande, vous pouvez le faire en tapant :

```{ .sh }
cp .env.example .env
```

### Build and run

1. En ligne de commande, exécutez :

```{ .sh }
./bw-dev create_secrets       # Create the secrets file with random values. You only need to do this once.
./bw-dev dev up --build       # Build and start development stack
./bw-dev rundev python manage.py admin_code       # Shows the admin-code for initial setup. You only need to do this once.
```

1. Once the build is complete, you can access the instance at `http://localhost:1333`.
2. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

Pour les curieux·ses : la commande `./bw-dev` est un simple script shell qui exécute divers autres outils ; au lieu des commandes ci-dessus, vous auriez pu exécuter `docker-compose build` ou `docker-compose up` directement si vous le souhaitez. `./bw-dev` les rassemble dans un seul endroit pour plus de commodité. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Édition ou création du modèle de données

Si vous créez ou modifiez un modèle, vous changerez probablement la structure de la base de données. Pour que ces changements aient des effets, vous devrez utiliser la commande `makemigrations` de Django pour créer un nouveau [fichier de migration Django](https://docs.djangoproject.com/en/3.2/topics/migrations), puis la commande `migrate` pour le migrer :

```{ .sh }
./bw-dev makemigrations
./bw-dev rundev python manage.py migrate
```

## Édition des fichiers statiques

Chaque fois que vous éditez du CSS ou du JavaScript, vous devrez exécuter la commande `collectstatic` de Django pour que vos changements aient un effet :

```{ .sh }
./bw-dev rundev python manage.py collectstatic
```

Si vous avez [installé yarn](https://yarnpkg.com/getting-started/install), vous pouvez exécuter `yarn watch:static` qui va exécuter automatiquement le script précédent à chaque fois qu'un changement se produit dans le répertoire `bookwyrm/static`.

## Run code-linters and formatters

Before submitting patch, you should check ruff and other formatting tools. For those to work nicely, you should make sure you have development web-container and dev-tools build.

```{ .sh}
./bw-dev dev build # This is needed only once, if you haven't run dev stack previously
./bw-dev dev build dev-tools # This is needed only once and if you change pyproject.toml or Dockerfile
```

After those commands, you can run formatters and pytest and mypy with bw-dev command:

```{ .sh}
./bw-dev formatters
./bw-dev mypy
./bw-dev pytest
```

## Run development code behind ngrok or other tunneling/proxy service

In `.env.dev`:

1. If you use a tunneling/proxy service like [ngrok](https://ngrok.com), set `DOMAIN` to to the domain name you are using (e.g. `abcd-1234.ngrok-free.app`).
2. If you need to use a particular port other than 1333, change PORT to wanted port (e.g. `PORT=1333`).

Check that you have [all the required settings configured](/environment.html#required-environment-settings) before proceeding.

If you try to register your admin account and see a message that `CSRF verification failed` you may have set your domain or port incorrectly.

## Email (optional)

If you want to test sending emails, you will need to [set up appropriate real values](/environment.html#email-configuration) in the "Email config" section. You do not need to change anything for [the separate `EMAIL` setting](/environment.html#email). These settings are in `.env` -file
