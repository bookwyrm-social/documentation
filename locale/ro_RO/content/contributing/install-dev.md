- - -
Title: Developer Environment Date: 2025-05-26 Order: 5
- - -

## Cerințe preliminare

Aceste instrucțiuni presupun că dezvoltați BookWyrm folosind Docker. Va trebui să [instalați Docker](https://docs.docker.com/engine/install/) și [docker-compose](https://docs.docker.com/compose/install/) pentru a începe.

## Configurați mediul de dezvoltare

### Get the code

1. Obțineți o copie a [bazei de cod BookWyrm de pe GitHub](https://github.com/bookwyrm-social/bookwyrm). Puteți [crea un fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) al depozitului și apoi [folosi `git clone` pentru a descărca codul](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) pe calculatorul dumneavoastră.
2. Mergeți în dosarul care conține codul pe calculatorul dvs, veți lucra aici de aici în colo.
3. Configurați fișierul de variabile de mediu al dvs. copiind fișierul de mediu exemplu (`.env.example`) într-un nou fișier numit `.env`. În linia de comandă, puteți face asta cu:
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

8. În linia de comandă, rulați:

``` { .sh }
./bw-dev build            # Build the docker images
./bw-dev setup            # Initialize the database and run migrations. Note the ADMIN key at the end of this output. You'll need it to register the first admin user.
./bw-dev up               # Start the docker containers
```

9. Once the build is complete, you can access the instance at `http://localhost`, your ngrok domain, or `http://localhost:{PORT}`, depending on you domain and port configuration.
10. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

Dacă sunteți curios: comanda `./bw-dev` este un simplu script shell care rulează multe alte comenzi: deasupra, ați putea sări peste ea și rula `docker-compose build` sau `docker-compose up` direct dacă doriți. `./bw-dev` doar le colectează într-un singur loc pentru conveniență. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Editați sau configurați modele

Dacă schimbați sau creați un model, veți schimba probabil structura bazei de date. Pentru ca aceste schimbă să aibă efect va trebui să rulați comanda Django `makemigrations` pentru a crea un nou [fișier de migrare Django](https://docs.djangoproject.com/en/3.2/topics/migrations) și apoi `migrate`:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

## Editați fișiere statice
De fiecare dată când editați CSS sau JavaScript, va trebui să rulați comanda Django `collectstatic` pentru ca schimbările dvs. să aibă efect:
``` { .sh }
./bw-dev collectstatic
```

Dacă aveți [yarn instalat](https://yarnpkg.com/getting-started/install), puteți rula `yarn watch:static` pentru a rula automat scriptul precedent de fiecare dată când o schimbare are loc în dosarul `bookwyrm/static`.
