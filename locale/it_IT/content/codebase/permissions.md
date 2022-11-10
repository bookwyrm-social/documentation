- - -
Titolo: Permessi Data: 18-04-2021 Ordine: 2
- - -

L'accesso dell'utente a diverse funzioni è controllato tramite il sistema di autenticazione integrato [di Django](https://docs.djangoproject.com/en/3.2/topics/auth/default/). Quando viene creata un'istanza, lo script `initdb` crea un insieme di permessi, che vengono assegnati ai gruppi. Per impostazione predefinita, a tutti i nuovi utenti viene assegnato il gruppo `editor`, che consente loro di modificare i metadati del libro.

L'amministratore dell'istanza dovrebbe avere lo stato `superuser`, che gli consente l0accesso a Django admin (`/admin`) e conferisce tutte le autorizzazioni al suo utente.

## Permessi e gruppi
Questa tabella mostra i quattro gruppi (admin, moderatore, editor e utente) e quali permessi gli utenti di quel gruppo hanno:

|                                 | admin | moderatore | editor | utente |
| ------------------------------- | ----- | ---------- | ------ | ------ |
| modifica impostazioni istanza   | ✔️    | -          | -      | -      |
| modifica il livello dell'utente | ✔️    | -          | -      | -      |
| gestire la federazione          | ✔️    | ✔️         | -      | -      |
| invito a correggere errori      | ✔️    | ✔️         | -      | -      |
| disattiva utenti                | ✔️    | ✔️         | -      | -      |
| cancella post                   | ✔️    | ✔️         | -      | -      |
| modifica libri                  | ✔️    | ✔️         | ✔️     | -      |
 carica le copertine           |  ✔️    |     ✔️       |   ✔️     |  ✔️
