- - -
Title: Using a Reverse-Proxy Date: 2021-05-11 Order: 4
- - -

## Running BookWyrm Behind a Reverse-Proxy
If you are running another web-server on your machine, you should have it handle proxying web requests to BookWyrm.

The default BookWyrm configuration already has an nginx server that proxies requests to the django app that handles SSL and directly serves static files. The static files are stored in a Docker volume that several BookWyrm services access, so it is not recommended to remove this server completely.

To run BookWyrm behind a reverse-proxy, make the following changes:

- In `nginx/default.conf`:
    - Comment out the two default servers
    - Uncomment the server labeled Reverse-Proxy server
    - Replace `your-domain.com` with your domain name
- In `docker-compose.yml`:
    - In `services` -> `nginx` -> `ports`, comment out the default ports and add `- 8001:8001`
    - In `services` -> `nginx` -> `volumes`, comment out the two volumes that begin `./certbot/`
    - In `services`, comment out the `certbot` service

At this point, you can follow, the [setup](#server-setup) instructions as listed. Once docker is running, you can access your BookWyrm instance at `http://localhost:8001` (**NOTE:** your server is not accessible over `https`).

Steps for setting up a reverse-proxy are server dependent.

#### Nginx

Przed konfiguracją nginx należy zlokalizować swój katalog konfiguracji nginx, który jest zależny od platformy i jak nginx został zainstalowany. Sprawdź [przewodnik nginx](http://nginx.org/en/docs/beginners_guide.html) po więcej szczegółów.

Aby skonfigurować swój serwer:

- Upewnij się, że w pliku `nginx.conf` wiersz `include servers/*;` nie jest zawarty w komentarzu.
- W swoim katalogu `servers` utwórz nowy plik z nazwą Twojej domeny zawierający następujące informacje:

``` { .nginx }
server {
    server_name your-domain.com www.your-domain.com;

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

    listen [::]:80 ssl;
    listen 80 ssl;
}
```

Do konfiguracji bloku SSL:
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
- wykonaj `sudo certbot run --nginx --email TWÓJ_EMAIL -d twoja-domena.pl -d www.twoja-domena.pl`
- uruchom ponownie nginx

Jeśli wszystko przebiegło pomyślnie, Twoja instancja BookWyrm powinna być od teraz dostępna z zewnątrz.

*Note: the `proxy_set_header Host $host;` is essential; if you do not include it, incoming messages from federated servers will be rejected.*

*Uwaga: lokalizacja certyfikatów SSL może różnić się w zależności od systemu operacyjnego Twojego serwera*

