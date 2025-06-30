---
Title: Legg til bøker
Date: 2022-07-29
Order: 3
---

Det er forskjellige måter å legge til bøker til din BookWyrm-instans! Om du ikke finner boken du leter etter, prøv disse alternativene i rekkefølge -- det er bedre å importere en bok enn å opprette en fra bunnen av.

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

## Laster inn bøker fra andre kataloger

If the book you're looking for isn't available on your BookWyrm instance, there are a few different ways to add it. Den beste måten er å importere den fra en ekstern kilde -- din instans kan laste inn bøker fra andre BookWyrm-instanser, samt [OpenLibrary](http://openlibrary.org/) og [Inventaire](http://inventaire.io/). Hvis det ikke finnes noen søkeresultater for dine søk, blir disse kildene automatisk spurt, og vil dukke opp sammen med en knapp til «**Importer bok**». Hvis det finnes lokale søkeresultater som ikke er det du leter etter, kan du trykke på «**Last resultater fra andre kataloger**»-lenken for å laste inn flere resultater.


## Legg til en ny utgave

Hvis du fant boken du ønsker, men ikke den riktige utgaven, kan du legge til en annen utgave av verket fra listen av utgaver. Trykk på lenken nedenfor beskrivelsen som forteller deg hvor mange utgaver det er (for eksempel «**4 utgaver**»). På bunnen av utgave-listen finnes det en knapp «**Legg til en annen utgave**».

## Legg til en helt ny bok

Når du har prøvd å søke etter boken din, å importere den fra en annen katalog, og å finne andre utgaver av boken, kan du legge til en ny bok manuelt. Lenken for å legge til en bok manuelt finnes nederst på søkesiden når eksterne kataloger vises. You can also navigate directly to `/create-book` on your instance.
