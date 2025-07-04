- - -
Title: ActivityPub Date: 2025-04-21 Order: 1
- - -

BookWyrm utiliza el protocolo [ActivityPub](http://activitypub.rocks/) para enviar y recibir actividad de usuario entre otras instancias de BookWyrm y otros servicios que implementan ActivityPub, como [Mastodon](https://joinmastodon.org/). Para manejar los datos de los libros, BookWyrm tiene un puñado de tipos de actividades extendidas que no son parte del estándar, pero son legibles para otras instancias de BookWyrm.

To view the ActivityPub data for a BookWyrm entity (user, book, list, etc) you can usually add `.json` to the end of the URL. e.g. `https://www.example.com/user/sam.json` and see the JSON in your web browser or via an http request (e.g. using `curl`).

## Actividades y objetos

### Usuarios y relaciones
Las interacciones de las relaciones de usuario siguen la especificación estándar de ActivityPub.

- `Seguir`: solicita recibir estados de un usuario y ver sus estados que tienen la opción de privacidad «sólo seguidores» activado
- `Aceptar`: aprueba la acción `Seguir` y finaliza la relación
- `Rechazar`: deniega una acción `Seguir`
- `Bloquear`: evita que los usuarios vean los estados de los demás, y evita que el usuario bloqueado vea el perfil del actor
- `Actualizar`: actualiza el perfil y la configuración de un usuario
- `Eliminar`: desactiva un usuario
- `Deshacer`: deshace un `Seguir` o un `Bloquear`
- `Move`: communicate that a user has changed their ID and has moved to a new server. Most ActivityPub software will "follow" the user to the new identity. BookWyrm sends a notification to followers and requires them to confirm they want to follow the user to their new identity.

### Estados
#### Tipos de objetos

- `Nota`: en servicios como Mastodon, las `Nota`s son el tipo de estado principal. Contienen el cuerpo de un mensaje, pueden tener archivos adjuntos, mencionar a otres usuaries y ser una respuesta a cualquier tipo de estado. En BookWyrm, las `Nota`s pueden crearse únicamente como mensajes directos o como respuestas a otros estados.
- `Reseña`: una reseña es un estado relacionado con un libro (indicado por el campo `inReplyToBook`) que posee un título, un cuerpo y una valoración numérica entre 0 (no valorado) y 5.
- `Comentario`: un comentario sobre un libro menciona al libro y tiene un cuerpo del mensaje.
- `Cita`: Una cita posee un cuerpo del mensaje, un extracto de un libro y menciona al libro.

#### Actividad

- `Crear`: guarda un nuevo estado en la base de datos.

    **Observación**: BookWyrm solo acepta `Crear` una actividad si:

    - Es un mensaje directo (como `Nota`s con `directo` como nivel de privacidad, que menciona a une usuarie local),
    - Está relacionado con un libro (es un tipo de estado personalizado que incluye el campo `inReplyToBook`),
    - Responde a estados existentes guardados en la base de datos

- `Eliminar`: suprime un estado
- `Me gusta`: marca el estado como favorito
- `Difundir`: impulsa el estado en la línea de tiempo de quien realiza la acción
- `Deshacer`: deshacer el `Me gusta` o el `Difundir`

### Colecciones
Los libros y listas de une usuarie están representados por [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objetos

- `Estantería`: la colección de libros de une usuarie. By default, every user has a `to-read`, `reading`, `stop-reading` and `read` shelf which are used to track reading progress.
- `Lista`: una colección de libros a la que pueden contribuir otres usuaries aunque no sean quienes han creado la lista.

#### Actividad

- `Crear`: añade una estantería o una lista a la base de datos.
- `Eliminar`: suprime una estantería o una lista.
- `Añadir`: añade un libro a una estantería o lista.
- `Eliminar`: quita un libro de una estantería o lista.

## Serialización alternativa
Puesto que BookWyrm emplea tipos de objetos personalizados (`Reseña`, `Comentario`, `Cita`) que no son compatibles con ActivityPub, los estados son transformados en tipos estándar cuando se envían a o se ven desde servicios diferentes a BookWyrm. Las `Reseñas`s se convierten en `Artículo`s y los `Comentario`s y las `Cita`s se convierten en `Nota`s, con un enlace al libro y una imagen de portada adjunta.

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
