Title: Using a Reverse-Proxy
Date: 2021-04-13
Order: 3

## Running BookWyrm Behind a Reverse-Proxy
If you are running another web-server on your machine, you should have it handle proxying web requests to BookWyrm.

The default BookWyrm configuration already has an nginx server that proxies requests to the django app that handles SSL and directly serves static files.
The static files are stored in a Docker volume that several BookWyrm services access, so it is not recommended to remove this server completely.

To run BookWyrm behind a reverse-proxy, make the following changes:

- In `nginx/default.conf`:
    - Comment out the two default servers
    - Uncomment the server labeled Reverse-Proxy server
    - Replace `your-domain.com` with your domain name
- In `docker-compose.yml`:
    - In `services` -> `nginx` -> `ports`, comment out the default ports and add `- 8001:8001`
    - In `services` -> `nginx` -> `volumes`, comment out the two volumes that begin `./certbot/`
    - In `services`, comment out the `certbot` service

At this point, you can follow, the [setup](#server-setup) instructions as listed.
Once docker is running, you can access your BookWyrm instance at `http://localhost:8001` (**NOTE:** your server is not accessible over `https`).

Steps for setting up a reverse-proxy are server dependent.

#### Nginx

Before you can set up nginx, you will need to locate your nginx configuration directory, which is dependent on your platform and how you installed nginx.
See [nginx's guide](http://nginx.org/en/docs/beginners_guide.html) for details.

To set up your server:
- In you `nginx.conf` file, ensure that `include servers/*;` isn't commented out.
- In your nginx `servers` directory, create a new file named after your domain containing the following information:
```
:::nginx linenums=false
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
- run `sudo certbot run --nginx --email YOUR_EMAIL -d your-domain.com -d www.your-domain.com`
- restart nginx

If everything worked correctly, your BookWyrm instance should now be externally accessible.


