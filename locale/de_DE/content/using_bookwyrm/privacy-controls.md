---
Title: Privatsphäre-Einstellungen
Date: 2025-05-26
Order: 7
---

BookWyrm hat verschiedene Privatsphäre-Level, die Nutzer\*innen entscheiden lassen, wie öffentlich etwas ist und wer es sehen kann.
Möchtest du deine Leseaktivität mit dem gesamten Internet oder deinen Freund\*innen teilen oder sie lieber für dich behalten?

Es gibt vier Privatsphäre-Level: Öffentlich, Ungelistet, Follower\*innen und Privat.
Ganz allgemein gesprochen ist Öffentliches für jede\*n sichtbar, Ungelistetes wird auf den Entdecken-Seiten verborgen; Follower\*innen-Inhalte können nur Menschen sehen, die dir folgen, und Privates ist nur für dich sichtbar.
Es gibt ein paar feine Unterschiede darin, wie diese Level auf verschiedene Dinge in BookWyrm angewendet werden.

Das Privatsphäre-Level kannst du bei allem auf der Website am Symbol daneben erkennen.
Öffentlich zeigt eine Weltkugel, Ungelistet markiert ein geöffnetes Schloss, Follower\*innen-Inhalte sind am verriegelten Schloss zu erkennen und Privates kennzeichnet ein Umschlag.

Hinweis: Jede\*r kann dir folgen und dann die Inhalte sehen, die du nur für Follower\*innen freigegeben hast.
Um dies einzuschränken, gehe zu `Einstellungen - Privatsphäre` und aktiviere "Follower\*innen manuell bestätigen".
Das erlaubt dir, Folgeanfragen zu überprüfen oder nur deinen Freund\*innen zu gestatten, dir zu folgen.

Andere Privatsphäre-Einstellungen werden [am Ende dieser Seite](#privacy-related-settings) erklärt.

## Beiträge

Auf BookWyrm können [Beiträge](/posting-statuses.html) mit vier verschiedenen Privatsphäre-Levels veröffentlicht werden. Sie entscheiden, wer einen Beitrag sehen kann und ob er auf öffentlichen Seiten erscheint.
Jeder Beitrag hat sein eigenes Privatsphäre-Level, du kannst also entscheiden, wann du ihn öffentlich oer privat schalten möchtest. In den Einstellungen kannst du ein Standard-Level festlegen.
Beachte, dass das Privatsphäre-Level nicht geändert werden kann, sobald der Beitrag veröffentlicht wurde.

### Öffentlich

Die Standardauswahl.

- Jede\*r kann deinen Beitrag sehen, ohne sich anzumelden.
- Dein Beitrag wird erscheinen:
  - in öffentlichen Zeitleisten
  - auf Entdecken-Seiten
  - auf der Seite des zugehörigen Buches
  - auf der Start-Zeitleiste von Personen, die dir folgen
- Dein Status kann durch einen **Boost** in die Start-Zeitleiste anderer Menschen verbreitet werden.

### Ungelistet

Dasselbe Verhalten wie bei Öffentlich, nur:

- Dein Beitrag wird **nicht** in öffentlichen Zeitleisten oder auf Entdecken-Seiten auftauchen.

### Follower\*innen

- Nur Personen, die dir folgen, können deinen Beitrag in ihren Zeitleisten oder auf der Seite des zugehörigen Buchs sehen.
- Dein Beitrag kann nicht geboostet werden.

### Privat

- Dein Beitrag kann nur von dir gesehen werden sowie von Personen, die darin **erwähnt** wurden oder schon vorher Teil der Konversation waren.
- Das ist das Privatsphäre-Level, das bei Direktnachrichten zum Einsatz kommt.

## Regale

Regale sind standardmäßig öffentlich, aber du kannst sie bearbeiten, um ihre Sichtbarkeit auf deine Follower\*innen oder dich selbst zu begrenzen.

### Öffentlich/Ungelistet

- Es gibt bei Regalen keinen Unterschied zwischen Öffentlich und Ungelistet. Die Option Ungelistet könnte in der Zukunft entfernt werden.
- Jede\*r kann diese Regale und alle Bücher darin sehen.

### Follower\*innen

- Nur Menschen, die dir folgen, können dieses Regal und die Bücher darin sehen.

### Privat

- Nur du kannst dieses Regal und die Bücher darin sehen.

### Regal "Alle Bücher"

- Das Regal "Alle Bücher" wird automatisch erstellt und zeigt Bücher aller Regale, auf die du Zugriff hast.

| Nutzer\*in | Bücher in öffentlichen Regalen | Bücher in ungelisteten Regalen | Bücher in Regalen nur für Follower\*innen | Bücher in privaten Regalen |
| ---------- | ------------------------------ | ------------------------------ | ----------------------------------------- | -------------------------- |
| Jede\*r    | ✔                              | ✔                              |                                           |                            |
| Folgt dir  | ✔                              | ✔                              | ✔                                         |                            |
| Du selbst  | ✔                              | ✔                              | ✔                                         | ✔                          |

### Implikationen

- Wenn du ein Buch liest und das auf BookWyrm nachverfolgen möchtest, aber nicht willst, dass andere darüber Bescheid wissen, musst du es in ein privates Regal legen, nicht in ein öffentliches.

## Listen

### Öffentlich

- Jede\*r kann deine [Liste](/lists.html) sehen, ohne sich anzumelden.
- Deine Liste wird erscheinen:
  - auf der Listen-Entdecken-Seite (Reiter "Listen")
  - seitlich auf der Seite von Büchern, die darin enthalten sind
  - auf deiner Profilseite
- Jede\*r kann deine Liste "speichern", also ein Lesezeichen setzen.

### Ungelistet

- Es gibt aktuell bei Listen keinen Unterschied zwischen Öffentlich und Ungelistet.
  Zukünftig werden ungelistete Listen nicht mehr auf der Listen-Entdecken-Seite und auf Seiten zu Büchern auftauchen.
  Siehe [#3265](https://github.com/bookwyrm-social/bookwyrm/issues/3265) auf GitHub für Details.

### Follower\*innen

- Nur Personen, die dir folgen, können deine Liste auf den oben genannten Seiten sehen.

### Privat

- Nur du kannst deine Liste auf den oben genannten Seiten sehen.

## Gruppen

[Gruppen](/groups.html) haben dieselben Privatsphäre-Levels wie Beiträge und Listen, bis auf dass sie nicht auf Follower\*innen begrenzt werden können.
Die Gruppenmitgliedschaft bedarf immer einer Einladung der Person, der die Gruppe gehört, selbst wenn die Gruppe als öffentlich markiert wurde.
Beachte, dass der Gruppen-Reiter auf einer Profilseite aktuell nur dann angezeigt wird, wenn du angemeldet bist (siehe [#3610](https://github.com/bookwyrm-social/bookwyrm/issues/3610)).

### Öffentlich

- Jede\*r kann die Gruppenseite, die Mitglieder und die zugehörigen Listen (private ausgenommen) einsehen.

- Zukünftig wird die Gruppe auf einer Gruppen-Entdecken-Seite erscheinen.

### Ungelistet

- Jede\*r kann die Gruppenseite, die Mitglieder und die zugehörigen Listen (private ausgenommen) einsehen.

### Privat

- Nur Mitglieder der Gruppe können die Gruppenseite, die Mitglieder und die zugehörigen Listen einsehen.
- Alle Listen der Gruppe sind ebenfalls privat.

## Einstellungen zur Privatsphäre

### Follower\*innen manuell bestätigen

Zu finden unter `Einstellungen - Profil bearbeiten - Privatsphäre`.

Wenn dies aktiviert ist, erhältst du eine Benachrichtigung, wenn dir jemand folgen möchte, und du kannst entscheiden, ob du die Anfrage annehmen möchtest oder nicht.
Das ist nützlich, wenn du immer prüfen willst, wer dir folgen möchte, oder du nur Freund\*innen und Leuten, die du kennst, erlauben möchtest, dir zu folgen.

### Folgende und Gefolgte im Profil ausblenden

Zu finden unter `Einstellungen - Profil bearbeiten - Privatsphäre`.

Standardmäßig kann jede Person einsehen, wem du folgst und wer dir folgt.
Es gibt viele Gründe, warum du das lieber nicht wollen könntest, darum erlaubt BookWyrm, diese Listen auszublenden.

### Diesen Account in vorgeschlagene Accounts einschließen

Zu finden unter `Einstellungen - Profil bearbeiten - Anzeige`.

Wenn dies aktiviert ist, kann dein Profil anderen Personen vorgeschlagen werden. Es erscheint außerdem im Profilverzeichnis.

