- - -
Title: Środowisko programistyczne Date: 2021-04-12 Order: 3
- - -

## Wymagania wstępne

Te instrukcje zakładają, że rozwijasz BookWyrm przy użyciu Docker. Aby rozpocząć, należy [zainstalować Docker](https://docs.docker.com/engine/install/) i [docker-compose](https://docs.docker.com/compose/install/).

## Konfigurowanie środowiska programistycznego

- Uzyskaj kopię [kodu BookWyrm z GitHub](https://github.com/bookwyrm-social/bookwyrm). Możesz [zduplikować](https://docs.github.com/en/get-started/quickstart/fork-a-repo) repozytorium, a następnie [użyć `git clone`, aby pobrać kod](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) na swój komputer.
- Katalog, na którym znajduje się kod na Twoim komputerze to miejsce, z którego od teraz będziesz pracować.
- Skonfiguruj plik zmiennych środowiskowych swojego środowiska programistycznego kopiując przykładowy plik (`.env.example`) do nowego pliku o nazwie `.env`. W wierszu polecenia można to zrobić następująco:
``` { .sh }
cp .env.example .env
```
- W pliku `.env` zmień `DEBUG` na `true`
- Jeśli chcesz, możesz skorzystać z usług, takich jak [ngrok](https://ngrok.com/), aby skonfigurować nazwę domeny oraz ustawić zmienną `DOMAIN` w swoim pliku `.env` dla nazwy domeny wygenerowanej przez ngrok.

- Set up nginx for development by copying the developer nginx configuration file (`nginx/development`) into a new file named `nginx/default.conf`:
``` { .sh }
cp nginx/development nginx/default.conf
```

- Start the application. In the command line, run:
``` { .sh }
./bw-dev build            # Build the docker images
./bw-dev setup            # Initialize the database and run migrations
./bw-dev up               # Start the docker containers
```
- Once the build is complete, you can access the instance at `http://localhost:1333` and create an admin user.

If you're curious: the `./bw-dev` command is a simple shell script runs various other tools: above, you could skip it and run `docker-compose build` or `docker-compose up` directly if you like. `./bw-dev` just collects them into one common place for convenience. Run it without arguments to get a list of available commands, read the [documentation page](/command-line-tool.html) for it, or open it up and look around to see exactly what each command is doing!

### Editing or creating Models

If you change or create a model, you will probably change the database structure. For these changes to have effect you will need to run Django's `makemigrations` command to create a new [Django migrations file](https://docs.djangoproject.com/en/3.2/topics/migrations), and then `migrate` it:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

### Editing static files
Any time you edit the CSS or JavaScript, you will need to run Django's `collectstatic` command again in order for your changes to have effect:
``` { .sh }
./bw-dev collectstatic
```

If you have [installed yarn](https://yarnpkg.com/getting-started/install), you can run `yarn watch:static` to automatically run the previous script every time a change occurs in `bookwyrm/static` directory.
