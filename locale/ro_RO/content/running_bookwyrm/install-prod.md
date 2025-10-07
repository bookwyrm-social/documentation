- - -
Title: Installing in Production Date: 2025-04-01 Order: 1
- - -

Acest proiect este încă tânăr și nu foarte stabil în acest moment, așa că vă rugăm să continuați cu precauție atunci când rulați în producție.

## Configurarea server-ului
- Obțineți un nume de domeniu și configurați DNS-ul pentru server-ul dvs. Veți avea nevoie să indicați numele server-ului furnizorului dvs. DNS pentru server-ul unde veți găzdui BookWyrm. Iată instrucțiunile pentru [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Configurați server-ul dvs. cu paravanele de protecție (firewalls) adecvate pentru rularea unei aplicații web (acest set de instrucțiuni a fost testat cu Ubuntu 20.04). Iată instrucțiunile pentru [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Configurați un serviciu email (precum [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) și setările adecvate SMTP/DNS. Folosiți documentația serviciului pentru configurarea DNS dvs.
- [Instalați Docker și docker-compose](https://docs.docker.com/compose/install/)

## Instalați și configurați BookWyrm

There are several repos in the BookWyrm org, including documentation, a static landing page, and the actual Bookwyrm code. To run BookWyrm, you want the actual app code which is in [bookwyrm-social/bookwyrm](https://github.com/bookwyrm-social/bookwyrm).

Ramura de `producție` BookWyrm conține un număr de unelte care nu sunt prezente pe ramura `main` și care sunt potrivite pentru rularea în producție, precum `docker-compose` care schimbă comenzile de bază sau configurarea containerelor și schimbări individuale pentru a activa lucruri precum SSL sau copii de rezervă regulate (regular backups).

Instrucțiuni pentru rularea BookWyrm în producție:

- Obțineți codul aplicației: `git clone git@github.com:bookwyrm-social/bookwyrm.git`
- Comutați la ramura de `production`: `git checkout production`
- Creați un fișier cu variabilele de mediu, `cp .env.example .env` și actualizați următoarele:
    - `DOMAIN` | Domeniul dvs. web
    - `EMAIL` | Adresa de email utilizată pentru verificarea de domeniu certbot
    - `FLOWER_USER` | Setați propriul nume de utilizator pentru accesarea „Flower queue monitor”
    - `EMAIL_HOST_USER` | Adresa „de la” pe care aplicația dvs. o va folosi pentru trimiterea email-urilor
    - `EMAIL_HOST_PASSWORD` | Parola furnizată de serviciul dvs. email
- Initialize secrets by running `./bw-dev create_secrets` or manually update following in `.env`:
    - `SECRET_KEY` | Un șir de caractere secret, greu de ghicit
    - `POSTGRES_PASSWORD` | Setați o parolă sigură pentru baza de date
    - `REDIS_ACTIVITY_PASSWORD` | Setați o parolă sigură pentru subsistemul Redis Activity
    - `REDIS_BROKER_PASSWORD` | Setați o parolă sigură pentru „Redis queue broker subsystem”
    - `FLOWER_PASSWORD` | Setați propria parolă sigură pentru accesul la „Flower queue monitor”
    - If you are running another web-server on your host machine, you will need to follow the [reverse-proxy instructions](/reverse-proxy.html)
- Check that you have [all the required settings configured](/environment.html#required-environment-settings) before proceeding further
- Setup ssl certificate via letsencrypt by running `./bw-dev init_ssl`
- Inițializați baza de date rulând `./bw-dev migrate`
- Run the application with `docker-compose up --build`, and make sure all the images build successfully
    - Dacă rulați alte servicii pe calculatorul gazdă al dvs., s-ar putea să vă confruntați cu erori când serviciile eșuează încercând să se lege la un port. Vedeți [ghidul de depanare](#port_conflicts) pentru sfaturi despre rezolvarea acestor probleme.
- Când Docker s-a compilat cu succes, opriți procesul cu `CTRL-C`
- Dacă doriți să folosiți un mediu de stocare externă pentru modelele statice și fișierele media (precum un serviciu S3 compatibil), [urmați instrucțiunile](/external-storage.html) până când vă spune să reveniți aici
- Inițializați aplicația cu `./bw-dev setup` și copiați codul adminului pentru a îl folosi când vă creați contul dvs. de admin.
    - Afișajul `./bw-dev setup` ar trebui să se termine cu codul dvs. de admin. Puteți obține codul dvs. oricând rulând `./bw-dev admin_code` din linia de comandă. Iată un exemplu de afișaj:

``` { .sh }
*******************************************
Use this code to create your admin account:
c6c35779-af3a-4091-b330-c026610920d6
*******************************************
```

- Rulați docker-compose în fundal cu: `docker-compose up -d`
- Aplicația ar trebui să ruleze la domeniul dvs. Când încărcați domeniul, ar trebui să obțineți o pagină de configurare ce confirmă setările instanței dvs. și un formular pentru crearea unui cont de admin. Folosiți codul dvs. de admin pentru înregistrare.

Felicitări! Ați reușit! Configurați instanța dvs. oricum doriți.


## Copii de rezervă

Serviciul db al BookWyrm creează o copie de rezervă în dosarul său `/backups` în fiecare zi la miezul nopții UTC. Copiile de rezervă sunt numite `backup__%Y-%m-%d.sql`.

Serviciul db are un script opțional ce șterge periodic dosarul cu copii de rezervă în așa fel încât toate copiile recente sunt păstrate, dar în cazul celor mai vechi, doar cele săptămânale sau lunare sunt păstrate. Pentru a activa acest script:

- Decomentați linia finală în `postgres-docker/cronfile`
- recompilați instanța dvs. `docker-compose up --build`

Puteți copia copii de rezervă din volumul cu copii de rezervă către mașina dvs. gazdă cu `docker cp`:

- Rulați `docker-compose ps` pentru a confirma numele întreg al serviciul db (probabil `bookwyrm_db_1`).
- Rulați `docker cp <container_name>:/backups <host machine path>`

## Conflicte la porturi

BookWyrm are multiple servicii care rulează pe porturile lor implicite. Asta înseamnă că, depinzând de ce altceva rulați pe mașina dvs. gazdă, s-ar putea să vă confruntați cu erori la compilarea sau rularea BookWyrm când conectarea la aceste porturi eșuează.

Dacă se întâmplă acest lucru, veți avea nevoie să schimbați fișierul dvs. de configurare pentru a rula serviciile pe porturi diferite. Acest lucru poate necesita una sau multe schimbări ale următoarelor fișiere:

- `docker-compose.yml`
- `nginx/production.conf` or `nginx/reverse_proxy.conf` depending on NGINX_SETUP in .env-file
- `.env` (Dvs. creați acest fișier în timpul configurării)

Dacă rulați deja un server web pe mașina dvs., veți avea nevoie să configurați un reverse-proxy.

## Conectați-vă

Deoarece BookWyrm este un proiect tânăr, încă lucrăm la un program de lansare stabil, existând o mulțime de buguri și schimbări care strică totul. Avem o echipă GitHub care poate fi notificată când este ceva important de știut despre o actualizare, echipă căreia vă puteți alătura partajând numele dvs. GitHub. Există câteva moduri de a lua legătura:

 - Open an issue or pull request to add your instance to the [official list](https://joinbookwyrm.com/instances/)
 - Contactați proiectul pe [Mastodon](https://tech.lgbt/@bookwyrm) sau prin [email-ul maintainer-ului](mailto:mousereeve@riseup.net) direct cu numele dvs. GitHub
 - Alăturați-vă salonului de discuție (chat room) [Matrix](https://matrix.to/#/#bookwyrm:matrix.org)
