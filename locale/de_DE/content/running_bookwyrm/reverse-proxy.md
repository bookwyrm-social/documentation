- - -
Titel: Verwenden eines Reverse-Proxy Datum: 2021-05-11 Bestellung: 3
- - -

## BookWyrm hinter einem Reverse-Proxy ausführen
Wenn Sie einen anderen Webserver auf Ihrem Rechner betreiben, sollten Sie ihn als Proxy für Web-Anfragen an BookWyrm einrichten.

Die Standardkonfiguration von BookWyrm hat bereits einen nginx-Server, der Anfragen an die Django-App weiterleitet, die SSL verarbeitet und statische Dateien direkt bedient. Die statischen Dateien werden in einem Docker Volume gespeichert, auf das mehrere BookWyrm Dienste zugreifen, daher wird es nicht empfohlen, diesen Server komplett zu entfernen.

Um BookWyrm hinter einem Reverse-Proxy auszuführen, führen Sie folgende Änderungen aus:

- In `nginx/default.conf`:
    - Kommentieren Sie die zwei Standardserver
    - Kommentieren Sie den Server beschrift als Reverse-Proxy Server aus
    - Ersetzen Sie `your-domain.com` durch Ihren Domain-Namen
- In `docker-compose.yml`:
    - In `-services` -> `nginx` -> `ports`, kommentieren Sie die Standard-Ports und fügen Sie `- 8001:8001` hinzu
    - In `services` -> `nginx` -> `volumes` kommentieren Sie die beiden Volumes, die mit `./certbot/` beginnen
    - In `services` kommentieren Sie den `certbot` Dienst

An dieser Stelle folgen Sie den Anweisungen [Setup](#server-setup) wie aufgeführt. Sobald Docker läuft, können Sie auf Ihre BookWyrm-Instanz zugreifen unter `http://localhost:8001` (**HINWEIS:** Ihr Server ist nicht über `https`).

Schritte zum Einrichten eines Reverse-Proxys sind vom Server abhängig.

#### Nginx

Bevor Sie nginx einrichten können, müssen Sie Ihr nginx-Konfigurationsverzeichnis finden, das von Ihrer Plattform abhängt und wie Sie nginx installiert haben. See [nginx's guide](http://nginx.org/en/docs/beginners_guide.html) for details.

To set up your server:

- In you `nginx.conf` file, ensure that `include servers/*;` isn't commented out.
- In your nginx `servers` directory, create a new file named after your domain containing the following information:

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
- run `sudo certbot run --nginx --email YOUR_EMAIL -d your-domain.com -d www.your-domain.com`
- nginx neustarten

If everything worked correctly, your BookWyrm instance should now be externally accessible.

*Note: the `proxy_set_header Host $host;` is essential; if you do not include it, incoming messages from federated servers will be rejected.*

*Note: the location of the ssl certificates may vary depending on the OS of your server*

