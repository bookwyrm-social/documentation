- - -
Title: ActivityPub Date: 2025-04-21 Order: 1
- - -

BookWyrm uses the [ActivityPub](http://activitypub.rocks/) protocol to send and receive user activity between other BookWyrm instances and other services that implement ActivityPub, like [Mastodon](https://joinmastodon.org/). To handle book data, BookWyrm has a handful of extended Activity types which are not part of the standard, but are legible to other BookWyrm instances.

To view the ActivityPub data for a BookWyrm entity (user, book, list, etc) you can usually add `.json` to the end of the URL. e.g. `https://www.example.com/user/sam.json` and see the JSON in your web browser or via an http request (e.g. using `curl`).

## Activities and Objects

### Nariai ir santykiai
Narių santykių sąveika atitinka standartinę „ActivityPub“ specifikaciją.

- `Sekti`: užklausa gauti nario būsenas ir peržiūrėti tas, kurios turi tik stebėtojų privatumą
- `Patvirtinti`: patvirtina kvietimą `Sekti` ir finalizuoja santykį
- `Atmesti`: atmeta prašymą `Sekti`
- `Blokuoti`: neleisti nariams matyti vienas kito būsenų ir neleisti užblokuotam nariui matyti profilio
- `Atnaujinti`: atnaujina nario paskyrą ir nustatymus
- `Ištrinti`: išaktyvuoja narį
- `Grąžinti į pradinę būseną`: pakeičia `Sekimo` arba `Blokavimo` būseną
- `Move`: communicate that a user has changed their ID and has moved to a new server. Most ActivityPub software will "follow" the user to the new identity. BookWyrm sends a notification to followers and requires them to confirm they want to follow the user to their new identity.

### Būsenos
#### Objekto tipai

- `Užrašas`: tokiose paslaugose, kaip „Mastodon“, `Užrašas` yra pirminis būsenos tipas. Juose yra žinutė, prisegtukai, galima minėti narius arba atsakyti į bet kokio tipo būsenas. „BookWyrm“ `Užrašus` galima sukurti kaip tiesiogines žinutes arba atsakymus į kitas būsenas.
- `Review`: A review is a status in response to a book (indicated by the `inReplyToBook` field), which has a title, body, and numerical rating between 0 (not rated) and 5.
- `Komentaras`: knygos komentare minima knyga ir yra pranešimo tekstas.
- `Quotation`: A quote has a message body, an excerpt from a book, and mentions a book.

#### Veiklos

- `Sukurti`: išsaugo naują būseną duomenų bazėje.

    **Užrašas**: „BookWyrm“ priima tik `Sukūrimo` veiklas, jei jos:

    - Tiesioginės žinutės (pvz., `Užrašas`, kurio privatumo lygis `tiesioginis` ir minintis vietos narį);
    - Susiję su knyga (būsenos tipas, kuriame yra laukelis `inReplyToBook`);
    - Atsako į duomenų bazėje išsaugotas būsenas

- `Ištrinti`: ištrina būseną
- `Patinka`: pažymi, kad būsena patinka
- `Pranešimas`: iškelia būseną į laiko juostą
- `Grąžinti į pradinę būseną`: pakeičia `Patinka` arba `Pranešimo` būseną

### Kolekcijos
Naudotojo knygas ir sąrašus reprezentuoja [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objektai

- `Lentyna`: nario knygų kolekcija. By default, every user has a `to-read`, `reading`, `stop-reading` and `read` shelf which are used to track reading progress.
- `Sąrašas`: knygų rinkinys, kuriame gali būti kitų narių knygų, o ne tik sąrašą sukūrusių narių.

#### Veiklos

- `Sukurti`: prideda lentyną arba sąrašą į duomenų bazę.
- `Ištrinti`: pašalina lentyną arba sąrašą.
- `Pridėti`: prideda knygą į lentyną arba sąrašą.
- `Pašalinti`: pašalina knygą iš lentynos arba sąrašo.

## Alternatyvus serializavimas
Kadangi „BookWyrm“ naudoja pasirinktinius objektų tipus (`Apžvalga`, `Komentaras`, `Citavimas`), kurių „ActivityPub“ nepalaiko, siunčiamos būsenos transformuojamos į standartinius tipus, kai siunčia arba peržiūri ne „BookWyrm“. `Apžvalga` paverčiama `Straipsniu`, o `Komentaras` ir `Citavimas` paverčiami `Užrašu` su nuoroda į knygą ir prisegtą viršelio nuotrauką.

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
