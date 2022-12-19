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

Quando ci sono cambiamenti in `production`, puoi aggiornare la tua istanza senza tempi di inattività.

Questo comando `git pull`s negli ultimi aggiornamenti del ramo `produzione`, genera immagini docker se necessario, esegue migrazioni Django, aggiorna i file statici e riavvia tutti i contenitori Docker.

### admin_code

Ottieni il codice di amministrazione segreto utilizzato per registrare l'utente amministratore inital su una nuova istanza di BookWyrm.

## Impostazione dello storage compatibile con S3

Per impostazione predefinita, BookWyrm utilizza la memoria locale per le risorse statiche (favicon, avatar predefinito, ecc...) e supporti (avatar utente, copertine di libri, ecc.), ma è possibile utilizzare un servizio di archiviazione esterno per questi file. BookWyrm utilizza django-storages per gestire l'archiviazione esterna come ad esempio servizi compatibili con S3, Apache Libcloud o SFTP.

Vedi [Memoria esterna](/external-storage.html) per ulteriori informazioni.

### copy_media_to_s3

Migrare tutti i media caricati da un'installazione di Bookwrym esistente a un "bucket" compatibile con S3. Usa per il caricamento iniziale in un secchio vuoto.

### sync_media_to_s3

Sincronizza i media caricati, nuovi o modificati da un'installazione di Bookwrym esistente a un "bucket" compatibile con S3. Utilizzare per garantire che tutti i file locali siano caricati su un bucket esistente.

### set_cors_to_s3 filename

Copia un file JSON regole CORS nel tuo secchio S3, dove `nome del file` è il nome del tuo file JSON (e.. `./bw-dev set_cors_to_s3 cors.json`)

## Sviluppo e test

_Questi comandi non sono disponibili sul ramo `produzione`_.

### nero

BookWyrm utilizza il formattatore del codice [Black](https://github.com/psf/black) per mantenere coerente lo stile del codebase Python. Esegui `black` prima di effettuare le modifiche in modo che il task `pylint` non fallisca per la tua pull request e ti renda triste.

### prettier

BookWyrm utilizza [Prettier](https://prettier.io/) per mantenere il codice JavaScript costantemente stilizzato. Esegui `prettier` prima di inviare modifiche agli script per formattare automaticamente il codice.

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

### deactivate_2fa

Deactivates two factor authentication for a given user.

### manual_confirm

Confirms a users email, sets the user to active.
