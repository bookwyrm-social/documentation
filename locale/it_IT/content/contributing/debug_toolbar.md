- - -
Titolo: Django Debug Toolbar Data: 2022-05-16 Ordine: 5
- - -

BookWyrm ha un ramo che è configurato per avviare [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/). Questo ramo non verrà mai unito in `main` e ha alcune modifiche che lo fanno funzionare con la barra degli strumenti, ma pericoloso da usare in qualsiasi cosa assomigli a un ambiente di produzione. Per utilizzare questo ramo, è necessario passare attraverso alcuni passaggi per farlo funzionare.

## Configura

- Utilizzando git, controlla il ramo [`debug-toolbar`](https://github.com/bookwyrm-social/bookwyrm/tree/debug-toolbar)
- Aggiorna il ramo relativo a `main` usando `git merge main`. Il ramo viene aggiornato periodicamente, ma probabilmente sarà più tardi.
- Ricostruisci le immagini Docker usando `docker-compose up --build` per assicurarsi che la libreria della barra degli strumenti di Debug sia installata da `requirements.txt`
- Accedi direttamente all'immagine `web` dell'applicazione (invece che tramite `nginx`) utilizzando la porta `8000`
