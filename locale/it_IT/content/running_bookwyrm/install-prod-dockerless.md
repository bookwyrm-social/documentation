---
Title: Installazione Senza Docker
Date: 2023-8-19
Order: 2
---

This project is still young and isn't, at the moment, very stable, so please proceed with caution when running in production.

This method of installation is more involved, and therefore is for more experienced admins. **Docker install is the recommended method** as there may not be much support available for Dockerless installation. If you have expertise in this area, we would love your help to improve this documentation!

This install method assumes you already have ssl configured with certificates available.

## Configurazione server
- Ottieni un nome di dominio e imposta il DNS per il server. Dovrai indicare i nameservers del tuo dominio sul tuo provider DNS al server in cui ospiterai BookWyrm. Qui ci sono istruzioni per [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Impostare il server con firewall appropriati per l'esecuzione di un'applicazione web (questo set di istruzioni viene testato contro Ubuntu 20.04). Qui ci sono istruzioni per [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Impostare un servizio email (come [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) e le impostazioni SMTP/DNS appropriate. Utilizza la documentazione del servizio per configurare il DNS
- Installare le dipendenze. On debian this could look like `apt install postgresql redis nginx python3-venv python3-pip python3-dev libpq-dev gunicorn gettext-base`

## Installa e configura BookWyrm

Il ramo di produzione `` di BookWyrm contiene una serie di strumenti non presenti sul ramo `principale` che sono adatti per funzionare nella produzione, come `docker-compose` modifiche per aggiornare i comandi o la configurazione predefinita dei container, e cambiamenti individuali alla configurazione del contenitore per abilitare cose come SSL o backup regolari. Non tutte queste modifiche effetto l'installazione dockerless, tuttavia il ramo `production` è ancora consigliato

Istruzioni per la gestione di BookWyrm in produzione senza Docker:

- Crea ed inserisci anche la directory che vuoi installare bookwyrm. Per esempio, `/opt/bookwyrm`: `mkdir /opt/bookwyrm && cd /opt/bookwyrm`
- Get the application code, note that this only clones the `production` branch: `git clone https://github.com/bookwyrm-social/bookwyrm.git --branch production --single-branch ./`
- Create your environment variables file, `cp .env.example .env`, and update the following. Passwords should generally be enclosed in "quotation marks". You can use `bw-dev create_secrets` to generate passwords in `.env`-file:
    - `SECRET_KEY` | A difficult to guess, secret string of characters.
    - `DOMANDA` <unk> Il tuo dominio web
    - `POSTGRES_PASSWORD` <unk> Imposta una password sicura per il database
    - `POSTGRES_HOST` <unk> Impostare a `localhost` (la macchina che esegue il vostro db)
    - `POSTGRES_USER` <unk> Impostare a `bookwyrm` (raccomandato) o qualcosa di personalizzato (configurato in seguito)
    - `POSTGRES_DB` <unk> Impostare a `bookwyrm`
    - `REDIS_ACTIVITY_PASSWORD` <unk> Impostare a nulla (multare su una macchina locale con un firewall)
    - `REDIS_ACTIVITY_HOST` <unk> Impostare su `localhost` (la macchina che esegue redis)
    - `REDIS_BROKER_PASSWORD` <unk> Impostare a nulla (multare su una macchina locale con un firewall)
    - `REDIS_BROKER_HOST` <unk> Imposta su `localhost` (la macchina che esegue redis)
    - `EMAIL_HOST_USER` <unk> L'indirizzo "da" che la tua app utilizzerà quando invierai un'email
    - `EMAIL_HOST_PASSWORD` <unk> La password fornita dal vostro servizio email
- If you are on Debian and some other operating systems, you may need to create the `/var/cache/nginx` directory:
``` { .sh }
mkdir /var/cache/nginx
chown www-data:www-data /var/cache/nginx
```
- Configura nginX
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
        - Change upstream addresses in lines 4 and 7 to `server localhost:8000` and `server localhost:8888`. Puoi scegliere una porta diversa qui se desideri
    - Enable the nginx config: `ln -s /etc/nginx/sites-available/bookwyrm.conf /etc/nginx/sites-enabled/bookwyrm.conf`
     - Ricarica nginx: `systemctl reload nginx`
- Configura l'ambiente virtuale python
    - Make the python venv directory in your install dir: `python3 -m venv ./venv`
    - Installa le dipendenze di python di bookwyrm con pip: `./venv/bin/pip3 install -r requirements.txt`
- Crea il database postgresql di bookwyrm. Make sure to change the password to what you set in the `.env` config: `sudo -i -u postgres psql`

``` { .sql }
CREA bookwyrm UTILIZZATORE CON PASSWORD 'securedbypassword123';

CREA DATABASE bookwyrm TEMPLATE template0 CODIFICAZIONE 'UNICODIZIONE'.

ALTER DATABASE bookwyrm OWNER TO bookwyrm;

CONSERVARE TUTTI I PRIVILEGI SUL bookwyrm di DATABASE A bookwyrm;

\q
```

- Migrare lo schema del database eseguendo `venv/bin/python3 manage.py Migrate`
- Inizializza il database con `venv/bin/python3 manage.py initdb`
- Compile the themes by running `venv/bin/python3 manage.py compile_themes`
- Create the static files by running `venv/bin/python3 manage.py collectstatic --no-input`
- Se si desidera utilizzare un archivio esterno per risorse statiche e file multimediali (come un servizio compatibile con S3), [segui le istruzioni](/external-storage.html) fino a quando ti dice di tornare qui
- Crea e imposta il tuo utente di `bookwyrm`
    - Crea il bookwyrm di sistema utente: `useradd bookwyrm -r`
    - Cambia il proprietario della tua cartella di installazione in bookwyrm: `chown -R bookwyrm:bookwyrm /opt/bookwyrm`
    - Ora dovresti eseguire i comandi relativi a bookwyrm come utente bookwyrm: `sudo -u bookwyrm echo Io sono l'utente $(whoami)`
- Configure, enable, and start BookWyrm's `systemd` services:
    - Copy the service configurations by running `cp contrib/systemd/*.service /etc/systemd/system/`
    - Enable and start the services with `systemctl enable bookwyrm bookwyrm-worker bookwyrm-scheduler`

- Generare il codice di amministrazione con `sudo -u bookwyrm venv/bin/python3 manage. y admin_code`, e copia il codice di amministrazione da usare quando crei il tuo account amministrativo.
- È possibile ottenere il tuo codice in qualsiasi momento rieseguendo quel comando. Ecco un risultato di esempio:

```  { .sh }
*********************************************
Usa questo codice per creare il tuo account amministratore:
c6c35779-af3a-4091-b330-c026610920d6
***********************************************************
```
- The application should now be running at your domain. When you load the domain, you should get a configuration page to confirm your instance settings, and a form to create an admin account. Usa il tuo codice amministratore per registrarsi.

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

## Partecipa

Vedi [Partecipa](https://joinbookwyrm.com/get-involved/) per dettagli.
