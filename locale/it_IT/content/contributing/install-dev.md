- - -
Title: Developer Environment Date: 2025-05-26 Order: 5
- - -

## Prerequisiti

Queste istruzioni presuppongono che tu stia sviluppando BookWyrm usando Docker. Dovrai [installare Docker](https://docs.docker.com/engine/install/) e [docker-compose](https://docs.docker.com/compose/install/) per iniziare.

## Impostazioni dell'ambiente di sviluppo

### Ottieni il codice

1. Ottieni una copia del [codebase di BookWyrm da GitHub](https://github.com/bookwyrm-social/bookwyrm). Puoi [creare un fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) del repository, e poi [usare `git clone` per scaricare il codice](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) sul tuo computer.
2. Vai alla directory che contiene il codice sul tuo computer, lavorerai da qui d'ora in poi.
3. Development occurs on the `main` branch, so ensure that is the branch you have checked out: `git checkout main`
4. Imposta il file delle variabili di ambiente di sviluppo copiando il file di ambiente di esempio (`. nv.example`) in un nuovo file denominato `.env`. Nella riga di comando, puoi farlo con:
``` { .sh }
cp .env.example .env
```

### Configura le impostazioni del tuo ambiente

In `.env`:

4. Cambia `DEBUG` in `true`
5. Se usi un servizio di tunneling/proxy come [ngrok](https://ngrok.com), imposta `DOMAIN` sul nome di dominio che stai usando (ad esempio `abcd-1234.ngrok-free.app`). Altrimenti, imposta `DOMAIN` su `localhost`.
6. Cambia `NGINX_SETUP` in `reverse_proxy` (questo impedisce a BookWyrm di provare a configurare i certificati HTTPS sulla tua macchina di sviluppo)
7. Se devi usare una porta specifica (ad esempio se stai usando un tunnel con ngrok), decommenta `PORT` e impostala (ad esempio `PORT=1333`). Se usi `localhost`, questo è opzionale.

Check that you have [all the required settings configured](/environment.html#required-environment-settings) before proceeding.

If you try to register your admin account and see a message that `CSRF verification failed` you may have set your domain or port incorrectly.

### Email (opzionale)

If you want to test sending emails, you will need to [set up appropriate real values](/environment.html#email-configuration) in the "Email config" section. Non è necessario modificare nulla per [l’impostazione separata `EMAIL`](/environment.html#email).

### Compila ed esegui

8. Dalla riga di comando esegui:

``` { .sh }
./bw-dev build            # Compila le immagini Docker  
./bw-dev setup            # Inizializza il database ed esegui le migrazioni. Note the ADMIN key at the end of this output. Avrai bisogno di registrare il primo utente amministratore.
./bw-dev verso l'alto # Avviare i contenitori docker
```

9. Una volta completata la build, puoi accedere all'istanza su `http://localhost`, il tuo dominio ngrok, o `http://localhost:{PORT}`a seconda del dominio e della configurazione della porta.
10. Puoi inserire la admin key e creare l'utente admin. Da qui in poi la procedura è la stessa di quanto descritto in  descritto in "Eseguire BookWyrm".

Se sei curioso: il comando `./bw-dev` è un semplice script shell che esegue vari altri strumenti. Come visto sopra, puoi anche saltarlo ed eseguire direttamente `docker-compose build` o `docker-compose up`, se preferisci. `./bw-dev` si limita a raccoglierli tutti in un’unica posizione per comodità.

## Modifica o crea dei modelli

Se cambi o crei un modello, probabilmente dovrai cambiare la struttura del database. Affinché queste modifiche abbiano effetto, è necessario eseguire il comando `makemigrations` di Django per creare un nuovo [file di migrazione di Django](https://docs.djangoproject.com/en/3.2/topics/migrations), e poi `migrare`:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

## Modifica file statici
Ogni volta che modifichi il CSS o il JavaScript, dovrai eseguire nuovamente il comando `collectstatic` di Django affinché le modifiche abbiano effetto:
``` { .sh }
./bw-dev collectstatic
```

Se hai [installato yarn](https://yarnpkg.com/getting-started/install), puoi eseguire `yarn watch:static` per far partire automaticamente lo script precedente ogni volta che viene rilevata una modifica nella cartella `bookwyrm/static`.
