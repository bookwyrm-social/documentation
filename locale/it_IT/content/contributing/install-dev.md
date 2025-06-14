- - -
Title: Developer Environment Date: 2025-05-26 Order: 5
- - -

## Prerequisiti

Queste istruzioni presuppongono che tu stia sviluppando BookWyrm usando Docker. Dovrai [installare Docker](https://docs.docker.com/engine/install/) e [docker-compose](https://docs.docker.com/compose/install/) per iniziare.

## Impostazioni dell'ambiente di sviluppo

### Get the code

1. Ottieni una copia del [codebase di BookWyrm da GitHub](https://github.com/bookwyrm-social/bookwyrm). Puoi [creare un fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) del repository, e poi [usare `git clone` per scaricare il codice](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) sul tuo computer.
2. Vai alla directory che contiene il codice sul tuo computer, lavorerai da qui d'ora in poi.
3. Imposta il file delle variabili di ambiente di sviluppo copiando il file di ambiente di esempio (`. nv.example`) in un nuovo file denominato `.env`. Nella riga di comando, puoi farlo con:
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

8. Dalla riga di comando esegui:

``` { .sh }
./bw-dev build            # Build the docker images
./bw-dev setup            # Initialize the database and run migrations. Note the ADMIN key at the end of this output. You'll need it to register the first admin user.
./bw-dev up               # Start the docker containers
```

9. Once the build is complete, you can access the instance at `http://localhost`, your ngrok domain, or `http://localhost:{PORT}`, depending on you domain and port configuration.
10. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

Se sei curioso: il comando `./bw-dev` è un semplice script di shell esegue vari altri strumenti: puoi comunque eseguire `docker-compose build` o `docker-compose` direttamente se preferisci. `./bw-dev` li raccoglie in un unico posto comune per comodità. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Modifica o crea dei modelli

Se cambi o crei un modello, probabilmente dovrai cambiare la struttura del database. Affinché queste modifiche abbiano effetto, è necessario eseguire il comando `makemigrations` di Django per creare un nuovo [file di migrazione di Django](https://docs.djangoproject.com/en/3.2/topics/migrations), e poi `migrare`:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

## Modifica file statici
Ogni volta che modifichi il CSS o JavaScript, è necessario eseguire nuovamente il comando `collectstatic` di Django affinché le modifiche abbiano effetto:
``` { .sh }
./bw-dev collectstatic
```

Se hai [installato yarn](https://yarnpkg.com/getting-started/install), è possibile eseguire `yarn watch:static` per eseguire automaticamente lo script precedente ogni volta che si verifica un cambiamento nella directory `bookwyrm/static`.
