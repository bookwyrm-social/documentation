Acest proiect este încă tânăr și nu foarte stabil în acest moment, așa că vă rugăm să continuați cu precauție atunci când rulați în producție.

## Configurarea server-ului
- Obțineți un nume de domeniu și configurați DNS-ul pentru server-ul dvs. Veți avea nevoie să indicați numele server-ului furnizorului dvs. DNS pentru server-ul unde veți găzdui BookWyrm. Iată instrucțiunile pentru [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Configurați server-ul dvs. cu paravanele de protecție (firewalls) adecvate pentru rularea unei aplicații web (acest set de instrucțiuni a fost testat cu Ubuntu 20.04). Iată instrucțiunile pentru [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Configurați un serviciu email (precum [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) și setările adecvate SMTP/DNS. Folosiți documentația serviciului pentru configurarea DNS dvs.
- [Instalați Docker și docker-compose](https://docs.docker.com/compose/install/)

## Instalați și configurați BookWyrm

Ramura de `producție` BookWyrm conține un număr de unelte care nu sunt prezente pe ramura `main` și care sunt potrivite pentru rularea în producție, precum `docker-compose` care schimbă comenzile de bază sau configurarea containerelor și schimbări individuale pentru a activa lucruri precum SSL sau copii de rezervă regulate (regular backups).

Instrucțiuni pentru rularea BookWyrm în producție:

- Obțineți codul aplicației: `git clone git@github.com:bookwyrm-social/bookwyrm.git`
- Comutați la ramura de `production`: `git checkout production`
- Creați un fișier cu variabilele de mediu, `cp .env.example .env` și actualizați următoarele:
    - `SECRET_KEY` | Un șir de caractere secret, greu de ghicit
    - `DOMAIN` | Domeniul dvs. web
    - `EMAIL` | Adresa de email utilizată pentru verificarea de domeniu certbot
    - `POSTGRES_PASSWORD` | Setați o parolă sigură pentru baza de date
    - `REDIS_ACTIVITY_PASSWORD` | Setați o parolă sigură pentru subsistemul Redis Activity
    - `REDIS_BROKER_PASSWORD` | Setați o parolă sigură pentru „Redis queue broker subsystem”
    - `FLOWER_USER` | Setați propriul nume de utilizator pentru accesarea „Flower queue monitor”
    - `FLOWER_PASSWORD` | Setați propria parolă sigură pentru accesul la „Flower queue monitor”
    - `EMAIL_HOST_USER` | Adresa „de la” pe care aplicația dvs. o va folosi pentru trimiterea email-urilor
    - `EMAIL_HOST_PASSWORD` | Parola furnizată de serviciul dvs. email
- Configurare nginx
    - Faceți o copie a șablonului de configurare de producție și setați-l pentru a fi utilizat de nginx `cp nginx/production nginx/default.conf`
    - Actualizați `nginx/default.conf`:
        - Înlocuiți `your-domain.com` cu numele domeniului dvs. peste tot în fișier (inclusiv liniile care sunt momentan comentate)
        - Dacă nu folosiți subdomeniul `www`, înlăturați versiunea www.your-domain.com a domeniului din `server_name` în primul bloc al server-ului în `nginx/default.conf` și înlăturați opțiunea `-d www.${DOMAIN}` de la finalul comenzii `certbot` din `docker-compose.yml`.
        - Dacă rulați un alt server web pe calculatorul dvs. gazdă, veți avea nevoie să urmați [instrucțiunile pentru reverse-proxy](/using-a-reverse-proxy.html)
- Rulați aplicația prin `docker-compose up --build` (asta ar trebui să configureze de asemenea și un Certbot ssl cert pentru domeniul dvs.) și asigurați-vă că toate imaginile au fost compilate cu succes
    - Dacă rulați alte servicii pe calculatorul gazdă al dvs., s-ar putea să vă confruntați cu erori când serviciile eșuează încercând să se lege la un port. Vedeți [ghidul de depanare](#port_conflicts) pentru sfaturi despre rezolvarea acestor probleme.
- Când Docker s-a compilat cu succes, opriți procesul cu `CTRL-C`
- Configurați redirecționarea HTTPS
    - În `docker-compose.yml`, comentați comanda certbot activă, care instalează certificatul, și decomentați linia de mai jos, care configurează automat reînnoirea.
    - În `nginx/default.conf`, decomentați de la linia 18 până la 50 pentru a activa redirecționarea HTTPS. Ar trebui să aveți două blocuri `server` activate
- Configurați o sarcină (job) `cron` pentru a păstra certificatele dvs. actualizate (certificatele Lets Encrypt expiră după 90 de zile)
    - Tastați `crontab -e ` pentru a edita fișierul dvs. cron pe mașina gazdă
    - adăugați o linie pentru a încerca reînnoirea o dată pe zi: `5 0 * * * cd /path/to/your/bookwyrm && docker-compose run --rm certbot`
- Dacă doriți să folosiți un mediu de stocare externă pentru modelele statice și fișierele media (precum un serviciu S3 compatibil), [urmați instrucțiunile](/external-storage.html) până când vă spune să reveniți aici
- Configurați baza de date cu `./bw-dev setup` și copiați codul adminului pentru a îl folosi când vă creați contul dvs. de admin.
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
- `nginx/default.conf`
- `.env` (Dvs. creați acest fișier în timpul configurării)

Dacă rulați deja un server web pe mașina dvs., veți avea nevoie să configurați un reverse-proxy.

## Conectați-vă

Deoarece BookWyrm este un proiect tânăr, încă lucrăm la un program de lansare stabil, existând o mulțime de buguri și schimbări care strică totul. Avem o echipă GitHub care poate fi notificată când este ceva important de știut despre o actualizare, echipă căreia vă puteți alătura partajând numele dvs. GitHub. Există câteva moduri de a lua legătura:

 - Deschideți un tichet sau o cerere de extragere pentru a adăuga instanța dvs. la [lista oficială](https://github.com/bookwyrm-social/documentation/blob/main/content/using_bookwyrm/instances.md)
 - Contactați proiectul pe [Mastodon](https://tech.lgbt/@bookwyrm) sau prin [email-ul maintainer-ului](mailto:mousereeve@riseup.net) direct cu numele dvs. GitHub
 - Alăturați-vă salonului de discuție (chat room) [Matrix](https://matrix.to/#/#bookwyrm:matrix.org)
