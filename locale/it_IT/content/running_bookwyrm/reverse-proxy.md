- - -
Titolo: Usare un Proxy inverso Data: 2021-05-11 Ordine: 4
- - -

## Avvio di BookWyrm Dietro un Proxy inverso
Se si esegue un altro web-server sulla vostra macchina, si dovrebbe avere esso gestire le richieste di proxy web a BookWyrm.

La configurazione predefinita di BookWyrm ha già un server nginx che i proxy richiedono all'app django che gestisce SSL e serve direttamente file statici. I file statici sono memorizzati in un volume Docker che diversi servizi di accesso a BookWyrm, quindi non è consigliabile rimuovere completamente questo server.

Per eseguire BookWyrm dietro un proxy inverso, effettuare le seguenti modifiche:

- In `nginx/default.conf`:
    - Commenta i due server predefiniti
    - Annulla il commento del server etichettato Server Reverse-Proxy
    - Sostituisci `your-domain.com` con il tuo nome di dominio
- In `docker-compose.yml`:
    - In `services` -> `nginx` -> `ports`, commenta le porte predefinite e aggiungi `- 8001:8001`
    - Nei servizi `` -> `nginx` -> `volumi`commenta i due volumi che iniziano `./certbot/`
    - In `services`, commenta il servizio `certbot`

A questo punto, puoi seguire, le istruzioni di configurazione [](#server-setup) come elencate. Una volta avviato il docker, puoi accedere alla tua istanza BookWyrm su `http://localhost:8001` (**NOTA:** il tuo server non è accessibile su `https`).

I passaggi per configurare un proxy inverso dipendono dal server.

#### Nginx

Prima di poter impostare nginx, dovrai individuare la tua directory di configurazione nginx, che dipende dalla tua piattaforma e da come hai installato nginx. Vedi la guida [nginx](http://nginx.org/en/docs/beginners_guide.html) per i dettagli.

Per configurare il server:

- Nel tuo file `nginx.conf`, assicurati che `includa server/*;` non sia commentato.
- Nella directory di nginx `server`, crea un nuovo file dal nome del tuo dominio contenente le seguenti informazioni:

``` { .nginx }
server {
    server_name your-domain.com www.your-domain. om;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
    }

    location /images/ {
        proxy_pass http://localhost:8001;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
    }

    location /static/ {
        proxy_pass http://localhost:8001;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
    }

    ascolta [::]:80 ssl;
    ascolta 80 ssl;
}
```

Per impostare con un blocco ssl:
``` { .nginx }
server {
    server_name your. omain;

    listen [::]:80;
    listen 80;
    add_header Strict-Transport-Security "max-age=31536000; ncludeSubDomains" sempre;
    riscrivere ^ ↓ ://$server_name$request_uri;
    location / { return 301 ↓ ://$host$request_uri; }
}

# Codice SSL
ssl_certificate /etc/letsencrypt/live/your. omain/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/your.domain/privkey. em;

server {
    listen [::]:443 ssl http2;
    ascolta 443 ssl http2;

    server_name tuo. omain;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" sempre;
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
    }

    location /images/ {
        proxy_pass http://localhost:8001;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
    }

    location /static/ {
        proxy_pass http://localhost:8001;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
    }
}
```
- esegui `sudo certbot esegui --nginx --email YOUR_EMAIL -d your-domain.com -d www.your-domain.com`
- riavvia nginx

Se tutto funzionava correttamente, ora la tua istanza BookWyrm dovrebbe essere accessibile esternamente.

*Nota: l'host `proxy_set_header $host;` è essenziale; se non lo includi, i messaggi in arrivo da server federati saranno rifiutati.*

*Nota: la posizione dei certificati ssl può variare a seconda del sistema operativo del server*

