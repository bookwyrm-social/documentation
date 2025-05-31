- - -
Titolo: ActivityPub Data: 2021-04-20 Ordine: 1
- - -

BookWyrm utilizza il protocollo [ActivityPub](http://activitypub.rocks/) per inviare e ricevere le attività dell'utente tra altre istanze di BookWyrm e altri servizi che implementano ActivityPub, come [Mastodon](https://joinmastodon.org/). Per gestire i dati del libro, BookWyrm ha una manciata di tipi di attività estesi che non fanno parte dello standard, ma sono leggibili ad altre istanze di BookWyrm.

## Attività e oggetti

### Utenti e relazioni
Le interazioni tra gli utenti seguono le specifiche standard di ActivityPub.

- `Segui`: richiesta di ricevere aggiornamenti di un utente e visualizzare i sui stati che hanno privacy solo follower
- `Accetta`: approva un `Segui` e finalizza la relazione
- `Rifiuta`: nega un `Segui`
- `Blocco`: impedisce agli utenti di vedere gli stati degli altri e impedisce all'utente bloccato di visualizzare il profilo del bloccante
- `Aggiorna`: aggiorna il profilo e le impostazioni di un utente
- `Elimina`: disattiva un utente
- `Annulla`: inverte un `Segui` o `Blocco`

### Stati
#### Tipologia di oggetto

- `Nota`: Su servizi come Mastodon, `Nota` è il tipo primario di stato. Contengono il corpo del messaggio, gli allegati, possono menzionare gli utenti, ed posso ricevere in risposta qualsiasi tipo di stato. All'interno di BookWyrm, la `Nota`s può essere creata solo come messaggio diretto o come risposta ad altri stati.
- `Recensione`: Una recensione è uno stato in risposta a un libro (indicato dal campo `inReplyToBook`), avente un titolo, un corpo e una valutazione numerica compresa tra 0 (non valutato) e 5.
- `Comment`: Un commento a un libro parla del libro stesso e ha un corpo messaggio.
- `Citazione`: Una citazione ha un corpo del messaggio, un estratto da un libro e menziona un libro.


#### Attività

- `Crea`: salva un nuovo stato nel database.

   **Note**: BookWyrm accetta attività `Create` solo se sono:

   - Messaggi diretti (cioè, `Note`s con il livello di privacy `direct`, che menzionano un utente locale),
   - Relativo a un libro (un tipo di stato personalizzato che include il campo `inReplyToBook`),
   - Risposte agli stati esistenti salvati nel database
- `Delete`: Rimuove uno stato
- `Like`: Crea un preferito sullo stato
- `Annuounce`: Condivide lo stato nella timeline dell'utente
- `Undo`: Inverte un `Like` o `Announce`

### Collezioni
I libri e le liste degli utenti sono rappresentati da [`OrdinedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Obiettivi

- `Scaffale`: Collezione di libri di un utente. Per impostazione predefinita, ogni utente ha gli scaffali `da leggere`, `letture correnti`, e `letti` che vengono utilizzati per monitorare i progressi di lettura.
- `Lista`: Una raccolta di libri che può avere elementi forniti da utenti diversi da quello che ha creato la lista.

#### Attività

- `Crea`: Aggiunge uno scaffale o una lista al database.
- `Elimina`: Rimuove uno scaffale o una lista.
- `Aggiungi`: Aggiunge un libro a uno scaffale o una lista.
- `Rimuovi`: Rimuove un libro da uno scaffale o da una lista.


## Serializzazione Alternativa
Poiché BookWyrm utilizza tipi di oggetti personalizzati (`Recensione`, `Commento`, `Citazione`) che non sono supportati da ActivityPub, gli stati si trasformano in tipi standard quando inviati o visualizzati da servizi non-BookWyrm. `Recensione`s viene convertita in `Articolo`s, `Commento`s e `Citazione`s vengono convertiti in `Nota`s, con un link al libro e l'immagine di copertina allegata.
