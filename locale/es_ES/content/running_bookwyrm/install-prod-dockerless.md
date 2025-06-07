---
Title: Instalación sin Docker
Date: 2022-10-02
Order: 2
---

Este proyecto es todavía joven y por el momento no es muy estable, así que por favor procede con precaución cuando se ejecuta en producción. Este método de instalación está más implicado, y por lo tanto es para administradores con más experiencia. Docker install es recomendado Este método de instalación asume que ya tienes ssl configurado con certificados disponibles.

## Configuración del Servidor
- Obtén un nombre de dominio y configura el DNS para tu servidor. Tendrás que apuntar los servidores de nombres de tu dominio en tu proveedor de DNS al servidor donde hospedarás BookWyrm. Aquí hay instrucciones para [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Configura tu servidor con los cortafuegos adecuados para ejecutar una aplicación web (este conjunto de instrucciones se testeó en Ubuntu 20.04). Aquí hay instrucciones para [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Configura tu servicio de correo electrónico (como [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) y las configuraciones apropiadas de SMTP/DNS. Utiliza la documentación del servicio para configurar tu DNS
- Instala las dependencias. En Debian puedes utilizar `apt install postgresql redis nginx python3-venv python3-pip python3-dev libpq-dev`

## Instalar y configurar BookWyrm

La rama `production` de BookWyrm contiene una serie de herramientas que no están en la rama `main` y que son adecuadas para ejecutarse en production como: los cambios de `docker-compose` para actualizar los comandos predeterminados; o la configuración de los contenedores; y cambios individuales en la configuración del contenedor para habilitar cosas como SSL o copias de seguridad periódicas. No todos estos cambios afectan la instalación sin Docker, sin embargo, aún se recomienda la rama `producción`.

Instrucciones para ejecutar BookWyrm en producción sin Docker:

- Crea el directorio donde quieras instalar BookWyrm. Por ejemplo `/opt/bookwyrm`: `mkdir /opt/bookwyrm && cd /opt/bookwyrm`
- Obtén el código de aplicación: `git clone git@github.com:bookwyrm-social/bookwyrm.git`
- Cambia a la rama `production`: `git checkout production`
- Crea el archivo de variables, `cp .env.example .env`y actualiza lo siguiente:
    - `SECRET_KEY` | Una cadena de caracteres secreta
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
- Configuración de Nginx
    - Copie el server_config de nginx a conf.d: `cp nginx/server_config (0)[video] /nginx/conf.d/server_config`
    - Haz una copia de la configuración de la plantilla de producción y establécela para su uso en nginx `cp nginx/production nginx/bookwyrm.conf`
    - Actualiza `nginx/bookwyrm.conf`:
        - Reemplaza `tu-dominio.com` con tu nombre de dominio en todas las partes del archivo (incluyendo las líneas que están comentadas)
        - Reemplaza `/app/` con tu directorio de instalación `/opt/bookwyrm/` en toda parte del archivo (incluyendo comentarios)
        - Descomenta las líneas de 18 a 67 para habilitar el reenvío a HTTPS. Debes tener dos bloques del `servidor` habilitados
        - Cambie las rutas de `ssl_certificate` y `ssl_certificate_key` a sus ubicaciones de fullchain y privkey
        - Cambie la línea 4 a `server localhost:8000`. Puedes elegir un puerto diferente aquí si lo deseas
        - Si estás ejecutando otro servidor web en tu máquina, necesitarás seguir las instrucciones de [reverse-proxy](/reverse-proxy.html)
    - Habilita la configuración de nginx: `ln -s mañana/nginx/sites-available/bookwyrm.conf (0)[video] /nginx/sites-enabled/bookwyrm.conf`
     - Recarga nginx: `systemctl reload nginx`
- Configura el entorno virtual de python
    - Crea el directorio venv de python en tu directorio de instalación: `mkdir venv` `python3 -m venv ./venv`
    - Instala las dependencias de bookwyrm python con pip: `./venv/bin/pip3 install -r requirements.txt`
- Crea la base de datos postgresql de bookwyrm. Asegúrate de cambiar la contraseña a lo que configuraste en la configuración de `.env`:

    `sudo -i -u postgres psql`

```
CREATE USER bookwyrm WITH PASSWORD 'securedbypassword123';

CREATE DATABASE bookwyrm TEMPLATE template0 ENCODING 'UNICODE';

ALTER DATABASE bookwyrm OWNER TO bookwyrm;

GRANT ALL PRIVILEGES ON DATABASE bookwyrm TO bookwyrm;

\q
```

- Migra el esquema de base de datos ejecutando `venv/bin/python3 manage.py migrate`
- Inicializa la base de datos ejecutando `venv/bin/python3 manage.py initdb`
- Crea la static ejecutando `venv/bin/python3 manage.py collectstatic --no.U`
- Si deseas utilizar un almacenamiento externo para recursos estáticos y archivos multimedia (como un servicio compatible con S3), [sigue las instrucciones](/external-storage.html) hasta que te indique que vuelvas aquí
- Crea y configura tu usuario de `bookwyrm`
    - Agrega al usuario de bookwyrm: `useradd bookwyrm -r`
    - Cambie el propietario del directorio de instalación a bookwyrm: `chown -R bookwyrm:bookwyrm /opt/bookwyrm`
    - Ahora deberías ejecutar los comandos relacionados con bookwyrm como el usuario: `sudo -u bookwyrm echo I soy el usuario $(whoami)`

- Genera el código de administración con `sudo -u bookwyrm venv/bin/python3 manage.py admin_code`, y copia el código de administración a usar cuando crees tu cuenta de administrador.
- Puedes obtener tu código en cualquier momento reejecutando dicho comando. Aquí hay un ejemplo de salida:

``` { .sh }
***********************************************
Usa este código para crear tu cuenta de administrador:
c6c35779-af3a-4091-b330-c026610920d6
***************************************************
```

- Crea y configura el script de ejecución
    - Crea un archivo llamado dockerless-run.sh y llénalo con los siguientes contenidos

``` { .sh }
#!/bin/bash

# stop if one process fails
set -e

# bookwyrm
/opt/bookwyrm/venv/bin/gunicorn bookwyrm.wsgi:application --bind 0.0.0.0:8000 &

# celery
/opt/bookwyrm/venv/bin/celery -A celerywyrm worker -l info -Q high_priority,medium_priority,low_priority &
/opt/bookwyrm/venv/bin/celery -A celerywyrm beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler &
# /opt/bookwyrm/venv/bin/celery -A celerywyrm flower &
```
    - Reemplaza `/opt/bookwyrm` con tu directorio de instalación
    - Cambia `8000` a tu número de puerto personalizado
    - Flower ha sido deshabilitada aquí porque no está configurada automáticamente con la contraseña establecida en el archivo `.env`
- Ahora puede ejecutar BookWyrm con: `sudo -u bookwyrm bash /opt/bookwyrm/dockerless-run.sh`
- La aplicación debería estar ejecutándose en tu dominio. Cuando cargues el dominio, deberías obtener una página de configuración que confirme la configuración de tu instancia y un formulario para crear una cuenta de administrador. Usa tu código de administrador para registrarte.
- Puede configurar BookWyrm para que se ejecute automáticamente con un servicio systemd. Aquí tienes un ejemplo:
```
# /etc/systemd/system/bookwyrm.service
[Unit]
Description=Bookwyrm Server
After=network.target
After=systemd-user-sessions.service
After=network-online.target

[Service]
User=bookwyrm
Type=simple
Restart=always
ExecStart=/bin/bash /opt/bookwyrm/dockerless-run.sh
WorkingDirectory=/opt/bookwyrm/

[Install]
WantedBy=multi-user.target
```
Necesitarás configurar un trabajo de Cron para que el servicio se inicie automáticamente al reiniciar el servidor.

¡Felicidades! ¡Lo hiciste! Configura tu instancia como desees.

## Involúcrate

Ve [Involúcrate](https://joinbookwyrm.com/get-involved/) para más detalles.
