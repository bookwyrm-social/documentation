- - -
Title: ActivityPub Date: 2025-04-21 Order: 1
- - -

BookWyrm utilise le protocole [ActivityPub](http://activitypub.rocks/) pour envoyer et recevoir des activités utilisateur entre des instances de BookWyrm et d’autres services qui implémentent ActivityPub, comme [Mastodon](https://joinmastodon.org/). Pour gérer les données de livres, BookWyrm utilise plusieurs extensions de types d’Activity qui ne font pas partie de la norme, mais sont interopérables avec les autres instances de BookWyrm.

To view the ActivityPub data for a BookWyrm entity (user, book, list, etc) you can usually add `.json` to the end of the URL. e.g. `https://www.example.com/user/sam.json` and see the JSON in your web browser or via an http request (e.g. using `curl`).

## Activités et Objets

### Utilisateurs et relations
Les interactions de relations entre les utilisateurs suivent la spécification standard ActivityPub.

- `Follow` : demande à recevoir les statuts d'un utilisateur et consultez leurs statuts qui ont un réglage de lecture réservée aux abonnés
- `Accept` : approuve un `Follow` et finalise la relation
- `Reject` : refuse un `Follow`
- `Block` : empêche les utilisateurs de voir les statuts de l'autre et empêche l'utilisateur bloqué de voir le profil de l'acteur
- `Update` : met à jour le profil et les paramètres d'un utilisateur
- `Delete` : désactive un utilisateur
- `Undo` : Ne plus suivre `Follow` ou Bloquer `Block`
- `Move`: communicate that a user has changed their ID and has moved to a new server. Most ActivityPub software will "follow" the user to the new identity. BookWyrm sends a notification to followers and requires them to confirm they want to follow the user to their new identity.

### Statuts
#### Types d'Object

- `Note` : Sur les services comme Mastodon, les `Note`s sont le type principal de statut. Ils contiennent un corps de message, des pièces jointes, peuvent mentionner les utilisateurs et être des réponses à des statuts de n'importe quel type. Dans BookWyrm, les `Notes` ne peuvent être créés qu'en tant que messages directs ou en tant que réponses à d'autres statuts.
- `Critique` : Une critique est un statut en réponse à un livre (indiqué par le champ `inReplyToBook`), qui a un titre, un corps et une évaluation numérique entre 0 (non évalué) et 5.
- `Comment` : Un commentaire sur un livre mentionne un livre et a un corps de message.
- `Citation` : Une citation a un corps de message, un extrait d'un livre et mentionne un livre.

#### Activities

- `Create` : sauvegarde un nouveau statut dans la base de données.

    **Remarque** : BookWyrm n'accepte les activités `Create` que si elles sont :

    - des messages directs (c'est à dire des `Note`s avec le niveau de confidentialité `direct`, qui mentionnent un utilisateur local),
    - liées à un livre (d'un type de statut personnalisé qui inclut le champ `inReplyToBook`),
    - en réponse à des statuts existants enregistrés dans la base de données

- `Delete` : Supprime un statut
- `Like` : Crée un favori sur le statut
- `Announce` : Booste (reposte) le statut dans la chronologie de l'acteur
- `Undo` : Inverse un `Like` ou un `Announce`

### Collections
Les livres et listes d'un utilisateurs sont représentés par [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objects

- `Shelf` : Collection de livres d'un utilisateur. By default, every user has a `to-read`, `reading`, `stop-reading` and `read` shelf which are used to track reading progress.
- `List` : Une collection de livres qui peut avoir des éléments contribués par des utilisateurs autres que celui qui a créé la liste.

#### Activities

- `Create` : sauvegarde une étagère ou une liste dans la base de données.
- `Delete` : Supprime une étagère ou une liste.
- `Add` : Ajoute un livre à une étagère ou une liste.
- `Remove` : Supprime un livre d'une étagère ou d'une liste.

## Sérialisation alternative
Parce que BookWyrm utilise des types d'objets personnalisés (`Review`, `Comment`, `Quotation`) qui ne sont pas pris en charge par ActivityPub, les statuts sont transformés en types standards lorsqu'ils sont envoyés ou vus par des services non-BookWyrm. Les `Review`s sont converties en `Article`s, les `Comment`s et `Quotation`s sont convertis en `Note`s, avec un lien vers le livre et l'image de couverture en pièce jointe.

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
