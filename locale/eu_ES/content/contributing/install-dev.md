- - -
Title: Developer Environment Date: 2026-02-22 Order: 5
- - -

## Aurrebaldintzak

Jarraibide hauen arabera, BookWyrm ari zara garatzen Docker erabiliz. Ezer baino lehenago instalatu behar dituzu [Docker](https://docs.docker.com/engine/install/) eta [docker-compose](https://docs.docker.com/compose/install/).

_If you are contributing to BookWyrm in a dockerless development environment we would love for you to [help us update this guide](/documentation.html) to include instructions for setting up a dockerless development environment_.

## Garapen ingurunearen konfigurazioa

### Get the code

1. Eskura ezazu [GitHub-etik BookWyrm-en kode-basea](https://github.com/bookwyrm-social/bookwyrm). Paketearen [fork bat sortu](https://docs.github.com/en/get-started/quickstart/fork-a-repo) dezakezu, ondotik [erabili `git clone` kodea deskargatzeko](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) zure ordenagailuan.
2. Joan zure ordenagailuko kodea duen direktoriora, orain direktorio honetatik lan egingo duzu.
3. Development occurs on the `main` branch, so ensure that is the branch you have checked out: `git checkout main`
4. Konfigura ezazu zure garapen-inguruneko aldagaien artxiboa, inguruneko adibide-fitxategia (`.env.example`) `.env` izeneko fitxategi berri batean kopiatuz. Komando-lerroan, hori egin dezakezu idatziz:

```{ .sh }
cp .env.example .env
```

### Build and run

1. Komando-lerroan, exekutatu:

```{ .sh }
./bw-dev create_secrets       # Create the secrets file with random values. You only need to do this once.
./bw-dev dev up --build       # Build and start development stack
./bw-dev rundev python manage.py admin_code       # Shows the admin-code for initial setup. You only need to do this once.
```

1. Once the build is complete, you can access the instance at `http://localhost:1333`.
2. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

Kuriosa bazara: `./bw-dev` komandoa shell skript soil bat da eta beste hainbat tresna exekutatzen ditu: aurreko komandoen ordez, zuk `docker-compose build` edo `docker-compose up` exekutatzen ahal zenuen zuzenean, nahi izanez gero. `./bw-dev` komandoak leku bakar batean biltzen ditu erosotasun gehiagorako. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Ereduak editatzea edo sortzea

Eredu bat aldatzen edo sortzen baduzu, seguruenik datu-basearen egitura aldatuko duzu. Aldaketa horiek eragina izan dezaten, Djangoko `makemigrations` komandoa exekutatu beharko duzu [Django migrations file](https://docs.djangoproject.com/en/3.2/topics/migrations) berri bat sortzeko, eta, ondoren, `migrate` komandoa, azken hau migratzeko:

```{ .sh }
./bw-dev makemigrations
./bw-dev rundev python manage.py migrate
```

## Fitxategi estatikoak editatzea

CSS edo JavaScript kodea editatzen duzun bakoitzean, berriro exekutatu beharko duzu `collectstatic` komandoa, zure aldaketek eragina izan dezaten:

```{ .sh }
./bw-dev rundev python manage.py collectstatic
```

[yarn instalatuta](https://yarnpkg.com/getting-started/install) baduzu, exekuta dezakezu `yarn watch:static`, `bookwyrm/static` errepertorioan aldaketa bat gertatzen den bakoitzean aurreko scripta automatikoki exekutatzeko.

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
