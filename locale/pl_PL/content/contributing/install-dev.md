- - -
Title: Developer Environment Date: 2026-02-22 Order: 5
- - -

## Wymagania wstępne

Te instrukcje zakładają, że rozwijasz BookWyrm przy użyciu Docker. Aby rozpocząć, należy [zainstalować Docker](https://docs.docker.com/engine/install/) i [docker-compose](https://docs.docker.com/compose/install/).

_If you are contributing to BookWyrm in a dockerless development environment we would love for you to [help us update this guide](/documentation.html) to include instructions for setting up a dockerless development environment_.

## Konfigurowanie środowiska programistycznego

### Get the code

1. Uzyskaj kopię [kodu BookWyrm z GitHub](https://github.com/bookwyrm-social/bookwyrm). Możesz [zduplikować](https://docs.github.com/en/get-started/quickstart/fork-a-repo) repozytorium, a następnie [użyć `git clone`, aby pobrać kod](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) na swój komputer.
2. Katalog, na którym znajduje się kod na Twoim komputerze to miejsce, z którego od teraz będziesz pracować.
3. Development occurs on the `main` branch, so ensure that is the branch you have checked out: `git checkout main`
4. Skonfiguruj plik zmiennych środowiskowych swojego środowiska programistycznego kopiując przykładowy plik (`.env.example`) do nowego pliku o nazwie `.env`. W wierszu polecenia można to zrobić następująco:

```{ .sh }
cp .env.example .env
```

### Build and run

1. W wierszu polecenia wykonaj:

```{ .sh }
./bw-dev create_secrets       # Create the secrets file with random values. You only need to do this once.
./bw-dev dev up --build       # Build and start development stack
./bw-dev rundev python manage.py admin_code       # Shows the admin-code for initial setup. You only need to do this once.
```

1. Once the build is complete, you can access the instance at `http://localhost:1333`.
2. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

Dla ciekawskich: polecenie `./bw-dev` to prosty skrypt uruchamiający wiele różnych narzędzi: powyżej możesz pominąć je i wykonać `docker-compose build` lub `docker-compose up` bezpośrednio, jeśli chcesz. `./bw-dev` po prostu gromadzi je wszystkie w jednym miejscu. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Edytowanie lub tworzenie modeli

Zmieniając lub tworząc model prawdopodobnie ulegnie zmianie struktura bazy danych. Aby te zmiany zostały zastosowane, należy uruchomić polecenie Django `makemigrations`, aby utworzyć nowy [plik migracji Django](https://docs.djangoproject.com/en/3.2/topics/migrations), a następnie przenieść go (`migrate`):

```{ .sh }
./bw-dev makemigrations
./bw-dev rundev python manage.py migrate
```

## Edytowanie plików statycznych

Za każdym razem, gdy edytujesz CSS lub JavaScript, należy ponownie uruchomić polecenie Django `collectstatic`, aby miany zostały zastosowane:

```{ .sh }
./bw-dev rundev python manage.py collectstatic
```

Jeśli [zainstalowano yarn](https://yarnpkg.com/getting-started/install), możesz wykonać `yarn watch:static`, aby automatycznie wykonać poprzedni skrypt za każdym razem, gdy zajdzie zmiana w katalogu `bookwyrm/static`.

## Run code-linters and formatters

Before submitting patch, you should check ruff and other formatting tools. For those to work nicely, you should make sure you have development web-container and dev-tools build.

```{ .sh}
./bw-dev dev build # This is needed only once, if you haven't run dev stack previously
./bw-dev dev build dev-tools # This is needed only once and if you change pyproject.toml or Dockerfile
```

After those commands, you can run formatters and pytest and mypy with bw-dev command:

```{ .sh}
./bw-dev formatters
./bw-dev mypy
./bw-dev pytest
```

## Run development code behind ngrok or other tunneling/proxy service

In `.env.dev`:

1. If you use a tunneling/proxy service like [ngrok](https://ngrok.com), set `DOMAIN` to to the domain name you are using (e.g. `abcd-1234.ngrok-free.app`).
2. If you need to use a particular port other than 1333, change PORT to wanted port (e.g. `PORT=1333`).

Check that you have [all the required settings configured](/environment.html#required-environment-settings) before proceeding.

If you try to register your admin account and see a message that `CSRF verification failed` you may have set your domain or port incorrectly.

## Email (optional)

If you want to test sending emails, you will need to [set up appropriate real values](/environment.html#email-configuration) in the "Email config" section. You do not need to change anything for [the separate `EMAIL` setting](/environment.html#email). These settings are in `.env` -file
