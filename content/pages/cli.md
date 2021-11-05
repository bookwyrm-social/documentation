Title: Command Line Tool
Date: 2021-11-06

Bookwyrm developers and instance managers can use the `bw-dev` script for common tasks. This can make your commands shorter, easier to remember, and harder mess up.

Once you have installed Bookwyrm [in production](installing-in-production.html) or [in development](https://docs.joinbookwyrm.com/developer-environment.html#setting_up_the_developer_environment), you can run the script from the command line with `./bw-dev` followed by the subcommand you want to run.

## Docker shortcuts

### bash

Open an interactive `bash` session inside the docker `web` container.

### build

Equivalent to `docker-compose build`.

### dbshell

Open an interactive Postgres database shell. I hope you know what you're doing.

### run

Run an arbitrary command in the `web` cointainer.

Equivalent to `docker-compose run --rm --service-ports web`. 

### rundb

TODO: this command does not appear to actually exist!

### runweb [args]

Run an arbitrary command in the `web` container.

Equivalent to `docker-compose run --rm web`.

### shell

Open an interactive Django shell inside the docker `web` container. You would use this if you want to run Django shell commands directly. For example when [making your initial user a superuser](installing-in-production.html#configure_your_instance).

### up [args]

Start or restart Docker containers. Equivalent to `docker-compose up --build [args]`

## Managing the database

### initdb

Initialize a database.

### makemigrations

Runs Django's `makemigrations` command inside your Docker container. If you have changed the database structure in a development branch you will need to run this for your changes to have effect.

### migrate

Runs Django's `migrate` command inside your Docker container. You always need to run this after `makemigrations`.

### resetdb

Reset the database. **This command will delete your entire Bookwyrm database**. You should probably not run it in production! It is however useful for development servers. Note that `resetdb` will also initialise a fresh database and run all migrations, so you should delete any recent migration files you do not want to run, _before_ running `resetdb`.s

## Managing a Bookwyrm instance

### collectstatic

Migrate static assets to either a Docker container or to an S3-compatible "bucket", depending on the context.

### generate_preview_images

Does what it says on the tin. Generate preview images for site, users, and books. This can take a while if you have a large database.

### populate_streams

Re-populates Redis streams (user feeds). You will usually need to run this after `update`.

### populate_suggestions

Populate suggested users for all users. You may want to run this manually to refresh suggestions, for some reason.

### restart_celery

Restarts the `celery_worker` Docker container.

### update

When there are changes to the `production` branch, you can update your instance without downtime.

This command `git pull`s the latest `production` branch updates, builds docker images if necessary, runs Django migrations, updates static files, and restarts all Docker containers.

## Setting up S3 compatible storage

By default, BookWyrm uses local storage for static assets (favicon, default avatar, etc.), and media (user avatars, book covers, etc.), but you can use an external storage service to serve these files. BookWyrm uses django-storages to handle external storage, such as S3-compatible services, Apache Libcloud or SFTP.

See [External Storage](/external-storage.html) for more information.

### copy_media_to_s3

Migrate uploaded media from an existing Bookwrym installation to an S3-compatible "bucket".

### set_cors_to_s3 [filename]

Copy a CORS rules JSON file to your S3 bucket, where `filename` is the name of your JSON file (e.g. `./bw-dev set_cors_to_s3 cors.json`)

## Development and testing

### black

BookWyrm uses the Black code formatter to keep the Python codebase consistent styled. Run `black` before committing your changes so the `pylint` task does not fail for your pull request and make you sad.

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

### pytest

Run tests. This will not provide a coverage report if your tests fail: in that case use `test` for the coverage report.

### test

Run [a coverage report](https://coverage.readthedocs.io/en/6.1.1/cmd.html#cmd-run) to see how good unit test coverage is.

### generate_thumbnails

TODO: is this the same as generate_preview_images???
