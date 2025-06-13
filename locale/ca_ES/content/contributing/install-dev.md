- - -
Title: Developer Environment Date: 2025-05-26 Order: 5
- - -

## Requisits previs

Aquestes instruccions assumeixen que estàs desenvolupant BookWyrm mitjançant Docker. Necessitaràs [instal·lar Docker](https://docs.docker.com/engine/install/) i [docker-compose](https://docs.docker.com/compose/install/) per començar.

## Configuració de l'entorn de desenvolupament

### Get the code

1. Aconsegueix una còpia del [codi base de BookWyrm a GitHub](https://github.com/bookwyrm-social/bookwyrm). Pots [crear una derivació](https://docs.github.com/en/get-started/quickstart/fork-a-repo) del repositori i, llavors [utilitzar `git clone` per descarregar el codi](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) a l'ordinador.
2. Ves al directori que conté el codi al teu ordinador, treballaràs des d'aquí d'ara en endavant.
3. Configura el teu fitxer de variables d'entorn de desenvolupament copiant el fitxer d'entorn d'exemple (`.env.example`) a un nou fitxer anomenat `.env`. A la línia de comandes, pots fer-ho mitjançant:
``` { .sh }
cp .env.example .env
```

### Configure your environment settings

In `.env`:

4. change `DEBUG` to `true`
5. If you use a tunneling/proxy service like [ngrok](https://ngrok.com), set `DOMAIN` to to the domain name you are using (e.g. `abcd-1234.ngrok-free.app`). Otherwise, set `DOMAIN` to `localhost`
6. change `NGINX_SETUP` to `reverse_proxy` (this prevents BookWyrm trying to set up https certificates on your development machine)
7. If you need to use a particular port (e.g. if you are tunneling via ngrok), uncomment `PORT` and set it (e.g. `PORT=1333`). If using `localhost` this is optional.

If you try to register your admin account and see a message that `CSRF verification failed`, you should check these settings, as you may have set your domain or port incorrectly.

### Email (optional)

If you want to test sending emails, you will need to [set up appropriate values](/environment.html#email-configuration) in the "Email config" section. You do not need to change anything for [the separate `EMAIL` setting](/environment.html#email).

### Build and run

8. A la línia de comandes, executa:

``` { .sh }
./bw-dev build            # Build the docker images
./bw-dev setup            # Initialize the database and run migrations. Note the ADMIN key at the end of this output. You'll need it to register the first admin user.
./bw-dev up               # Start the docker containers
```

9. Once the build is complete, you can access the instance at `http://localhost`, your ngrok domain, or `http://localhost:{PORT}`, depending on you domain and port configuration.
10. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

Si ets curiós: el comandament `./bw-dev` és un senzill script que fa funcionar unes altres eines: a sobre, pots ometre o iniciar directament `docker-composer build` o `docker-composer up` si vols. `./bw-dev` els recull tots a un lloc comú per comoditat. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Editant o creant Models

Si modifiqueu o creeu un model, és probable que canvieu l'estructura de la base de dades. A fi que aquests canvis siguin efectius, haureu d'executar l'ordre `makemigrations` de Django per a crear un [fitxer de migració de Django](https://docs.djangoproject.com/en/3.2/topics/migrations) nou, i després `migrar-lo`:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

## Editant fitxers estàtics
Sempre que editeu el CSS o el JavaScript, haureu de tornar a executar l'ordre `collectstatic` a fi que els canvis tinguin efecte:
``` { .sh }
./bw-dev collectstatic
```

Si heu [instal·lat el Yarn](https://yarnpkg.com/getting-started/install), podeu executar `yarn watch:static` a fi que s'executi de forma automàtica l'script anterior cada cop que hi hagi un canvi al directori `bookwyrm/static`.
