- - -
Title: ActivityPub Date: 2025-04-21 Order: 1
- - -

BookWyrm utilizza il protocollo [ActivityPub](http://activitypub.rocks/) per inviare e ricevere le attività dell'utente tra altre istanze di BookWyrm e altri servizi che implementano ActivityPub, come [Mastodon](https://joinmastodon.org/). Per gestire i dati del libro, BookWyrm ha una manciata di tipi di attività estesi che non fanno parte dello standard, ma sono leggibili ad altre istanze di BookWyrm.

To view the ActivityPub data for a BookWyrm entity (user, book, list, etc) you can usually add `.json` to the end of the URL. e.g. `https://www.example.com/user/sam.json` and see the JSON in your web browser or via an http request (e.g. using `curl`).

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
- `Move`: communicate that a user has changed their ID and has moved to a new server. Most ActivityPub software will "follow" the user to the new identity. BookWyrm sends a notification to followers and requires them to confirm they want to follow the user to their new identity.

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

- `Scaffale`: Collezione di libri di un utente. By default, every user has a `to-read`, `reading`, `stop-reading` and `read` shelf which are used to track reading progress.
- `Lista`: Una raccolta di libri che può avere elementi forniti da utenti diversi da quello che ha creato la lista.

#### Attività

- `Crea`: Aggiunge uno scaffale o una lista al database.
- `Elimina`: Rimuove uno scaffale o una lista.
- `Aggiungi`: Aggiunge un libro a uno scaffale o una lista.
- `Rimuovi`: Rimuove un libro da uno scaffale o da una lista.

## Serializzazione Alternativa
Poiché BookWyrm utilizza tipi di oggetti personalizzati (`Recensione`, `Commento`, `Citazione`) che non sono supportati da ActivityPub, gli stati si trasformano in tipi standard quando inviati o visualizzati da servizi non-BookWyrm. `Recensione`s viene convertita in `Articolo`s, `Commento`s e `Citazione`s vengono convertiti in `Nota`s, con un link al libro e l'immagine di copertina allegata.

This may change in future in favor of the more ActivityPub-compliant [extended Object types](https://www.w3.org/TR/activitystreams-core/#fig-following-is-an-example-object-that-uses-the-id-and-type-properties-to-express-the-global-identifier-and-object-type) listed alongside core ActivityPub types.

## Making ActivityPub-aware models

The way BookWyrm sends and receives ActivityPub objects can be confusing for developers who are new to BookWyrm. It is mostly controlled by:

* Functions and [data classes](https://docs.python.org/3/library/dataclasses.html) outlined in the [activitypub](https://github.com/bookwyrm-social/bookwyrm/tree/main/bookwyrm/activitypub) directory
* The [ActivitypubMixin](https://github.com/bookwyrm-social/bookwyrm/blob/c458cdcb992a36f3c4a06752499461c3dd991e07/bookwyrm/models/activitypub_mixin.py#L40) and its children for models that are serializable for ActivityPub requests

### Serializing data to and from ActivityPub JSON

BookWyrm needs to know how to _serialize_ the data from the model into an ActivityPub JSON-LD object.

The `/activitypub/base_activity.py` file provides the core functions that turn ActivityPub JSON-LD strings into usable Django model objects, and vice-versa. We do this by creating a data class in `bookwyrm/activitypub`, and defining how the model should be serialized by providing an `activity_serializer` value in the model, which points to the relevant data class. From `ActivityObject` we inherit `id` and `type`, and two _class methods_:

**`to_model`**

This method takes an ActivityPub JSON string and tries to turn it into a BookWyrm model object, finding an existing object wherever possible. This is how we process **incoming** ActivityPub objects.

**`serialize`**

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
