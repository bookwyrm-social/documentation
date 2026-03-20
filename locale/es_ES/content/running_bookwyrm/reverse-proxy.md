- - -
Title: Using a Reverse-Proxy Date: 2021-05-11 Order: 5
- - -

## Ejecutar BookWyrm detrás de un Proxy Inverso
Si estás ejecutando otro servidor web en tu máquina, deberías tener el control de las solicitudes web proxy a BookWyrm.

La configuración predeterminada de BookWyrm ya tiene un servidor nginx que envía solicitudes a la aplicación de Django la cual maneja SSL y proporciona directamente archivos estáticos. Los archivos estáticos se almacenan en un volumen Docker al que acceden varios servicios de BookWyrm, por lo que no se recomienda eliminar este servidor por completo.

Para ejecutar BookWyrm detrás de un proxy inverso, haz los siguientes cambios:

- In `.env`:
    - change `NGINX_SETUP=reverse_proxy`
    - set `PORT=8001` or another port number of your choice

En este punto, puedes seguir, las instrucciones de [configuración](#server-setup) tal y como se listan. Once docker is running, you can access your BookWyrm instance at `http://localhost:8001` (**NOTE:** your server is not accessible over `https` directly as this is handled by your proxy server).

Los pasos para configurar un proxy inverso son dependientes del servidor.

#### Nginx

Antes de configurar nginx, necesitarás localizar tu directorio de configuración de nginx, el cual depende de tu plataforma y de cómo instalaste nginx. Consulta la [guía de nginx](http://nginx.org/en/docs/beginners_guide.html) para más detalles.

Para configurar tu servidor:

- En tu archivo `nginx.conf` asegúrate que `include servers/*;` no esté comentado.
- En el directorio `servers` de tu nginx, crea un nuevo archivo con el nombre de tu dominio que contenga la siguiente información:

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

Para configurar con un bloque ssl:
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
- Ejecuta `sudo certbot run --nginx --email YOUR_EMAIL -d your-domain.com -d www.your-domain.com`
- Reinicia Nginx

Si todo funciona correctamente, ahora tu instancia de BookWyrm debería ser accesible externamente.

_**Note**: the `proxy_set_header Host $host;` is essential; if you do not include it, incoming messages from federated servers will be rejected._

_**Note**: the location of the ssl certificates may vary depending on the OS of your server*_
