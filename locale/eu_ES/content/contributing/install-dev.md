- - -
Title: Developer Environment Date: 2025-05-26 Order: 5
- - -

## Aurrebaldintzak

Jarraibide hauen arabera, BookWyrm ari zara garatzen Docker erabiliz. Ezer baino lehenago instalatu behar dituzu [Docker](https://docs.docker.com/engine/install/) eta [docker-compose](https://docs.docker.com/compose/install/).

## Garapen ingurunearen konfigurazioa

### Get the code

1. Eskura ezazu [GitHub-etik BookWyrm-en kode-basea](https://github.com/bookwyrm-social/bookwyrm). Paketearen [fork bat sortu](https://docs.github.com/en/get-started/quickstart/fork-a-repo) dezakezu, ondotik [erabili `git clone` kodea deskargatzeko](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) zure ordenagailuan.
2. Joan zure ordenagailuko kodea duen direktoriora, orain direktorio honetatik lan egingo duzu.
3. Development occurs on the `main` branch, so ensure that is the branch you have checked out: `git checkout main`
4. Konfigura ezazu zure garapen-inguruneko aldagaien artxiboa, inguruneko adibide-fitxategia (`.env.example`) `.env` izeneko fitxategi berri batean kopiatuz. Komando-lerroan, hori egin dezakezu idatziz:
``` { .sh }
cp .env.example .env
```

### Configure your environment settings

In `.env`:

4. change `DEBUG` to `true`
5. If you use a tunneling/proxy service like [ngrok](https://ngrok.com), set `DOMAIN` to to the domain name you are using (e.g. `abcd-1234.ngrok-free.app`). Otherwise, set `DOMAIN` to `localhost`
6. change `NGINX_SETUP` to `reverse_proxy` (this prevents BookWyrm trying to set up https certificates on your development machine)
7. If you need to use a particular port (e.g. if you are tunneling via ngrok), uncomment `PORT` and set it (e.g. `PORT=1333`). If using `localhost` this is optional.

Check that you have [all the required settings configured](/environment.html#required-environment-settings) before proceeding.

If you try to register your admin account and see a message that `CSRF verification failed` you may have set your domain or port incorrectly.

### Email (optional)

If you want to test sending emails, you will need to [set up appropriate real values](/environment.html#email-configuration) in the "Email config" section. You do not need to change anything for [the separate `EMAIL` setting](/environment.html#email).

### Build and run

8. Komando-lerroan, exekutatu:

``` { .sh }
./bw-dev build            # Build the docker images
./bw-dev setup            # Initialize the database and run migrations. Note the ADMIN key at the end of this output. You'll need it to register the first admin user.
./bw-dev up               # Start the docker containers
```

9. Once the build is complete, you can access the instance at `http://localhost`, your ngrok domain, or `http://localhost:{PORT}`, depending on you domain and port configuration.
10. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

Kuriosa bazara: `./bw-dev` komandoa shell skript soil bat da eta beste hainbat tresna exekutatzen ditu: aurreko komandoen ordez, zuk `docker-compose build` edo `docker-compose up` exekutatzen ahal zenuen zuzenean, nahi izanez gero. `./bw-dev` komandoak leku bakar batean biltzen ditu erosotasun gehiagorako. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Ereduak editatzea edo sortzea

Eredu bat aldatzen edo sortzen baduzu, seguruenik datu-basearen egitura aldatuko duzu. Aldaketa horiek eragina izan dezaten, Djangoko `makemigrations` komandoa exekutatu beharko duzu [Django migrations file](https://docs.djangoproject.com/en/3.2/topics/migrations) berri bat sortzeko, eta, ondoren, `migrate` komandoa, azken hau migratzeko:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

## Fitxategi estatikoak editatzea
CSS edo JavaScript kodea editatzen duzun bakoitzean, berriro exekutatu beharko duzu `collectstatic` komandoa, zure aldaketek eragina izan dezaten:
``` { .sh }
./bw-dev collectstatic
```

[yarn instalatuta](https://yarnpkg.com/getting-started/install) baduzu, exekuta dezakezu `yarn watch:static`, `bookwyrm/static` errepertorioan aldaketa bat gertatzen den bakoitzean aurreko scripta automatikoki exekutatzeko.
