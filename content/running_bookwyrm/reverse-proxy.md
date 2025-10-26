---
Title: Using a Reverse-Proxy
Date: 2021-05-11
Order: 5
---

## Running BookWyrm Behind a Reverse-Proxy
If you are running another web-server on your machine, you should have it handle proxying web requests to BookWyrm.

The default BookWyrm configuration already has an nginx server that proxies requests to the django app that handles SSL and directly serves static files.
The static files are stored in a Docker volume that several BookWyrm services access, so it is not recommended to remove this server completely.

To run BookWyrm behind a reverse-proxy, make the following changes:

- In `.env`:
    - change `NGINX_SETUP=reverse_proxy`
    - set `PORT=8001`
    - set `USE_HTTPS=true` if your webserver in front of bookwyrm handles the https

At this point, you can follow, the [setup](#server-setup) instructions as listed.
Once docker is running, you can access your BookWyrm instance at `http://localhost:8001` (**NOTE:** your server is not accessible over `https` directly).

Steps for setting up a reverse-proxy are server dependent.

#### Nginx

Before you can set up nginx, you will need to locate your nginx configuration directory, which is dependent on your platform and how you installed nginx.
See [nginx's guide](http://nginx.org/en/docs/beginners_guide.html) for details.

To set up your server:

- In you `nginx.conf` file, ensure that `include servers/*;` isn't commented out.
- In your nginx `servers` directory, create a new file named after your domain containing the following information:

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
- run `sudo certbot run --nginx --email YOUR_EMAIL -d your-domain.com -d www.your-domain.com`
- restart nginx

If everything worked correctly, your BookWyrm instance should now be externally accessible.

*Note: the `proxy_set_header Host $host;` is essential; if you do not include it, incoming messages from federated servers will be rejected.*

*Note: the location of the ssl certificates may vary depending on the OS of your server*


#### Caddy

[Caddy](https://caddyserver.com) is an alternative reverse-proxy server that is simple to use and can manage TLS certificate renewals and static file serving automatically. This guide assumes that you already have a Caddy server running and it has access to the bookwyrm docker network.

To use Caddy instead of nginx as the Reverse-Proxy server, make the following changes:

- In `nginx/default.conf`:
    - Comment out the two default servers
    - Uncomment the server labeled Reverse-Proxy server
    - Replace `your-domain.com` with your domain name
    
- In `docker-compose.yml`:
    - In `services` -> `nginx` -> `ports`, comment out the default ports and add `- 8001:8001`
    - In `services` -> `nginx` -> `volumes`, comment out the two volumes that begin `./certbot/`
    - In `services`, comment out the `certbot` service

- In your Caddyfile add your bookwyrm subdomain:
```Caddyfile
your.domain {
    reverse_proxy /images/* localhost:8001
    reverse_proxy /static/* localhost:8001
    reverse_proxy localhost:8000
}
``
If you were to give `container_name`s to the `nginx` and `web` containers in `docker-compose.yml`, then you could comment out the `ports` sections and use the container names in place of `localhost`. This would secure the raw services from being accessible directly from the outside world.

Caddy will set the headers needed by default for you so there is no further configuration necessary.

It should also be possible to share the static and images volumes with caddy and use caddy's inbuilt file server to server these directly, but this is beyond the scope of this guide.
