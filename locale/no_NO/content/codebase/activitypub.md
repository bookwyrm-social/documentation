- - -
Title: ActivityPub Date: 2025-04-21 Order: 1
- - -

BookWyrm bruker [ActivityPub](http://activitypub.rocks/)-protokollen for å sende og motta brukeraktivitet mellom andre BookWyrm-instanser og andre tjenester som implementerer ActivityPub, som [Mastodon](https://joinmastodon.org/). For å håndtere bokdata, har BookWyrm en håndfull utvidede aktivitetstyper som ikke er en del av standarden, men er forståelige for andre BookWyrm-instanser.

To view the ActivityPub data for a BookWyrm entity (user, book, list, etc) you can usually add `.json` to the end of the URL. e.g. `https://www.example.com/user/sam.json` and see the JSON in your web browser or via an http request (e.g. using `curl`).

## Aktiviteter og objekter

### Brukere og relasjoner
Interaksjoner for brukerrelasjoner følger standard ActivityPub-spesifikasjon.

- `Follow`: be om å motta statuser fra en bruker, og se deres statuser som er begrenset til å sees kun av følgere
- `Accept`: godkjenner en `Follow` og fullfører forholdet
- `Reject`: nekter en `Follow`
- `Block`: forhindrer brukere fra å se hverandres statuser, og forhindrer at blokkerte brukere fra å se aktørens profil
- `Update`: oppdaterer brukerens profil og innstillinger
- `Delete`: deaktiverer en bruker
- `Undo`: reverserer en `Follow` eller `Block`
- `Move`: communicate that a user has changed their ID and has moved to a new server. Most ActivityPub software will "follow" the user to the new identity. BookWyrm sends a notification to followers and requires them to confirm they want to follow the user to their new identity.

### Statuser
#### Objekttyper

- `Note`: På tjenester som Mastodon er `Note` den primære typen status. De inneholder meldingens brødtekst, vedlegg, kan nevne brukere, og kan være svar til statuser av alle typer. I BookWyrm kan `Note` bare opprettes som direktemeldinger eller som svar på andre statuser.
- `Review`: A anmeldelse er en responsstatus til en bok (indikert med `inReplyToBook`-feltet), og har en tittel, en brødtekst, og en numerisk vurdering mellom 0 (ikke vurdert) og 5.
- `Comment`: En kommentar til en bok nevner en bok og har en brødtekst.
- `Quotation`: Et sitat har en brødtekst, et utdrag fra en bok, og nevner en bok.

#### Aktiviteter

- `Create`: lagrer en ny status i databasen.

    **Merk**: BookWyrm godtar bare `Create`-aktiviteter dersom de er:

    - direktemeldinger (f.eks. `Note` med personvernsnivå `direct`, som nevner en lokal bruker),
    - svar til en bok (av en egendefinert statustype som inkluderer feltet `inReplyToBook`),
    - svar til en eksisterende status lagret i databasen

- `Delete`: Fjerner en status
- `Like`: Oppretter en favoritt på statusen
- `Announce`: Booster statusen inn i aktørens tidslinje
- `Undo`: reverserer en `Like` eller `Announce`

### Samlinger
Brukerens bøker og lister er representert av en [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objekter

- `Shelf`: En brukers boksamling. By default, every user has a `to-read`, `reading`, `stop-reading` and `read` shelf which are used to track reading progress.
- `List`: En samling med bøker som kan ha elementer bidratt av andre enn den som opprettet listen.

#### Aktiviteter

- `Create`: Legger til en hylle eller en liste i databasen.
- `Delete`: Fjerner en hylle eller en liste.
- `Add`: Legger til en bok til en hylle eller liste.
- `Delete`: Fjerner en bok fra en hylle eller liste.

## Alternativ serialisering
Ettersom BookWyrm bruker tilpassede objecttyper (`Review`, `Comment`, `Quotation`) som ikke er støttet av ActivityPub, vil statuser bli oversatt til standardtyper når de blir sendt til eller sett på av ikke-BookWyrm-tjenester. `Review` blir konvertert til `Article`, og `Comment` og `Quotation` blir konvertert til `Note`, med en lenke til boka med vedlagt omslagsbilde.

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
