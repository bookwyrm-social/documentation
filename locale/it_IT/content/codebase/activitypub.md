- - -
Title: ActivityPub Date: 2021-04-20 Order: 1
- - -

BookWyrm utilizza il protocollo [ActivityPub](http://activitypub.rocks/) per inviare e ricevere le attività dell'utente tra altre istanze di BookWyrm e altri servizi che implementano ActivityPub, come [Mastodon](https://joinmastodon.org/). Per gestire i dati del libro, BookWyrm ha una manciata di tipi di attività estesi che non fanno parte dello standard, ma sono leggibili ad altre istanze di BookWyrm.

## Attività e oggetti

### Utenti e relazioni
Le interazioni tra gli utenti seguono le specifiche standard di ActivityPub.

- `Segui`: richiesta di ricevere aggiornamenti di un utente e visualizzare i sui stati che hanno privacy solo follower
- `Accetta`: approva un `Segui` e finalizza la relazione
- `Rifiuta`: nega un `Segui`
- `Block`: prevent users from seeing one another's statuses, and prevents the blocked user from viewing the actor's profile
- `Aggiorna`: aggiorna il profilo e le impostazioni di un utente
- `Elimina`: disattiva un utente
- `Annulla`: inverte un `Segui` o `Blocco`

### Stati
#### Tipologia di oggetto

- `Nota`: Su servizi come Mastodon, `Nota` è il tipo primario di stato. Contengono il corpo del messaggio, gli allegati, possono menzionare gli utenti, ed posso ricevere in risposta qualsiasi tipo di stato. All'interno di BookWyrm, la `Nota`s può essere creata solo come messaggio diretto o come risposta ad altri stati.
- `Review`: Una recensione è uno stato in risposta un libro (indicato dal campo `inReplyToBook`), che ha un titolo, un corpo e una valutazione numerica compresa tra 0 (non valutato) e 5.
- `Comment`: Un commento a un libro parla del libro stesso e ha un corpo messaggio.
- `Citazione`: Una citazione ha un corpo del messaggio, un estratto da un libro e menziona un libro


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
User's books and lists are represented by [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Obiettivi

- `Shelf`: A user's book collection. By default, every user has a `to-read`, `reading`, and `read` shelf which are used to track reading progress.
- `List`: A collection of books that may have items contributed by users other than the one who created the list.

#### Attività

- `Create`: Adds a shelf or list to the database.
- `Delete`: Removes a shelf or list.
- `Add`: Adds a book to a shelf or list.
- `Remove`: Removes a book from a shelf or list.


## Alternative Serialization
Because BookWyrm uses custom object types (`Review`, `Comment`, `Quotation`) that aren't supported by ActivityPub, statuses are transformed into standard types when sent to or viewed by non-BookWyrm services. `Review`s are converted into `Article`s, and `Comment`s and `Quotation`s are converted into `Note`s, with a link to the book and the cover image attached.
