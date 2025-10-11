---
Title: Installing Without Docker
Date: 2023-8-19
Order: 2
---

This project is still young and isn't, at the moment, very stable, so please proceed with caution when running in production.

This method of installation is more involved, and therefore is for more experienced admins. **Docker install is the recommended method** as there may not be much support available for Dockerless installation. If you have expertise in this area, we would love your help to improve this documentation!

This install method assumes you already have ssl configured with certificates available.

## Server setup
- Get a domain name and set up DNS for your server. You'll need to point the nameservers of your domain on your DNS provider to the server where you'll be hosting BookWyrm. Here are instructions for [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Set your server up with appropriate firewalls for running a web application (this instruction set is tested against Ubuntu 20.04). Here are instructions for [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Set up an email service (such as [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) and the appropriate SMTP/DNS settings. Use the service's documentation for configuring your DNS
- Install dependencies. On debian this could look like `apt install postgresql redis nginx python3-venv python3-pip python3-dev libpq-dev gunicorn`

## Install and configure BookWyrm

The `production` branch of BookWyrm contains a number of tools not on the `main` branch that are suited for running in production, such as `docker-compose` changes to update the default commands or configuration of containers, and individual changes to container config to enable things like SSL or regular backups. Not all of these changes effect the dockerless install, however the `production` branch is still recommended

Instructions for running BookWyrm in production without Docker:

- Make and enter directory you want to install bookwyrm too. For example `/opt/bookwyrm`:
	`mkdir /opt/bookwyrm && cd /opt/bookwyrm`
- Get the application code, note that this only clones the `production` branch:
    `git clone https://github.com/bookwyrm-social/bookwyrm.git --branch production --single-branch ./`
- Create your environment variables file, `cp .env.example .env`, and update the following. Passwords should generally be enclosed in "quotation marks":
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
    - Copy the server_config to nginx's conf.d: `cp nginx/server_config /etc/nginx/conf.d/server_config`
    - Make a copy of the production template config and set it for use in nginx: `cp nginx/production /etc/nginx/sites-available/bookwyrm.conf`
    - Update nginx `bookwyrm.conf`:
        - Replace `your-domain.com` with your domain name everywhere in the file (including the lines that are currently commented out)
        - Replace `/app` with your install directory `/opt/bookwyrm` everywhere in the file (including commented out)
        - Uncomment [lines 23 to 111](https://github.com/bookwyrm-social/bookwyrm/blob/production/nginx/production#L23-L111) to enable
            forwarding to HTTPS. You should have two `server` blocks enabled
        - Change the `ssl_certificate` and `ssl_certificate_key` paths to your fullchain and privkey locations
        - Change [line 4](https://github.com/chdorner/secretbearlibrary/blob/main/bookwyrm/bookwyrm-nginx.conf#L4) so that it says
            `server localhost:8000`. You may choose a different port here if you wish
        - If you are running another web-server on your host machine, you will need to follow the [reverse-proxy instructions](/reverse-proxy.html)
    - Enable the nginx config:
        `ln -s /etc/nginx/sites-available/bookwyrm.conf /etc/nginx/sites-enabled/bookwyrm.conf`
     - Reload nginx: `systemctl reload nginx`
- Setup the python virtual enviroment
    - Make the python venv directory in your install dir:
        `python3 -m venv ./venv`
    - Install bookwyrm python dependencies with pip:
        `./venv/bin/pip3 install --upgrade "pip>=25.1.0"`
        `./venv/bin/pip3 install --group main`
- Make the bookwyrm postgresql database. Make sure to change the password to what you set in the `.env` config:
    `sudo -i -u postgres psql`

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
    - Make the system bookwyrm user:
        `useradd bookwyrm -r`
    - Change the owner of your install directory to bookwyrm:
        `chown -R bookwyrm:bookwyrm /opt/bookwyrm`
    - You should now run bookwyrm related commands as the bookwyrm user:
        `sudo -u bookwyrm echo I am the $(whoami) user`
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

While BookWyrm's application logs will most often be enough, you can find logs for other services like Nginx,
PostgreSQL, or Redis are usually in `.log` files located somewhere in `/var/logs`.

## Get Involved

See [Get Involved](https://joinbookwyrm.com/get-involved/) for details.
