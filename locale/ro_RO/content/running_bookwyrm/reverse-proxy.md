## Rularea BookWyrm în spatele unui Reverse-Proxy
Dacă rulați un alt server web pe mașina dvs., trebuie să-l configurați să transmită cererile web către BookWyrm.

Configurația BookWyrm de bază are deja un server nginx care redirecționează cererile către aplicația Django care se ocupă de SSL și deservește în mod direct fișierele statice. Fișierele statice sunt stocate într-un volum Docker la care au acces mai multe servicii BookWrym, deci nu este recomandat să înlăturați complet acest server.

Pentru a rula BookWyrm în spatele unui reverse-proxy, faceți următoarele schimbări:

- În `nginx/default.conf`:
    - Comentați cele două servere implicite
    - Decomentați server-ul etichetat „Reverse-Proxy server”
    - Înlocuiți `your-domain.com` cu numele domeniului dvs.
- În `docker-compose.yml`:
    - În `services` -> `nginx` -> `ports`, comentați porturile implicite și adăugați `- 8001:8001`
    - În `services` -> `nginx` -> `volumes`, comentați cele două volume care încep `./certbot/`
    - În `services`, comentați serviciul `certbot`

În acest moment, puteți urmări instrucțiunile [setup](#server-setup) listate. Odată ce Docker rulează, puteți accesa instanța dvs. de BookWyrm la `http://localhost:8001` (**NOTĂ:** serverul dvs. nu este accesibil prin `https`).

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
- rulați `sudo certbot run --nginx --email YOUR_EMAIL -d your-domain.com -d www.your-domain.com`
- reporniți nginx

Dacă totul a funcționat corect, instanța dvs. BookWyrm ar trebui să fie acum accesibilă din exterior.

*Notă: `proxy_set_header Host $host;` este esențial; dacă nu-l includeți, mesajele primite de la serverele federate vor fi respinse.*

*Notă: locația certificatelor SSL poate varia în funcție de SO (sistemul de operare) al serverului dvs.*

