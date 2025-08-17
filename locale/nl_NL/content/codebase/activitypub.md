- - -
Title: ActivityPub Date: 2025-04-21 Order: 1
- - -

BookWyrm maakt gebruik van het [ActivityPub](http://activitypub.rocks/) protocol voor het verzenden en ontvangen van gebruikersactiviteit tussen andere BookWyrm instanties en andere diensten die ActivityPub implementeren zoals [Mastodon](https://joinmastodon.org/). Om gegevens van boeken te verwerken heeft BookWyrm een handvol uitgebreide activiteitstypen die niet deel zijn van de standaard, maar leesbaar zijn voor andere BookWyrm instanties.

To view the ActivityPub data for a BookWyrm entity (user, book, list, etc) you can usually add `.json` to the end of the URL. e.g. `https://www.example.com/user/sam.json` and see the JSON in your web browser or via an http request (e.g. using `curl`).

## Activiteiten en Objecten

### Gebruikers en relaties
Gebruikersrelatie interacties volgen de standaard ActivityPub specificatie.

- `Follow`: verzoek om statussen van een gebruiker te ontvangen en hun statussen met alleen volgers-only privacy te bekijken
- `Accept`: keurt een `Follow` goed en voltooit de relatie
- `Reject`: weigert een `Follow`
- `Block`: voorkomen dat gebruikers elkaars statussen zien, en voorkomt dat de geblokkeerde gebruiker het profiel van de speler bekijkt
- `Update`: updates het profiel en instellingen van een gebruiker
- `Delete`: deactiveert een gebruiker
- `Undo`: draait een `Follow` of `Block` terug
- `Move`: communicate that a user has changed their ID and has moved to a new server. Most ActivityPub software will "follow" the user to the new identity. BookWyrm sends a notification to followers and requires them to confirm they want to follow the user to their new identity.

### Statussen
#### Objecttypes

- `Note`: Voor diensten zoals Mastodon, `Note`s zijn het primaire status type. Ze bevatten een bericht, bijlagen, kunnen gebruikers vermelden en zijn antwoorden op statussen van elk type. Binnen BookWyrm kan `Note`s alleen worden gemaakt als directe berichten of als antwoord op andere statussen.
- `Review`: Een recensie is een status in reactie op een boek (aangegeven door het `inReplyToBook` veld) die een titel, lichaam en numerieke beoordeling tussen 0 (niet beoordeeld) en 5 heeft.
- `Comment`: Een reactie op een boek vermeldt een boek en bevat een bericht.
- `Quotation`: Een citaat heeft een bericht, een extract uit een boek en vermeldt een boek.

#### Activiteiten

- `Create`: slaat een nieuwe status op in de database.

    **Let op**: BookWyrm accepteert alleen `Create` activiteiten als ze zijn:

    - Directe berichten (d.w.z. `Note`met het privacyniveau `direct`, die een lokale gebruiker vermeldt),
    - Gerelateerd aan een boek (van een aangepast statustype dat het veld `inReplyToBook` bevat),
    - Antwoorden op bestaande statussen opgeslagen in de database

- `Delete`: Verwijdert een status
- `Like`: Maakt een favoriet aan op de status
- `Announce`: Vergroot de status in de tijdlijn van de speler
- `Undo`: draait een `Like` of `Announce` terug

### Verzamelingen
De boeken en lijsten van gebruikers worden vertegenwoordigd door [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objecten

- `Shelf`: Een boekverzameling van gebruikers. By default, every user has a `to-read`, `reading`, `stop-reading` and `read` shelf which are used to track reading progress.
- `List`: Een verzameling boeken waarbij items kunnen worden bijgedragen door andere gebruikers dan degene die de lijst hebben gemaakt.

#### Activiteiten

- `Aanmaken`: Voegt een plank of een lijst toe aan de database.
- `Delete`: Verwijdert een plank of lijst.
- `Add`: Voegt een boek toe aan een plank of lijst.
- `Remove`: Verwijdert een boek van een plank of lijst.

## Alternatieve serialisatie
Omdat BookWyrm gebruikmaakt van aangepaste objecttypes (`Review`, `Comment`, `Quotation`) die niet worden ondersteund door ActivityPub, worden statussen omgezet in standaard types wanneer ze worden verzonden naar of bekeken door niet-BookWyrm diensten. `Review`s worden omgezet in `Article`s, en `Comment`s en `Quotation`s worden omgezet in `Note`s, met een koppeling naar het boek en de bijgevoegde omslagafbeelding.

This may change in future in favor of the more ActivityPub-compliant [extended Object types](https://www.w3.org/TR/activitystreams-core/#fig-following-is-an-example-object-that-uses-the-id-and-type-properties-to-express-the-global-identifier-and-object-type) listed alongside core ActivityPub types.

## Making ActivityPub-aware models

The way BookWyrm sends and receives ActivityPub objects can be confusing for developers who are new to BookWyrm. Het wordt voornamelijk gecontroleerd door:

* Functies en [gegevensklassen](https://docs.python.org/3/library/dataclasses.html) geschetst in de [activitypub](https://github.com/bookwyrm-social/bookwyrm/tree/main/bookwyrm/activitypub) map
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
