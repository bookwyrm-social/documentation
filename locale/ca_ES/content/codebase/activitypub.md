- - -
Title: ActivityPub Date: 2025-04-21 Order: 1
- - -

BookWyrm utiltza el protocol [ActivityPub](http://activitypub.rocks/) per enviar i rebre activitat d'usuari entre diferents instàncies de BookWyrm i altres serveis que implementen ActivityPub, com [Mastodon](https://joinmastodon.org/). Per manegar les dades d'un llibre, BookWyrm té molts tipus d'activitats que no formen parts de l'estàndard, però que altres instàncies de BookWyrm poden llegir.

Per veure les dades ActivityPub d'una entitat a BookWyrm (usuari, llibre, llista, etc.) pots afegir `.json` al final de l'URL. per exemple. `https://www.example.com/user/sam.json` i veure el resultat JSON al teu navegador o a través d'una petició http (per exemple, utilitzant `curl`).

## Activitats i Objectes

### Usuaris i relacions
Les interaccions entre usuaris segueixen les especificacions estandars d'ActivityPub.

- `Segueix`: sol·licita rebre les entrades d'un usuari i veure aquelles que només són accessibles per part dels seguidors
- `Accepta`: aprova un `Segueix` i finalitza la sol·licitud
- `Refusa`: denega un `Segueix`
- `Bloqueja`: impossibilita als usuaris que es vegin mútuament les entrades i l'accés de la persona bloquejada al perfil de qui l'ha bloquejat
- `Actualitza`: actualitza el perfil i configuració de l'usuari
- `Elimina`: desactiva l'usuari
- `Desfés`: desfà un `Segueix` o `Bloqueja`
- `Moure`: informa que un usuari ha canviat el seu ID i s'ha mogut a un nou servidor. La majoria del software que utilitza ActivityPub "seguirà" a l'usuari a la nova identitat. BookWyrm envia una notificació als seguidors i demana de confirmar que volen seguir l'usuari en la seva nova identitat.

### Estats
#### Tipus d'objecte

- `Nota`: En serveis com Mastodon, les `Notes` són el tipus principal d'estat. Contenen un cos del missatge, adjunts, poden fer menció a usuaris i, ser respostes altres tipus d'estat. Dins de BookWyrm, les `Notes` només poden ser creades com a missatges directes o com a respostes a altres estats.
- `Ressenya`: Una ressenya és un estat en resposta a un llibre (indicat pel camp `inReplyToBook`), el qual conté títol, cos i, una valoració numèrica entre 0 (no valorat) i 5.
- `Comentari`: Un comentari en un llibre fa referència a un llibre i té un cos del missatge.
- `Cita`: Una cita té un cos del missatge, un extracte d'un llibre i, menciona un llibre.

#### Activitats

- `Crear`: guarda un nou estat a la base de dades.

    **Nota**: BookWyrm nomès accepta activitats de `Crear` si són:

    - Missatges directes (per exemple `Notes` amb el nivell de privacitat `directe`, el qual menciona a un usuari local),
    - Relacionat amb un llibre (amb un estat personalitzat que inclogui el camp `inReplyToBook`),
    - Respostes a estats ja existents guardats a la base de dades

- `Eliminar`: Elimina un estat
- `M'agrada`: Crea un favorit a l'estat
- `Anunci`: Destaca l'estat a la línia de temps de l'actor
- `Desfer`: Desfà un `M'agrada` o un `Anunci`

### Col·leccions
Els llibres i llistats de l'usuari son representats per [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objectes

- `Prestatge`: Una col·lecció de llibres d'un usuari. By default, every user has a `to-read`, `reading`, `stop-reading` and `read` shelf which are used to track reading progress.
- `Llista`: Una col·lecció de llibres que pot contenir contribucions realitzades per altres usuaris a més a més de qui ha creat la llista.

#### Activitats

- `Create`: Afegeix un prestatge o llista a la base de dades.
- `Delete`: Elimina un prestatge o llista.
- `Add`: Afegeix un llibre al prestatge o llista.
- `Remove`: Elimina un llibre del prestatge o llista.

## Serialitzacions alternatives
Degut a que BookWyrm fa ús de tipus d'objectes personalitzats (`Ressenya`, `Comentari`, `Cita`) que no són reconeguts per l'ActiityPub, els estats són transformats a tipus estàndard quan s'envien o són llegits per serveis que no són BookWyrm. `Ressenyes` són convertides en `Article`s i, `Comentari`s i `Cites` són transformats en `Notes`, amb un enllaç al llibre i a la imatge de portada adjunta.

Això podria canviar en un futur a favor del [extended Object types](https://www.w3.org/TR/activitystreams-core/#fig-following-is-an-example-object-that-uses-the-id-and-type-properties-to-express-the-global-identifier-and-object-type) més conforme amb ActivityPub, llistat amb els principals tipus a ActivityPub.

## Making ActivityPub-aware models

El mode que BookWyrm envia i rep objectes ActivityPub pot ser confús per als desenvolupadors que són nous a BookWyrm. It is mostly controlled by:

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
