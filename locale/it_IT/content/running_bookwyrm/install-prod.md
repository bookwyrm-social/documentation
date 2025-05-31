- - -
Titolo: Installazione in produzione Data: 2021-05-18 Ordine: 1
- - -

Questo progetto è ancora giovane e al momento non è molto stabile, quindi si prega di procedere con cautela quando si esegue in produzione.

## Configurazione server
- Ottieni un nome di dominio e imposta DNS per il tuo server. Dovrai indicare i nameservers del tuo dominio sul tuo provider DNS al server dove ospiterai BookWyrm. Ecco le istruzioni per [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Impostare il server con i firewall appropriati per l'esecuzione di un'applicazione web (questo set di istruzioni è testato contro Ubuntu 20.04). Ecco le istruzioni per [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Imposta un servizio email (come [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) e le impostazioni SMTP/DNS appropriate. Usa la documentazione del servizio per configurare il tuo DNS
- [Installa Docker e docker-compose](https://docs.docker.com/compose/install/)

## Installa e configura BookWyrm

La filiale `di produzione` di BookWyrm contiene una serie di strumenti non presenti nel ramo `principale` che sono adatti per funzionare in produzione, come le modifiche `docker-compose` per aggiornare i comandi predefiniti o la configurazione dei container, e le singole modifiche alla configurazione del contenitore per abilitare cose come SSL o backup regolari.

Istruzioni per la gestione di BookWyrm in produzione:

- Ottieni il codice applicativo: `git clone git@github.com:bookwyrm-social/bookwyrm.git`
- Passa alla filiale `produzione`: `git checkout production`
- Crea il tuo file di variabili di ambiente, `cp .env.example .env`e aggiorna quanto segue:
    - `SECRET_KEY` <unk> Una stringa segreta di caratteri difficile da indovinare
    - `DOMAIN` <unk> Il tuo dominio web
    - `EMAIL` <unk> Indirizzo email da utilizzare per la verifica del dominio certbot
    - `POSTGRES_PASSWORD` <unk> Imposta una password sicura per il database
    - `REDIS_ACTIVITY_PASSWORD` <unk> Imposta una password sicura per il sottosistema Attività Redis
    - `REDIS_BROKER_PASSWORD` <unk> Imposta una password sicura per il sottosistema Broker coda Redis
    - `FLOWER_USER` <unk> Il tuo nome utente per accedere al monitor della coda di Flower
    - `FLOWER_PASSWORD` <unk> La tua password sicura per accedere al monitor delle code di Flower
    - `EMAIL_HOST_USER` <unk> L'indirizzo "da" che la tua app utilizzerà quando invierai email
    - `EMAIL_HOST_PASSWORD` <unk> La password fornita dal tuo servizio email
- Configura nginx
    - Crea una copia della configurazione del modello di produzione e impostala per l'uso in nginx `cp nginx/production nginx/default.conf`
    - Aggiorna `nginx/default.conf`:
        - Sostituisci `your-domain.com` con il tuo nome di dominio ovunque nel file (incluse le righe che sono attualmente commentate)
        - Se non stai usando il sottodominio `www`, rimuovi il dominio www.your-dominio. om version of the domain from the `server_name` in the first server block in `nginx/default. onf` e rimuovere `-d www.${DOMAIN}` flag alla fine del comando `certbot` in `docker-compose.yml`.
        - Se stai utilizzando un altro web-server sulla tua macchina ospite, dovrai seguire le istruzioni [reverse-proxy](/reverse-proxy.html)
- Inizializza il database eseguendo la migrazione `./bw-dev`
- Eseguire l'applicazione (questo dovrebbe anche impostare un Certbot ssl cert per il tuo dominio) con `docker-compose up --build`, e assicurati che tutte le immagini siano compilate con successo
    - Se si eseguono altri servizi sulla macchina ospite, si possono verificare errori in cui i servizi non funzionano quando si tenta di collegarsi a una porta. Vedi la guida [per la risoluzione dei problemi](#port_conflicts) per consigli su come risolverlo.
- Quando il docker è stato costruito con successo, interrompere il processo con `CTRL-C`
- Configura il reindirizzamento HTTPS
    - In `docker-compose.yml`, commenta il comando certbot attivo, che installa il certificato, e deseleziona la riga sotto, che imposta il rinnovo automatico.
    - In `nginx/default.conf`, decommenta le righe da 18 a 50 per abilitare l'inoltro a HTTPS. Dovresti avere abilitato due blocchi `server`
- Imposta un lavoro `cron` per mantenere i tuoi certificati aggiornati (Lets Encrypt certificates scadono dopo 90 giorni)
    - Digita `crontab -e` per modificare il tuo file cron nella macchina host
    - aggiungi una riga per provare a rinnovare una volta al giorno: `5 0 * * * cd /path/to/your/bookwyrm && docker-compose run --rm certbot`
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
- `nginx/default.conf`
- `.env` (Si crea questo file da soli durante l'installazione)

Se si è già in esecuzione un server web sulla propria macchina, è necessario impostare un proxy inverso.

## Connettiti

Poiché BookWyrm è un progetto giovane, stiamo ancora lavorando per un programma di rilascio stabile, e ci sono molti bug e cambiamenti di rottura. C'è un team GitHub che può essere etichettato quando c'è qualcosa di importante da sapere su un aggiornamento, a cui puoi unirti condividendo il tuo nome utente GitHub. Ci sono alcuni modi per entrare in contatto:

 - Apri un problema o una richiesta di pull per aggiungere la tua istanza alla lista ufficiale [](https://github.com/bookwyrm-social/documentation/blob/main/content/using_bookwyrm/instances.md)
 - Raggiungi al progetto su [Mastodon](https://tech.lgbt/@bookwyrm) o [invia un'email al manutentore](mailto:mousereeve@riseup.net) direttamente con il tuo nome utente GitHub
 - Entra nella stanza di chat [Matrix](https://matrix.to/#/#bookwyrm:matrix.org)
