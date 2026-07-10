---
Title: Command Line Tool
Date: 2025-04-28
Order: 2
---

Bookwyrm developers and instance managers can use the `bw-dev` script for common tasks. This can make your commands shorter, easier to remember, and harder to mess up.

Once you have installed Bookwyrm [in production](install-prod.html) or [in development](https://docs.joinbookwyrm.com/install-dev.html#setting-up-the-developer-environment), you can run the script from the command line with `./bw-dev` followed by the subcommand you want to run.

Some commands only run in development environments, most can be run in either development or production, and a small number should only be run in production. Development commands run in a dedicated Docker environment configured in `docker-compose.dev.yml`, whereas production commands run in the production environment configured in `docker-compose.yml`. Production containers and volumes have names starting with `bookwyrm`, and development containers and volumes start with `dev-wyrm`

## Development commands

These commands always run in the `dev-wyrm` container, without needing to use the `dev` prefix. They generally are commands that interact with the local file system.

In the standard BookWyrm docker configuration, `dev-wyrm` uses a bind mount to link the BookWyrm directory on the host machine to the container file system.

### devcommand _args_

You can use `devcommand` to run an arbitrary `docker compose` command with development-related flags e.g. `./bw-dev devcommand restart`.

### makemigrations

Runs Django's `makemigrations` command inside your Docker container. If you have changed the database structure in a development branch you will need to run this for your changes to have effect.

If your production BookWyrm has diverged from the production code for some reason and you need to use `makemigrations`, you will need to run this command against the development database, then `build` against production. See [this issue for more detail](https://github.com/bookwyrm-social/bookwyrm/issues/3919).

### pytest [args]

Run tests with `pytest`. You can add pytest arguments to this command to check only a certain directory or file, or include logging (`-s`), omit coverage reports (`--no-cov`) etc.

### Internationalisation and localisation

#### makemessages

Finds all translation strings in the app and puts them in the one reference file, `locale/en_US/LC_MESSAGES/django.po`. After you have run `makemessages` you need to run `compilemessages` to compile the translations. See [Django's makemessages](https://docs.djangoproject.com/en/5.2/ref/django-admin/#makemessages).

#### compilemessages

Compiles translation files. See [Django's compilemessages](https://docs.djangoproject.com/en/5.2/ref/django-admin/#compilemessages).

#### update_locales

Runs `makemessages` followed by `compilemessages`.

### Formatters and linters

#### mypy

Runs the [`mypy` type checker](https://www.mypy-lang.org). We are gradually adding type checking to the BookWyrm codebase. This is not required for code contributions, but is encouraged.

#### ruff

Runs the [ruff](https://docs.astral.sh/ruff/) formatter and linter. (i.e. `ruff format` followed by `ruff check`).

#### ruff-format

Runs the [ruff](https://docs.astral.sh/ruff/) formatter. (i.e. `ruff format`).

#### ruff-check

Runs the [ruff](https://docs.astral.sh/ruff/) linter. (i.e. `ruff check`).

#### ruff-fix

Auto-fix errors identified by the ruff linter. (i.e. `ruff check --fix`).

#### eslint

Runs [eslint](https://eslint.org/) to lint JavaScript in the `bookwyrm/static` directory.

#### prettier

BookWyrm uses [Prettier](https://prettier.io/) to keep the JavaScript codebase consistently styled. Run `prettier` before committing changes to scripts to automatically format your code.

#### stylelint

BookWyrm uses [Stylelint](uhttps://stylelint.io/) to keep the CSS files consistently styled. Run `stylelint` before committing changes to scripts to automatically format your code.

#### formatters

This command runs all code formatters (`ruff format`, `ruff check`, `prettier`,`eslint`  and `stylelint`) in one go.

## Dangerous development commands

These commands only run if you use the `dev` prefix. This ensures that they run in the `dev-wyrm` container, but also serves as a reminder that they should not run in production. These commands can be dangerous or highly destructive and you should ensure you understand what they do before using them!

### clean

Remove all stopped Docker containers.

Equivalent to:

```shell
docker-compose stop
docker-compose rm -f
```

### collectstatic_watch

Runs [`npm watch`](https://www.npmjs.com/package/watch) against the `static` directory.

### resetdb

**This command will delete your entire Bookwyrm database**. It then initiates a fresh database and runs all migrations. You should delete any recent migration files you do not want to use, _before_ running `resetdb`.

### service_ports_web _args_

Run an arbitrary command in the `web` container (represented above by `args`) with ports exposed. This is useful if you want to run `pdb` tests because `runweb` will not expose the `pdb` prompt.

Equivalent to `docker-compose run --rm --service-ports web`.

## Dual purpose commands

These commands are designed to run in production, but can be prefixed with `dev` to run in the development environment (i.e. in the `dev-wrym` containers). For example `./bw-dev dev migrate` or `./bw-dev dev up -d`

### create_secrets

Automatically populates your `.env` file with random cryptographically secure values for the following secret keys:

* `SECRET_KEY`
* `POSTGRES_PASSWORD`
* `REDIS_ACTIVITY_PASSWORD`
* `REDIS_BROKER_PASSWORD`
* `FLOWER_PASSWORD`

### setup

Run this command to set up a new BookWyrm instance. This will:

* run all database migrations
* run `initdb`
* compile themes
* run `collectstatic`
* print the admin code to the console

### initdb

Initialize a database.

### init_ssl

Initialize SSL with LetsEncrypt.

### admin_code

Gets the secret admin code used to register the inital admin user on a new BookWyrm instance.

### up [args]

Start or restart Docker containers, optionally including any arguments (represented above by `args`). Equivalent to `docker compose up [args]`

### down

Equivalent to [`docker compose down`](https://docs.docker.com/reference/cli/docker/compose/down/).

### build

Equivalent to `docker-compose build`.

### migrate [appname migration number]

Runs Django's `migrate` command inside your Docker container. Optionally, you can specify a specific migration to run, e.g. `./bw-dev makemigrations bookwyrm 0108`. You always need to run this after `makemigrations`, but it also runs automatically when using `./bw-dev [dev] up`.

### runweb _args_

Run an arbitrary command (represented above by `args`) in the `web` container.

Equivalent to `docker-compose run --rm web`.

### bash

Open an interactive `bash` session inside the docker `web` container.

### shell

Open an interactive Django shell inside the docker `web` container. You would use this if you want to run Django shell commands directly.

### dbshell

Open an interactive Postgres database shell. I hope you know what you're doing.

### compile_themes

Compiles all BookWyrm themes, which are `*.scss` files listed in `bookwyrm/static/css/themes`.

### collectstatic

Migrate static assets to either a Docker container or to an S3-compatible "bucket", depending on the context. See Django's [collectstatic](https://docs.djangoproject.com/en/5.2/ref/contrib/staticfiles/#collectstatic) for more detail.

### populate_streams _args_

Re-populates Redis streams (user feeds). You will not usually need to run this unless there is an error that wipes out your user feeds for some reason. You can specify which stream using the `--stream` argument.

### populate_list_streams

Re-populates Redis cache of lists. You will not usually need to run this unless there is an error that wipes out your users' lists for some reason.

### populate_suggestions

Populate suggested users for all users. You may want to run this manually to refresh suggestions.

### restart_celery

Restarts the `celery_worker` Docker container.

### generate_thumbnails

Generates thumbnail images for book covers.

### generate_preview_images

Generate preview images for site, users, and books. This can take a while if you have a large database. See [Optional Features: Generating preview images](/optional_features.html)

### remove_remote_user_preview_images

Remove generated preview images for remote users. See [Optional Features: Removing preview images for remote users](/optional_features.html)

### set_cors_to_s3 filename

Copy a CORS rules JSON file to your S3 bucket, where `filename` is the name of your JSON file (e.g. `./bw-dev set_cors_to_s3 cors.json`)

### remove_2fa _username_

Deactivates two factor authentication for a given user identified by _username_.

### confirm_email _username_

Confirms a users email, sets the user to active.

### docker_cache_cleanup

Prunes all docker build caches older than 24 hours, and reports space taken by Docker containers, images, volumes, and build caches.

## Production-only commands

You would not normally use these commands in development. When developing, be cautious with the s3 commands as they may incur unexpected data transfer costs, or potentially overwrite production data.

_Setting up S3 compatible storage_

By default, BookWyrm uses local storage for static assets (favicon, default avatar, etc.), and media (user avatars, book covers, etc.), but you can use an external storage service to serve these files. BookWyrm uses django-storages to handle external storage, such as S3-compatible services, Apache Libcloud or SFTP.

### update

When there are changes to the `production` branch, you can update your instance without downtime.

This command `git pull`s the latest `production` branch updates, builds docker images if necessary, runs Django migrations, updates static files, and restarts all Docker containers.

See [External Storage](/external-storage.html) for more information.

### copy_media_to_s3

Migrate all uploaded media from an existing BookWyrm installation to an S3-compatible "bucket". Use for initial upload to an empty bucket.

### sync_media_to_s3

Sync new or changed uploaded media from an existing BookWyrm installation to an S3-compatible "bucket". Use to ensure all local files are uploaded to an existing bucket.

## Utilities

These commands are designed for one-off needs.

### upgrade_db_version

Runs a Postgres database upgrade to Postgres version `17`. This was introduced in BookWyrm `v0.8.0`, where Django was upgraded to version `5.2` and the minimum required Postgres version moved to version `14`, with `17` preferred.
