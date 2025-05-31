- - -
Títol: Entorn de desenvolupament Data: 2021-04-12 Ordre: 3
- - -

## Requisits previs

Aquestes instruccions assumeixen que estàs desenvolupant BookWyrm mitjançant Docker. Necessitaràs [instal·lar Docker](https://docs.docker.com/engine/install/) i [docker-compose](https://docs.docker.com/compose/install/) per començar.

## Configuració de l'entorn de desenvolupament

- Aconsegueix una còpia del [codi base de BookWyrm a GitHub](https://github.com/bookwyrm-social/bookwyrm). Pots [crear una derivació](https://docs.github.com/en/get-started/quickstart/fork-a-repo) del repositori i, llavors [utilitzar `git clone` per descarregar el codi](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) a l'ordinador.
- Ves al directori que conté el codi al teu ordinador, treballaràs des d'aquí d'ara en endavant.
- Configura el teu fitxer de variables d'entorn de desenvolupament copiant el fitxer d'entorn d'exemple (`.env.example`) a un nou fitxer anomenat `.env`. A la línia de comandes, pots fer-ho mitjançant:
``` { .sh }
cp .env.example .env
```
- A `.env`, modifica `DEBUG` a `true`
- Opcionalment, pots utilitzar un servei com [ngrok](https://ngrok.com/) per configurar el nom de domini i, establir la variable `DOMAIN` al teu fitxer `.env` al nom de domini generat per ngrok.

- Configura nginx per desenvolupament copiant el fitxer de configuració de nginx desenvolupador (`nginx/development`) a un nou fitxer de nom `nginx/default.conf`:
``` { .sh }
cp nginx/development nginx/default.conf
```

- Inicia l'aplicació. A la línia de comandes, executa:
``` { .sh }
./bw-dev build            # Crea les imatges docker
./bw-dev setup            # Inicialitza la base de dades i executa migracions
./bw-dev up               # Inicia els contenidors del docker
```
- Un cop la creació s'ha completat, pots accedir a la instància a través de `http://localhost:1333` i crear un usuari administrador.

Si ets curiós: el comandament `./bw-dev` és un senzill script que fa funcionar unes altres eines: a sobre, pots ometre o iniciar directament `docker-composer build` o `docker-composer up` si vols. `./bw-dev` els recull tots a un lloc comú per comoditat. Sense arguments torna una llista dels comandaments disponibles, llegeix la [documentation page](/command-line-tool.html) per veure'ls, o obre-la i mira per a veure que és el que fa exactament cada comandament!

### Editant o creant Models

Si modifiqueu o creeu un model, és probable que canvieu l'estructura de la base de dades. A fi que aquests canvis siguin efectius, haureu d'executar l'ordre `makemigrations` de Django per a crear un [fitxer de migració de Django](https://docs.djangoproject.com/en/3.2/topics/migrations) nou, i després `migrar-lo`:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

### Editant fitxers estàtics
Sempre que editeu el CSS o el JavaScript, haureu de tornar a executar l'ordre `collectstatic` a fi que els canvis tinguin efecte:
``` { .sh }
./bw-dev collectstatic
```

Si heu [instal·lat el Yarn](https://yarnpkg.com/getting-started/install), podeu executar `yarn watch:static` a fi que s'executi de forma automàtica l'script anterior cada cop que hi hagi un canvi al directori `bookwyrm/static`.
