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
Das erlaubt dir, Folgeanfragen zu überprüfen oder ausschließlich deine Freund\*innen zuzulassen.

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
- This is the privacy level used in Direct Messages.

## Shelves

Shelves are Public by default, but you can edit them to make them only visible to your followers or just yourself.

### Public / Unlisted

- There is no difference between Public and Unlisted for Shelves. The Unlisted option may be removed in the future.
- Anyone can see these shelves and all the books on them.

### Followers

- Only people who follow you will see this shelf and the books on it.

### Private

- Only you will be able to see this shelf and the books on it.

### All books shelf

- The 'All books' shelf is a default shelf which displays books from all visible shelves to the user viewing it.

| User        | Books on Public shelves | Books on Unlisted shelves | Books on Followers-only shelves | Books on Private shelves |
| ----------- | ----------------------- | ------------------------- | ------------------------------- | ------------------------ |
| Anyone      | ✔                       | ✔                         |                                 |                          |
| Follows you | ✔                       | ✔                         | ✔                               |                          |
| Yourself    | ✔                       | ✔                         | ✔                               | ✔                        |

### Implications

- If you read a book, want to track it on Bookwyrm, but don't want anyone to know that you did, you'll need to put it on a new Private shelf, not a Public shelf.

## Lists

### Public

- Anyone can see your [List](/lists.html) without logging in.
- Your List will appear on:
  - the Lists discovery page (Lists tab).
  - the pages of books that are in it, displayed on the side of the screen.
  - your profile.
- Anyone can 'save' (bookmark) your List.

### Unlisted

- There is currently no difference between Public and Unlisted for Lists.
  In the future, Unlisted will hide the List from the Lists discovery page and books pages.
  For details, see [#3265](https://github.com/bookwyrm-social/bookwyrm/issues/3265) on GitHub.

### Followers

- Only people who follow you can see your List on the aforementioned pages.

### Private

- Only you can see your List on the aforementioned pages.

## Groups

[Groups](/groups.html) have the same privacy settings as statuses and lists do, except they can't be Followers-only.
Group membership always requires an invitation from the group's owner, even if it is marked Public.
Note that currently, the Groups tab on a profile is only shown if the user viewing it is logged in (see [#3610](https://github.com/bookwyrm-social/bookwyrm/issues/3610)).

### Public

- Anyone can view the Group page, members and its Lists (except for private Lists)

- In the future it will be displayed on a Groups discovery page.

### Unlisted

- Anyone can view the group page, members and its Lists (except for private Lists)

### Private

- Only members of the group can view the group page, members and its Lists
- All the Groups Lists will also be private.

## Privacy related settings

### Manually approve followers

Found in `Settings - Edit Profile - Privacy`.

When enabled, you will get a notification when someone wants to follow you, and you'll be able to choose whether or not to accept it.
Useful if you want to check who they are or restrict your followers to only be your friends and people you know.

### Hide followers and following lists on profile

Found in `Settings - Edit Profile - Privacy`.

By default, anyone can view the list of people you follow and who follow you.
There are many reasons you might not want this, so Bookwyrm allows you to hide these lists.

### Show this account in suggested users

Found in `Settings - Edit Profile - Display`.

When enabled, your account may be suggested to other users and will be on the account directory.

