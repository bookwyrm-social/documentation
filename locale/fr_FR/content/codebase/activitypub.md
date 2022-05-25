BookWyrm utilise le protocole [ActivityPub](http://activitypub.rocks/) pour envoyer et recevoir des activités utilisateur entre des instances de BookWyrm et d’autres services qui implémentent ActivityPub, comme [Mastodon](https://joinmastodon.org/). Pour gérer les données de livres, BookWyrm utilise plusieurs extensions de types d’Activity qui ne font pas partie de la norme, mais sont interopérables avec les autres instances de BookWyrm.

## Activités et Objets

### Utilisateurs et relations
Les interactions de relations entre les utilisateurs suivent la spécification ActivityPub standard.

- `Follow` : demande à recevoir les statuts d'un utilisateur et consultez leurs statuts qui ont un réglage de lecture réservée aux abonnés
- `Accept` : approuve un `Follow` et finalise la relation
- `Reject` : refuse un `Follow`
- `Block` : empêche les utilisateurs de voir les statuts de l'autre et empêche l'utilisateur bloqué de voir le profil de l'acteur
- `Update` : met à jour le profil et les paramètres d'un utilisateur
- `Delete` : désactive un utilisateur
- `Undo` : inverse un `Follow` ou un `Block`

### Statuts
#### Types d'Object

- `Note` : Sur les services comme Mastodon, les `Note`s sont le type principal de statut. They contain a message body, attachments, can mention users, and be replies to statuses of any type. Within BookWyrm, `Note`s can only be created as direct messages or as replies to other statuses.
- `Review`: A review is a status in repsonse to a book (indicated by the `inReplyToBook` field), which has a title, body, and numerical rating between 0 (not rated) and 5.
- `Comment`: A comment on a book mentions a book and has a message body.
- `Quotation`: A quote has a message body, an excerpt from a book, and mentions a book


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
