- - -
Title: Developer Environment Date: 2025-05-26 Order: 5
- - -

## Requisitos previos

Estas instrucciones asumen que estás desarrollando BookWyrm usando Docker. Necesitarás [install Docker](https://docs.docker.com/engine/install/) y [docker-compose](https://docs.docker.com/compose/install/) para empezar.

## Configurar el entorno de desarrollo

### Get the code

1. Obtén una copia de [el código base de BookWyrm desde GitHub](https://github.com/bookwyrm-social/bookwyrm). Puedes [crear un fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) del repositorio y [usar `git clone` para descargar el código](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) a tu computadora.
2. Ve al directorio que contiene el código en tu computadora, podrás estar trabajando aquí desde allí.
3. Configura el archivo de variables del entorno de desarrollo copiando el archivo de ejemplo (`.env.example`) en un nuevo archivo llamado `.env`. En la línea de comando, puedes hacer esto con:
``` { .sh }
cp .env.example .env
```

### Configure your environment settings

In `.env`:

4. change `DEBUG` to `true`
5. If you use a tunneling/proxy service like [ngrok](https://ngrok.com), set `DOMAIN` to to the domain name you are using (e.g. `abcd-1234.ngrok-free.app`). Otherwise, set `DOMAIN` to `localhost`
6. change `NGINX_SETUP` to `reverse_proxy` (this prevents BookWyrm trying to set up https certificates on your development machine)
7. If you need to use a particular port (e.g. if you are tunneling via ngrok), uncomment `PORT` and set it (e.g. `PORT=1333`). If using `localhost` this is optional.

If you try to register your admin account and see a message that `CSRF verification failed`, you should check these settings, as you may have set your domain or port incorrectly.

### Email (optional)

If you want to test sending emails, you will need to [set up appropriate values](/environment.html#email-configuration) in the "Email config" section. You do not need to change anything for [the separate `EMAIL` setting](/environment.html#email).

### Build and run

8. En la línea de comandos, ejecuta:

``` { .sh }
./bw-dev build            # Build the docker images
./bw-dev setup            # Initialize the database and run migrations. Note the ADMIN key at the end of this output. You'll need it to register the first admin user.
./bw-dev up               # Start the docker containers
```

9. Once the build is complete, you can access the instance at `http://localhost`, your ngrok domain, or `http://localhost:{PORT}`, depending on you domain and port configuration.
10. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

Si tienes curiosidad: el comando `./bw-dev` es un código de shell simple que corre varias herramientas: arriba, puedes omitirlo y correr `docker-compose build` o `docker-compose up` directamente si quieres. `./bw-dev` solo los recoge en un lugar común para su conveniencia. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Editar o crear modelos

Si modificas o creas un modelo, probablemente también modifiques la estructura de la base de datos. Para que estos cambios surtan efecto necesitas correr el comando `makemigrations` de Django para crear un nuevo [archivo de migraciones de Django](https://docs.djangoproject.com/en/3.2/topics/migrations), y luego `migrarlo`:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

## Editar archivos estáticos
Cada vez que edites CSS o JavaScript, necesitarás ejecutar el comando `collectstatic` de Django otra vez para que los cambios tengan efecto:
``` { .sh }
./bw-dev collectstatic
```

Si tienes [instalado yarn](https://yarnpkg.com/getting-started/install), puedes ejecutar `yarn watch:static` para correr automáticamente el código previo cada vez que ocurra un cambio en el directorio `bookwyrm/static`.
