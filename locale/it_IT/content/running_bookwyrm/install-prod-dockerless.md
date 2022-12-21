---
Title: Installazione Senza Docker
Date: 2022-10-02
Order: 2
---

Questo progetto è ancora giovane e al momento non è molto stabile, quindi vi prego di procedere con cautela quando si esegue in produzione. Questo metodo di installazione è più coinvolto, e quindi è per admin più esperti. L'installazione via docker è raccomandato. Questo metodo di installazione assume che tu hai ssl configurato con certifiche disponibili

## Configurazione server
- Ottieni un nome di dominio e imposta il DNS per il server. Dovrai indicare i nameservers del tuo dominio sul tuo provider DNS al server in cui ospiterai BookWyrm. Qui ci sono istruzioni per [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Impostare il server con firewall appropriati per l'esecuzione di un'applicazione web (questo set di istruzioni viene testato contro Ubuntu 20.04). Qui ci sono istruzioni per [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Impostare un servizio email (come [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) e le impostazioni SMTP/DNS appropriate. Utilizza la documentazione del servizio per configurare il DNS
- Installare le dipendenze. Su debian questo potrebbe apparire come `apt install postgresql redis nginx python3-venv python3-pip python3-dev libpq-dev`,

## Installa e configura BookWyrm

Il ramo di produzione `` di BookWyrm contiene una serie di strumenti non presenti sul ramo `principale` che sono adatti per funzionare nella produzione, come `docker-compose` modifiche per aggiornare i comandi o la configurazione predefinita dei container, e cambiamenti individuali alla configurazione del contenitore per abilitare cose come SSL o backup regolari. Non tutte queste modifiche effetto l'installazione dockerless, tuttavia il ramo `production` è ancora consigliato

Istruzioni per la gestione di BookWyrm in produzione senza Docker:

- Crea ed inserisci anche la directory che vuoi installare bookwyrm. Per esempio, `/opt/bookwyrm`: `mkdir /opt/bookwyrm && cd /opt/bookwyrm`
- Scarica il codice applicativo: `git clone git@github.com:bookwyrm-social/bookwyrm.git ./`
- Passa al ramo `produzione`: `git checkout production`
- Crea il tuo file delle variabili di ambiente, `cp .env.example .env`e aggiorna quanto segue:
    - `SECRET_KEY` <unk> Una stringa segreta di personaggi difficile da indovinare
    - `DOMANDA` <unk> Il tuo dominio web
    - `POSTGRES_PASSWORD` <unk> Imposta una password sicura per il database
    - `POSTGRES_HOST` <unk> Impostare a `localhost` (la macchina che esegue il vostro db)
    - `POSTGRES_USER` <unk> Impostare a `bookwyrm` (raccomandato) o qualcosa di personalizzato (configurato in seguito)
    - `POSTGRES_DB` <unk> Impostare a `bookwyrm`
    - `REDIS_ACTIVITY_PASSWORD` <unk> Impostare a nulla (multare su una macchina locale con un firewall)
    - `REDIS_ACTIVITY_HOST` | Set to `localhost` (the machine running redis)
    - `REDIS_BROKER_PASSWORD` | Set to nothing (fine on a local machine with a firewall)
    - `REDIS_BROKER_HOST` | Set to `localhost` (the machine running redis)
    - `EMAIL_HOST_USER` | The "from" address that your app will use when sending email
    - `EMAIL_HOST_PASSWORD` | The password provided by your email service
- Configure nginx
    - Copy the server_config to nginx's conf.d: `cp nginx/server_config /etc/nginx/conf.d/server_config`
    - Make a copy of the production template config and set it for use in nginx: `cp nginx/production /etc/nginx/sites-available/bookwyrm.conf`
    - Update nginx `bookwyrm.conf`:
        - Replace `your-domain.com` with your domain name everywhere in the file (including the lines that are currently commented out)
        - Replace `/app/` with your install directory `/opt/bookwyrm/` everywhere in the file (including commented out)
        - Uncomment lines 18 to 67 to enable forwarding to HTTPS. You should have two `server` blocks enabled
        - Change the `ssl_certificate` and `ssl_certificate_key` paths to your fullchain and privkey locations
        - Change line 4 so that it says `server localhost:8000`. You may choose a different port here if you wish
        - If you are running another web-server on your host machine, you will need to follow the [reverse-proxy instructions](/reverse-proxy.html)
    - Enable the nginx config: `ln -s /etc/nginx/sites-available/bookwyrm.conf /etc/nginx/sites-enabled/bookwyrm.conf`
     - Reload nginx: `systemctl reload nginx`
- Setup the python virtual enviroment
    - Make the python venv directory in your install dir: `mkdir venv` `python3 -m venv ./venv`
    - Install bookwyrm python dependencies with pip: `./venv/bin/pip3 install -r requirements.txt`
- Make the bookwyrm postgresql database. Make sure to change the password to what you set in the `.env` config:

    `sudo -i -u postgres psql`

```
CREATE USER bookwyrm WITH PASSWORD 'securedbypassword123';

CREATE DATABASE bookwyrm TEMPLATE template0 ENCODING 'UNICODE';

ALTER DATABASE bookwyrm OWNER TO bookwyrm;

GRANT ALL PRIVILEGES ON DATABASE bookwyrm TO bookwyrm;

\q
```

- Migrate the database schema by running `venv/bin/python3 manage.py migrate`
- Initialize the database by running `venv/bin/python3 manage.py initdb`
- Create the static by running `venv/bin/python3 manage.py collectstatic --no-input`
- If you wish to use an external storage for static assets and media files (such as an S3-compatible service), [follow the instructions](/external-storage.html) until it tells you to come back here
- Create and setup your `bookwyrm` user
    - Make the system bookwyrm user: `useradd bookwyrm -r`
    - Change the owner of your install directory to bookwyrm: `chown -R bookwyrm:bookwyrm /opt/bookwyrm`
    - You should now run bookwyrm related commands as the bookwyrm user: `sudo -u bookwyrm echo I am the $(whoami) user`

- Generate the admin code with `sudo -u bookwyrm venv/bin/python3 manage.py admin_code`, and copy the admin code to use when you create your admin account.
- You can get your code at any time by re-running that command. Here's an example output:

``` { .sh }
*******************************************
Use this code to create your admin account:
c6c35779-af3a-4091-b330-c026610920d6
*******************************************
```

- Make and configure the run script
    - Make a file called dockerless-run.sh and fill it with the following contents

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
    - Replace `/opt/bookwyrm` with your install dir
    - Change `8000` to your custom port number
    - Flower has been disabled here because it is not autoconfigured with the password set in the `.env` file
- You can now run BookWyrm with: `sudo -u bookwyrm bash /opt/bookwyrm/dockerless-run.sh`
- The application should be running at your domain. When you load the domain, you should get a configuration page which confirms your instance settings, and a form to create an admin account. Use your admin code to register.
- You may want to configure BookWyrm to autorun with a systemd service. Here is an example:
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
You will need to set up a Cron job for the service to start automatically on a server restart.

Congrats! You did it!! Configure your instance however you'd like.

## Partecipa

Vedi [Partecipa](https://joinbookwyrm.com/get-involved/) per dettagli.
