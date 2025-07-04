- - -
Title: ActivityPub Date: 2025-04-21 Order: 1
- - -

BookWyrm korzysta z protokołu [ActivityPub](http://activitypub.rocks/) do wysyłania i odbierania aktywności użytkownika pomiędzy instancjami BookWyrm oraz innymi usługami, które korzystają z ActivityPub, takimi jak [Mastodon](https://joinmastodon.org/). Do obsługi danych na temat książek BookWyrm posiada kilka rozszerzonych typów Aktywności, które nie są częścią standardu, ale są czytelne dla innych instancji BookWyrm.

To view the ActivityPub data for a BookWyrm entity (user, book, list, etc) you can usually add `.json` to the end of the URL. e.g. `https://www.example.com/user/sam.json` and see the JSON in your web browser or via an http request (e.g. using `curl`).

## Aktywności i obiekty

### Użytkownicy i stosunki
Interakcje stosunków między użytkownikami są zgodne ze specyfikacją ActivityPub.

- `Obserwuj`: poproś o otrzymywanie statusów od użytkownika oraz przeglądanie ich statusów, które mogą wyświetlić tylko obserwujący
- `Akceptuj`: zatwierdza `Obserwowanie` i nawiązuje stosunek
- `Odmów`: odrzuca `Obserwowanie`
- `Zablokuj`: uniemożliwia użytkownikowi wzajemne wyświetlanie statusów oraz uniemożliwia wyświetlanie profilu
- `Aktualizuj`: aktualizuje profil i ustawienia użytkownika
- `Usuń`: dezaktywuje użytkownika
- `Cofnij`: anuluje `Obserwowanie` lub `Zablokowanie`
- `Move`: communicate that a user has changed their ID and has moved to a new server. Most ActivityPub software will "follow" the user to the new identity. BookWyrm sends a notification to followers and requires them to confirm they want to follow the user to their new identity.

### Statusy
#### Typy obiektów

- `Notatka`: W usługach takich jak Mastodon, `Notatki` są podstawowym typem statusów. Zawierają treść wiadomości, załączniki, wzmianki o użytkownikach oraz są odpowiedziami na inne statusy dowolnego typu. Within BookWyrm, `Note`s can only be created as direct messages or as replies to other statuses.
- `Review`: A review is a status in response to a book (indicated by the `inReplyToBook` field), which has a title, body, and numerical rating between 0 (not rated) and 5.
- `Komentarz`: komentarz do książki wspomina o książce i zawiera treść.
- `Quotation`: A quote has a message body, an excerpt from a book, and mentions a book.

#### Aktywności

- `Tworzenie`: zapisuje nowy status w bazie danych.

    **Uwaga**: BookWyrm akceptuje aktywności `Tworzenie`, tylko jeśli:

    - Są wiadomościami bezpośrednimi (np. `Notatki` z ustawieniem `bezpośrednie`, które wspominają lokalnego użytkownika),
    - Related to a book (of a custom status type that includes the field `inReplyToBook`),
    - Replies to existing statuses saved in the database

- `Usuń`: Usuwa status
- `Polub`: Dodaje reakcję do statusu
- `Ogłoś`: Promuje status do osi czasu podmiotu
- `Cofnij`: Anuluje `Polub` lub `Ogłoś`

### Kolekcje
Listy oraz książki użytkownika są reprezentowane przez [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Obiekty

- `Półka`: Kolekcja książek użytkownika. By default, every user has a `to-read`, `reading`, `stop-reading` and `read` shelf which are used to track reading progress.
- `Lista`: Kolekcja książek, która może zawierać elementy od użytkowników innych niż jej autor.

#### Aktywności

- `Utwórz`: Dodaje półkę lub listę do bazy danych.
- `Usuń`: Usuwa półkę lub listę.
- `Dodaj`: Dodaje książkę na półkę lub do listy.
- `Usuń`: Usuwa książkę z półki lub listy.

## Alternatywna serializacja
BookWyrm wykorzystuje niestandardowe typy obiektów (`Recenzja`, `Komentarz`, `Cytat`), które nie są obsługiwane przez ActivityPub, dlatego statusy są zamieniane na standardowe typy, gdy są wysyłane do lub wyświetlane w usługach poza BookWyrm. `Recenzja` jest konwertowana na `Artykuł`, a `Komentarz` oraz `Cytat` są konwertowane na `Notatki` z odnośnikiem do książki oraz załączonym obrazem okładki.

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
