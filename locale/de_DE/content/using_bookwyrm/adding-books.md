---
Title: Bücher hinzufügen
Date: 2022-07-29
Order: 3
---

Es gibt einige verschiedene Möglichkeiten, um Bücher zu deiner BookWyrm-Instanz hinzuzufügen! Wenn du das gesuchte Buch nicht finden kannst, versuche diese Optionen in der Reihenfolge -- es ist besser, ein Buch zu importieren als eines von Grund auf neu zu erstellen.

## Importing data about your books and reading

If you're coming to BookWyrm from another platform for tracking books and reading, you may want to import your books and reading data. Currently BookWyrm is capable of importing export files from the following platforms:

* Calibre (CSV)
* Goodreads (CSV)
* LibraryThing (TSV)
* OpenLibrary (CSV)
* Storygraph (CSV)
* OpenReads (CSV)

Under 'Settings' navigate to 'Import Book List', select the matching data source, select your file and, if relevant, select whether to import reviews and what privacy setting to give them. When you press 'Import' a background task will begin to import your data. You will be notified when it has finished.

It is important to understand that the import process does not import data directly from the other service - in many cases (e.g. Goodreads) this is not possible. When you import a data file, BookWyrm will search the local database, connected BookWyrm servers, and selected public data sources to find a match. For this reason, BookWyrm may not be able to import all of your data. We are always looking for new data sources with free and open APIs, especially for data about books in languages other than English. If you are aware of such a data source, please consider [creating an Issue](https://github.com/bookwyrm-social/bookwyrm/issues),

## Bücher aus anderen Katalogen laden

If the book you're looking for isn't available on your BookWyrm instance, there are a few different ways to add it. Der beste Weg ist, sie von einer externen Quelle zu importieren -- deine Instanz kann Bücher von anderen BookWyrm-Instanzen laden, sowie [OpenLibrary](http://openlibrary.org/) und [Inventaire](http://inventaire.io/). Wenn es keine Suchergebnisse für Ihre Anfrage gibt, werden diese Quellen automatisch abgefragt und erscheint mit einem Button zum "**Buch importieren**". Wenn es lokale Suchergebnisse gibt, die nicht das sind, was Sie suchen, können Sie auf den Link "**Ergebnisse aus anderen Katalogen laden**" klicken, um mehr Ergebnisse zu laden.


## Eine weitere Ausgabe hinzufügen

Wenn du das gesuchte Buch gefunden hast, es aber die falsche Ausgabe ist, kannst du eine andere Ausgabe aus der Liste der Ausgaben hinzufügen. Klicke auf den Link unter der Beschreibung, der angibt, wie viele Ausgaben es gibt (zum Beispiel "**4 Ausgaben**"). Am unteren Rand der Editionsliste befindet sich ein Button zum "**Eine weitere Ausgabe hinzufügen**".

## Ein komplett neues Buch hinzufügen

Sobald du versucht hast, nach deinem Buch zu suchen, es aus einem anderen Katalog zu importieren und findest nur andere Ausgaben des Buchs, kannst du ein neues Buch manuell hinzufügen. Der Link zum manuellen Hinzufügen eines Buches befindet sich am Ende der Suchseite, wenn externe Kataloge angezeigt werden. You can also navigate directly to `/create-book` on your instance.
