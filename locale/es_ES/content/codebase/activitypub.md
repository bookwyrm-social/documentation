- - -
Título: ActivityPub Fecha: 2021-04 Pedido: 1
- - -

BookWyrm utiliza el protocolo [ActivityPub](http://activitypub.rocks/) para enviar y recibir actividad de usuario entre otras instancias de BookWyrm y otros servicios que implementan ActivityPub, como [Mastodon](https://joinmastodon.org/). Para manejar los datos de los libros, BookWyrm tiene un puñado de tipos de actividades extendidas que no son parte del estándar, pero son legibles para otras instancias de BookWyrm.

## Actividades y objetos

### Usuarios y relaciones
Las interacciones de las relaciones de usuario siguen la especificación estándar de ActivityPub.

- `Seguir`: solicita recibir estados de un usuario y ver sus estados que tienen la opción de privacidad «sólo seguidores» activado
- `Aceptar`: aprueba la acción `Seguir` y finaliza la relación
- `Rechazar`: deniega una acción `Seguir`
- `Bloquear`: evita que los usuarios vean los estados de los demás, y evita que el usuario bloqueado vea el perfil del actor
- `Actualizar`: actualiza el perfil y la configuración de un usuario
- `Eliminar`: desactiva un usuario
- `Undo`: reverses a `Follow` or `Block`

### Statuses
#### Object types

- `Note`: On services like Mastodon, `Note`s are the primary type of status. They contain a message body, attachments, can mention users, and be replies to statuses of any type. Within BookWyrm, `Note`s can only be created as direct messages or as replies to other statuses.
- `Review`: A review is a status in response to a book (indicated by the `inReplyToBook` field), which has a title, body, and numerical rating between 0 (not rated) and 5.
- `Comment`: A comment on a book mentions a book and has a message body.
- `Quotation`: A quote has a message body, an excerpt from a book, and mentions a book.


#### Activities

- `Create`: saves a new status in the database.

   **Note**: BookWyrm only accepts `Create` activities if they are:

   - Direct messages (i.e., `Note`s with the privacy level `direct`, which mention a local user),
   - Related to a book (of a custom status type that includes the field `inReplyToBook`),
   - Replies to existing statuses saved in the database
- `Delete`: Removes a status
- `Like`: Creates a favorite on the status
- `Announce`: Boosts the status into the actor's timeline
- `Undo`: Reverses a `Like` or `Announce`

### Collections
User's books and lists are represented by [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objects

- `Shelf`: A user's book collection. By default, every user has a `to-read`, `reading`, and `read` shelf which are used to track reading progress.
- `List`: A collection of books that may have items contributed by users other than the one who created the list.

#### Activities

- `Create`: Adds a shelf or list to the database.
- `Delete`: Removes a shelf or list.
- `Add`: Adds a book to a shelf or list.
- `Remove`: Removes a book from a shelf or list.


## Alternative Serialization
Because BookWyrm uses custom object types (`Review`, `Comment`, `Quotation`) that aren't supported by ActivityPub, statuses are transformed into standard types when sent to or viewed by non-BookWyrm services. `Review`s are converted into `Article`s, and `Comment`s and `Quotation`s are converted into `Note`s, with a link to the book and the cover image attached.
