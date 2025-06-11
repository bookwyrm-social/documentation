---
Title: Engadir Libros
Date: 2022-07-29
Order: 3
---

Hai dous xeitos diferentes de engadir libros á túa instancia BookWyrm! Cando non atopas o libro que buscas, segue estas instruccións en orde -- é mellor importar un libro que crear un novo desde cero.

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

## Cargar libros desde outros catálogos

If the book you're looking for isn't available on your BookWyrm instance, there are a few different ways to add it. O mellor xeito é importalo desde unha orixe externa -- a túa instancia pode obter libros desde outras instancias BookWyrm, así como de [OpenLibrary](http://openlibrary.org/) e [Inventaire](http://inventaire.io/). Se non obtés resultados para a busca, estas orixes serán consultadas automáticamente, e mostrarán un botón para "**Importar libro**". Se hai resultados locais que non son o que estabas a buscar, podes premer na ligazón "**Cargar resultados doutros catálogos**" para ver máis suxestións.


## Engadir outra edición

Se atopaches o libro que buscabas, pero non a edición correcta, podes engadir outra edición desde a lista de edicións. Preme na ligazón debaixo da descrición que indica cantas edicións existen (exemplo, "**4 edicións**"). Debaixo da lista de edición, hai un botón para "**Engadir outra edición**".

## Engadir un libro desde cero

Unha vez intentaches atopar o libro, importalo desde outro catálogo, e outras edicións do libro, podes engadir manualmente un libro novo. A ligazón para engadir manualmente un libro está abaixo na páxina de busca cando se mostran catálogos externos. You can also navigate directly to `/create-book` on your instance.
