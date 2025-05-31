- - -
Izenburua: Garapen ingurumena Eguna: 2021-04-12 Ordena: 3
- - -

## Aurrebaldintzak

Jarraibide hauen arabera, BookWyrm ari zara garatzen Docker erabiliz. Ezer baino lehenago instalatu behar dituzu [Docker](https://docs.docker.com/engine/install/) eta [docker-compose](https://docs.docker.com/compose/install/).

## Garapen ingurunearen konfigurazioa

- Eskura ezazu [GitHub-etik BookWyrm-en kode-basea](https://github.com/bookwyrm-social/bookwyrm). Paketearen [fork bat sortu](https://docs.github.com/en/get-started/quickstart/fork-a-repo) dezakezu, ondotik [erabili `git clone` kodea deskargatzeko](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) zure ordenagailuan.
- Joan zure ordenagailuko kodea duen direktoriora, orain direktorio honetatik lan egingo duzu.
- Konfigura ezazu zure garapen-inguruneko aldagaien artxiboa, inguruneko adibide-fitxategia (`.env.example`) `.env` izeneko fitxategi berri batean kopiatuz. Komando-lerroan, hori egin dezakezu idatziz:
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

Kuriosa bazara: `./bw-dev` komandoa shell skript soil bat da eta beste hainbat tresna exekutatzen ditu: aurreko komandoen ordez, zuk `docker-compose build` edo `docker-compose up` exekutatzen ahal zenuen zuzenean, nahi izanez gero. `./bw-dev` komandoak leku bakar batean biltzen ditu erosotasun gehiagorako. Exekutatu komando hori argumenturik gabe eskura dauden komandoen zerrenda lortzeko, irakurri dagokion [dokumentazio orrialdea](/command-line-tool.html) edo ireki fitxategia eta berrikusi zehatz-mehatz komando bakoitzak egiten duena!

### Ereduak editatzea edo sortzea

Eredu bat aldatzen edo sortzen baduzu, seguruenik datu-basearen egitura aldatuko duzu. Aldaketa horiek eragina izan dezaten, Djangoko `makemigrations` komandoa exekutatu beharko duzu [Django migrations file](https://docs.djangoproject.com/en/3.2/topics/migrations) berri bat sortzeko, eta, ondoren, `migrate` komandoa, azken hau migratzeko:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

### Fitxategi estatikoak editatzea
CSS edo JavaScript kodea editatzen duzun bakoitzean, berriro exekutatu beharko duzu `collectstatic` komandoa, zure aldaketek eragina izan dezaten:
``` { .sh }
./bw-dev collectstatic
```

[yarn instalatuta](https://yarnpkg.com/getting-started/install) baduzu, exekuta dezakezu `yarn watch:static`, `bookwyrm/static` errepertorioan aldaketa bat gertatzen den bakoitzean aurreko scripta automatikoki exekutatzeko.
