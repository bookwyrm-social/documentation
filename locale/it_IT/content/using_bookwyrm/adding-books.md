---
Title: Aggiungere libri
Date: 2022-07-29
Order: 3
---

Ci sono alcuni modi diversi per aggiungere libri alla vostra istanza BookWyrm! Quando non trovi il libro che stai cercando, provare queste opzioni in ordine -- è meglio importare un libro che crearne uno da zero.

## Importing data about your books and reading

If you're coming to BookWyrm from another platform for tracking books and reading, you may want to import your books and reading data. Currently BookWyrm is capable of importing export files from the following platforms:

* Calibre (CSV)
* Goodreads (CSV)
* LibraryThing (TSV)
* OpenLibrary (CSV)
* Storygraph (CSV)
* OpenReads (CSV)

Under 'Settings' navigate to 'Import Book List', select the matching data source, select your file and, if relevant, select whether to import reviews and what privacy setting to give them. When you press 'Import' a background task will begin to import your data. Verrai avvisato quando avrà finito.

It is important to understand that the import process does not import data directly from the other service - in many cases (e.g. Goodreads) this is not possible. When you import a data file, BookWyrm will search the local database, connected BookWyrm servers, and selected public data sources to find a match. For this reason, BookWyrm may not be able to import all of your data. We are always looking for new data sources with free and open APIs, especially for data about books in languages other than English. If you are aware of such a data source, please consider [creating an Issue](https://github.com/bookwyrm-social/bookwyrm/issues),

## Carica libri da altri cataloghi

If the book you're looking for isn't available on your BookWyrm instance, there are a few different ways to add it. Il modo migliore è quello di importarlo da una fonte esterna -- la tua istanza può importare libri da altre istanze di BookWyrm, così come [OpenLibrary](http://openlibrary.org/) e [Inventaire](http://inventaire.io/). Se non ci sono risultati per la tua ricerca, queste fonti verranno automaticamente interrogate, e verrà visualizzate con un pulsante "**Importa libro**". Se ci sono i risultati di ricerca locali che non sono quello che stai cercando, è possibile cliccare sul link "**Carica i risultati da altri cataloghi**" per caricare più risultati.


## Aggiungere un'altra versione

Se hai trovato il libro che vuoi, ma non la giusta edizione, puoi aggiungere un'altra edizione al lavoro dalla lista delle edizioni. Clicca sul link sottostante la descrizione che ti dice quante edizioni ci sono (per esempio, "4 edizioni****"). Nella parte inferiore della lista delle edizioni, c'è un pulsante per "**Aggiungere un'altra edizione**".

## Aggiunge un libro nuovo

Una volta che hai provato a cercare il tuo libro, importandolo da un altro catalogo e trovare altre edizioni del libro, puoi aggiungere un nuovo libro manualmente. Il link per aggiungere manualmente un libro è nella parte inferiore della pagina di ricerca quando vengono visualizzati cataloghi esterni. You can also navigate directly to `/create-book` on your instance.
