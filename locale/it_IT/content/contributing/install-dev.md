- - -
Titolo: Ambiente di sviluppo Data: 12-04-2021 Ordine: 3
- - -

## Prerequisiti

Queste istruzioni presuppongono che tu stia sviluppando BookWyrm usando Docker. Dovrai [installare Docker](https://docs.docker.com/engine/install/) e [docker-compose](https://docs.docker.com/compose/install/) per iniziare.

## Impostazioni dell'ambiente di sviluppo

- Ottieni una copia del [codebase di BookWyrm da GitHub](https://github.com/bookwyrm-social/bookwyrm). Puoi [creare un fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) del repository, e poi [usare `git clone` per scaricare il codice](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) sul tuo computer.
- Vai alla directory che contiene il codice sul tuo computer, lavorerai da qui d'ora in poi.
- Imposta il file delle variabili di ambiente di sviluppo copiando il file di ambiente di esempio (`. nv.example`) in un nuovo file denominato `.env`. Nella riga di comando, puoi farlo con:
``` { .sh }
cp .env.example .env
```
- In `.env`, cambia `DEBUG` in `true`
- Facoltativamente, puoi usare un servizio come [ngrok](https://ngrok.com/) per impostare un nome di dominio, e impostare la variabile `DOMAIN` nel tuo file`.env` al nome del dominio generato da ngrok.

- Imposta nginx per lo sviluppo copiando il file di configurazione dello sviluppatore nginx (`nginx/development`) in un nuovo file chiamato `nginx/default. onf`:
``` { .sh }
cp nginx/development nginx/default.conf
```

- Avvia l'applicazione. Dalla riga di comando esegui:
``` { .sh }
./bw-dev build        # Costrusce le immagini docker
./bw-dev setup.      # Inizializza il database ed esegue le migrazioni
./bw-dev up # Avvia i contenitori docker
```
- Una volta completato il build, puoi accedere all'istanza su `http://localhost:1333` e creare un utente amministratore.

Se sei curioso: il comando `./bw-dev` è un semplice script di shell esegue vari altri strumenti: puoi comunque eseguire `docker-compose build` o `docker-compose` direttamente se preferisci. `./bw-dev` li raccoglie in un unico posto comune per comodità. Eseguilo senza argomenti per ottenere un elenco dei comandi disponibili, leggi la [pagina di documentazione](/command-line-tool.html) o aprilo e guardati intorno per vedere esattamente cosa fa ogni comando!

### Modifica o crea dei modelli

Se cambi o crei un modello, probabilmente dovrai cambiare la struttura del database. Affinché queste modifiche abbiano effetto, è necessario eseguire il comando `makemigrations` di Django per creare un nuovo [file di migrazione di Django](https://docs.djangoproject.com/en/3.2/topics/migrations), e poi `migrare`:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

### Modifica file statici
Ogni volta che modifichi il CSS o JavaScript, è necessario eseguire nuovamente il comando `collectstatic` di Django affinché le modifiche abbiano effetto:
``` { .sh }
./bw-dev collectstatic
```

Se hai [installato yarn](https://yarnpkg.com/getting-started/install), è possibile eseguire `yarn watch:static` per eseguire automaticamente lo script precedente ogni volta che si verifica un cambiamento nella directory `bookwyrm/static`.
