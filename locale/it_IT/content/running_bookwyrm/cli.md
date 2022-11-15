- - -
Title: Command Line Tool Date: 2021-11-11 Order: 9
- - -

Gli sviluppatori e i gestori di istanze di Bookwyrm possono utilizzare lo script `bw-dev` per le attività comuni. Questo può rendere i tuoi comandi più brevi, più facile da ricordare, e più difficile da sbagliare.

Una volta installato Bookwyrm [in produzione](installing-in-production.html) o [in sviluppo](https://docs.joinbookwyrm.com/developer-environment.html#setting_up_the_developer_environment), è possibile eseguire lo script dalla riga di comando con `. bw-dev` seguito dal sottocomando che si desidera eseguire.

## Scorciatoie Docker

### bash

Apri una sessione interattiva `bash` all'interno del contenitore `web` docker.

### build

Equivalente a `docker-compose build`.

### dbshell

Apri una shell interattiva per il database Postgres. Spero che tu sappia cosa stai facendo.

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

Resetta il database. **Questo comando eliminerà l'intero database di Bookwyrm**, quindi avvierà un nuovo database ed eseguirà tutte le migrazioni. È necessario eliminare qualsiasi file di migrazione recente che non si desidera eseguire, _prima di_ eseguire `resetdb`.

## Gestione di un'istanza Bookwyrm

### collectstatic

Migrare risorse statiche a un contenitore Docker o a un "bucket" compatibile con S3, a seconda del contesto.

### generate_preview_images

Genera immagini di anteprima per sito, utenti e libri. Questo può richiedere un po' di tempo se il database è molto grande.

### generate_thumbnails

Genera le miniature per le copertine dei libri.

### populate_streams args

Ripopolare i flussi Redis (feed utente). Di solito non è necessario eseguire questo a meno che non vi sia un errore che cancella i tuoi feed utente per qualche motivo. Puoi specificare quale stream usando l'argomento `--stream`.

### populate_list_streams

Ripopola la cache Redis delle liste. Di solito non è necessario eseguire questo a meno che non vi sia un errore che cancella le tue liste per qualche motivo.

### populate_suggestions

Popolare utenti suggeriti per tutti gli utenti. Potresti voler eseguire manualmente questa operazione per aggiornare i suggerimenti.

### restart_celery

Riavvia il contenitore Docker `celery_worker`.

### aggiorna

When there are changes to the `production` branch, you can update your instance without downtime.

This command `git pull`s the latest `production` branch updates, builds docker images if necessary, runs Django migrations, updates static files, and restarts all Docker containers.

### admin_code

Gets the secret admin code used to register the inital admin user on a new BookWyrm instance.

## Impostazione dello storage compatibile con S3

Per impostazione predefinita, BookWyrm utilizza la memoria locale per le risorse statiche (favicon, avatar predefinito, ecc...) e supporti (avatar utente, copertine di libri, ecc.), ma è possibile utilizzare un servizio di archiviazione esterno per questi file. BookWyrm utilizza django-storages per gestire l'archiviazione esterna come ad esempio servizi compatibili con S3, Apache Libcloud o SFTP.

See [External Storage](/external-storage.html) for more information.

### copy_media_to_s3

Migrare tutti i media caricati da un'installazione di Bookwrym esistente a un "bucket" compatibile con S3. Use for initial upload to an empty bucket.

### sync_media_to_s3

Sincronizza i media caricati, nuovi o modificati da un'installazione di Bookwrym esistente a un "bucket" compatibile con S3. Utilizzare per garantire che tutti i file locali siano caricati su un bucket esistente.

### set_cors_to_s3 filename

Copy a CORS rules JSON file to your S3 bucket, where `filename` is the name of your JSON file (e.g. `./bw-dev set_cors_to_s3 cors.json`)

## Sviluppo e test

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
