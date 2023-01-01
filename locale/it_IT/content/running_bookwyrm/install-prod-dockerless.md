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
    - `REDIS_ACTIVITY_HOST` <unk> Impostare su `localhost` (la macchina che esegue redis)
    - `REDIS_BROKER_PASSWORD` <unk> Impostare a nulla (multare su una macchina locale con un firewall)
    - `REDIS_BROKER_HOST` <unk> Imposta su `localhost` (la macchina che esegue redis)
    - `EMAIL_HOST_USER` <unk> L'indirizzo "da" che la tua app utilizzerà quando invierai un'email
    - `EMAIL_HOST_PASSWORD` <unk> La password fornita dal vostro servizio email
- Configura nginX
    - Copia il server_config in nginx's conf.d: `cp nginx/server_config /etc/nginx/conf.d/server_config`
    - Crea una copia della configurazione del modello di produzione e impostalo per l'uso in nginx: `cp nginx/production /etc/nginx/sites-available/bookwyrm.conf`
    - Aggiorna nginx `bookwyrm.conf`:
        - Sostituisci `your-domain.com` con il tuo nome di dominio ovunque nel file (incluse le righe che sono attualmente commentate)
        - Sostituisci `/app/` con la tua directory di installazione `/opt/bookwyrm/` ovunque nel file (incluso commentato)
        - Decommenta le righe da 18 a 67 per consentire l'inoltro a HTTPS. Dovresti avere abilitato due blocchi `server`
        - Cambia i percorsi `ssl_certificate` e `ssl_certificate_key` alla tua catena completa e alla tua posizione privkey
        - Cambia la riga 4 in modo che dica `server localhost:8000`. Puoi scegliere una porta diversa qui se desideri
        - Se stai utilizzando un altro web-server sulla tua macchina host, dovrai seguire le istruzioni [reverse-proxy](/reverse-proxy.html)
    - Abilita la configurazione nginx: `ln -s /etc/nginx/sites-available/bookwyrm.conf /etc/nginx/sites-enabled/bookwyrm.conf`Name
     - Ricarica nginx: `systemctl reload nginx`
- Configura l'ambiente virtuale python
    - Rendi la directory python venv nella tua directory di installazione: `mkdir venv` `python3 -m venv ./venv`
    - Installa le dipendenze di python di bookwyrm con pip: `./venv/bin/pip3 install -r requirements.txt`
- Crea il database postgresql di bookwyrm. Assicurati di cambiare la password in quello che hai impostato nel config: `.env`:

    `sudo -i -u postgres psql`

```
CREA bookwyrm UTILIZZATORE CON PASSWORD 'securedbypassword123';

CREA DATABASE bookwyrm TEMPLATE template0 CODIFICAZIONE 'UNICODIZIONE'.

ALTER DATABASE bookwyrm OWNER TO bookwyrm;

CONSERVARE TUTTI I PRIVILEGI SUL bookwyrm di DATABASE A bookwyrm;

\q
```

- Migrare lo schema del database eseguendo `venv/bin/python3 manage.py Migrate`
- Inizializza il database con `venv/bin/python3 manage.py initdb`
- Crea lo statico eseguendo `venv/bin/python3 manage.py collectstatico --no-input`
- Se si desidera utilizzare un archivio esterno per risorse statiche e file multimediali (come un servizio compatibile con S3), [segui le istruzioni](/external-storage.html) fino a quando ti dice di tornare qui
- Crea e imposta il tuo utente di `bookwyrm`
    - Crea il bookwyrm di sistema utente: `useradd bookwyrm -r`
    - Cambia il proprietario della tua cartella di installazione in bookwyrm: `chown -R bookwyrm:bookwyrm /opt/bookwyrm`
    - Ora dovresti eseguire i comandi relativi a bookwyrm come utente bookwyrm: `sudo -u bookwyrm echo Io sono l'utente $(whoami)`

- Generare il codice di amministrazione con `sudo -u bookwyrm venv/bin/python3 manage. y admin_code`, e copia il codice di amministrazione da usare quando crei il tuo account amministrativo.
- È possibile ottenere il tuo codice in qualsiasi momento rieseguendo quel comando. Ecco un risultato di esempio:

``` { .sh }
*********************************************
Usa questo codice per creare il tuo account amministratore:
c6c35779-af3a-4091-b330-c026610920d6
***********************************************************
```

- Crea e configurare lo script di esecuzione
    - Crea un file chiamato dockerless-run.sh e riempirlo con i seguenti contenuti

``` { .sh }
#!/bin/bash

# stop se un processo non riesce
set -e

# bookwyrm
/opt/bookwyrm/venv/bin/gunicorn bookwyrm.wsgi:application --bind 0.0.0.:8000 &

# sedano
/opt/bookwyrm/venv/bin/sedano -A celerywyrm worker -l info -Q High_priority,medium_priority, ow_priority &
/opt/bookwyrm/venv/bin/sedano -A battuto celerywyrm -l INFO --scheduler django_celery_beat. chedulers:DatabaseScheduler &
# /opt/bookwyrm/venv/bin/sedano -A fiore di sedano sedano &
```
    - Sostituisci `/opt/bookwyrm` con la cartella di installazione
    - Cambia `8000` al tuo numero di porta personalizzato
    - Flower è stato disabilitato qui perché non è autoconfigurato con la password impostata nel file `.env`
- Puoi ora eseguire BookWyrm con: `sudo -u bookwyrm bash /opt/bookwyrm/dockerless-run.sh`
- L'applicazione deve essere in esecuzione nel tuo dominio. Quando carichi il dominio, dovresti ottenere una pagina di configurazione che confermi le impostazioni dell'istanza e un modulo per creare un account amministratore. Usa il tuo codice amministratore per registrarsi.
- Si consiglia di configurare BookWyrm per autorun con un servizio di sistema. Ecco un esempio:
```
# /etc/systemd/system/bookwyrm.service
[Unit]
Description=Bookwyrm server
After=network.target
After=systemd-user-sessions.service
After=network-online. arget

[Service]
User=bookwyrm
Type=simple
Riavvio=always
ExecStart=/bin/bash /opt/bookwyrm/dockerless-run.sh
WorkingDirectory=/opt/bookwyrm/

[Install]
WantedBy=multi-user.target
```
È necessario impostare un lavoro di Cron per avviare automaticamente il servizio su un riavvio del server.

Congratulazioni! Ce l'hai fatta!! Configura la tua istanza come preferisci.

## Partecipa

Vedi [Partecipa](https://joinbookwyrm.com/get-involved/) per dettagli.
