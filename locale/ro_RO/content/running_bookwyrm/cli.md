- - -
Title: Command Line Tool Date: 2021-11-11 Order: 9
- - -

Dezvoltatorii BookWyrm și managerii de instanțe pot folosi scriptul `bw-dev` pentru sarcinile comune. Poate face comenzile dvs. mai scurte, mai ușor de reținut și mai greu de confundat.

Odată ce ați instalat BookWyrm [în producție](installing-in-production.html) sau [în dezvoltare](https://docs.joinbookwyrm.com/developer-environment.html#setting_up_the_developer_environment), puteți rula scriptul din linia de comandă cu `./bw-dev` urmat de o subcomandă pe care doriți să o rulați.

## Scurtături Docker

### bash

Deschide o sesiune interactivă de `bash` în interiorul containerului docker `web`.

### build

Echivalent cu `docker-compose build`.

### dbshell

Deschide un shell interactiv pentru baza de date Postgres. Sper că știți ceea ce faceți.

### runweb args

Rulează o comandă arbitrară (reprezentată deasupra de `args`) în containerul `web`.

Echivalent cu `docker-compose run --rm web`.

### service_ports_web args

Rulează o comandă arbitrară în containerul `web` (reprezentată deasupra de `args`) cu porturile expuse. Aceasta este utilă dacă vreți să rulați teste `pdb` deoarece `runweb` nu expune promptul `pdb`.

Echivalent cu `docker-compose run --rm --service-ports web`.

### shell

Deschide un shell interactiv Django în interiorul containerului docker `web`. O veți folosi dacă vreți să rulați comenzi de shell Django direct.

### up [args]

Pornește sau repornește containerele Dcoker, opțional incluzând orice argument(reprezentat mai sus de `args`). Echivalent cu `docker-compose up --build [args]`

## Gestionarea bazei de date

### initdb

Inițializează o bază de date.

### makemigrations [appname migration number]

_Această comandă nu este disponibilă în ramura de `producție`_.

Rulează comanda Django `makemigrations` în interiorul containerului dvs. Docker. Dacă ați schimbat structura bazei de date în ramura de dezvoltare veți avea nevoie să o rulați pentru ca schimbările dvs. să aibă efect. Opțional, puteți specifica o migrație specifică pe care să o rulați, de ex. `./bw-dev makemigrations bookwyrm 0108`

### migrate

Rulează comanda Django `migrate` în interiorul containerului dvs. Docker. Veți avea nevoie mereu de a o rula după `makemigrations`.

### resetdb

_Această comandă nu este disponibilă în ramura de `producție`_.

Resetează baza de date. **Această comandă va șterge întreaga bază de date BookWyrm**, iar apoi va iniția o bază de date nouă și rula toate migrațiile. Va trebui să ștergeți orice fișier de migrație recent pe care nu vreți să-l rulați _înainte_ de a rula `resetdb`.

## Gestionarea unei instanțe BookWyrm

### compile_themes

Compiles all BookWyrm themes, which are `*.scss` files listed in `bookwyrm/static/css/themes`.

### collectstatic

Migrate static assets to either a Docker container or to an S3-compatible "bucket", depending on the context.

### generate_preview_images

Generate preview images for site, users, and books. This can take a while if you have a large database. See [Optional Features: Generating preview images](/optional_features.html)

### remove_remote_user_preview_images

Remove generated preview images for remote users. See [Optional Features: Removing preview images for remote users](/optional_features.html)

### generate_thumbnails

Generates thumbnail images for book covers.

### populate_streams args

Re-populates Redis streams (user feeds). You will not usually need to run this unless there is an error that wipes out your user feeds for some reason. You can specify which stream using the `--stream` argument.

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

## Configurați stocare S3 compatibilă

By default, BookWyrm uses local storage for static assets (favicon, default avatar, etc.), and media (user avatars, book covers, etc.), but you can use an external storage service to serve these files. BookWyrm uses django-storages to handle external storage, such as S3-compatible services, Apache Libcloud or SFTP.

See [External Storage](/external-storage.html) for more information.

### copy_media_to_s3

Migrate all uploaded media from an existing BookWyrm installation to an S3-compatible "bucket". Use for initial upload to an empty bucket.

### sync_media_to_s3

Sync new or changed uploaded media from an existing BookWyrm installation to an S3-compatible "bucket". Use to ensure all local files are uploaded to an existing bucket.

### set_cors_to_s3 filename

Copy a CORS rules JSON file to your S3 bucket, where `filename` is the name of your JSON file (e.g. `./bw-dev set_cors_to_s3 cors.json`)

## Dezvoltare și testare

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

### deactivate_2fa

Deactivates two factor authentication for a given user.

### manual_confirm

Confirms a users email, sets the user to active.
