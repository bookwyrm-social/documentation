---
Title: Adding Books
Date: 2022-07-29
Order: 3
---

Existuje několik různých způsobů, jak přidat knihy do vaší BookWyrm instance! Když nemůžete najít knihu, kterou hledáte, vyzkoušejte tyto možnosti v tomto pořadí -- je lepší importovat knihu než ji vytvořit od nuly.

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

## Nahrávání knih z jiných katalogů

If the book you're looking for isn't available on your BookWyrm instance, there are a few different ways to add it. Nejlepší způsob, je ji importovat z externího zdroje – vaše instance může načíst knihy z jiných instancí BookWyrm, stejně tak z [OpenLibrary](http://openlibrary.org/) a [Inventaire](http://inventaire.io/). If there are no search results for your query, these sources will automatically be queried, and will show up with a button to "**Import book**". If there are local search results that aren't what you're looking for, you can click the "**Load results from other catalogues**" link to load more results.


## Přidání další edice

If you found the book you want, but not the right edition, you can add another edition to the work from the list of editions. Click the link below the description that tells you how many editions there are (for example, "**4 editions**"). At the bottom of the editions list, there is a button to "**Add another edition**".

## Přidat úplně novou knihu

Once you've tried searching for your book, importing it from another catalog, and finding other editions of the book, you can add a new book manually. The link to manually add a book is at the bottom of the search page when external catalogs are shown. You can also navigate directly to `/create-book` on your instance.
