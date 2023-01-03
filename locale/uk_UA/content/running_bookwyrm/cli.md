- - -
Title: Command Line Tool Date: 2021-11-11 Order: 9
- - -

Розробники і менеджери bookwyrm можуть використовувати скрипт `bw-dev` для загальних завдань. Це може зробити команди коротшими, зручнішими до запам'ятання, і складніше робити помилки.

Once you have installed Bookwyrm [in production](installing-in-production.html) or [in development](https://docs.joinbookwyrm.com/developer-environment.html#setting_up_the_developer_environment), you can run the script from the command line with `./bw-dev` followed by the subcommand you want to run.

## Docker shortcuts

### bash

Open an interactive `bash` session inside the docker `web` container.

### build

Equivalent to `docker-compose build`.

### dbshell

Open an interactive Postgres database shell. I hope you know what you're doing.

### runweb args

Run an arbitrary command (represented above by `args`) in the `web` container.

Equivalent to `docker-compose run --rm web`.

### service_ports_web args

Run an arbitrary command in the `web` container (represented above by `args`) with ports exposed. This is useful if you want to run `pdb` tests because `runweb` will not expose the `pdb` prompt.

Equivalent to `docker-compose run --rm --service-ports web`.

### shell

Open an interactive Django shell inside the docker `web` container. You would use this if you want to run Django shell commands directly.

### up [args]

Start or restart Docker containers, optionally including any arguments (represented above by `args`). Equivalent to `docker-compose up --build [args]`

## Managing the database

### initdb

Initialize a database.

### makemigrations [appname migration number]

_This command is not available on the `production` branch_.

Runs Django's `makemigrations` command inside your Docker container. If you have changed the database structure in a development branch you will need to run this for your changes to have effect. Optionally, you can specify a specific migration to run, e.g. `./bw-dev makemigrations bookwyrm 0108`

### migrate

Runs Django's `migrate` command inside your Docker container. You always need to run this after `makemigrations`.

### resetdb

_This command is not available on the `production` branch_.

Resets the database. **This command will delete your entire Bookwyrm database**, and then initiate a fresh database and run all migrations. You should delete any recent migration files you do not want to run, _before_ running `resetdb`.

## Managing a Bookwyrm instance

### compile_themes

Компілює всі BookWyrm теми, які є `*.scss` файлами, перелічені в `bookwyrm/static/css/themes`.

### collectstatic

Migrate static assets to either a Docker container or to an S3-compatible "bucket", depending on the context.

### generate_preview_images

Generate preview images for site, users, and books. This can take a while if you have a large database. See [Optional Features: Generating preview images](/optional_features.html)

### remove_remote_user_preview_images

Remove generated preview images for remote users. See [Optional Features: Removing preview images for remote users](/optional_features.html)

### generate_thumbnails

Generates thumbnail images for book covers.

### populate_streams args

Re-populates Redis streams (user feeds). Зазвичай вам не потрібно це запускати, якщо немає помилки, яка зачищає ваші стрічки користувачів з якихось причин. You can specify which stream using the `--stream` argument.

### populate_list_streams

Re-populates Redis cache of lists. You will not usually need to run this unless there is an error that wipes out your users' lists for some reason.

### populate_suggestions

Populate suggested users for all users. You may want to run this manually to refresh suggestions.

### restart_celery

Restarts the `celery_worker` Docker container.

### update

When there are changes to the `production` branch, you can update your instance without downtime.

This command `git pull`s the latest `production` branch updates, builds docker images if necessary, runs Django migrations, updates static files, and restarts all Docker containers.

### admin_code

Gets the secret admin code used to register the inital admin user on a new BookWyrm instance.

## Setting up S3 compatible storage

By default, BookWyrm uses local storage for static assets (favicon, default avatar, etc.), and media (user avatars, book covers, etc.), but you can use an external storage service to serve these files. BookWyrm uses django-storages to handle external storage, such as S3-compatible services, Apache Libcloud or SFTP.

See [External Storage](/external-storage.html) for more information.

### copy_media_to_s3

Migrate all uploaded media from an existing BookWyrm installation to an S3-compatible "bucket". Use for initial upload to an empty bucket.

### sync_media_to_s3

Sync new or changed uploaded media from an existing BookWyrm installation to an S3-compatible "bucket". Use to ensure all local files are uploaded to an existing bucket.

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

Запустити тести з `pytest`.

### deactivate_2fa

Деактивує двофакторну аутентифікацію для цього користувача.

### manual_confirm

Confirms a users email, sets the user to active.
