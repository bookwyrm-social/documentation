- - -
Title: Developer Environment Date: 2026-02-22 Order: 5
- - -

## Requisits previs

Aquestes instruccions assumeixen que estàs desenvolupant BookWyrm mitjançant Docker. Necessitaràs [instal·lar Docker](https://docs.docker.com/engine/install/) i [docker-compose](https://docs.docker.com/compose/install/) per començar.

_If you are contributing to BookWyrm in a dockerless development environment we would love for you to [help us update this guide](/documentation.html) to include instructions for setting up a dockerless development environment_.

## Configuració de l'entorn de desenvolupament

### Get the code

1. Aconsegueix una còpia del [codi base de BookWyrm a GitHub](https://github.com/bookwyrm-social/bookwyrm). Pots [crear una derivació](https://docs.github.com/en/get-started/quickstart/fork-a-repo) del repositori i, llavors [utilitzar `git clone` per descarregar el codi](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) a l'ordinador.
2. Ves al directori que conté el codi al teu ordinador, treballaràs des d'aquí d'ara en endavant.
3. Development occurs on the `main` branch, so ensure that is the branch you have checked out: `git checkout main`
4. Configura el teu fitxer de variables d'entorn de desenvolupament copiant el fitxer d'entorn d'exemple (`.env.example`) a un nou fitxer anomenat `.env`. A la línia de comandes, pots fer-ho mitjançant:

```{ .sh }
cp .env.example .env
```

### Build and run

1. A la línia de comandes, executa:

```{ .sh }
./bw-dev create_secrets       # Create the secrets file with random values. You only need to do this once.
./bw-dev dev up --build       # Build and start development stack
./bw-dev rundev python manage.py admin_code       # Shows the admin-code for initial setup. You only need to do this once.
```

1. Once the build is complete, you can access the instance at `http://localhost:1333`.
2. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

Si ets curiós: el comandament `./bw-dev` és un senzill script que fa funcionar unes altres eines: a sobre, pots ometre o iniciar directament `docker-composer build` o `docker-composer up` si vols. `./bw-dev` els recull tots a un lloc comú per comoditat. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Editant o creant Models

Si modifiqueu o creeu un model, és probable que canvieu l'estructura de la base de dades. A fi que aquests canvis siguin efectius, haureu d'executar l'ordre `makemigrations` de Django per a crear un [fitxer de migració de Django](https://docs.djangoproject.com/en/3.2/topics/migrations) nou, i després `migrar-lo`:

```{ .sh }
./bw-dev makemigrations
./bw-dev rundev python manage.py migrate
```

## Editant fitxers estàtics

Sempre que editeu el CSS o el JavaScript, haureu de tornar a executar l'ordre `collectstatic` a fi que els canvis tinguin efecte:

```{ .sh }
./bw-dev rundev python manage.py collectstatic
```

Si heu [instal·lat el Yarn](https://yarnpkg.com/getting-started/install), podeu executar `yarn watch:static` a fi que s'executi de forma automàtica l'script anterior cada cop que hi hagi un canvi al directori `bookwyrm/static`.

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
