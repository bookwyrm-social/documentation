- - -
Título: Utilizando un Proxy Inverso Fecha: 2021-05-11 Orden: 4
- - -

## Ejecutar BookWyrm detrás de un Proxy Inverso
Si estás ejecutando otro servidor web en tu máquina, deberías tener el control de las solicitudes web proxy a BookWyrm.

La configuración predeterminada de BookWyrm ya tiene un servidor nginx que envía solicitudes a la aplicación de Django la cual maneja SSL y proporciona directamente archivos estáticos. Los archivos estáticos se almacenan en un volumen Docker al que acceden varios servicios de BookWyrm, por lo que no se recomienda eliminar este servidor por completo.

Para ejecutar BookWyrm detrás de un proxy inverso, haz los siguientes cambios:

- En `nginx/default.conf`:
    - Comentar los dos servidores por defecto
    - Descomentar el servidor etiquetado como 'Reverse-Proxy'
    - Reemplaza `your-domain.com` con tu nombre de dominio
- En `docker-compose.yml`:
    - En `services` -> `nginx` -> `ports`, comenta los puertos por defecto y agrega `- 8001:8001`
    - En `services` -> `nginx` -> `volumes`, comento los dos volúmenes que empiecen con `./certbot/`
    - En `services`, comenta el servicio `certbot`

En este punto, puedes seguir, las instrucciones de [configuración](#server-setup) tal y como se listan. Una vez que docker se esté ejecutando, puedes acceder a tu instancia de BookWyrm en `http://localhost:8001` (**NOTA:** tu servidor no es accesible a través de `https`).

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
- Ejecuta `sudo certbot run --nginx --email YOUR_EMAIL -d your-domain.com -d www.your-domain.com`
- Reinicia Nginx

Si todo funciona correctamente, ahora tu instancia de BookWyrm debería ser accesible externamente.

*Nota: el servidor `proxy_set_header $host;` es esencial; si no lo incluyes, los mensajes entrantes de servidores federados serán rechazados.*

*Nota: la ubicación de los certificados ssl puede variar dependiendo del sistema operativo de tu servidor.*

