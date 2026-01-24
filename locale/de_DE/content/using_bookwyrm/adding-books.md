---
Title: Bücher hinzufügen
Date: 2022-07-29
Order: 3
---

Es gibt einige verschiedene Möglichkeiten, um Bücher zu deiner BookWyrm-Instanz hinzuzufügen! Wenn du das gesuchte Buch nicht finden kannst, versuche diese Optionen in der Reihenfolge -- es ist besser, ein Buch zu importieren als eines von Grund auf neu zu erstellen.

## Bücher und Lesedaten importieren

Wenn du von einer anderen Lese-Plattform zu BookWyrm wechselst, willst du vielleicht deine Bücher- und Lesedaten importieren. Momentan kann BookWyrm Daten der folgenden Plattformen importieren:

* Calibre (CSV)
* Goodreads (CSV)
* LibraryThing (TSV)
* OpenLibrary (CSV)
* Storygraph (CSV)
* OpenReads (CSV)

Navigiere unter "Einstellungen" zu "Bücherliste importieren", wähle die passende Datenquelle aus und gib deine Datei an. Sofern zutreffend, lege fest, ob du auch Rezensionen importieren möchtest und welche Privatsphäreeinstellung ihnen zugewiesen werden soll. Wenn du auf "Importieren" klickst, wird im Hintergrund mit dem Import deiner Daten begonnen. Du wirst benachrichtigt, wenn der Import abgeschlossen ist.

Es ist wichtig, zu verstehen, dass der Import-Prozess Daten nicht direkt von einem anderen Dienst importiert – in vielen Fällen (z. B. bei Goodreads) ist dies nicht möglich. Wenn du eine Datei importierst, wird BookWyrm die lokale Datenbank, verbundene BookWyrm-Server und ausgewählte öffentliche Datenquellen nach passenden Einträgen durchsuchen. Aus diesem Grund kann es sein, dass BookWym nicht all deine Daten importieren kann. Wir suchen ständig nach neuen Datenquellen mit freien und offenen Schnittstellen, besonders zu Daten über Bücher in anderen Sprachen als Englisch. Wenn du solch eine Datenquelle kennst, denke bitte darüber nach, [einen Issue zu erstellen](https://github.com/bookwyrm-social/bookwyrm/issues)

## Bücher aus anderen Katalogen laden

Wenn das Buch, das du suchst, nicht auf deiner BookWyrm-Instanz verfügbar ist, gibt es ein paar andere Wege, es aufzunehmen. Der beste Weg ist, es von einer externen Quelle zu importieren -- deine Instanz kann Bücher von anderen BookWyrm-Instanzen sowie von [OpenLibrary](http://openlibrary.org/) und [Inventaire](http://inventaire.io/) laden. Wenn es keine Suchergebnisse für deine Anfrage gibt, werden diese Quellen automatisch abgefragt und es erscheint ein Button mit der Aufschrift "**Buch importieren**". Wenn es lokale Suchergebnisse gibt, die nicht das sind, was du suchst, kannst du auf den Link "**Ergebnisse aus anderen Katalogen laden**" klicken, um mehr Ergebnisse zu laden.


## Eine weitere Ausgabe hinzufügen

Wenn du das gesuchte Buch gefunden hast, es aber die falsche Ausgabe ist, kannst du eine andere Ausgabe aus der Liste der Ausgaben hinzufügen. Klicke auf den Link unter der Beschreibung, der angibt, wie viele Ausgaben es gibt (zum Beispiel "**4 Ausgaben**"). Am unteren Rand der Editionsliste befindet sich ein Button mit der Aufschrift "**Eine weitere Ausgabe hinzufügen**".

## Ein komplett neues Buch hinzufügen

Sobald du vergeblich versucht hast, nach deinem Buch zu suchen, es aus einem anderen Katalog zu importieren und andere Ausgaben des Buches zu finden, kannst du es als neues Buch manuell hinzufügen. Der Link zum manuellen Hinzufügen eines Buches befindet sich am Ende der Suchseite, wenn externe Kataloge angezeigt werden. Du kannst auf deiner Instanz auch direkt zum URL-Pfad `/create-book` navigieren.
