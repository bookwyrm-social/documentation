- - -
Title: Developer Environment Date: 2021-04-12 Order: 3
- - -

## Cerințe preliminare

Aceste instrucțiuni presupun că dezvoltați BookWyrm folosind Docker. Va trebui să [instalați Docker](https://docs.docker.com/engine/install/) și [docker-compose](https://docs.docker.com/compose/install/) pentru a începe.

## Configurați mediul de dezvoltare

- Obțineți o copie a [bazei de cod BookWyrm de pe GitHub](https://github.com/bookwyrm-social/bookwyrm). Puteți [crea un fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) al depozitului și apoi [folosi `git clone` pentru a descărca codul](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) pe calculatorul dumneavoastră.
- Mergeți în dosarul care conține codul pe calculatorul dvs, veți lucra aici de aici în colo.
- Configurați fișierul de variabile de mediu al dvs. copiind fișierul de mediu exemplu (`.env.example`) într-un nou fișier numit `.env`. În linia de comandă, puteți face asta cu:
``` { .sh }
cp .env.example .env
```
- În `.env`, schimbați `DEBUG` în `true`
- Opțional, puteți folosi un serviciu precum [ngrok](https://ngrok.com/) pentru a configura un nume de domeniu și seta variabila `DOMAIN` în fișierul dumneavoastră `.env` în numele de domeniu generat de ngrok.

- Configurați nginx pentru dezvoltare prin copierea fișierului de configurație nginx (`nginx/development`) într-un nou fișier numit `nginx/default.conf`:
``` { .sh }
cp nginx/development nginx/default.conf
```

- Porniți aplicația. În linia de comandă, rulați:
``` { .sh }
./bw-dev build            # Build the docker images
./bw-dev setup            # Initialize the database and run migrations
./bw-dev up               # Start the docker containers
```
- Odată compilarea terminată, puteți accesa instanța la `http://localhost:1333` și crea un utilizator administrator.

Dacă sunteți curios: comanda `./bw-dev` este un simplu script shell care rulează multe alte comenzi: deasupra, ați putea sări peste ea și rula `docker-compose build` sau `docker-compose up` direct dacă doriți. `./bw-dev` doar le colectează într-un singur loc pentru conveniență. Rulați-o fără argumente pentru a obține o listă a comenzilor disponibile, citiți [pagina de documentație](/command-line-tool.html) pentru ea sau deschideți-o pentru a vedea ce face fiecare comandă!

### Editați sau configurați modele

Dacă schimbați sau creați un model, veți schimba probabil structura bazei de date. Pentru ca aceste schimbă să aibă efect va trebui să rulați comanda Django `makemigrations` pentru a crea un nou [fișier de migrare Django](https://docs.djangoproject.com/en/3.2/topics/migrations) și apoi `migrate`:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

### Editați fișiere statice
De fiecare dată când editați CSS sau JavaScript, va trebui să rulați comanda Django `collectstatic` pentru ca schimbările dvs. să aibă efect:
``` { .sh }
./bw-dev collectstatic
```

Dacă aveți [yarn instalat](https://yarnpkg.com/getting-started/install), puteți rula `yarn watch:static` pentru a rula automat scriptul precedent de fiecare dată când o schimbare are loc în dosarul `bookwyrm/static`.
