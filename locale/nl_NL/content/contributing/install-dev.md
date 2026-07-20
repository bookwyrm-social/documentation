- - -
Title: Developer Environment Date: 2026-02-22 Order: 5
- - -

## Vereisten

Deze instructies gaan ervan uit dat je BookWyrm ontwikkelt met Docker. Je moet [Docker](https://docs.docker.com/engine/install/) en [docker-compose](https://docs.docker.com/compose/install/) installeren om aan de slag te gaan.

_If you are contributing to BookWyrm in a dockerless development environment we would love for you to [help us update this guide](/documentation.html) to include instructions for setting up a dockerless development environment_.

## Het instellen van de ontwikkelaarsomgeving

### Ontvang de code

1. Krijg een kopie van [de BookWyrm codebase van GitHub](https://github.com/bookwyrm-social/bookwyrm). You can [create a fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) of the repository, and then [use `git clone` to download the code](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) to your computer.
2. Go to the directory which contains the code on your computer, you'll be working from there from here on out.
3. Development occurs on the `main` branch, so ensure that is the branch you have checked out: `git checkout main`
4. Set up your development environment variables file by copying the example environment file (`.env.example`) into a new file named `.env`. In de opdrachtregel kun je dit doen met:

```{ .sh }
cp .env.example .env
```

### Build and run

1. Voer op de opdrachtregel het volgende uit:

```{ .sh }
./bw-dev create_secrets       # Create the secrets file with random values. You only need to do this once.
./bw-dev dev up --build       # Build and start development stack
./bw-dev rundev python manage.py admin_code       # Shows the admin-code for initial setup. You only need to do this once.
```

1. Once the build is complete, you can access the instance at `http://localhost:1333`.
2. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

If you're curious: the `./bw-dev` command is a simple shell script runs various other tools: above, you could skip it and run `docker-compose build` or `docker-compose up` directly if you like. `./bw-dev` just collects them into one common place for convenience. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Het bewerken of maken van modellen

Als je een model wijzigt of creëert, dan verander je waarschijnlijk de structuur van de database. For these changes to have effect you will need to run Django's `makemigrations` command to create a new [Django migrations file](https://docs.djangoproject.com/en/3.2/topics/migrations), and then `migrate` it:

```{ .sh }
./bw-dev makemigrations
./bw-dev rundev python manage.py migrate
```

## Statische bestanden bewerken

Any time you edit the CSS or JavaScript, you will need to run Django's `collectstatic` command again in order for your changes to have effect:

```{ .sh }
./bw-dev rundev python manage.py collectstatic
```

If you have [installed yarn](https://yarnpkg.com/getting-started/install), you can run `yarn watch:static` to automatically run the previous script every time a change occurs in `bookwyrm/static` directory.

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

## Email (optioneel)

If you want to test sending emails, you will need to [set up appropriate real values](/environment.html#email-configuration) in the "Email config" section. You do not need to change anything for [the separate `EMAIL` setting](/environment.html#email). These settings are in `.env` -file
