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
- `Deshacer`: deshace un `Seguir` o un `Bloquear`

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

- `Estantería`: la colección de libros de une usuarie. Por defecto, cada usuarie tiene las estanterías `para leer`, `leyendo actualmente` y `leído`, las cuales sirven para llevar un registro del progreso de lectura.
- `Lista`: una colección de libros a la que pueden contribuir otres usuaries aunque no sean quienes han creado la lista.

#### Actividad

- `Crear`: añade una estantería o una lista a la base de datos.
- `Eliminar`: suprime una estantería o una lista.
- `Añadir`: añade un libro a una estantería o lista.
- `Eliminar`: quita un libro de una estantería o lista.


## Alternative Serialization
Because BookWyrm uses custom object types (`Review`, `Comment`, `Quotation`) that aren't supported by ActivityPub, statuses are transformed into standard types when sent to or viewed by non-BookWyrm services. `Review`s are converted into `Article`s, and `Comment`s and `Quotation`s are converted into `Note`s, with a link to the book and the cover image attached.
