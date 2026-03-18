- - -
Title: Developer Environment Date: 2026-02-22 Order: 5
- - -

## Prerequisiti

Queste istruzioni presuppongono che tu stia sviluppando BookWyrm usando Docker. Dovrai [installare Docker](https://docs.docker.com/engine/install/) e [docker-compose](https://docs.docker.com/compose/install/) per iniziare.

_If you are contributing to BookWyrm in a dockerless development environment we would love for you to [help us update this guide](/documentation.html) to include instructions for setting up a dockerless development environment_.

## Impostazioni dell'ambiente di sviluppo

### Ottieni il codice

1. Ottieni una copia del [codebase di BookWyrm da GitHub](https://github.com/bookwyrm-social/bookwyrm). Puoi [creare un fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) del repository, e poi [usare `git clone` per scaricare il codice](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) sul tuo computer.
2. Vai alla directory che contiene il codice sul tuo computer, lavorerai da qui d'ora in poi.
3. Development occurs on the `main` branch, so ensure that is the branch you have checked out: `git checkout main`
4. Imposta il file delle variabili di ambiente di sviluppo copiando il file di ambiente di esempio (`. nv.example`) in un nuovo file denominato `.env`. Nella riga di comando, puoi farlo con:

```{ .sh }
cp .env.example .env
```

### Compila ed esegui

1. Dalla riga di comando esegui:

```{ .sh }
./bw-dev create_secrets       # Create the secrets file with random values. You only need to do this once.
./bw-dev dev up --build       # Build and start development stack
./bw-dev rundev python manage.py admin_code       # Shows the admin-code for initial setup. You only need to do this once.
```

1. Once the build is complete, you can access the instance at `http://localhost:1333`.
2. Puoi inserire la admin key e creare l'utente admin. Da qui in poi la procedura è la stessa di quanto descritto in  descritto in "Eseguire BookWyrm".

Se sei curioso: il comando `./bw-dev` è un semplice script shell che esegue vari altri strumenti. Come visto sopra, puoi anche saltarlo ed eseguire direttamente `docker-compose build` o `docker-compose up`, se preferisci. `./bw-dev` si limita a raccoglierli tutti in un’unica posizione per comodità.

## Modifica o crea dei modelli

Se cambi o crei un modello, probabilmente dovrai cambiare la struttura del database. Affinché queste modifiche abbiano effetto, è necessario eseguire il comando `makemigrations` di Django per creare un nuovo [file di migrazione di Django](https://docs.djangoproject.com/en/3.2/topics/migrations), e poi `migrare`:

```{ .sh }
./bw-dev makemigrations
./bw-dev rundev python manage.py migrate
```

## Modifica file statici

Ogni volta che modifichi il CSS o il JavaScript, dovrai eseguire nuovamente il comando `collectstatic` di Django affinché le modifiche abbiano effetto:

```{ .sh }
./bw-dev rundev python manage.py collectstatic
```

Se hai [installato yarn](https://yarnpkg.com/getting-started/install), puoi eseguire `yarn watch:static` per far partire automaticamente lo script precedente ogni volta che viene rilevata una modifica nella cartella `bookwyrm/static`.

## Run code-linters and formatters

Before submitting patch, you should check ruff and other formatting tools. For those to work nicely, you should make sure you have development web-container and dev-tools build.

```{ .sh}
./bw-dev dev build # This is needed only once, if you haven't run dev stack previously
./bw-dev dev build dev-tools # This is needed only once and if you change pyproject.toml or Dockerfile
```

After those commands, you can run formatters and pytest and mypy with bw-dev command:

```{ .sh}
./bw-dev formatters
./bw-dev mypy
./bw-dev pytest
```

## Run development code behind ngrok or other tunneling/proxy service

In `.env.dev`:

1. Se usi un servizio di tunneling/proxy come [ngrok](https://ngrok.com), imposta `DOMAIN` sul nome di dominio che stai usando (ad esempio `abcd-1234.ngrok-free.app`).
2. If you need to use a particular port other than 1333, change PORT to wanted port (e.g. `PORT=1333`).

Check that you have [all the required settings configured](/environment.html#required-environment-settings) before proceeding.

If you try to register your admin account and see a message that `CSRF verification failed` you may have set your domain or port incorrectly.

## Email (opzionale)

If you want to test sending emails, you will need to [set up appropriate real values](/environment.html#email-configuration) in the "Email config" section. Non è necessario modificare nulla per [l’impostazione separata `EMAIL`](/environment.html#email). These settings are in `.env` -file
