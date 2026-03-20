- - -
Title: Using a Reverse-Proxy Date: 2021-05-11 Order: 5
- - -

## BookWyrm hinter einem Reverse-Proxy ausführen
Wenn du einen anderen Webserver auf Ihrem Rechner betreibst, solltest du ihn als Proxy für Web-Anfragen an BookWyrm einrichten.

Die Standardkonfiguration von BookWyrm hat bereits einen nginx-Server, der Anfragen an die Django-App weiterleitet, die SSL verarbeitet und statische Dateien direkt bedient. Die statischen Dateien werden in einem Docker Volume gespeichert, auf das mehrere BookWyrm Dienste zugreifen, daher wird es nicht empfohlen, diesen Server komplett zu entfernen.

Um BookWyrm hinter einem Reverse-Proxy auszuführen, führe folgende Änderungen aus:

- In `.env`:
    - change `NGINX_SETUP=reverse_proxy`
    - set `PORT=8001` or another port number of your choice

An dieser Stelle folge den Anweisungen [Setup](#server-setup) wie aufgeführt. Once docker is running, you can access your BookWyrm instance at `http://localhost:8001` (**NOTE:** your server is not accessible over `https` directly as this is handled by your proxy server).

Schritte zum Einrichten eines Reverse-Proxys sind vom Server abhängig.

#### Nginx

Bevor du nginx einrichten kannst, musst du Ihr nginx-Konfigurationsverzeichnis finden, das abhängig von deiner Plattform und nginx-Installation ist. Weitere Informationen findest du im [nginx Guide](http://nginx.org/en/docs/beginners_guide.html).

Um deinen Server einzurichten:

- Stelle in deiner `nginx.conf`-Datei sicher, dass `include servers/*;` nicht auskommentiert ist.
- Erstelle im nginx-`Server`-Verzeichnis eine neue Datei, die nach deiner Domain benannt ist und die folgenden Informationen enthält:

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

Um mit einem SSL-Block einzurichten:
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
- führe `sudo certbot run --nginx --email YOUR_EMAIL -d your-domain.com -d www.your-domain.com` aus
- nginx neustarten

Wenn alles richtig funktioniert hat, sollte deine BookWyrm-Instanz nun extern zugänglich sein.

_**Note**: the `proxy_set_header Host $host;` is essential; if you do not include it, incoming messages from federated servers will be rejected._

_**Note**: the location of the ssl certificates may vary depending on the OS of your server*_
