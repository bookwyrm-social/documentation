- - -
Title: Using a Reverse-Proxy Date: 2021-05-11 Order: 3
- - -

## Rularea BookWyrm în spatele unui Reverse-Proxy
If you are running another web-server on your machine, you should have it handle proxying web requests to BookWyrm.

The default BookWyrm configuration already has an nginx server that proxies requests to the django app that handles SSL and directly serves static files. The static files are stored in a Docker volume that several BookWyrm services access, so it is not recommended to remove this server completely.

To run BookWyrm behind a reverse-proxy, make the following changes:

- În `nginx/default.conf`:
    - Comentați cele două servere implicite
    - Decomentați server-ul etichetat „Reverse-Proxy server”
    - Înlocuiți `your-domain.com` cu numele domeniului dvs.
- În `docker-compose.yml`:
    - În `services` -> `nginx` -> `ports`, comentați porturile implicite și adăugați `- 8001:8001`
    - În `services` -> `nginx` -> `volumes`, comentați cele două volume care încep `./certbot/`
    - În `services`, comentați serviciul `certbot`

At this point, you can follow, the [setup](#server-setup) instructions as listed. Once docker is running, you can access your BookWyrm instance at `http://localhost:8001` (**NOTE:** your server is not accessible over `https`).

Steps for setting up a reverse-proxy are server dependent.

#### Nginx

Before you can set up nginx, you will need to locate your nginx configuration directory, which is dependent on your platform and how you installed nginx. See [nginx's guide](http://nginx.org/en/docs/beginners_guide.html) for details.

To set up your server:

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

To set up with an ssl block:
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

If everything worked correctly, your BookWyrm instance should now be externally accessible.

*Note: the `proxy_set_header Host $host;` is essential; if you do not include it, incoming messages from federated servers will be rejected.*

*Note: the location of the ssl certificates may vary depending on the OS of your server*

