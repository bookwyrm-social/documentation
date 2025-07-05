---
Title: Afegir llibres
Date: 2022-07-29
Order: 3
---

Hi ha diferents vies per tal d'afegir llibres a la teva instància de BookWyrm! Quan no trobis el llibre que estàs cercant, prova aquestes opcions per ordre -- és millor fer una importació que crear un des de zero.

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

## Carregar llibres d'altres catàlegs

If the book you're looking for isn't available on your BookWyrm instance, there are a few different ways to add it. La millor via és important-lo des d'una font externa -- la teva instància pot carregar llibres d'altres instàncies de BookWyrm, com també d'[OpenLibrary](http://openlibrary.org/) i d'[Inventaire](http://inventaire.io/). Si no hi ha resultats per a la teva cerca, aquestes fonts seran automàticament consultades i, se't mostrarà un botó per "**Importar llibre**". Si hi han resultats locals no desitjats, pots pitjar l'enllaç "**Carregar resultats d'altres catàlegs**" per carregar més resultats.


## Afegir una altra edició

Si trobes el llibre desitjat, però no l'edició correcta, pots afegir una edició diferent des del llistat d'edicions. Pitja l'enllaç situat sota la descripció on es mostra el número d'edicions que hi ha (per exemple "**4 edicions**"). Al final de la llista d'edicions, hi trobaràs el botó "**Afegir una altra edició**".

## Afegir un llibre completament nou

Un cop has provat de cercar el llibre, importar-lo d'un altre catàleg i, comprovar altres edicions, pots afegir un nou llibre manualment. L'enllaç per a afegir manualment el llibre es troba al final de la pàgina de cerca quan es mostren catàlegs externs. You can also navigate directly to `/create-book` on your instance.
