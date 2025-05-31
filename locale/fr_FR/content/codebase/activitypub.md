- - -
Title: ActivityPub Date: 2021-04-20 Order: 1
- - -

BookWyrm utilise le protocole [ActivityPub](http://activitypub.rocks/) pour envoyer et recevoir des activités utilisateur entre des instances de BookWyrm et d’autres services qui implémentent ActivityPub, comme [Mastodon](https://joinmastodon.org/). Pour gérer les données de livres, BookWyrm utilise plusieurs extensions de types d’Activity qui ne font pas partie de la norme, mais sont interopérables avec les autres instances de BookWyrm.

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

- `Shelf` : Collection de livres d'un utilisateur. Par défaut, chaque utilisateur a les étagères `to-read` (à lire), `reading` (en cours de lecture), et `read` (livres lus), qui sont utilisées pour suivre la progression de la lecture.
- `List` : Une collection de livres qui peut avoir des éléments contribués par des utilisateurs autres que celui qui a créé la liste.

#### Activities

- `Create` : sauvegarde une étagère ou une liste dans la base de données.
- `Delete` : Supprime une étagère ou une liste.
- `Add` : Ajoute un livre à une étagère ou une liste.
- `Remove` : Supprime un livre d'une étagère ou d'une liste.


## Sérialisation alternative
Parce que BookWyrm utilise des types d'objets personnalisés (`Review`, `Comment`, `Quotation`) qui ne sont pas pris en charge par ActivityPub, les statuts sont transformés en types standards lorsqu'ils sont envoyés ou vus par des services non-BookWyrm. Les `Review`s sont converties en `Article`s, les `Comment`s et `Quotation`s sont convertis en `Note`s, avec un lien vers le livre et l'image de couverture en pièce jointe.
