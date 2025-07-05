- - -
Title: ActivityPub Date: 2025-04-21 Order: 1
- - -

BookWyrm folosește protocolul [ActivityPub](http://activitypub.rocks/) pentru a trimite și primi activitatea utilizatorului între alte instanțe BookWyrm și alte servicii care implementează ActivityPub, precum [Mastodon](https://joinmastodon.org/). Pentru a gestiona datele cărților, BookWyrm are câteva tipuri Activity extinse care nu fac parte din standard, dar înțelese de alte instanțe BookWyrm.

To view the ActivityPub data for a BookWyrm entity (user, book, list, etc) you can usually add `.json` to the end of the URL. e.g. `https://www.example.com/user/sam.json` and see the JSON in your web browser or via an http request (e.g. using `curl`).

## Activități și obiecte

### Utilizatori și relații
Interacțiunile dintre relațiile utilizatorilor respectă specificația ActivityPub.

- `Follow`: solicitați să primiți stări de la un utilizator și să le vizualizați pe cele cu confidențialitatea „numai urmăritori”
- `Accept`: aprobă o `cerere de urmărire` și finalizează relația
- `Reject`: respinge o `cerere de urmărire`
- `Block`: împiedică utilizatorii de a își vedea unul altuia stările și împiedică utilizatorul blocat de a vizualiza profilul actorului
- `Update`: actualizează profilul și setările unui utilizator
- `Delete`: dezactivează un utilizator
- `Undo`: anulează o `cerere de urmărire` sau `de blocare`
- `Move`: communicate that a user has changed their ID and has moved to a new server. Most ActivityPub software will "follow" the user to the new identity. BookWyrm sends a notification to followers and requires them to confirm they want to follow the user to their new identity.

### Stări
#### Tipuri de obiecte

- `Notă`: pe servicii precum Mastodon, `Notele` sunt tipul principal de stare. Ele conțin corpul mesajului, atașamentele, pot menționa utilizatori și pot fi răspunsuri la stări de orice tip. În cadrul BookWyrm, `notele` pot fi create ca mesaje directe sau ca răspunsuri la alte stări.
- `Review`: A review is a status in response to a book (indicated by the `inReplyToBook` field), which has a title, body, and numerical rating between 0 (not rated) and 5.
- `Comentariu`: un comentariu despre o carte menționează cartea respectivă și are un corp de mesaj.
- `Quotation`: A quote has a message body, an excerpt from a book, and mentions a book.

#### Activități

- `Create`: salvează o nouă stare în baza de date.

    **Note**: BookWyrm acceptă activități de `Create` numai dacă sunt:

    - Mesaje directe (de exemplu `Note` cu nivel de confidențialitate `direct`, care menționează un utilizator local),
    - În legătură cu o carte (de un tip de stare personalizat care include câmpul `inReplyToBook`),
    - Răspunsuri la stări existente salvate în baza de date

- `Delete`: elimină o stare
- `Like`: marchează starea ca favorit
- `Announce`: partajează starea pe fluxul actorului
- `Undo`: anulează `Like` sau `Announce`

### Colecții
Cărțile și listele utilizatorului sunt reprezentate de [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Obiecte

- `Shelf`: o colecție de cărți a utilizatorului. By default, every user has a `to-read`, `reading`, `stop-reading` and `read` shelf which are used to track reading progress.
- `List`: o colecție de cărți care poate avea articole contribuite de alți utilizatori.

#### Activități

- `Create`: adaugă un raft sau o listă în baza de date.
- `Delete`: înlătură un raft sau o listă.
- `Add`: adaugă o carte pe un raft sau într-o listă.
- `Remove`: înlătură o carte de pe un raft sau dintr-o listă.

## Serializare alternativă
Deoarece BookWyrm folosește propriile tipuri de obiecte (`Review`, `Comment`, `Quotation`) care nu sunt suportate de ActivityPub, stările sunt transformate în tipuri standard când sunt trimise sau vizualizate de servicii din afara BookWyrm. `Review`s sunt convertite în `Article`s, iar `Comment`s și `Quotation`s sunt convertite în `Note`s cu o legătură către cartea și imaginea de copertă atașate.

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
