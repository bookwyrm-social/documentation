- - -
Title: ActivityPub Date: 2021-04-20 Order: 1
- - -

BookWyrm utiltza el protocol [ActivityPub](http://activitypub.rocks/) per enviar i rebre activitat d'usuari entre diferents instàncies de BookWyrm i altres serveis que implementen ActivityPub, com [Mastodon](https://joinmastodon.org/). To handle book data, BookWyrm has a handful of extended Activity types which are not part of the standard, but are legible to other BookWyrm instances.

## Activities and Objects

### Users and relationships
User relationship interactions follow the standard ActivityPub spec.

- `Follow`: request to receive statuses from a user, and view their statuses that have followers-only privacy
- `Accept`: approves a `Follow` and finalizes the relationship
- `Reject`: denies a `Follow`
- `Block`: prevent users from seeing one another's statuses, and prevents the blocked user from viewing the actor's profile
- `Update`: updates a user's profile and settings
- `Delete`: deactivates a user
- `Undo`: reverses a `Follow` or `Block`

### Statuses
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

- `Shelf`: A user's book collection. By default, every user has a `to-read`, `reading`, and `read` shelf which are used to track reading progress.
- `List`: A collection of books that may have items contributed by users other than the one who created the list.

#### Activitats

- `Create`: Afegeix un prestatge o llista a la base de dades.
- `Delete`: Elimina un prestatge o llista.
- `Add`: Afegeix un llibre al prestatge o llista.
- `Remove`: Elimina un llibre del prestatge o llista.


## Serialitzacions alternatives
Because BookWyrm uses custom object types (`Review`, `Comment`, `Quotation`) that aren't supported by ActivityPub, statuses are transformed into standard types when sent to or viewed by non-BookWyrm services. `Review`s are converted into `Article`s, and `Comment`s and `Quotation`s are converted into `Note`s, with a link to the book and the cover image attached.
