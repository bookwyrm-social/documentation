- - -
Title: Developer Environment Date: 2026-02-22 Order: 5
- - -

## Requisitos previos

Estas instrucciones asumen que estás desarrollando BookWyrm usando Docker. Necesitarás [install Docker](https://docs.docker.com/engine/install/) y [docker-compose](https://docs.docker.com/compose/install/) para empezar.

_If you are contributing to BookWyrm in a dockerless development environment we would love for you to [help us update this guide](/documentation.html) to include instructions for setting up a dockerless development environment_.

## Configurar el entorno de desarrollo

### Obtener el código

1. Obtén una copia de [el código base de BookWyrm desde GitHub](https://github.com/bookwyrm-social/bookwyrm). Puedes [crear un fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) del repositorio y [usar `git clone` para descargar el código](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) a tu computadora.
2. Ve al directorio que contiene el código en tu computadora, podrás estar trabajando aquí desde allí.
3. Development occurs on the `main` branch, so ensure that is the branch you have checked out: `git checkout main`
4. Configura el archivo de variables del entorno de desarrollo copiando el archivo de ejemplo (`.env.example`) en un nuevo archivo llamado `.env`. En la línea de comando, puedes hacer esto con:

```{ .sh }
cp .env.example .env
```

### Compilar y ejecutar

1. En la línea de comandos, ejecuta:

```{ .sh }
./bw-dev create_secrets       # Create the secrets file with random values. You only need to do this once.
./bw-dev dev up --build       # Build and start development stack
./bw-dev rundev python manage.py admin_code       # Shows the admin-code for initial setup. You only need to do this once.
```

1. Once the build is complete, you can access the instance at `http://localhost:1333`.
2. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

Si tienes curiosidad: el comando `./bw-dev` es un código de shell simple que corre varias herramientas: arriba, puedes omitirlo y correr `docker-compose build` o `docker-compose up` directamente si quieres. `./bw-dev` solo los recoge en un lugar común para su conveniencia. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Editar o crear modelos

Si modificas o creas un modelo, probablemente también modifiques la estructura de la base de datos. Para que estos cambios surtan efecto necesitas correr el comando `makemigrations` de Django para crear un nuevo [archivo de migraciones de Django](https://docs.djangoproject.com/en/3.2/topics/migrations), y luego `migrarlo`:

```{ .sh }
./bw-dev makemigrations
./bw-dev rundev python manage.py migrate
```

## Editar archivos estáticos

Cada vez que edites CSS o JavaScript, necesitarás ejecutar el comando `collectstatic` de Django otra vez para que los cambios tengan efecto:

```{ .sh }
./bw-dev rundev python manage.py collectstatic
```

Si tienes [instalado yarn](https://yarnpkg.com/getting-started/install), puedes ejecutar `yarn watch:static` para correr automáticamente el código previo cada vez que ocurra un cambio en el directorio `bookwyrm/static`.

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

1. Si utilizas un servicio túnel/proxy, como [ngrok](https://ngrok.com), pon `DOMAIN` al nombre de dominio que estás usando (por ej. `abcd-1234.ngrok-free.app`).
2. If you need to use a particular port other than 1333, change PORT to wanted port (e.g. `PORT=1333`).

Check that you have [all the required settings configured](/environment.html#required-environment-settings) before proceeding.

If you try to register your admin account and see a message that `CSRF verification failed` you may have set your domain or port incorrectly.

## Email (opcional)

If you want to test sending emails, you will need to [set up appropriate real values](/environment.html#email-configuration) in the "Email config" section. You do not need to change anything for [the separate `EMAIL` setting](/environment.html#email). These settings are in `.env` -file
