- - -
Title: ActivityPub Date: 2025-04-21 Order: 1
- - -

BookWyrm verwendet das [ActivityPub](http://activitypub.rocks/)-Protokoll, um Benutzer*innenaktivitäten zwischen anderen BookWyrm-Instanzen und anderen Diensten, die ActivityPub implementieren (wie [Mastodon](https://joinmastodon.org/)), zu senden und zu empfangen. Um Buchdaten zu handhaben, hat BookWyrm eine Handvoll erweiterter Aktivitätstypen, die nicht zum Standard gehören, aber für andere BookWyrm-Instanzen lesbar sind.

To view the ActivityPub data for a BookWyrm entity (user, book, list, etc) you can usually add `.json` to the end of the URL. e.g. `https://www.example.com/user/sam.json` and see the JSON in your web browser or via an http request (e.g. using `curl`).

## Aktivitäten und Objekte

### Benutzer*innen und Beziehungen
Benutzer*innenbeziehungsinteraktionen folgen der Standard ActivityPub Spezifikation.

- `Folgen`: Bitte, um den Status eine*r Benutzer*in zu erhalten und anzusehen, die die Privatsphäre auf nur Follower haben
- `Akzeptieren`: genehmigt `Folgen` und erstellt die Beziehung
- `Ablehnen`: verweigert `Folgen`
- `Blocken`: verhindert, dass Benutzer*innen einander Status ansehen und verhindert, dass der blockierte Benutzer*innen das Profil des Akteurs ansehen
- `Update`: Aktualisiert das Profil und die Einstellungen eine*r Benutzer*in
- `Löschen`: Deaktiviert eine*n Benutzer*in
- `Rückgängig`: Reversiert `Folgen` oder `Blocken`
- `Move`: communicate that a user has changed their ID and has moved to a new server. Most ActivityPub software will "follow" the user to the new identity. BookWyrm sends a notification to followers and requires them to confirm they want to follow the user to their new identity.

### Status
#### Objekttypen

- `Notiz`: Bei Diensten wie Mastodon, ist `Notiz`en der primäre Typ des Status. Sie enthalten einen Text, Anhänge, können Benutzer erwähnen und Antworten auf Status jeder Art sein. In BookWyrm können `Notiz`en nur als direkte Nachrichten oder als Antworten auf andere Status erstellt werden.
- `Rezension`: Eine Rezension ist ein Status, der sich auf ein Buch bezieht (angezeigt durch das `inReplyToBook`-Feld), welches einen Titel, Text sowie die numerische Bewertung auf einer Skala von 0 (keine Bewertung) bis 5 enthält.
- `Kommentar`: Ein Kommentar zu einem Buch erwähnt ein Buch und hat einen Text.
- `Zitat`: Ein Zitat enthält einen Text, einen Auszug aus dem Buch und erwähnt ein Buch.

#### Aktivitäten

- `Erstellen`: Speichert einen neuen Status in der Datenbank.

    **Hinweis**: BookWyrm akzeptiert nur `Erstellen`-Aktivitäten, wenn sie sind:

    - Direktnachrichten (d.h. `Hinweis`e mit der Datenschutzstufe `direkt`, welche einen lokalen Benutzer erwähnen),
    - Verbunden mit einem Buch (eines benutzerdefinierten Statusstyps, der das Feld `inReplyToBook` enthält),
    - Antworten auf existierende Status in der Datenbank

- `Löschen`: Entfernt einen Status
- `Gefällt`: Erstellt einen Favoriten für den Status
- `Ankündigung`: Teilt den Status in der Zeitleiste des Akteurs
- `Rückgängig`: Reversiert `Gefällt` oder `Ankündigung`

### Sammlungen
Bücher und Listen von Benutzern werden durch [`Sortierte Sammlung`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection) repräsentiert

#### Objekte

- `Regal`: Buchsammlung eines Benutzers. By default, every user has a `to-read`, `reading`, `stop-reading` and `read` shelf which are used to track reading progress.
- `Liste`: Eine Sammlung von Büchern, zu der auch andere Personen als die, die die Liste erstellt hat, Bücher beitragen können.

#### Aktivitäten

- `Erstellen`: Fügt der Datenbank ein Regal oder eine Liste hinzu.
- `Löschen`: Entfernt ein Regal oder eine Liste.
- `Hinzufügen`: Fügt ein Buch zu einem Regal oder einer Liste hinzu.
- `Entfernen`: Entfernt ein Buch aus einem Regal oder einer Liste.

## Alternative Serialisierung
Weil BookWyrm eigene Objekttypen (`Rezension`, `Kommentar`, `Zitat`) benutzt, die nicht von ActivityPub unterstützt werden, werden Status in Standardtypen umgewandelt, wenn sie an nicht-BookWyrm-Dienste gesendet oder angezeigt werden. `Rezension`en werden in `Artikel` umgewandelt und `Kommentar`e und `Zitat`e werden in `Notiz`en mit einem Link zu dem Buch und dem Titelbild als Anhang konvertiert.

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
