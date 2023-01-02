- - -
Title: Verwenden eines Reverse-Proxy Date: 2021-05-11 Order: 4
- - -

## BookWyrm hinter einem Reverse-Proxy ausführen
Wenn du einen anderen Webserver auf Ihrem Rechner betreibst, solltest du ihn als Proxy für Web-Anfragen an BookWyrm einrichten.

Die Standardkonfiguration von BookWyrm hat bereits einen nginx-Server, der Anfragen an die Django-App weiterleitet, die SSL verarbeitet und statische Dateien direkt bedient. Die statischen Dateien werden in einem Docker Volume gespeichert, auf das mehrere BookWyrm Dienste zugreifen, daher wird es nicht empfohlen, diesen Server komplett zu entfernen.

Um BookWyrm hinter einem Reverse-Proxy auszuführen, führe folgende Änderungen aus:

- In `nginx/default.conf`:
    - Kommentiere die zwei Standardserver aus
    - Kommentiere den Server beschrift als Reverse-Proxy Server aus
    - Ersetze `your-domain.com` durch deinen Domain-Namen
- In `docker-compose.yml`:
    - In `-services` -> `nginx` -> `ports`, kommentiere die Standard-Ports aus und füge `- 8001:8001` hinzu
    - In `services` -> `nginx` -> `volumes` kommentiere die beiden Volumes aus, die mit `./certbot/` beginnen
    - In `services` kommentiere den `certbot` Dienst aus

An dieser Stelle folge den Anweisungen [Setup](#server-setup) wie aufgeführt. Sobald Docker läuft, kannst du auf deine BookWyrm-Instanz zugreifen unter `http://localhost:8001` (**HINWEIS:** Dein Server ist nicht über `https` erreichbar).

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
- führe `sudo certbot run --nginx --email YOUR_EMAIL -d your-domain.com -d www.your-domain.com` aus
- nginx neustarten

Wenn alles richtig funktioniert hat, sollte deine BookWyrm-Instanz nun extern zugänglich sein.

*Hinweis: Der `proxy_set_header Host $host;` ist unerlässlich; wenn du ihn nicht einbindest, werden eingehende Nachrichten von föderierten Servern abgelehnt.*

*Hinweis: Der Pfad der SSL Zertifikate kann je nach Betriebssystem Ihres Servers variieren*

