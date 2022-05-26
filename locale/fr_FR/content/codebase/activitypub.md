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

- `Note` : Sur les services comme Mastodon, les `Note`s sont le type principal de statut. Ils contiennent un corps de message, des pièces jointes, peuvent mentionner les utilisateurs et être des réponses à des statuts de n'importe quel type. Dans BookWyrm, les `Note`s ne peuvent être créés qu'en tant que messages directs ou en tant que réponses à d'autres statuts.
- `Review` : Une critique est un statut en réponse à un livre (indiqué par le champ `inReplyToBook` ), qui a un titre, un corps et une note numérique entre 0 (non évalué) et 5.
- `Comment` : Un commentaire sur un livre mentionne un livre et a un corps de message.
- `Quotation` : Une citation a un corps de message, un extrait d'un livre et mentionne un livre


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

- `Shelf` : Collection de livres d'un utilisateur. By default, every user has a `to-read`, `reading`, and `read` shelf which are used to track reading progress.
- `List`: A collection of books that may have items contributed by users other than the one who created the list.

#### Activities

- `Create`: Adds a shelf or list to the database.
- `Delete`: Removes a shelf or list.
- `Add`: Adds a book to a shelf or list.
- `Remove`: Removes a book from a shelf or list.


## Alternative Serialization
Because BookWyrm uses custom object types (`Review`, `Comment`, `Quotation`) that aren't supported by ActivityPub, statuses are transformed into standard types when sent to or viewed by non-BookWyrm services. `Review`s are converted into `Article`s, and `Comment`s and `Quotation`s are converted into `Note`s, with a link to the book and the cover image attached.
