- - -
Titolo: Strumento linea di comando Data: 2021-11-11 Ordine: 9
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

Esegue un comando arbitrario (rappresentato da `args`) nel contenitore `web`.

Equivalente a `docker-compose run --rm web`.

### service_ports_web args

Esegue un comando arbitrario nel contenitore `web` (rappresentato sopra da `args`) con porte esposte. Questo è utile se vuoi eseguire `test pdb` perché `runweb` non esporrà il prompt `pdb`.

Equivalente a `docker-compose run --rm --service-ports web`.

### shell

Apri una shell interattiva di Django all'interno del contenitore docker `web`. Puoi usarlo se vuoi eseguire direttamente i comandi della shell Django.

### up [args]

Avvia o riavvia i contenitori Docker, opzionalmente includi gli argomenti (rappresentati da `args`). Equivalente a `docker-compose up --build [args]`

## Gestione del database

### initdb

Inizializza un database.

### makemigrations [appname migration number]

_This command is not available on the `production` branch_.

Esegue il comando `makemigrations` di Django all'interno del contenitore Docker. Se hai cambiato la struttura del database in un ramo di sviluppo, dovrai eseguirlo così che le modifiche abbiano effetto. Facoltativamente, puoi specificare una migrazione specifica da eseguire, ad esempio `./bw-dev makemigrations bookwyrm 0108`

### migrate

Esegue il comando `migrate` di Django all'interno del contenitore Docker. È sempre necessario eseguire questo dopo `makemigrations`.

### resetdb

_This command is not available on the `production` branch_.

Resetta il database. **Questo comando eliminerà l'intero database di Bookwyrm**, quindi avvierà un nuovo database ed eseguirà tutte le migrazioni. È necessario eliminare qualsiasi file di migrazione recente che non si desidera eseguire, _prima di_ eseguire `resetdb`.

## Gestione di un'istanza Bookwyrm

### compile_themes

Compila tutti i temi di BookWyrm, che sono file `*.scss` in `bookwyrm/static/css/themes`.

### collectstatic

Migrate static assets to either a Docker container or to an S3-compatible "bucket", depending on the context.

### generate_preview_images

Genera un'anteprima per siti, utenti e libri. Può richiedere un po' di tempo se il database è molto grande. See [Optional Features: Generating preview images](/optional_features.html)

### remove_remote_user_preview_images

Remove generated preview images for remote users. See [Optional Features: Removing preview images for remote users](/optional_features.html)

### generate_thumbnails

Genera le thumbnail per le copertine dei libri.

### populate_streams args

Re-populates Redis streams (user feeds). You will not usually need to run this unless there is an error that wipes out your user feeds for some reason. You can specify which stream using the `--stream` argument.

### populate_list_streams

Re-populates Redis cache of lists. You will not usually need to run this unless there is an error that wipes out your users' lists for some reason.

### populate_suggestions

Populate suggested users for all users. You may want to run this manually to refresh suggestions.

### restart_celery

Riavvia il contenitore Docker `celery_worker`.

### update

Quando ci sono cambiamenti in `production`, puoi aggiornare la tua istanza senza tempo fuori servizio.

Questo comando fa `git pull` degli ultimi aggiornamenti sul branch `production`, genera immagini docker se necessario, esegue migrazioni Django, aggiorna i file statici e riavvia tutti i contenitori Docker.

### admin_code

Ottiene il codice amministratore segreto utilizzato per registrare l'utente amministratore iniziale su una nuova istanza di BookWyrm.

## Impostazione dello storage compatibile con S3

By default, BookWyrm uses local storage for static assets (favicon, default avatar, etc.), and media (user avatars, book covers, etc.), but you can use an external storage service to serve these files. BookWyrm uses django-storages to handle external storage, such as S3-compatible services, Apache Libcloud or SFTP.

See [External Storage](/external-storage.html) for more information.

### copy_media_to_s3

Migrate all uploaded media from an existing BookWyrm installation to an S3-compatible "bucket". Use for initial upload to an empty bucket.

### sync_media_to_s3

Sync new or changed uploaded media from an existing Bookwrym installation to an S3-compatible "bucket". Use to ensure all local files are uploaded to an existing bucket.

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

Compila file di traduzione. See [Django's compilemessages](https://docs.djangoproject.com/en/3.2/ref/django-admin/#compilemessages).

### pytest args

Esegui test con `pytest`.

### deactivate_2fa

Disattiva l'autenticazione a due fattori per un determinato utente.

### manual_confirm

Conferma l'email degli utenti, imposta l'utente a attivare.
