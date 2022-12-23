- - -
Izenburua: Garapen ingurumena Eguna: 2021-04-12 Ordena: 3
- - -

## Aurrebaldintzak

Jarraibide hauen arabera, BookWyrm ari zara garatzen Docker erabiliz. Ezer baino lehenago instalatu behar dituzu [Docker](https://docs.docker.com/engine/install/) eta [docker-compose](https://docs.docker.com/compose/install/).

## Garapen ingurunearen konfigurazioa

- Eskura ezazu [GitHub-etik BookWyrm-en kode-basea](https://github.com/bookwyrm-social/bookwyrm). Paketearen [fork bat sortu](https://docs.github.com/en/get-started/quickstart/fork-a-repo) dezakezu, ondotik [erabili `git clone` kodea deskargatzeko](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) zure ordenagailuan.
- Joan zure ordenagailuko kodea duen direktoriora, orain direktorio honetatik lan egingo duzu.
- Konfigura ezazu zure garapen-inguruneko aldagaien artxiboa, inguruneko adibide-fitxategia (`.env.example`) `.env` izeneko fitxategi berri batean kopiatuz. Komando-lerroan, hau egin dezakezu idatziz:
``` { .sh }
cp .env.example .env
```
- `.env` lerroan aldatu `DEBUG` eta idatzi `true`
- Aukera gisa, [ngrok](https://ngrok.com/) gisako zerbitzua erabil dezakezu domeinu-izen bat konfiguratzeko, ondoren, ezarri `.env` fitxategian `DOMAIN` balioa, ngrok bidez sortutako domeinu-izena erabiliz.

- Konfiguratu nginx garapenerako, nginx konfigurazio-fitxategia (`nginx/development`) kopiatuz `nginx/default.conf` izeneko fitxategi berrian:
``` { .sh }
cp nginx/development nginx/default.conf
```

- Hasi aplikazioa. Komando-lerroan, exekutatu:
``` { .sh }
./bw-dev build            # Eraiki docker irudiak
./bw-dev setup            # Inizializatu datu-basea eta abiarazi migrazioak
./bw-dev up               # Hasi docker edukitzaileak
```
- Konpilazioa bukatuta, `http://localhost:1333` instantziara irits zaitezke eta admin erabiltzaile bat sor dezakezu.

If you're curious: the `./bw-dev` command is a simple shell script runs various other tools: above, you could skip it and run `docker-compose build` or `docker-compose up` directly if you like. `./bw-dev` just collects them into one common place for convenience. Run it without arguments to get a list of available commands, read the [documentation page](/command-line-tool.html) for it, or open it up and look around to see exactly what each command is doing!

### Editing or creating Models

If you change or create a model, you will probably change the database structure. For these changes to have effect you will need to run Django's `makemigrations` command to create a new [Django migrations file](https://docs.djangoproject.com/en/3.2/topics/migrations), and then `migrate` it:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

### Editing static files
Any time you edit the CSS or JavaScript, you will need to run Django's `collectstatic` command again in order for your changes to have effect:
``` { .sh }
./bw-dev collectstatic
```

If you have [installed yarn](https://yarnpkg.com/getting-started/install), you can run `yarn watch:static` to automatically run the previous script every time a change occurs in `bookwyrm/static` directory.
