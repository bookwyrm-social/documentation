- - -
Title: Using a Reverse-Proxy Date: 2021-05-11 Order: 5
- - -

## Rularea BookWyrm în spatele unui Reverse-Proxy
Dacă rulați un alt server web pe mașina dvs., trebuie să-l configurați să transmită cererile web către BookWyrm.

Configurația BookWyrm de bază are deja un server nginx care redirecționează cererile către aplicația Django care se ocupă de SSL și deservește în mod direct fișierele statice. Fișierele statice sunt stocate într-un volum Docker la care au acces mai multe servicii BookWrym, deci nu este recomandat să înlăturați complet acest server.

Pentru a rula BookWyrm în spatele unui reverse-proxy, faceți următoarele schimbări:

- In `.env`:
    - change `NGINX_SETUP=reverse_proxy`
    - set `PORT=8001` or another port number of your choice

În acest moment, puteți urmări instrucțiunile [setup](#server-setup) listate. Once docker is running, you can access your BookWyrm instance at `http://localhost:8001` (**NOTE:** your server is not accessible over `https` directly as this is handled by your proxy server).

Pașii pentru configurarea unui reverse-proxy sunt independenți de server.

#### Nginx

Înainte de a putea configura nginx, veți avea nevoie să localizați dosarul dvs. de configurare nginx, care este dependent de platforma dvs. și de cum ați instalat nginx. Vedeți [ghidul nginx](http://nginx.org/en/docs/beginners_guide.html) pentru detalii.

Pentru a configura serverul dvs.:

- În fișierul dvs. `nginx.conf`, asigurați-vă că `include servers/*;` nu este comentat.
- În dosarul dvs. nginx `servers`, creați un nou fișier numit după domeniul dvs. conținând următoarele informații:

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

Pentru a configura un bloc SSL:
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
- rulați `sudo certbot run --nginx --email YOUR_EMAIL -d your-domain.com -d www.your-domain.com`
- reporniți nginx

Dacă totul a funcționat corect, instanța dvs. BookWyrm ar trebui să fie acum accesibilă din exterior.

_**Note**: the `proxy_set_header Host $host;` is essential; if you do not include it, incoming messages from federated servers will be rejected._

_**Note**: the location of the ssl certificates may vary depending on the OS of your server*_
