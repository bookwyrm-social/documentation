- - -
Title: Using a Reverse-Proxy Date: 2021-05-11 Order: 5
- - -

## Faire fonctionner BookWyrm derrière un proxy inverse
Si un autre serveur web est installé sur la machine, il serait préférable que ce dernier fasse proxy pour les requêtes vers BookWyrm.

La configuration par défaut de BookWyrm a déjà un serveur Nginx qui sert de proxy pour les requêtes vers l'application Django gérant le SSL et servant directement les fichiers statiques. Les fichiers statiques sont stockés dans un volume Docker accessible par plusieurs services BookWyrm, il est donc déconseillé de complétement retirer ce serveur.

Pour faire fonctionner BookWyrm derrière un proxy inverse, les changements suivants doivent être faits :

- In `.env`:
    - change `NGINX_SETUP=reverse_proxy`
    - set `PORT=8001` or another port number of your choice

À partir de là, il est possible de suivre [les instructions d'installation](#server-setup) telles quelles. Once docker is running, you can access your BookWyrm instance at `http://localhost:8001` (**NOTE:** your server is not accessible over `https` directly as this is handled by your proxy server).

Les étapes pour configurer un proxy inverse dépendent du serveur.

#### Nginx

Avant de pouvoir configurer Nginx, il faudra trouver son dossier de configuration, qui dépend de la plateforme et de la manière dont Nginx a été installé. Voir [le guide de Nginx](http://nginx.org/en/docs/beginners_guide.html) pour plus de détails.

Pour configurer le serveur :

- Dans le fichier `nginx.conf`, vérifier que `include servers/*;` n'est pas commenté.
- Dans le dossier `servers` de Nginx, créer un nouveau fichier nommé d'après le nom de domaine de l'instance et contenant les informations suivantes :

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

Pour configurer avec un bloc SSL :
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
- Exécuter `sudo certbot run --nginx --email VOTRE_ADRESSE_MAIL -d votre-nom-de-domaine.com -d www.votre-nom-de-domaine.com`
- Redémarrer Nginx

Si tout fonctionne correctement, l'instance BookWyrm devrait à présent être accessible depuis l'extérieur.

_**Note**: the `proxy_set_header Host $host;` is essential; if you do not include it, incoming messages from federated servers will be rejected._

_**Note**: the location of the ssl certificates may vary depending on the OS of your server*_
