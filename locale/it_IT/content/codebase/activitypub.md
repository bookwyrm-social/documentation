BookWyrm uses the [ActivityPub](http://activitypub.rocks/) protocol to send and receive user activity between other BookWyrm instances and other services that implement ActivityPub, like [Mastodon](https://joinmastodon.org/). To handle book data, BookWyrm has a handful of extended Activity types which are not part of the standard, but are legible to other BookWyrm instances.

## Attività e oggetti

### Utenti e relazioni
User relationship interactions follow the standard ActivityPub spec.

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
- `Comment`: A comment on a book mentions a book and has a message body.
- `Quotation`: A quote has a message body, an excerpt from a book, and mentions a book


#### Activities

- `Create`: saves a new status in the database.

   **Note**: BookWyrm only accepts `Create` activities if they are:

   - Direct messages (i.e., `Note`s with the privacy level `direct`, which mention a local user),
   - Related to a book (of a custom status type that includes the field `inReplyToBook`),
   - Replies to existing statuses saved in the database
- `Delete`: Removes a status
- `Like`: Creates a favorite on the status
- `Announce`: Boosts the status into the actor's timeline
- `Undo`: Reverses a `Like` or `Announce`

### Collections
User's books and lists are represented by [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objects

- `Shelf`: A user's book collection. By default, every user has a `to-read`, `reading`, and `read` shelf which are used to track reading progress.
- `List`: A collection of books that may have items contributed by users other than the one who created the list.

#### Activities

- `Create`: Adds a shelf or list to the database.
- `Delete`: Removes a shelf or list.
- `Add`: Adds a book to a shelf or list.
- `Remove`: Removes a book from a shelf or list.


## Alternative Serialization
Because BookWyrm uses custom object types (`Review`, `Comment`, `Quotation`) that aren't supported by ActivityPub, statuses are transformed into standard types when sent to or viewed by non-BookWyrm services. `Review`s are converted into `Article`s, and `Comment`s and `Quotation`s are converted into `Note`s, with a link to the book and the cover image attached.
