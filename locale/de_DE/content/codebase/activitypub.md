- - -
Titel: ActivityPub Datum: 2021-04-20 Bestellung: 1
- - -

BookWyrm verwendet das [ActivityPub](http://activitypub.rocks/)-Protokoll, um Benutzeraktivitäten zwischen anderen BookWyrm-Instanzen und anderen Diensten zu senden und zu empfangen, die ActivityPub implementieren, wie [Mastodon](https://joinmastodon.org/). Um Buchdaten zu behandeln, hat BookWyrm eine Handvoll erweiterter Aktivitätstypen, die nicht zum Standard gehören, aber nur für andere BookWyrm-Instanzen lesbar sind.

## Aktivitäten und Objekte

### Benutzer und Beziehungen
Benutzerbeziehungsinteraktionen folgen der Standard ActivityPub Spezifikation.

- `Folgen`: Bitte, um den Status eines Benutzers zu erhalten und anzusehen, die die Privatsphäre auf nur Follower haben
- `Akzeptieren`: genehmigt `Folgen` und erstellt die Beziehung
- `Ablehnen`: verweigert `Folgen`
- `Block`: prevent users from seeing one another's statuses, and prevents the blocked user from viewing the actor's profile
- `Update`: Aktualisiert das Profil und die Einstellungen eines Benutzers
- `Löschen`: Deaktiviert einen Benutzer
- `Undo`: reverses a `Follow` or `Block`

### Status
#### Objekttypen

- `Note`: On services like Mastodon, `Note`s are the primary type of status. They contain a message body, attachments, can mention users, and be replies to statuses of any type. Within BookWyrm, `Note`s can only be created as direct messages or as replies to other statuses.
- `Review`: A review is a status in repsonse to a book (indicated by the `inReplyToBook` field), which has a title, body, and numerical rating between 0 (not rated) and 5.
- `Kommentar`: Ein Kommentar zu einem Buch erwähnt ein Buch und hat einen Text.
- `Zitat`: Ein Zitat hat einen Text, einen Auszug aus einem Buch und erwähnt ein Buch


#### Aktivitäten

- `Erstellen`: Speichert einen neuen Status in der Datenbank.

   **Hinweis**: BookWyrm akzeptiert nur `Erstellen`-Aktivitäten, wenn sie sind:

   - Direktnachrichten (d.h. `Hinweis`e mit der Datenschutzstufe `direkt`, welche einen lokalen Benutzer erwähnen),
   - Verbunden mit einem Buch (eines benutzerdefinierten Statusstyps, der das Feld `inReplyToBook` enthält),
   - Antworten auf existierende Status in der Datenbank
- `Löschen`: Entfernt einen Status
- `Gefällt`: Erstellt einen Favoriten für den Status
- `Ankündigung`: Teilt den Status in der Zeitleiste des Akteurs
- `Rückgängig`: Reversiert `Gefällt` oder `Ankündigung`

### Sammlungen
Bücher und Listen von Benutzern werden durch [`Sortierte Sammlung`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection) repräsentiert

#### Objekte

- `Regal`: Buchsammlung eines Benutzers. By default, every user has a `to-read`, `reading`, and `read` shelf which are used to track reading progress.
- `List`: A collection of books that may have items contributed by users other than the one who created the list.

#### Aktivitäten

- `Create`: Adds a shelf or list to the database.
- `Delete`: Removes a shelf or list.
- `Add`: Adds a book to a shelf or list.
- `Remove`: Removes a book from a shelf or list.


## Alternative Serialisierung
Because BookWyrm uses custom object types (`Review`, `Comment`, `Quotation`) that aren't supported by ActivityPub, statuses are transformed into standard types when sent to or viewed by non-BookWyrm services. `Review`s are converted into `Article`s, and `Comment`s and `Quotation`s are converted into `Note`s, with a link to the book and the cover image attached.
