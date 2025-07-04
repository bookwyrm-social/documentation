- - -
Title: ActivityPub Date: 2025-04-21 Order: 1
- - -

BookWyrm-ek [Activity Pub](http://activitypub.rocks/) protokoloa erabiltzen du erabiltzailearen jarduera bidaltzeko eta jasotzeko, BookWyrm instantzien eta ActivityPub ezarria duten beste zerbitzu baten artean, [Mastodon](https://joinmastodon.org/) bezala. Liburuko datuak erabiltzeko, BookWyrm-ek estandarrak ez diren Activity motako hainbat gehigarri erabiltzen ditu, baina BookWyrm-en beste instantziekin erabilgarriak direnak.

To view the ActivityPub data for a BookWyrm entity (user, book, list, etc) you can usually add `.json` to the end of the URL. e.g. `https://www.example.com/user/sam.json` and see the JSON in your web browser or via an http request (e.g. using `curl`).

## Jarduerak eta Objektuak

### Erabiltzaileak eta harremanak
Erabiltzaile-harremanaren elkarrekintzek Activity Pub-en berezitasun estandarrari jarraitzen diote.

- `Jarraitu`: erabiltzaile baten egoera jasotzeko eskatzen du eta pribatutasun-aukera «jarraitzaileak soilik» aktibatuta duten egoerak erakusten ditu
- `Onartu`: `Jarraitzea` onartzen eta harremana gauzatzen du
- `Ukatu`: `Jarraitze` bati uko egiten dio
- `Blokeatu`: erabiltzaileek bestearen egoerak ikustea eragozten du eta blokeatutako erabiltzaileak aktorearen profila ikustea eragozten du
- `Eguneratu`: erabiltzaile baten profila eta konfigurazioa eguneratzen ditu
- `Ezabatu`: erabiltzaile bat desaktibatzen du
- `Desegin`: desegiten ditu `Jarraitze` bat edo `Blokeo` bat
- `Move`: communicate that a user has changed their ID and has moved to a new server. Most ActivityPub software will "follow" the user to the new identity. BookWyrm sends a notification to followers and requires them to confirm they want to follow the user to their new identity.

### Egoerak
#### Objektu motak

- `Oharra`: Mastodon bezalako zerbitzuetan, `Oharra` elementuak egoera-mota nagusia dira. Barne hartzen dute mezu eremu bat, fitxategi erantsiak, erabiltzaileak aipa ditzakete eta edozein motatako estatutuen erantzunak izan daitezke. BookWyrm-en, `Oharra` elementuak zuzeneko mezu gisa soilik sor daitezke edo beste egoera batzuei emandako erantzun gisa.
- `Kritika`: Kritika bidalketa bat da, liburu bati zuzenduta (`LiburuariBuruz` eremuak adierazita). Kritika batek honako atal hauek ditu: izenburua, gorputza eta 0 (kalifikatu gabea) eta 5 arteko kalifikazioa.
- `Iruzkina`: Liburu bati buruzko iruzkin batek liburu bat aipatzen du eta mezu gorputz bat dauka.
- `Aipua`: Aipu batek du mezuaren gorpuntz bat eta liburu baten zati bat, eta liburu bat aipatzen du.

#### Jarduerak

- `Sortu`: bidalketa berri bat gordetzen du datu-basean.

    **Oharra**: BookWyrm-ek `Sortu` jarduerak baimentzen ditu baldin eta:

    - Mezu zuzenak badira (hots, `Oharra` elementuak `zuzena` pribatutasun mailarekin, tokiko erabiltzailearen aipamenarekin),
    - Liburu batekin lotuta badira ( `LiburariBuruz` eremua barne duen egoera pertsonalizatuko mota batekoa),
    - Datu-basean gordetako egoerei emandako erantzunak

- `Ezabatu`: Egoera bat ezabatzen du
- `Atsegin`: Sortzen du gogoko bat egoeretan
- `Partekatu`: Egoera sustatzen du aktorearen kronologian
- `Desegin`: Desegiten ditu `Atsegin` bat edo `Partekatu` bat

### Bildumak
[`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection) elementuari esker erabiltzaile baten liburuak eta zerrendak ager daitezke

#### Objektuak

- `Apala`: erabiltzaile baten liburu bilduma. By default, every user has a `to-read`, `reading`, `stop-reading` and `read` shelf which are used to track reading progress.
- `Zerrenda`: Zerrenda sortu zuen erabiltzaileaz besteko elementuak izan ditzakeen liburu-bilduma.

#### Jarduerak

- `Sortu`: Gehitu apal bat edo zerrenda bat datu-basean.
- `Ezabatu`: Ezabatu apal bat edo zerrenda bat.
- `Gehitu`: Liburu bat gehitzen du apal edo zerrenda batean.
- `Kendu`: Apal edo zerrenda batetik liburu bat ezabatzen du.

## Serializazio alternatiboa
BookWyrm-ek Activity Pub-ekin bateragarriak ez diren objektu pertsonalizatu motak (`Kritika`, `Iruzkina`, `Aipua`) erabiltzen dituenez, egoerak tipo estandar bihurtzen dira BookWyrm ez diren zerbitzuek bidaltzen edo ikusten dituztenean. `Kritikak`, `Artikulu` bihurtzen dira, eta `Iruzkinak` eta `Aipuak` `Ohar` bihurtzen dira, libururako esteka batekin eta erantsitako azaleko irudi batekin.

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
