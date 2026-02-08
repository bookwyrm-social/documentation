- - -
Title: ActivityPub Date: 2025-04-21 Order: 1
- - -

BookWyrm verwendet das [ActivityPub](http://activitypub.rocks/)-Protokoll, um Benutzer*innenaktivitäten zwischen anderen BookWyrm-Instanzen und anderen Diensten, die ActivityPub implementieren (wie [Mastodon](https://joinmastodon.org/)), zu senden und zu empfangen. Um Buchdaten zu handhaben, hat BookWyrm eine Handvoll erweiterter Aktivitätstypen, die nicht zum Standard gehören, aber für andere BookWyrm-Instanzen lesbar sind.

Um die AktivityPub-Daten zu einer BookWyrm-Entität (Nutzer\*in, Buch, Liste, etc.) einzusehen, kannst du der URL die Endung `.json` anfügen. Beispiel: `https://www.example.com/user/sam.json`. Das JSON kannst du in deinem Browser ansehen oder mittels HTTP-Request anfragen (z. B. mit `curl`).

## Aktivitäten und Objekte

### Benutzer*innen und Beziehungen
Benutzer*innenbeziehungsinteraktionen folgen der Standard ActivityPub Spezifikation.

- `Folgen`: Anfrage, die Beiträge einer Person zu erhalten und solche Beiträge einzusehen, die auf Follower*innen beschränkt sind
- `Akzeptieren`: Genehmigt `Folgen` und erstellt die Beziehung
- `Ablehnen`: Verweigert `Folgen`
- `Blocken`: Verhindert, dass Nutzer\*innen gegenseitig ihre Beiträge ansehen können. Verhindert außerdem, dass die blockierte Person das Profil der blockierenden Person ansehen kann.
- `Update`: Aktualisiert das Profil und die Einstellungen eine*r Benutzer*in
- `Löschen`: Deaktiviert eine*n Benutzer*in
- `Rückgängig`: Nimmt `Folgen` oder `Blocken` zurück
- `Umziehen`: Kommuniziert, dass ein*e Nutzer*in die ID gewechselt hat und zu einem neuen Server umgezogen ist. Die meisten ActivityPub-Plattformen werden dem neuen Konto am neuen Ort folgen. BookWyrm sendet Nutzer*innen eine Benachrichtigung und fordert sie auf, zu bestätigen, dass sie auch dem neuen Konto am neuen Ort folgen wollen.

### Beiträge
#### Objekttypen

- `Notiz`: Bei Diensten wie Mastodon, ist `Notiz`en der primäre Typ des Status. Sie enthalten einen Text, Anhänge, können Benutzer erwähnen und Antworten auf Status jeder Art sein. In BookWyrm können `Notiz`en nur als direkte Nachrichten oder als Antworten auf andere Status erstellt werden.
- `Rezension`: Eine Rezension ist ein Status, der sich auf ein Buch bezieht (angezeigt durch das `inReplyToBook`-Feld), welches einen Titel, Text sowie die numerische Bewertung auf einer Skala von 0 (keine Bewertung) bis 5 enthält.
- `Kommentar`: Ein Kommentar zu einem Buch erwähnt ein Buch und hat einen Text.
- `Zitat`: Ein Zitat enthält einen Text, einen Auszug aus dem Buch und erwähnt ein Buch.

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

- `Regal`: Buchsammlung eines Benutzers. Standardmäßig hat jede*r Nutzer*in die Regale `Leseliste`, `Liest gerade` `Aufgehört zu lesen` und `Gelesen`, die verwendet werden, um den Lesefortschritt zu verfolgen.
- `Liste`: Eine Sammlung von Büchern, zu der auch andere Personen als die, die die Liste erstellt hat, Bücher beitragen können.

#### Aktivitäten

- `Erstellen`: Fügt der Datenbank ein Regal oder eine Liste hinzu.
- `Löschen`: Entfernt ein Regal oder eine Liste.
- `Hinzufügen`: Fügt ein Buch zu einem Regal oder einer Liste hinzu.
- `Entfernen`: Entfernt ein Buch aus einem Regal oder einer Liste.

## Alternative Serialisierung
Weil BookWyrm eigene Objekttypen (`Rezension`, `Kommentar`, `Zitat`) benutzt, die nicht von ActivityPub unterstützt werden, werden Beiträge in Standardtypen umgewandelt, wenn sie an Nicht-BookWyrm-Dienste gesendet oder darin angezeigt werden. `Rezension`en werden in `Artikel` umgewandelt und `Kommentar`e und `Zitat`e werden in `Notiz`en mit einem Link zu dem Buch und dem Titelbild als Anhang konvertiert.

Das kann sich in der Zukunft zugunsten der ActivityPub-konformeren [erweiterten Objekttypen](https://www.w3.org/TR/activitystreams-core/#fig-following-is-an-example-object-that-uses-the-id-and-type-properties-to-express-the-global-identifier-and-object-type) ändern, die neben den ActivityPub-Typen aufgeführt werden.

## Modelle mit ActivityPub-Anbindung erstellen

Die Weise, auf die BookWyrm ActivityPub-Objekte sendet und empfängt, kann Entwickler\*innen verwirren, die neu bei BookWyrm sind. Sie wird hauptsächlich bestimmt durch:

* Funktionen und [Datenklassen](https://docs.python.org/3/library/dataclasses.html), die im Verzeichnis [activitypub](https://github.com/bookwyrm-social/bookwyrm/tree/main/bookwyrm/activitypub) umrissen werden
* das [ActivityPubMixin](https://github.com/bookwyrm-social/bookwyrm/blob/c458cdcb992a36f3c4a06752499461c3dd991e07/bookwyrm/models/activitypub_mixin.py#L40) und seine Kinder für Modelle, die für ActivityPub-Anfragen serialisierbar sein müssen

### Daten in ActivityPub-JSON (de-)serialisieren

BookWyrm muss wissen, wie die Daten eines Modells in ein ActivityPub-JSON-LD-Objekt _serialisiert_ werden sollen.

Die Datei `/activitypub/base_activity.py` stellt die Kernfunktionen bereit, um ActivityPub-JSON-LD-Zeichenketten in nutzbare Django-Objekte umzuwandeln und anders herum. Wir erreichen das, indem wir in `bookwyrm/activitypub` eine Datenklasse anlegen und definieren, wie das Modell serialisiert werden soll. Hierzu geben wir im Modell einen Wert für `activity_serializer` an, der zur relevanten Datenklasse zeigt. Von `ActivityObject` erben wir `id` und `type` sowie _Klassenmethoden_:

**`to_model`**

Diese Methode nimmt eine ActivityPub-JSON-Zeichenkette und versucht, sie in ein BookWyrm-Objekt umzuwandeln, wobei nach Möglichkeit ein existierendes Objekt gefunden wird. So verarbeiten wir **eingehende** ActivityPub-Objekte.

**`serialize`**

Diese Methode nimmt ein BookWyrm-Objekt und wandelt es mit Hilfe der Datenklassen-Definitionen in eine valide ActivityPub-JSON-Zeichenkette um. So verarbeiten wir **ausgehende** ActivityPub-Objekte.

### Beispiel: Nutzer*innen

Ein*e BookWyrm-Nutzer*in wird [in `models/user.py` definiert](https://github.com/bookwyrm-social/bookwyrm/blob/main/bookwyrm/models/user.py):

```py
class User(OrderedCollectionPageMixin, AbstractUser):
    """a user who wants to read books"""
```
Beachte, dass unsere Unterklasse von `OrderedCollectionPageMixin` erbt. Dieses wiederum erbt von `ObjectMixin`, welches von `ActivitypubMixin` erbt. Das mag umständlich erscheinen, aber diese Vererbungskette erlaubt uns, Code-Duplikate zu vermeiden, wenn unsere ActivityPub-Objekte konkreter werden. `AbstractUser` ist [ein Django-Modell, das dazu gedacht ist, durch Unterklassen erweitert zu werden](https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#specifying-custom-user-model), was uns Dinge wie gehashte Passwort-Anmeldungen und Berechtigungsebenen "von Haus aus" mitgibt.

Da `User` von [`ObjectMixin`](https://github.com/bookwyrm-social/bookwyrm/blob/c458cdcb992a36f3c4a06752499461c3dd991e07/bookwyrm/models/activitypub_mixin.py#L213) erbt, kommt es beim Speichern (`save()`) eines `User`-Objekts dazu, dass wir wahlweise eine `Create`-Aktivität (wenn dies das erste Mal ist, dass unser*e Nutzer*in gespeichert wird) oder eine `Update`-Aktivität (wenn wir nur eine Änderung festhalten, z. B. an der Beschreibung oder am Avatar) senden. Alle anderen Modelle, die du zu BookWyrm hinzufügst, haben dieselben Möglichkeiten, wenn sie von `ObjectMixin` erben.

Für BookWyrm-Nutzer*innen wird der `activity_serializer` im Modell `User` definiert:

```py
activity_serializer = activitypub.Person
```

Die Definition der Datenklasse für`activitypub.Person` findet sich in `/activitypub/person.py`:

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

Du wirst bemerken, dass diese Felder nicht perfekt zu den Feldern im Modell `User` passen. Wenn du in deinem Modell einen Feldnamen hast, der im ActivityPub-Objekt anders heißen muss (z. B., um mit Python-Namenskonventionen im Modell übereinzustimmen, aber gleichzeitig auch mit JSON-Namenskonventionen), kannst du ein `activitypub_field` in der Definition des Modellfeldes angeben:

```py
followers_url = fields.CharField(max_length=255, activitypub_field="followers")
```
