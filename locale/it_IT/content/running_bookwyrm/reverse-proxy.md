- - -
Title: Using a Reverse-Proxy Date: 2021-05-11 Order: 5
- - -

## Avvio di BookWyrm Dietro un Proxy inverso
Se si esegue un altro web-server sulla vostra macchina, si dovrebbe avere esso gestire le richieste di proxy web a BookWyrm.

La configurazione predefinita di BookWyrm ha già un server nginx che i proxy richiedono all'app django che gestisce SSL e serve direttamente file statici. I file statici sono memorizzati in un volume Docker che diversi servizi di accesso a BookWyrm, quindi non è consigliabile rimuovere completamente questo server.

Per eseguire BookWyrm dietro un proxy inverso, effettuare le seguenti modifiche:

- In `.env`:
    - change `NGINX_SETUP=reverse_proxy`
    - set `PORT=8001` or another port number of your choice

A questo punto, puoi seguire, le istruzioni di configurazione [](#server-setup) come elencate. Once docker is running, you can access your BookWyrm instance at `http://localhost:8001` (**NOTE:** your server is not accessible over `https` directly as this is handled by your proxy server).

I passaggi per configurare un proxy inverso dipendono dal server.

#### Nginx

Prima di poter impostare nginx, dovrai individuare la tua directory di configurazione nginx, che dipende dalla tua piattaforma e da come hai installato nginx. Vedi la guida [nginx](http://nginx.org/en/docs/beginners_guide.html) per i dettagli.

Per configurare il server:

- Nel tuo file `nginx.conf`, assicurati che `includa server/*;` non sia commentato.
- Nella directory di nginx `server`, crea un nuovo file dal nome del tuo dominio contenente le seguenti informazioni:

``` { .nginx }
server {
    server_name your-domain.com www.your-domain.com;

    location / {
        proxy_pass http://localhost:8001;
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

    listen [::]:80 ssl;
    listen 80 ssl;
}
```

Per impostare con un blocco ssl:
``` { .nginx }
server {
    server_name your.domain;

    listen [::]:80;
    listen 80;
    add_header Strict-Transport-Security "max-age=31536000;includeSubDomains" always;
    rewrite ^ https://$server_name$request_uri;
    location / { return 301 https://$host$request_uri; }
}

# SSL code
ssl_certificate /etc/letsencrypt/live/your.domain/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/your.domain/privkey.pem;

server {
    listen [::]:443 ssl http2;
    listen 443 ssl http2;

    server_name your.domain;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    location / {
        proxy_pass http://localhost:8001;
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

_**Note**: the `proxy_set_header Host $host;` is essential; if you do not include it, incoming messages from federated servers will be rejected._

_**Note**: the location of the ssl certificates may vary depending on the OS of your server*_
