- - -
Title: Installing in Production Date: 2025-04-01 Order: 1
- - -

Este proyecto es todavía joven y por el momento no es muy estable, así que por favor proceda con precaución cuando se ejecuta en producción.

## Configuración del Servidor
- Obtenga un nombre de dominio y configure DNS para su servidor. Tendrá que apuntar los servidores de nombres de su dominio en su proveedor de DNS al servidor donde usted hospedará BookWyrm. Aquí hay instrucciones para [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Configure su servidor con los cortafuegos adecuados para ejecutar una aplicación web (este conjunto de instrucciones sé probo contra Ubuntu 20.04). Aquí hay instrucciones para [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Configure un servicio de correo electrónico (como [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) y las configuraciones apropiadas de SMTP/DNS. Utilice la documentación del servicio para configurar su DNS
- [Instale docker y docker-compose](https://docs.docker.com/compose/install/)

## Instalar y configurar BookWyrm

There are several repos in the BookWyrm org, including documentation, a static landing page, and the actual Bookwyrm code. To run BookWyrm, you want the actual app code which is in [bookwyrm-social/bookwyrm](https://github.com/bookwyrm-social/bookwyrm).

La rama `producción` de BookWyrm contiene una serie de herramientas que no están en la rama `principal` que son aptas para funcionar en producción, tales como cambios en `docker-compose` para actualizar los comandos por defecto o la configuración de contenedores, y cambios individuales a la configuración del contenedor para habilitar cosas como SSL o copias de seguridad regulares.

Instrucciones para ejecutar BookWyrm en producción:

- Obtenga el código de aplicación: `git clone git@github.com:bookwyrm-social/bookwyrm.git`
- Cambie a la rama de `producción`: `git checkout producción`
- Cree el archivo de variables de entorno, `cp .env.example .env`y actualice lo siguiente:
    - `DOMAIN` | Su dominio web
    - `EMAIL` | Dirección de correo electrónico que se utilizará para la verificación de dominio con certbot
    - `FLOWER_USER` | Tu propio nombre de usuario para acceder al monitor de colas Flower
    - `EMAIL_HOST_USER` | La dirección "desde" que tu aplicación utilizará al enviar correo electrónico
    - `EMAIL_HOST_PASSWORD` | La contraseña proporcionada por tu servicio de correo electrónico
- Initialize secrets by running `bw-dev create_secrets` or manually update following in `.env`:
    - `SECRET_KEY` | Una cadena secreta de caracteres
    - `POSTGRES_PASSWORD` | Establecer una contraseña segura para la base de datos
    - `REDIS_ACTIVITY_PASSWORD` | Establecer una contraseña segura para el subsistema Redis Activity
    - `REDIS_ACTIVITY_PASSWORD` | Establecer una contraseña segura para el subsistema Redis Activity
    - `FLOWER_PASSWORD` | Tu propia contraseña segura para acceder al monitor de cola Flower
    - Si está ejecutando otro servidor web en su máquina, necesitará seguir las instrucciones [reverse-proxy](/reverse-proxy.html)
- Setup ssl certificate via letsencrypt by running `./bw-dev init_ssl`
- Inicializa la base de datos ejecutando `./bw-dev migrate`
- Run the application with `docker-compose up --build`, and make sure all the images build successfully
    - Si está ejecutando otros servicios en su máquina host, puede encontrarse con errores en los que los servicios fallan al intentar enlazar a un puerto. Consulte la guía [de solución de problemas](#port_conflicts) para obtener consejos sobre cómo resolver esto.
- Cuando docker se ha construido con éxito, detener el proceso con `CTRL-C`
- Si desea utilizar un almacenamiento externo para recursos estáticos y archivos multimedia (como un servicio compatible con S3), [sigue las instrucciones](/external-storage.html) hasta que te indique que vuelvas aquí
- Inicializa la aplicación con `./bw-dev configuración`, y copia el código de administración a usar cuando crees tu cuenta de administrador.
    - La salida de `./bw-dev configuración` debe terminar con tu código de administración. Puedes obtener tu código en cualquier momento ejecutando `./bw-dev admin_code` desde la línea de comandos. Aquí hay un ejemplo de salida:

``` { .sh }
***********************************************
Utiliza este código para crear tu cuenta de administrador:
c6c35779-af3a-4091-b330-c026610920d6
***************************************************
```

- Ejecutar docker-compose en segundo plano con: `docker-compose up -d`
- La aplicación debería estar ejecutándose en su dominio. Cuando cargues el dominio, deberías obtener una página de configuración que confirma la configuración de tu instancia y un formulario para crear una cuenta de administrador. Usa tu código de administración para registrarte.

¡Felicidades! ¡Lo ha conseguido!! Configura tu instancia como desees.


## Respaldos

El servicio db de BookWyrm hace volcar una copia de seguridad de su base de datos a su directorio `/backups` todos los días a medianoche UTC. Las copias de seguridad se llaman `backup__%Y-%m-%d.sql`.

El servicio db tiene un script opcional para podar periódicamente el directorio de copias de seguridad de modo que todas las copias de seguridad diarias recientes se entiendan, pero para copias de seguridad más antiguas, sólo las copias de seguridad semanales o mensuales están aseguradas. Para activar este script:

- Descomentar la línea final en `postgres-docker/cronfile`
- reconstruir la instancia `docker-compose up --build`

Puede copiar copias de seguridad del volumen de las copias de seguridad a su máquina host con `docker cp`:

- Ejecute `docker-compose ps` para confirmar el nombre completo del servicio de db (probablemente sea `bookwyrm_db_1`.
- Ejecutar `docker cp <container_name>:/respaldos <host machine path>`

## Conflictos de puertos

BookWyrm tiene múltiples servicios que se ejecutan en sus puertos predeterminados. Esto significa que, dependiendo de qué más se está ejecutando en su máquina host, puede incurrir en errores al construir o ejecutar BookWyrm cuando fallen los intentos de enlazar con esos puertos.

Si esto ocurre, necesitará cambiar su configuración para ejecutar servicios en diferentes puertos. Esto puede requerir uno o más cambios en los siguientes archivos:

- `docker-compose.yml`
- `nginx/production.conf` or `nginx/reverse_proxy.conf` depending on NGINX_SETUP in .env-file
- `.env` (Usted crea este archivo usted mismo durante la configuración)

Si ya está ejecutando un servidor web en su máquina, necesitará configurar un proxy reverso.

## Conéctate

Debido a que BookWyrm es un proyecto joven, todavía estamos trabajando hacia un programa de publicación estable, y hay muchos errores y cambios de ruptura. Hay un equipo de GitHub que puede ser etiquetado cuando hay algo importante para saber acerca de una actualización, que puede unirse compartiendo su nombre de usuario de GitHub. Hay algunas maneras de ponerse en contacto:

 - Open an issue or pull request to add your instance to the [official list](https://joinbookwyrm.com/instances/)
 - Póngase en contacto con el proyecto en [Mastodon](https://tech.lgbt/@bookwyrm) o [envíe un correo electrónico al mantenedor](mailto:mousereeve@riseup.net) directamente con su nombre de usuario de GitHub
 - Únete a la sala de chat [Matrix](https://matrix.to/#/#bookwyrm:matrix.org)
