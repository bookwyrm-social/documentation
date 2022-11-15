- - -
Title: Verwenden eines Reverse-Proxy Date: 2021-05-11 Order: 4
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

Bevor Sie nginx einrichten können, müssen Sie Ihr nginx-Konfigurationsverzeichnis finden, das von Ihrer Plattform abhängt und wie Sie nginx installiert haben. Weitere Informationen finden Sie im [nginx Guide](http://nginx.org/en/docs/beginners_guide.html).

Um Ihren Server einzurichten:

- In Ihrer `nginx.conf`-Datei stellen Sie sicher, dass `include servers/*;` nicht auskommentiert ist.
- Erstellen Sie in Ihrem nginx-`Server`-Verzeichnis eine neue Datei, die nach deiner Domain benannt ist und die folgende Informationen enthält:

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
- führen Sie `sudo certbot run --nginx --email YOUR_EMAIL -d your-domain.com -d www.your-domain.com` aus
- nginx neustarten

Wenn alles richtig funktioniert hat, sollte Ihre BookWyrm-Instanz nun extern zugänglich sein.

*Hinweis: Der `proxy_set_header Host $host;` ist unerlässlich; wenn Sie ihn nicht einbinden, werden eingehende Nachrichten von föderierten Servern abgelehnt.*

*Hinweis: Der Pfad der SSL Zertifikate kann je nach Betriebssystem Ihres Servers variieren*

