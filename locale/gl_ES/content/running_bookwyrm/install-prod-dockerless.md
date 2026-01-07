---
Title: Installing Without Docker
Date: 19-8-2023
Order: 2
---

Este proxecto aínda é moi novo e, por agora, non é moi estable polo que actúa con tino cando o utilices en produción.

Esta forma de instalación require máis atención, polo que é máis axeitada para administradoras con experiencia. **Docker install is the recommended method** as there may not be much support available for Dockerless installation. If you have expertise in this area, we would love your help to improve this documentation!

This install method assumes you already have ssl configured with certificates available.

## Server setup
- Get a domain name and set up DNS for your server. You'll need to point the nameservers of your domain on your DNS provider to the server where you'll be hosting BookWyrm. Here are instructions for [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Set your server up with appropriate firewalls for running a web application (this instruction set is tested against Ubuntu 20.04). Here are instructions for [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Set up an email service (such as [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) and the appropriate SMTP/DNS settings. Use the service's documentation for configuring your DNS
- Install dependencies. On debian this could look like `apt install postgresql redis nginx python3-venv python3-pip python3-dev libpq-dev gunicorn gettext-base`

## Install and configure BookWyrm

The `production` branch of BookWyrm contains a number of tools not on the `main` branch that are suited for running in production, such as `docker-compose` changes to update the default commands or configuration of containers, and individual changes to container config to enable things like SSL or regular backups. Not all of these changes effect the dockerless install, however the `production` branch is still recommended

Instructions for running BookWyrm in production without Docker:

- Make and enter directory you want to install bookwyrm too. For example `/opt/bookwyrm`: `mkdir /opt/bookwyrm && cd /opt/bookwyrm`
- Get the application code, note that this only clones the `production` branch: `git clone https://github.com/bookwyrm-social/bookwyrm.git --branch production --single-branch ./`
- Create your environment variables file, `cp .env.example .env`, and update the following. Passwords should generally be enclosed in "quotation marks". You can use `bw-dev create_secrets` to generate passwords in `.env`-file:
    - `SECRET_KEY` | A difficult to guess, secret string of characters.
    - `DOMAIN` | Your web domain
    - `POSTGRES_PASSWORD` | Set a secure password for the database
    - `POSTGRES_HOST` | Set to `localhost` (the machine running your db)
    - `POSTGRES_USER` | Set to `bookwyrm` (recommended) or something custom (configured later)
    - `POSTGRES_DB` | Set to `bookwyrm`
    - `REDIS_ACTIVITY_PASSWORD` | Set to nothing (fine on a local machine with a firewall)
    - `REDIS_ACTIVITY_HOST` | Set to `localhost` (the machine running redis)
    - `REDIS_BROKER_PASSWORD` | Set to nothing (fine on a local machine with a firewall)
    - `REDIS_BROKER_HOST` | Set to `localhost` (the machine running redis)
    - `EMAIL_HOST_USER` | The "from" address that your app will use when sending email
    - `EMAIL_HOST_PASSWORD` | The password provided by your email service
- If you are on Debian and some other operating systems, you may need to create the `/var/cache/nginx` directory:
``` { .sh }
mkdir /var/cache/nginx
chown www-data:www-data /var/cache/nginx
```
- Configure nginx
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
        - Change upstream addresses in lines 4 and 7 to `server localhost:8000` and `server localhost:8888`. You may choose a different port here if you wish
    - Enable the nginx config: `ln -s /etc/nginx/sites-available/bookwyrm.conf /etc/nginx/sites-enabled/bookwyrm.conf`
     - Reload nginx: `systemctl reload nginx`
- Setup the python virtual enviroment
    - Make the python venv directory in your install dir: `python3 -m venv ./venv`
    - Install bookwyrm python dependencies with pip: `./venv/bin/pip3 install -r requirements.txt`
- Make the bookwyrm postgresql database. Make sure to change the password to what you set in the `.env` config: `sudo -i -u postgres psql`

``` { .sql }
CREATE USER bookwyrm WITH PASSWORD 'securedbypassword123';

CREATE DATABASE bookwyrm TEMPLATE template0 ENCODING 'UNICODE';

ALTER DATABASE bookwyrm OWNER TO bookwyrm;

GRANT ALL PRIVILEGES ON DATABASE bookwyrm TO bookwyrm;

\q
```

- Migrate the database schema by running `venv/bin/python3 manage.py migrate`
- Initialize the database by running `venv/bin/python3 manage.py initdb`
- Compile the themes by running `venv/bin/python3 manage.py compile_themes`
- Create the static files by running `venv/bin/python3 manage.py collectstatic --no-input`
- If you wish to use an external storage for static assets and media files (such as an S3-compatible service), [follow the instructions](/external-storage.html) until it tells you to come back here
- Create and setup your `bookwyrm` user
    - Make the system bookwyrm user: `useradd bookwyrm -r`
    - Change the owner of your install directory to bookwyrm: `chown -R bookwyrm:bookwyrm /opt/bookwyrm`
    - You should now run bookwyrm related commands as the bookwyrm user: `sudo -u bookwyrm echo I am the $(whoami) user`
- Configure, enable, and start BookWyrm's `systemd` services:
    - Copy the service configurations by running `cp contrib/systemd/*.service /etc/systemd/system/`
    - Enable and start the services with `systemctl enable bookwyrm bookwyrm-worker bookwyrm-scheduler`

- Generate the admin code with `sudo -u bookwyrm venv/bin/python3 manage.py admin_code`, and copy the admin code to use when you create your admin account.
- You can get your code at any time by re-running that command. Here's an example output:

```  { .sh }
*******************************************
Use this code to create your admin account:
c6c35779-af3a-4091-b330-c026610920d6
*******************************************
```
- The application should now be running at your domain. When you load the domain, you should get a configuration page to confirm your instance settings, and a form to create an admin account. Use your admin code to register.

Parabéns! Conseguíchelo! Configura a túa instancia como máis che guste.

## Atopar os ficheiros do rexistro

Como todo software, BookWyrm pode fallar, habitualmente estes problemas proceden do código Python e o xeito máis doado de reproducilos é obtendo máis contexto nos rexistros.

Se usas o servizo `systemd` proporcionado as configuracións de `contrib/systemd` poderás ler os rexistros con `journalctl`:

``` { .sh }
# ver rexistros dos procesos web
journalctl -u bookwyrm

# ver rexistros dos procesos das tarefas
journalctl -u bookwyrm-worker

# ver rexistros dos procesos programados
journalctl -u bookwyrm-scheduler
```
Animámoste a explorar outros xeitos de examinar os rexistros usando os modificadores documentados en `journalctl --help`.

Aínda que os rexistros de BookWyrm adoitan abondar, podes mirar o rexistro de outros servizos como Nginx, PostgreSQL ou Redis, que adoitan ter ficheiros `.log` nalgún lugar dentro de `/var/logs`.

## Get Involved

See [Get Involved](https://joinbookwyrm.com/get-involved/) for details.
