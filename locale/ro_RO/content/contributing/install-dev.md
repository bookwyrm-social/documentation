- - -
Title: Developer Environment Date: 2026-02-22 Order: 5
- - -

## Cerințe preliminare

Aceste instrucțiuni presupun că dezvoltați BookWyrm folosind Docker. Va trebui să [instalați Docker](https://docs.docker.com/engine/install/) și [docker-compose](https://docs.docker.com/compose/install/) pentru a începe.

_If you are contributing to BookWyrm in a dockerless development environment we would love for you to [help us update this guide](/documentation.html) to include instructions for setting up a dockerless development environment_.

## Configurați mediul de dezvoltare

### Get the code

1. Obțineți o copie a [bazei de cod BookWyrm de pe GitHub](https://github.com/bookwyrm-social/bookwyrm). Puteți [crea un fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) al depozitului și apoi [folosi `git clone` pentru a descărca codul](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) pe calculatorul dumneavoastră.
2. Mergeți în dosarul care conține codul pe calculatorul dvs, veți lucra aici de aici în colo.
3. Development occurs on the `main` branch, so ensure that is the branch you have checked out: `git checkout main`
4. Configurați fișierul de variabile de mediu al dvs. copiind fișierul de mediu exemplu (`.env.example`) într-un nou fișier numit `.env`. În linia de comandă, puteți face asta cu:

```{ .sh }
cp .env.example .env
```

### Build and run

1. În linia de comandă, rulați:

```{ .sh }
./bw-dev create_secrets       # Create the secrets file with random values. You only need to do this once.
./bw-dev dev up --build       # Build and start development stack
./bw-dev rundev python manage.py admin_code       # Shows the admin-code for initial setup. You only need to do this once.
```

1. Once the build is complete, you can access the instance at `http://localhost:1333`.
2. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

Dacă sunteți curios: comanda `./bw-dev` este un simplu script shell care rulează multe alte comenzi: deasupra, ați putea sări peste ea și rula `docker-compose build` sau `docker-compose up` direct dacă doriți. `./bw-dev` doar le colectează într-un singur loc pentru conveniență. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Editați sau configurați modele

Dacă schimbați sau creați un model, veți schimba probabil structura bazei de date. Pentru ca aceste schimbă să aibă efect va trebui să rulați comanda Django `makemigrations` pentru a crea un nou [fișier de migrare Django](https://docs.djangoproject.com/en/3.2/topics/migrations) și apoi `migrate`:

```{ .sh }
./bw-dev makemigrations
./bw-dev rundev python manage.py migrate
```

## Editați fișiere statice

De fiecare dată când editați CSS sau JavaScript, va trebui să rulați comanda Django `collectstatic` pentru ca schimbările dvs. să aibă efect:

```{ .sh }
./bw-dev rundev python manage.py collectstatic
```

Dacă aveți [yarn instalat](https://yarnpkg.com/getting-started/install), puteți rula `yarn watch:static` pentru a rula automat scriptul precedent de fiecare dată când o schimbare are loc în dosarul `bookwyrm/static`.

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
