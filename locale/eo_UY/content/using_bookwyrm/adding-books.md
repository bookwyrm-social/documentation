---
Title: Aldoni librojn
Date: 2022-07-29
Order: 3
---

Estas pluraj manieroj aldoni librojn al via instanco de BookWyrm! Kiam vi ne povas trovi la libron kiun vi serĉas, provu ĉi tiujn opciojn en tiu ordo – estas pli bone importi libron ol krei tute novan.

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

## Ŝargi per libroj de aliaj katalogoj

If the book you're looking for isn't available on your BookWyrm instance, there are a few different ways to add it. La plej bona maniero estas importi ĝin de ekstera fonto – via instanco povas ŝargi per libroj de aliaj instancoj de BookWyrm, kaj ankaŭ de [OpenLibrary](http://openlibrary.org/) kaj [Inventaire](http://inventaire.io/). Se estas neniu rezulto de la serĉo, ĉi tiuj fontoj estos aŭtomate demanditaj kaj la rezultoj aperos kun butono por «**importi libron**». Se estas lokaj rezultoj kiuj ne estas la ĝusta celata libro, vi povas alklaki la ligilon «**ŝarĝi per rezultoj de aliaj katalogoj**» por ŝargi per pliaj rezultoj.


## Aldoni plian eldonon

Se vi trovis la libron kiun vi celas, sed ne la ĝustan eldonon, vi povas aldoni plian eldonon al la verkaĵo ĉe la listo de eldonoj. Alklaku la ligilon sub la priskribo kiu diras al vi kiom da eldonoj ekzistas (ekzemple, «**4 eldonoj**»). Ĉe la subo de la listo de eldonoj, estas butono por «**aldoni plian eldonon**».

## Aldoni tute novan libron

Post kiam vi provis serĉi libron, importi ĝin de alia katalogo kaj trovi aliajn eldonojn de la libro, vi povas permani aldoni novan libron. La ligilo por permane aldoni libron estas ĉe la subo de la serĉpaĝo kiam montriĝas eksteraj katologoj. You can also navigate directly to `/create-book` on your instance.
