- - -
Title: Installing in Production Date: 2021-05-18 Order: 1
- - -

This project is still young and isn't, at the moment, very stable, so please proceed with caution when running in production.

## Configurarea server-ului
- Obțineți un nume de domeniu și configurați DNS-ul pentru server-ul dvs. Veți avea nevoie să indicați numele server-ului furnizorului dvs. DNS pentru server-ul unde veți găzdui BookWyrm. Iată instrucțiunile pentru [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Configurați server-ul dvs. cu paravanele de protecție (firewalls) adecvate pentru rularea unei aplicații web (acest set de instrucțiuni a fost testat cu Ubuntu 20.04). Iată instrucțiunile pentru [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Configurați un serviciu email (precum [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) și setările adecvate SMTP/DNS. Folosiți documentația serviciului pentru configurarea DNS dvs.
- [Instalați Docker și docker-compose](https://docs.docker.com/compose/install/)

## Instalați și configurați BookWyrm

The `production` branch of BookWyrm contains a number of tools not on the `main` branch that are suited for running in production, such as `docker-compose` changes to update the default commands or configuration of containers, and individual changes to container config to enable things like SSL or regular backups.

Instructions for running BookWyrm in production:

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
- Inițializați baza de date rulând `./bw-dev migrate`
- Rulați aplicația cu `docker-compose up --build` (acest lucru ar trebui să configureze de asemenea un Certbot ssl cert pentru domeniul dvs.) și asigurați-vă că toate imaginile au fost compilate cu succes
    - Dacă rulați alte servicii pe calculatorul gazdă al dvs., s-ar putea să vă confruntați cu erori când serviciile eșuează încercând să se lege la un port. Vedeți [ghidul de depanare](#port_conflicts) pentru sfaturi despre rezolvarea acestor probleme.
- Când Docker s-a compilat cu succes, opriți procesul cu `CTRL-C`
- Configurați redirecționarea HTTPS
    - În `docker-compose.yml`, comentați comanda certbot activă, care instalează certificatul, și decomentați linia de mai jos, care configurează automat reînnoirea.
    - În `nginx/default.conf`, decomentați de la linia 18 până la 50 pentru a activa redirecționarea HTTPS. Ar trebui să aveți două blocuri `server` activate
- Configurați o sarcină (job) `cron` pentru a păstra certificatele dvs. actualizate (certificatele Lets Encrypt expiră după 90 de zile)
    - Tastați `crontab -e ` pentru a edita fișierul dvs. cron pe mașina gazdă
    - adăugați o linie pentru a încerca reînnoirea o dată pe zi: `5 0 * * * cd /path/to/your/bookwyrm && docker-compose run --rm certbot`
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

Congrats! You did it!! Configure your instance however you'd like.


## Copii de rezervă

BookWyrm's db service dumps a backup copy of its database to its `/backups` directory daily at midnight UTC. Backups are named `backup__%Y-%m-%d.sql`.

The db service has an optional script for periodically pruning the backups directory so that all recent daily backups are kept, but for older backups, only weekly or monthly backups are kept. To enable this script:

- Decomentați linia finală în `postgres-docker/cronfile`
- recompilați instanța dvs. `docker-compose up --build`

You can copy backups from the backups volume to your host machine with `docker cp`:

- Rulați `docker-compose ps` pentru a confirma numele întreg al serviciul db (probabil `bookwyrm_db_1`).
- Rulați `docker cp <container_name>:/backups <host machine path>`

## Conflicte la porturi

BookWyrm has multiple services that run on their default ports. This means that, depending on what else you are running on your host machine, you may run into errors when building or running BookWyrm when attempts to bind to those ports fail.

If this occurs, you will need to change your configuration to run services on different ports. This may require one or more changes the following files:

- `docker-compose.yml`
- `nginx/default.conf`
- `.env` (Dvs. creați acest fișier în timpul configurării)

If you are already running a web-server on your machine, you will need to set up a reverse-proxy.

## Conectați-vă

Because BookWyrm is a young project, we're still working towards a stable release schedule, and there are a lot of bugs and breaking changes. There is a GitHub team which can be tagged when there's something important to know about an update, which you can join by sharing your GitHub username. There are a few ways in get in touch:

 - Deschideți un tichet sau o cerere de extragere pentru a adăuga instanța dvs. la [lista oficială](https://github.com/bookwyrm-social/documentation/blob/main/content/using_bookwyrm/instances.md)
 - Contactați proiectul pe [Mastodon](https://tech.lgbt/@bookwyrm) sau prin [email-ul maintainer-ului](mailto:mousereeve@riseup.net) direct cu numele dvs. GitHub
 - Alăturați-vă salonului de discuție (chat room) [Matrix](https://matrix.to/#/#bookwyrm:matrix.org)
