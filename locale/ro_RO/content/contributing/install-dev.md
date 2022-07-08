- - -
Title: Developer Environment Date: 2021-04-12 Order: 3
- - -

## Cerințe preliminare

These instructions assume you are developing BookWyrm using Docker. You'll need to [install Docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/) to get started.

## Configurați mediul de dezvoltare

- Obțineți o copie a [bazei de cod BookWyrm de pe GitHub](https://github.com/bookwyrm-social/bookwyrm). Puteți [crea un fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) al depozitului și apoi [folosi `git clone` pentru a descărca codul](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) pe calculatorul dumneavoastră.
- Mergeți în dosarul care conține codul pe calculatorul dvs, veți lucra aici de aici în colo.
- Configurați fișierul de variabile de mediu al dvs. copiind fișierul de mediu exemplu (`.env.example`) într-un nou fișier numit `.env`. În linia de comandă, puteți face asta cu:
``` { .sh }
cp .env.example .env
```
- În `.env`, schimbați `DEBUG` în `true`
- Opțional, puteți folosi un serviciu precum [ngrok](https://ngrok.com/) pentru a configura un nume de domeniu și seta variabila `DOMAIN` în fișierul dumneavoastră `.env` în numele de domeniu generat de ngrok.

- Configurați nginx pentru dezvoltare prin copierea fișierului de configurație nginx (`nginx/development`) într-un nou fișier numit `nginx/default.conf`:
``` { .sh }
cp nginx/development nginx/default.conf
```

- Porniți aplicația. În linia de comandă, rulați:
``` { .sh }
./bw-dev build            # Build the docker images
./bw-dev setup            # Initialize the database and run migrations
./bw-dev up               # Start the docker containers
```
- Odată compilarea terminată, puteți accesa instanța la `http://localhost:1333` și crea un utilizator administrator.

If you're curious: the `./bw-dev` command is a simple shell script runs various other tools: above, you could skip it and run `docker-compose build` or `docker-compose up` directly if you like. `./bw-dev` just collects them into one common place for convenience. Run it without arguments to get a list of available commands, read the [documentation page](/command-line-tool.html) for it, or open it up and look around to see exactly what each command is doing!

### Editați sau configurați modele

If you change or create a model, you will probably change the database structure. For these changes to have effect you will need to run Django's `makemigrations` command to create a new [Django migrations file](https://docs.djangoproject.com/en/3.2/topics/migrations), and then `migrate` it:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

### Editați fișiere statice
Any time you edit the CSS or JavaScript, you will need to run Django's `collectstatic` command again in order for your changes to have effect:
``` { .sh }
./bw-dev collectstatic
```

If you have [installed yarn](https://yarnpkg.com/getting-started/install), you can run `yarn watch:static` to automatically run the previous script every time a change occurs in `bookwyrm/static` directory.
