- - -
Titolo: ActivityPub Data: 21-04-2025 Ordine: 1
- - -

BookWyrm utilizza il protocollo [ActivityPub](http://activitypub.rocks/) per inviare e ricevere le attività dell'utente tra altre istanze di BookWyrm e altri servizi che implementano ActivityPub, come [Mastodon](https://joinmastodon.org/). Per gestire i dati del libro, BookWyrm ha una manciata di tipi di attività estesi che non fanno parte dello standard, ma sono leggibili ad altre istanze di BookWyrm.

Per accedere ai dati ActivityPub relativi a un'entità BookWyrm (come un utente, un libro o una lista), aggiungi `.json` alla fine dell'URL. visita `https://www.example.com/user/sam.json` per visualizzare i dati JSON nel browser o tramite una richiesta HTTP (ad esempio con `curl`).

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
- `Spostamento`: indica che un utente ha modificato il proprio ID e si è spostato su un altro server. La maggior parte delle applicazioni ActivityPub continuerà a seguire l’utente dopo il cambio di identità. BookWyrm invia una notifica ai follower e richiede loro di confermare se desiderano continuare a seguire l’utente nella sua nuova identità.

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

- `Scaffale`: Collezione di libri di un utente. Di default, ogni utente ha `una scaffale da leggere`, `in lettura`,`interrotto`letto</code>, utilizzati per tenere traccia del progresso di lettura.
- `Lista`: Una raccolta di libri che può avere elementi forniti da utenti diversi da quello che ha creato la lista.

#### Attività

- `Crea`: Aggiunge uno scaffale o una lista al database.
- `Elimina`: Rimuove uno scaffale o una lista.
- `Aggiungi`: Aggiunge un libro a uno scaffale o una lista.
- `Rimuovi`: Rimuove un libro da uno scaffale o da una lista.

## Serializzazione Alternativa
Poiché BookWyrm utilizza tipi di oggetti personalizzati (`Recensione`, `Commento`, `Citazione`) che non sono supportati da ActivityPub, gli stati si trasformano in tipi standard quando inviati o visualizzati da servizi non-BookWyrm. `Recensione`s viene convertita in `Articolo`s, `Commento`s e `Citazione`s vengono convertiti in `Nota`s, con un link al libro e l'immagine di copertina allegata.

Questo potrebbe cambiare in futuro a favore dei [tipi di oggetti estesi](https://www.w3.org/TR/activitystreams-core/#fig-following-is-an-example-object-that-uses-the-id-and-type-properties-to-express-the-global-identifier-and-object-type) più conformi a ActivityPub, elencati insieme ai tipi core di ActivityPub.

## Sviluppo di modelli compatibili con ActivityPub

Il modo in cui BookWyrm invia e riceve oggetti ActivityPub può risultare confuso per gli sviluppatori che si avvicinano per la prima volta a BookWyrm. È principalmente composto da:

* Funzioni e [classi dati](https://docs.python.org/3/library/dataclasses.html) descritte nella directory [activitypub](https://github.com/bookwyrm-social/bookwyrm/tree/main/bookwyrm/activitypub).
* Il [ActivitypubMixin](https://github.com/bookwyrm-social/bookwyrm/blob/c458cdcb992a36f3c4a06752499461c3dd991e07/bookwyrm/models/activitypub_mixin.py#L40) e i suoi elementi figli per i modelli che possono essere serializzati per le richieste ActivityPub

### Serializzazione dei dati in formato JSON per ActivityPub e viceversa

BookWyrm deve sapere come _serializzare_ i dati del modello in un oggetto JSON-LD compatibile con ActivityPub.

Il file `/activitypub/base_activity.py` fornisce le funzioni principali che trasformano le stringhe JSON-LD di ActivityPub in oggetti modello Django utilizzabili, e viceversa. Facciamo questo creando una data class in `bookwyrm/activitypub` e definendo come il modello debba essere serializzato, fornendo un valore `activity_serializer` nel modello, che punta alla data class corrispondente. Da `ActivityObject` ereditiamo `id` e `type`, e due _metodi di classe_:

**`to_model`**

Questo metodo prende una stringa JSON di ActivityPub e cerca di trasformarla in un oggetto modello di BookWyrm, trovando un oggetto esistente quando possibile. È così che processiamo gli oggetti ActivityPub **in entrata**.

**`serializza`**

This method takes a BookWyrm model object, and turns it into a valid ActivityPub JSON string using the dataclass definitions. This is how we process **outgoing** ActivityPub objects.

### Example - Users

A BookWyrm user [is defined in `models/user.py`](https://github.com/bookwyrm-social/bookwyrm/blob/main/bookwyrm/models/user.py):

```py
class User(OrderedCollectionPageMixin, AbstractUser):
    """a user who wants to read books"""
```
Notice that we are inheriting from ("subclassing") `OrderedCollectionPageMixin`. This in turn inherits from `ObjectMixin`, which inherits from `ActivitypubMixin`. This may seem convoluted, but this inheritence chain allows us to avoid duplicating code as our ActivityPub objects become more specific. `AbstractUser` is [a Django model intended to be subclassed](https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#specifying-custom-user-model), giving us things like hashed password logins and permission levels "out of the box".

Because `User` inherits from [`ObjectMixin`](https://github.com/bookwyrm-social/bookwyrm/blob/c458cdcb992a36f3c4a06752499461c3dd991e07/bookwyrm/models/activitypub_mixin.py#L213), when we `save()` a `User` object we will send a `Create` activity (if this is the first time the user was saved) or an `Update` activity (if we're just saving a change – e.g. to the user description or avatar). Any other model you add to BookWyrm will have the same capability if it inherits from `ObjectMixin`.

For BookWyrm users, the `activity_serializer` is defined in the `User` model:

```py
activity_serializer = activitypub.Person
```

The data class definition for `activitypub.Person` is at `/activitypub/person.py`:

```py
@dataclass(init=False)
class Person(ActivityObject):
    """actor activitypub json"""

    preferredUsername: str
    inbox: str
    publicKey: PublicKey
    followers: str = None
    following: str = None
    outbox: str = None
    endpoints: Dict = None
    name: str = None
    summary: str = None
    icon: Image = None
    bookwyrmUser: bool = False
    manuallyApprovesFollowers: str = False
    discoverable: str = False
    hideFollows: str = False
    movedTo: str = None
    alsoKnownAs: dict[str] = None
    type: str = "Person"
```

You might notice that some of these fields are not a perfect match to the fields in the `User` model. If you have a field name in your model that needs to be called something different in the ActivityPub object (e.g. to comply with Python naming conventions in the model but JSON naming conventions in JSON string), you can define an `activitypub_field` in the model field definition:

```py
followers_url = fields.CharField(max_length=255, activitypub_field="followers")
```
