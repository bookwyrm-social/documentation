- - -
Títol: Utilitzant un Reverse-Proxy Data: 2021-05-11 Ordre: 4
- - -

## Executant BookWyrm rere un Reverse-Proxy
Si s'està executant un altre servidor web a la teva màquina, ho has de gestionar mitjançant proxy per a les consultes a BookWyrm.

La configuració per defecte de BookWyrm ja té un servidor nginx que encamina les demandes a l'aplicatiu de Django que gestiona el SSL, serveix de forma directa els fitxers. Els fitxers estàtics es guarden en un volum Docker que dona servei a diversos serveis de BookWyrm, de manera que no es recomana eliminar aquest servidor completament.

Per fer córrer BookWyrm darrere d'un encaminador revers, fes els canvis següents:

- A `nginx/default.conf`:
    - Comenta els dos servidors per defecte
    - Descomenta el servidor etiquetat com a servidor Reverse-Proxy
    - Substitueix `el-teu-domini.com` pel nom del teu domini
- A `docker-compose.yml`:
    - A `services` -> `nginx` -> `ports`, comenta els ports per defecte i afegeix `- 8001:8001`
    - A `services` -> `nginx` -> `volumes`, comenta els dos volums que comencen per `./certbot/`
    - A `services`, descomenta el servei `Certbot`

En aquest punt, podeu seguir les instruccions de [configuració](#server-setup) que s'indiquen. Un cop s'està executant Docker, podeu accedir a la vostra instància de BookWyrm a `http://localhost:8001` (**NOTA:** el vostre servidor no és accessible a través de `https`).

Els passos per configurar un reverse-proxy són dependents del servidor.

#### Nginx

Abans de poder configurar nginx, haureu de localitzar el vostre directori de configuració de nginx, que depèn de la vostra plataforma i de com heu instal·lat nginx. Visita la [guia nginx](http://nginx.org/en/docs/beginners_guide.html) per a més informació.

Per configurar el teu servidor:

- Al vostre fitxer `nginx.conf`, assegureu-vos que `inclou servidors/*;` no estigui comentat.
- Al vostre directori `servidors` de nginx, creeu un fitxer nou amb el nom del vostre domini que contingui la informació següent:

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

Configuració amb bloqueig ssl:
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
- executa `sudo certbot run --nginx --email EL_TEU_EMAIL -d el-teu-domini.cat -d www.el-teu-domini.cat`
- reinicia nginx

Si tot ha anat bé, la teva instància de BookWyrm seria accessible externament.

*Nota: el `proxy_set_header Host $host;` és essencial; si no l'inclous, els missatges entrants de servidors federats seran rebutjats.*

*Nota: la ubicació dels certificats ssl pot variar segons el sistema operatiu del vostre servidor*

