---
Title: Adding Books
Date: 2022-07-29
Order: 3
---

Există câteva modalități diferite de a adăuga cărți instanței dvs. BookWyrm! Când nu găsiți o carte pe care o căutați, încercați aceste opțiuni în ordine: este mai bine să importați o carte decât să creați una de la zero.

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

## Încărcarea de cărți din alte cataloage

If the book you're looking for isn't available on your BookWyrm instance, there are a few different ways to add it. Cel mai bun mod este de a o importa dintr-o sursă exterioară -- instanța dvs. poate încărca cărți din alte instanțe BookWyrm, precum și din [OpenLibrary](http://openlibrary.org/) și [Inventaire](http://inventaire.io/). Dacă nu există rezultate pentru interogarea dvs., aceste surse vor fi automat întrebate și vor arăta un buton cu „**Importați carte**”. Dacă există rezultate locale care nu sunt ceea ce căutați, puteți face clic pe legătura „**Încărcați rezultate din alte cataloage**” pentru a încărca mai multe rezultate.


## Adăugați o nouă ediție

If you found the book you want, but not the right edition, you can add another edition to the work from the list of editions. Click the link below the description that tells you how many editions there are (for example, "**4 editions**"). În partea de jos a listei de ediții este un buton „**Adăugați o altă ediție**”.

## Adăugați o carte complet nouă

Odată ce ați încercat să găsiți cartea dvs., să o importați dintr-un alt catalog și să găsiți alte ediții ale cărții, puteți adăuga o carte nouă manual. The link to manually add a book is at the bottom of the search page when external catalogs are shown. You can also navigate directly to `/create-book` on your instance.
