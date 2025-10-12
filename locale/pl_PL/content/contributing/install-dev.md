- - -
Title: Developer Environment Date: 2025-05-26 Order: 5
- - -

## Wymagania wstępne

Te instrukcje zakładają, że rozwijasz BookWyrm przy użyciu Docker. Aby rozpocząć, należy [zainstalować Docker](https://docs.docker.com/engine/install/) i [docker-compose](https://docs.docker.com/compose/install/).

## Konfigurowanie środowiska programistycznego

### Get the code

1. Uzyskaj kopię [kodu BookWyrm z GitHub](https://github.com/bookwyrm-social/bookwyrm). Możesz [zduplikować](https://docs.github.com/en/get-started/quickstart/fork-a-repo) repozytorium, a następnie [użyć `git clone`, aby pobrać kod](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) na swój komputer.
2. Katalog, na którym znajduje się kod na Twoim komputerze to miejsce, z którego od teraz będziesz pracować.
3. Development occurs on the `main` branch, so ensure that is the branch you have checked out: `git checkout main`
4. Skonfiguruj plik zmiennych środowiskowych swojego środowiska programistycznego kopiując przykładowy plik (`.env.example`) do nowego pliku o nazwie `.env`. W wierszu polecenia można to zrobić następująco:
``` { .sh }
cp .env.example .env
```

### Configure your environment settings

In `.env`:

4. change `DEBUG` to `true`
5. If you use a tunneling/proxy service like [ngrok](https://ngrok.com), set `DOMAIN` to to the domain name you are using (e.g. `abcd-1234.ngrok-free.app`). Otherwise, set `DOMAIN` to `localhost`
6. change `NGINX_SETUP` to `reverse_proxy` (this prevents BookWyrm trying to set up https certificates on your development machine)
7. If you need to use a particular port (e.g. if you are tunneling via ngrok), uncomment `PORT` and set it (e.g. `PORT=1333`). If using `localhost` this is optional.

Check that you have [all the required settings configured](/environment.html#required-environment-settings) before proceeding.

If you try to register your admin account and see a message that `CSRF verification failed` you may have set your domain or port incorrectly.

### Email (optional)

If you want to test sending emails, you will need to [set up appropriate real values](/environment.html#email-configuration) in the "Email config" section. You do not need to change anything for [the separate `EMAIL` setting](/environment.html#email).

### Build and run

8. W wierszu polecenia wykonaj:

``` { .sh }
./bw-dev build            # Build the docker images
./bw-dev setup            # Initialize the database and run migrations. Note the ADMIN key at the end of this output. You'll need it to register the first admin user.
./bw-dev up               # Start the docker containers
```

9. Once the build is complete, you can access the instance at `http://localhost`, your ngrok domain, or `http://localhost:{PORT}`, depending on you domain and port configuration.
10. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

Dla ciekawskich: polecenie `./bw-dev` to prosty skrypt uruchamiający wiele różnych narzędzi: powyżej możesz pominąć je i wykonać `docker-compose build` lub `docker-compose up` bezpośrednio, jeśli chcesz. `./bw-dev` po prostu gromadzi je wszystkie w jednym miejscu. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Edytowanie lub tworzenie modeli

Zmieniając lub tworząc model prawdopodobnie ulegnie zmianie struktura bazy danych. Aby te zmiany zostały zastosowane, należy uruchomić polecenie Django `makemigrations`, aby utworzyć nowy [plik migracji Django](https://docs.djangoproject.com/en/3.2/topics/migrations), a następnie przenieść go (`migrate`):

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

## Edytowanie plików statycznych
Za każdym razem, gdy edytujesz CSS lub JavaScript, należy ponownie uruchomić polecenie Django `collectstatic`, aby miany zostały zastosowane:
``` { .sh }
./bw-dev collectstatic
```

Jeśli [zainstalowano yarn](https://yarnpkg.com/getting-started/install), możesz wykonać `yarn watch:static`, aby automatycznie wykonać poprzedni skrypt za każdym razem, gdy zajdzie zmiana w katalogu `bookwyrm/static`.
