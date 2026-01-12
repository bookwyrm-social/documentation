---
Title: Instalación sin Docker
Date: 2023-8-19
Order: 2
---

This project is still young and isn't, at the moment, very stable, so please proceed with caution when running in production.

This method of installation is more involved, and therefore is for more experienced admins. **Docker install is the recommended method** as there may not be much support available for Dockerless installation. If you have expertise in this area, we would love your help to improve this documentation!

This install method assumes you already have ssl configured with certificates available.

## Configuración del Servidor
- Obtén un nombre de dominio y configura el DNS para tu servidor. Tendrás que apuntar los servidores de nombres de tu dominio en tu proveedor de DNS al servidor donde hospedarás BookWyrm. Aquí hay instrucciones para [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Configura tu servidor con los cortafuegos adecuados para ejecutar una aplicación web (este conjunto de instrucciones se testeó en Ubuntu 20.04). Aquí hay instrucciones para [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Configura tu servicio de correo electrónico (como [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) y las configuraciones apropiadas de SMTP/DNS. Utiliza la documentación del servicio para configurar tu DNS
- Instala las dependencias. On debian this could look like `apt install postgresql redis nginx python3-venv python3-pip python3-dev libpq-dev gunicorn gettext-base`

## Instalar y configurar BookWyrm

La rama `production` de BookWyrm contiene una serie de herramientas que no están en la rama `main` y que son adecuadas para ejecutarse en production como: los cambios de `docker-compose` para actualizar los comandos predeterminados; o la configuración de los contenedores; y cambios individuales en la configuración del contenedor para habilitar cosas como SSL o copias de seguridad periódicas. No todos estos cambios afectan la instalación sin Docker, sin embargo, aún se recomienda la rama `producción`.

Instrucciones para ejecutar BookWyrm en producción sin Docker:

- Crea el directorio donde quieras instalar BookWyrm. Por ejemplo `/opt/bookwyrm`: `mkdir /opt/bookwyrm && cd /opt/bookwyrm`
- Get the application code, note that this only clones the `production` branch: `git clone https://github.com/bookwyrm-social/bookwyrm.git --branch production --single-branch ./`
- Create your environment variables file, `cp .env.example .env`, and update the following. Passwords should generally be enclosed in "quotation marks". You can use `bw-dev create_secrets` to generate passwords in `.env`-file:
    - `SECRET_KEY` | A difficult to guess, secret string of characters.
    - `DOMAIN` | Tu dominio web
    - `POSTGRES_PASSWORD` | Establece una contraseña segura para la base de datos
    - `POSTGRES_HOST` | Establece el `localhost` (la máquina ejecutando tu db)
    - `POSTGRES_USER` | Establecer a `bookwyrm` (recomendado) o algo personalizado (configurado más tarde)
    - `POSTGRES_DB` | Establécelo en `bookwyrm`
    - `REDIS_ACTIVITY_PASSWORD` | No establecer nada (en una máquina local con un cortafuegos está bien)
    - `REDIS_ACTIVITY_HOST` | Establecer en `localhost` (la máquina que ejecuta redis)
    - `REDIS_BROKER_PASSWORD` | Establecer en nada (bien en una máquina local con firewall)
    - `REDIS_BROKER_HOST` | Establecer en `localhost` (la máquina que ejecuta redis)
    - `EMAIL_HOST_USER` | La dirección "desde" la que tu aplicación enviará correos electrónicos
    - `EMAIL_HOST_PASSWORD` | La contraseña proporcionada por tu servicio de correo electrónico
- If you are on Debian and some other operating systems, you may need to create the `/var/cache/nginx` directory:
``` { .sh }
mkdir /var/cache/nginx
chown www-data:www-data /var/cache/nginx
```
- Configuración de Nginx
    - Copy the server_config to nginx's conf.d: `cp nginx/locations /etc/nginx/conf.d/locations`
    - Update nginx `/etc/nginx/conf.d/locations`:
        - Replace `/app` with your install directory `/opt/bookwyrm` everywhere in the file (including commented out)
    - Make a copy of the production template config and set it for use in nginx:
        - Set env-variables for DOMAIN and MAX_UPLOAD_MiB so envsubst can populate nginx templates. For example `export DOMAIN=your-web-domain MAX_UPLOAD_MiB=100`
        - `envsubst '$DOMAIN,$MAX_UPLOAD_MiB' < nginx/server_config > /etc/nginx/conf.d/server_config`
        - `envsubst '$DOMAIN,$MAX_UPLOAD_MiB' < nginx/server_name > /etc/nginx/conf.d/server_name`
        - `envsubst '$DOMAIN,$MAX_UPLOAD_MiB' < nginx/https.conf > /etc/nginx/sites-available/bookwyrm.conf`
    - If you are running another web-server on your host machine, you should use following command to use nginx as reverse-proxy: `envsubst '$DOMAIN,$MAX_UPLOAD_MiB' < nginx/reverse_proxy.conf > /etc/nginx/sites-available/bookwyrm.conf`
    - Update nginx `/etc/nginx/sites-available/bookwyrm.conf`:
        - Change the `ssl_certificate` and `ssl_certificate_key` paths to your fullchain and privkey locations if you are not using nginx as reverse-proxy
        - Change upstream addresses in lines 4 and 7 to `server localhost:8000` and `server localhost:8888`. Puedes elegir un puerto diferente aquí si lo deseas
    - Enable the nginx config: `ln -s /etc/nginx/sites-available/bookwyrm.conf /etc/nginx/sites-enabled/bookwyrm.conf`
     - Recarga nginx: `systemctl reload nginx`
- Configura el entorno virtual de python
    - Make the python venv directory in your install dir: `python3 -m venv ./venv`
    - Instala las dependencias de bookwyrm python con pip: `./venv/bin/pip3 install -r requirements.txt`
- Crea la base de datos postgresql de bookwyrm. Make sure to change the password to what you set in the `.env` config: `sudo -i -u postgres psql`

``` { .sql }
CREATE USER bookwyrm WITH PASSWORD 'securedbypassword123';

CREATE DATABASE bookwyrm TEMPLATE template0 ENCODING 'UNICODE';

ALTER DATABASE bookwyrm OWNER TO bookwyrm;

GRANT ALL PRIVILEGES ON DATABASE bookwyrm TO bookwyrm;

\q
```

- Migra el esquema de base de datos ejecutando `venv/bin/python3 manage.py migrate`
- Inicializa la base de datos ejecutando `venv/bin/python3 manage.py initdb`
- Compile the themes by running `venv/bin/python3 manage.py compile_themes`
- Create the static files by running `venv/bin/python3 manage.py collectstatic --no-input`
- Si deseas utilizar un almacenamiento externo para recursos estáticos y archivos multimedia (como un servicio compatible con S3), [sigue las instrucciones](/external-storage.html) hasta que te indique que vuelvas aquí
- Crea y configura tu usuario de `bookwyrm`
    - Agrega al usuario de bookwyrm: `useradd bookwyrm -r`
    - Cambie el propietario del directorio de instalación a bookwyrm: `chown -R bookwyrm:bookwyrm /opt/bookwyrm`
    - Ahora deberías ejecutar los comandos relacionados con bookwyrm como el usuario: `sudo -u bookwyrm echo I soy el usuario $(whoami)`
- Configure, enable, and start BookWyrm's `systemd` services:
    - Copy the service configurations by running `cp contrib/systemd/*.service /etc/systemd/system/`
    - Enable and start the services with `systemctl enable bookwyrm bookwyrm-worker bookwyrm-scheduler`

- Genera el código de administración con `sudo -u bookwyrm venv/bin/python3 manage.py admin_code`, y copia el código de administración a usar cuando crees tu cuenta de administrador.
- Puedes obtener tu código en cualquier momento reejecutando dicho comando. Aquí hay un ejemplo de salida:

```  { .sh }
***********************************************
Usa este código para crear tu cuenta de administrador:
c6c35779-af3a-4091-b330-c026610920d6
***************************************************
```
- The application should now be running at your domain. When you load the domain, you should get a configuration page to confirm your instance settings, and a form to create an admin account. Usa tu código de administrador para registrarte.

Congrats! You did it!! Configure your instance however you'd like.

## Finding log files

Like all software, BookWyrm can contain bugs, and often these bugs are in the Python code and easiest to reproduce by getting more context from the logs.

If you use the provided `systemd` service configurations from `contrib/systemd` you will be able to read the logs with `journalctl`:

``` { .sh }
# viewing logs of the web process
journalctl -u bookwyrm

# viewing logs of the worker process
journalctl -u bookwyrm-worker

# viewing logs of the scheduler process
journalctl -u bookwyrm-scheduler
```
Feel free to explore additional ways of slicing and dicing logs with flags documented in `journalctl --help`.

While BookWyrm's application logs will most often be enough, you can find logs for other services like Nginx, PostgreSQL, or Redis are usually in `.log` files located somewhere in `/var/logs`.

## Involúcrate

Ve [Involúcrate](https://joinbookwyrm.com/get-involved/) para más detalles.
