Bookwyrm developers and instance managers can use the `bw-dev` script for common tasks. This can make your commands shorter, easier to remember, and harder to mess up.

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

Reinicia o banco de dados. **Este comando vai excluir todo o banco de dados da BookWyrm**, criar outro banco de dados e executar todas as migrações. Você deve deletar todos os arquivos de migração recentes que não quer rodar _antes_ de executar `resetdb`.

## Gerenciando uma instância BookWyrm

### collectstatic

Migra os recursos estáticos para um container Docker ou para um "bucket" compatível com S3, dependendo do contexto.

### generate_preview_images

Gera imagens de pré-visualização de sites, usuários e livros. Isso pode demorar algum tempo se você tiver um banco de dados grande.

### generate_thumbnails

Gera miniaturas das capas dos livros.

### populate_streams args

Preenche novamente os streams do Redis (feeds dos usuários). Você geralmente não vai precisar rodar isto a não ser que haja algum erro que apague seus feeds de usuários por algum motivo. Você pode escpecificar o stream utilizando o argumento `--stream`.

### populate_list_streams

Preenche novamente o cache de listas do Redis. Você geralmente não vai precisar executar isso a não ser que haja um erro que apaguei as listas dos usuários por algum motivo.

### populate_suggestions

Gera sugestões de usuários para todos os usuários. Você pode executar isso manualmente para atualizar as sugestões.

### restart_celery

Reinicia o container Docker do `celery_worker`.

### update

When there are changes to the `production` branch, you can update your instance without downtime.

This command `git pull`s the latest `production` branch updates, builds docker images if necessary, runs Django migrations, updates static files, and restarts all Docker containers.

### admin_code

Gets the secret admin code used to register the inital admin user on a new BookWyrm instance.

## Setting up S3 compatible storage

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
