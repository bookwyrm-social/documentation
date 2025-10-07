- - -
Title: Installing in Production Date: 2025-04-01 Order: 1
- - -

Questo progetto è ancora giovane e al momento non è molto stabile, quindi si prega di procedere con cautela quando si esegue in produzione.

## Configurazione server
- Ottieni un nome di dominio e imposta DNS per il tuo server. Dovrai indicare i nameservers del tuo dominio sul tuo provider DNS al server dove ospiterai BookWyrm. Ecco le istruzioni per [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Impostare il server con i firewall appropriati per l'esecuzione di un'applicazione web (questo set di istruzioni è testato contro Ubuntu 20.04). Ecco le istruzioni per [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Imposta un servizio email (come [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) e le impostazioni SMTP/DNS appropriate. Usa la documentazione del servizio per configurare il tuo DNS
- [Installa Docker e docker-compose](https://docs.docker.com/compose/install/)

## Installa e configura BookWyrm

There are several repos in the BookWyrm org, including documentation, a static landing page, and the actual Bookwyrm code. To run BookWyrm, you want the actual app code which is in [bookwyrm-social/bookwyrm](https://github.com/bookwyrm-social/bookwyrm).

La filiale `di produzione` di BookWyrm contiene una serie di strumenti non presenti nel ramo `principale` che sono adatti per funzionare in produzione, come le modifiche `docker-compose` per aggiornare i comandi predefiniti o la configurazione dei container, e le singole modifiche alla configurazione del contenitore per abilitare cose come SSL o backup regolari.

Istruzioni per la gestione di BookWyrm in produzione:

- Ottieni il codice applicativo: `git clone git@github.com:bookwyrm-social/bookwyrm.git`
- Passa alla filiale `produzione`: `git checkout production`
- Crea il tuo file di variabili di ambiente, `cp .env.example .env`e aggiorna quanto segue:
    - `DOMAIN` <unk> Il tuo dominio web
    - `EMAIL` <unk> Indirizzo email da utilizzare per la verifica del dominio certbot
    - `FLOWER_USER` <unk> Il tuo nome utente per accedere al monitor della coda di Flower
    - `EMAIL_HOST_USER` <unk> L'indirizzo "da" che la tua app utilizzerà quando invierai email
    - `EMAIL_HOST_PASSWORD` <unk> La password fornita dal tuo servizio email
- Initialize secrets by running `./bw-dev create_secrets` or manually update following in `.env`:
    - `SECRET_KEY` <unk> Una stringa segreta di caratteri difficile da indovinare
    - `POSTGRES_PASSWORD` <unk> Imposta una password sicura per il database
    - `REDIS_ACTIVITY_PASSWORD` <unk> Imposta una password sicura per il sottosistema Attività Redis
    - `REDIS_BROKER_PASSWORD` <unk> Imposta una password sicura per il sottosistema Broker coda Redis
    - `FLOWER_PASSWORD` <unk> La tua password sicura per accedere al monitor delle code di Flower
    - Se stai utilizzando un altro web-server sulla tua macchina ospite, dovrai seguire le istruzioni [reverse-proxy](/reverse-proxy.html)
- Check that you have [all the required settings configured](/environment.html#required-environment-settings) before proceeding further
- Setup ssl certificate via letsencrypt by running `./bw-dev init_ssl`
- Inizializza il database eseguendo la migrazione `./bw-dev`
- Run the application with `docker-compose up --build`, and make sure all the images build successfully
    - Se si eseguono altri servizi sulla macchina ospite, si possono verificare errori in cui i servizi non funzionano quando si tenta di collegarsi a una porta. Vedi la guida [per la risoluzione dei problemi](#port_conflicts) per consigli su come risolverlo.
- Quando il docker è stato costruito con successo, interrompere il processo con `CTRL-C`
- Se si desidera utilizzare una memoria esterna per risorse statiche e file multimediali (come un servizio compatibile con S3), [segui le istruzioni](/external-storage.html) fino a quando non ti dice di tornare qui
- Inizializza l'applicazione con il setup `./bw-dev`e copia il codice di amministrazione da usare quando crei il tuo account amministratore.
    - L'output di `./bw-dev setup` dovrebbe concludersi con il tuo codice amministrativo. Puoi ottenere il tuo codice in qualsiasi momento eseguendo `./bw-dev admin_code` dalla riga di comando. Ecco un output di esempio:

``` { .sh }
*********************************************
Usa questo codice per creare il tuo account amministratore:
c6c35779-af3a-4091-b330-c026610920d6
***********************************************************
```

- Esegue docker-compose in background con: `docker-compose up -d`
- L'applicazione dovrebbe essere in esecuzione nel tuo dominio. Quando si carica il dominio, si dovrebbe ottenere una pagina di configurazione che conferma le impostazioni dell'istanza e un modulo per creare un account amministratore. Usa il tuo codice amministratore per registrarti.

Congratulazioni! Ce l'hai fatta!! Configura la tua istanza come preferisci.


## Backups

Il servizio db di BookWyrm scarica una copia di backup del suo database nella sua directory `/backups` ogni giorno a mezzanotte UTC. I backup sono chiamati `backup__%Y-%m-%d.sql`.

Il servizio db ha uno script opzionale per potare periodicamente la directory di backup in modo che tutti i backup giornalieri recenti siano mantenuti, ma per i backup più vecchi, vengono conservati solo i backup settimanali o mensili. Per abilitare questo script:

- Annulla il commento sulla riga finale in `postgres-docker/cronfile`
- ricostruisci la tua istanza `docker-compose up --build`

Puoi copiare i backup dal volume di backup alla tua macchina ospite con `docker cp`:

- Eseguire `docker-compose ps` per confermare il nome completo del servizio db (probabilmente è `bookwyrm_db_1`.
- Esegui `docker cp <container_name>:/backups <host machine path>`

## Conflitti Di Porta

BookWyrm ha più servizi che vengono eseguiti sulle loro porte predefinite. Ciò significa che, a seconda di che altro si sta eseguendo sulla vostra macchina ospite, si possono eseguire errori durante la costruzione o l'esecuzione di BookWyrm quando i tentativi di collegare a quelle porte falliscono.

Se ciò si verifica, è necessario modificare la configurazione per eseguire servizi su diverse porte. Questo può richiedere uno o più cambiamenti i seguenti file:

- `docker-compose.yml`
- `nginx/production.conf` or `nginx/reverse_proxy.conf` depending on NGINX_SETUP in .env-file
- `.env` (Si crea questo file da soli durante l'installazione)

Se si è già in esecuzione un server web sulla propria macchina, è necessario impostare un proxy inverso.

## Connettiti

Poiché BookWyrm è un progetto giovane, stiamo ancora lavorando per un programma di rilascio stabile, e ci sono molti bug e cambiamenti di rottura. C'è un team GitHub che può essere etichettato quando c'è qualcosa di importante da sapere su un aggiornamento, a cui puoi unirti condividendo il tuo nome utente GitHub. Ci sono alcuni modi per entrare in contatto:

 - Open an issue or pull request to add your instance to the [official list](https://joinbookwyrm.com/instances/)
 - Raggiungi al progetto su [Mastodon](https://tech.lgbt/@bookwyrm) o [invia un'email al manutentore](mailto:mousereeve@riseup.net) direttamente con il tuo nome utente GitHub
 - Entra nella stanza di chat [Matrix](https://matrix.to/#/#bookwyrm:matrix.org)
