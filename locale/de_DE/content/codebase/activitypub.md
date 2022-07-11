- - -
Title: ActivityPub Date: 2021-04-20 Order: 1
- - -

BookWyrm verwendet das [ActivityPub](http://activitypub.rocks/)-Protokoll, um Benutzeraktivitäten zwischen anderen BookWyrm-Instanzen und anderen Diensten zu senden und zu empfangen, die ActivityPub implementieren, wie [Mastodon](https://joinmastodon.org/). Um Buchdaten zu behandeln, hat BookWyrm eine Handvoll erweiterter Aktivitätstypen, die nicht zum Standard gehören, aber nur für andere BookWyrm-Instanzen lesbar sind.

## Aktivitäten und Objekte

### Benutzer und Beziehungen
Benutzerbeziehungsinteraktionen folgen der Standard ActivityPub Spezifikation.

- `Folgen`: Bitte, um den Status eines Benutzers zu erhalten und anzusehen, die die Privatsphäre auf nur Follower haben
- `Akzeptieren`: genehmigt `Folgen` und erstellt die Beziehung
- `Ablehnen`: verweigert `Folgen`
- `Blocken`: verhindert, dass Benutzer einander Status ansehen und verhindert, dass der blockierte Benutzer das Profil des Akteurs ansieht
- `Update`: Aktualisiert das Profil und die Einstellungen eines Benutzers
- `Löschen`: Deaktiviert einen Benutzer
- `Rückgängig`: Reversiert `Folgen` oder `Blocken`

### Status
#### Objekttypen

- `Notiz`: Bei Diensten wie Mastodon, ist `Notiz`en der primäre Typ des Status. Sie enthalten einen Text, Anhänge, können Benutzer erwähnen und Antworten auf Status jeder Art sein. In BookWyrm können `Notiz`en nur als direkte Nachrichten oder als Antworten auf andere Status erstellt werden.
- `Rezension`: Eine Rezension ist ein Status in Antwort auf ein Buch (angezeigt durch das `inReplyToBook`-Feld), der einen Titel, Text und eine numerische Bewertung zwischen 0 (nicht bewertet) und 5 hat.
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

- `Regal`: Buchsammlung eines Benutzers. Standardmäßig hat jeder Benutzer ein `zu lesen`, `liest`, und `gelesen` Regal, die verwendet werden, um den Lesefortschritt zu verfolgen.
- `Liste`: Eine Sammlung von Büchern, die möglicherweise von anderen Benutzern als derjenige, der die Liste erstellt hat, beigetragen haben.

#### Aktivitäten

- `Erstellen`: Fügt der Datenbank ein Regal oder eine Liste hinzu.
- `Löschen`: Entfernt ein Regal oder eine Liste.
- `Hinzufügen`: Fügt ein Buch zu einem Regal oder einer Liste hinzu.
- `Entfernen`: Entfernt ein Buch aus einem Regal oder einer Liste.


## Alternative Serialisierung
Weil BookWyrm eigene Objekttypen (`Rezension`, `Kommentar`, `Zitat`) benutzt, die nicht von ActivityPub unterstützt werden, werden Status in Standardtypen umgewandelt, wenn sie an nicht-BookWyrm-Dienste gesendet oder angezeigt werden. `Rezension`en werden in `Artikel` umgewandelt und `Kommentar`s und `Zitat`s werden in `Notiz`s konvertiert mit einem Link auf das Buch und das Titelbild wird angehängt.
