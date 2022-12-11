- - -
Title: Command Line Tool Date: 2021-11-11 Order: 9
- - -

Dezvoltatorii BookWyrm și managerii de instanțe pot folosi scriptul `bw-dev` pentru sarcinile comune. Poate face comenzile dvs. mai scurte, mai ușor de reținut și mai greu de confundat.

Odată ce ați instalat BookWyrm [în producție](installing-in-production.html) sau [în dezvoltare](https://docs.joinbookwyrm.com/developer-environment.html#setting_up_the_developer_environment), puteți rula scriptul din linia de comandă cu `./bw-dev` urmat de o subcomandă pe care doriți să o rulați.

## Scurtături Docker

### bash

Deschide o sesiune interactivă de `bash` în interiorul containerului docker `web`.

### build

Echivalent cu `docker-compose build`.

### dbshell

Deschide un shell interactiv pentru baza de date Postgres. Sper că știți ceea ce faceți.

### runweb args

Rulează o comandă arbitrară (reprezentată deasupra de `args`) în containerul `web`.

Echivalent cu `docker-compose run --rm web`.

### service_ports_web args

Rulează o comandă arbitrară în containerul `web` (reprezentată deasupra de `args`) cu porturile expuse. Aceasta este utilă dacă vreți să rulați teste `pdb` deoarece `runweb` nu expune promptul `pdb`.

Echivalent cu `docker-compose run --rm --service-ports web`.

### shell

Deschide un shell interactiv Django în interiorul containerului docker `web`. O veți folosi dacă vreți să rulați comenzi de shell Django direct.

### up [args]

Pornește sau repornește containerele Dcoker, opțional incluzând orice argument(reprezentat mai sus de `args`). Echivalent cu `docker-compose up --build [args]`

## Gestionarea bazei de date

### initdb

Inițializează o bază de date.

### makemigrations [appname migration number]

_Această comandă nu este disponibilă în ramura de `producție`_.

Rulează comanda Django `makemigrations` în interiorul containerului dvs. Docker. Dacă ați schimbat structura bazei de date în ramura de dezvoltare veți avea nevoie să o rulați pentru ca schimbările dvs. să aibă efect. Opțional, puteți specifica o migrație specifică pe care să o rulați, de ex. `./bw-dev makemigrations bookwyrm 0108`

### migrate

Rulează comanda Django `migrate` în interiorul containerului dvs. Docker. Veți avea nevoie mereu de a o rula după `makemigrations`.

### resetdb

_Această comandă nu este disponibilă în ramura de `producție`_.

Resetează baza de date. **Această comandă va șterge întreaga bază de date BookWyrm**, iar apoi va iniția o bază de date nouă și rula toate migrațiile. Va trebui să ștergeți orice fișier de migrație recent pe care nu vreți să-l rulați _înainte_ de a rula `resetdb`.

## Gestionarea unei instanțe BookWyrm

### collectstatic

Migrează modulele statice fie către un container web, fie către un „bucket” S3 compatibil, depinzând de context.

### generate_preview_images

Generează imagini de previzualizare pentru site, utilizatori și cărți. Acest lucru poate dura ceva timp dacă aveți o bază de date mare.

### generate_thumbnails

Generează miniaturi pentru coperțile cărților.

### populate_streams args

Repopulează fluxurile Redis (fluxurile utilizatorilor). De obicei nu veți avea nevoie să o rulați numai dacă o eroare șterge toate fluxurile de utilizator ale dvs. pentru un motiv sau altul. Puteți specifica fluxul folosind argumentul `--stream`.

### populate_list_streams

Repopulează cache-ul Redis de liste. De obicei nu veți avea nevoie să o rulați numai dacă o eroare șterge toate listele de utilizator ale dvs. dintr-un motiv sau altul.

### populate_suggestions

Populează utilizatorii sugerați pentru toți utilizatorii. S-ar putea să doriți să o rulați manual pentru a reîmprospăta sugestiile.

### restart_celery

Repornește containerul Docker `celery_worker`.

### update

Când există schimbări pentru ramura de `producție`, puteți actualiza instanța dvs. fără timp de oprire.

Această comandă extrage cele mai recente actualizări ale ramurii de `producție` prin `git pull`, construiește imaginile docker dacă este necesar, rulează migrările Django, actualizează fișierele statice și repornește toate containerele Docker.

### admid_code

Obține codul secret de admin folosit pentru a înscrie utilizatorul admin inițial pe o instanță BookWyrm nouă.

## Configurați stocare S3 compatibilă

În mod implicit, BookWyrm folosește stocarea locală pentru modelele statice (favicon, avatarul de bază etc.) și media (avatarurile utilizatorilor, coperțile cărților etc.), dar puteți folosi un serviciu de stocare extern pentru a deservi aceste fișiere. BookWyrm folosește stocare Django pentru a manipula stocarea externă, precum servicii S3 compatibile, Apache Libcloud sau SFTP.

Vedeți [Stocare externă](/external-storage.html) pentru mai multe detalii.

### copy_media_to_s3

Migrează toate fișierele media încărcate de pe o instalație BookWyrm către un serviciu „bucket” S3 compatibil. Utilizați pentru o încărcare inițială către un „bucket” gol.

### sync_media_to_s3

Sincronizează fișiere media noi sau schimbate de pe o instalație BookWyrm către un „bucket” S3 compatibil. Folosiți pentru a asigura că toate fișierele locale sunt încărcate către un „bucket” existent.

### set_cors_to_s3 filename

Copiază un fișier JSON cu reguli CORS către „găleata” dvs. S3, unde `filename` este numele fișierului dvs. JSON (de ex. `./bw-dev set_cors_to_s3 cors.json`)

## Dezvoltare și testare

_Aceste comenzi nu sunt disponibile în ramura de `producție`_.

### black

BookWyrm folosește formatorul de cod [Black](https://github.com/psf/black) pentru a menține stilul codului consistent. Rulați `black` înainte de a trimite schimbările dvs. pentru ca sarcina `pylint` să nu eșueze pentru cererea dvs. de extracție și să vă facă trist.

### prettier

BookWyrm folosește [Prettier](https://prettier.io/) pentru a păstra stilul codului JavaScript consistent. Executați `prettier` înainte de a trimite schimbările dvs. scripturilor pentru a formata automat codul dvs.

### stylelint

BookWyrm folosește [Stylelint](uhttps://stylelint.io/) pentru a păstra stilul fișierelor CSS consistent. Executați `stylelintprettier` înainte de a trimite schimbările scripturilor pentru a formata automat codul dvs.

### formatters

Această comandă rulează toate formatoarele (`black`, `prettier` și `stylelint`) într-o singură etapă.

### clean

Elimină toate containerele Docker oprite.

Echivalent cu:

```shell
docker-compose stop
docker-compose rm -f
```

### makemessages

Creează fișiere mesaj pentru toate șirurile de caractere de tradus. După ce ați rulat `makemessages` trebuie să rulați `compilemessages` pentru a compila traducerile. Vedeți [makemessages Django](https://docs.djangoproject.com/en/3.2/ref/django-admin/#makemessages).

### compilemessages

Compilează fișierele de traducere. Vedeți [compilemessages Django](https://docs.djangoproject.com/en/3.2/ref/django-admin/#compilemessages).

### pytest args

Rulează testele cu `pytest`.

### deactivate_2fa

Deactivates two factor authentication for a given user.

### manual_confirm

Confirms a users email, sets the user to active.
