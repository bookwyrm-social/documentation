- - -
Título: Developer Environment Fecha: 2021-04-12 Orden: 3
- - -

## Requisitos previos

Estas instrucciones asumen que estás desarrollando BookWyrm usando Docker. Necesitarás [install Docker](https://docs.docker.com/engine/install/) y [docker-compose](https://docs.docker.com/compose/install/) para empezar.

## Configurar el entorno de desarrollo

- Obtén una copia de [el código base de BookWyrm desde GitHub](https://github.com/bookwyrm-social/bookwyrm). Puedes [crear un fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) del repositorio y [usar `git clone` para descargar el código](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) a tu computadora.
- Ve al directorio que contiene el código en tu computadora, podrás estar trabajando aquí desde allí.
- Configura el archivo de variables del entorno de desarrollo copiando el archivo de ejemplo (`.env.example`) en un nuevo archivo llamado `.env`. En la línea de comando, puedes hacer esto con:
``` { .sh }
cp .env.example .env
```
- En `.env`, cambia `DEBUG` a `true`.
- Opcionalmente, puedes utilizar un servicio como [ngrok](https://ngrok.com/) para configurar el nombre del dominio, y establece la variable `DOMAIN` en tu archivo `.env` al nombre de dominio generado por ngrok.

- Configura nginx para el desarrollo copiando el archivo de configuración (`nginx/development`) a un nuevo archivo llamado `nginx/default.conf`:
``` { .sh }
cp nginx/development nginx/default.conf
```

- Inicia la aplicación. En la línea de comandos, ejecuta:
``` { .sh }
./bw-dev build            # Construye las imágenes docker
./bw-dev setup            # Inicializa la base de datos y corre las migraciones
./bw-dev up               # Inicia los contenedores docker
```
- Una vez que la compilación esté completa, puedes acceder a la instancia en `http://localhost:1333` y crea un usuario admin.

Si tienes curiosidad: el comando `./bw-dev` es un código de shell simple que corre varias herramientas: arriba, puedes omitirlo y correr `docker-compose build` o `docker-compose up` directamente si quieres. `./bw-dev` solo los recoge en un lugar común para su conveniencia. Ejecútalo sin argumentos para obtener una lista de comandos disponibles. Lee la [página de documentación](/command-line-tool.html) para ello, o ábrelo y revisa qué hace exactamente cada comando!

### Editar o crear modelos

Si modificas o creas un modelo, probablemente también modifiques la estructura de la base de datos. Para que estos cambios surtan efecto necesitas correr el comando `makemigrations` de Django para crear un nuevo [archivo de migraciones de Django](https://docs.djangoproject.com/en/3.2/topics/migrations), y luego `migrarlo`:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

### Editar archivos estáticos
Cada vez que edites CSS o JavaScript, necesitarás ejecutar el comando `collectstatic` de Django otra vez para que los cambios tengan efecto:
``` { .sh }
./bw-dev collectstatic
```

Si tienes [instalado yarn](https://yarnpkg.com/getting-started/install), puedes ejecutar `yarn watch:static` para correr automáticamente el código previo cada vez que ocurra un cambio en el directorio `bookwyrm/static`.
