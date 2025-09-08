---
Title: Agregar libros
Date: 2022-07-29
Order: 3
---

¡Hay varias maneras para añadir libros a tu instancia de BookWyrm! Cuando no puedas encontrar el libro que estás buscando, intenta estas opciones en orden -- es mejor importar un libro que crear uno desde cero.

## Importar datos de tus libros y lecturas

If you're coming to BookWyrm from another platform for tracking books and reading, you may want to import your books and reading data. Currently BookWyrm is capable of importing export files from the following platforms:

* Calibre (CSV)
* Goodreads (CSV)
* LibraryThing (TSV)
* OpenLibrary (CSV)
* Storygraph (CSV)
* OpenReads (CSV)

Under 'Settings' navigate to 'Import Book List', select the matching data source, select your file and, if relevant, select whether to import reviews and what privacy setting to give them. When you press 'Import' a background task will begin to import your data. You will be notified when it has finished.

It is important to understand that the import process does not import data directly from the other service - in many cases (e.g. Goodreads) this is not possible. When you import a data file, BookWyrm will search the local database, connected BookWyrm servers, and selected public data sources to find a match. For this reason, BookWyrm may not be able to import all of your data. We are always looking for new data sources with free and open APIs, especially for data about books in languages other than English. If you are aware of such a data source, please consider [creating an Issue](https://github.com/bookwyrm-social/bookwyrm/issues),

## Cargar libros de otros catálogos

If the book you're looking for isn't available on your BookWyrm instance, there are a few different ways to add it. La mejor manera es importarlo desde una fuente externa -- tu instancia puede cargar libros desde otras instancias de BookWyrm, así como de [OpenLibrary](http://openlibrary.org/) e [Inventaire](http://inventaire.io/). Si no hay resultados de búsqueda para tu consulta, estas fuentes serán automáticamente consultadas, y se mostrará con un botón a "**Importar libro**". Si hay resultados de búsqueda locales que no son lo que buscas, puede hacer clic en el enlace "**Cargar resultados de otros catálogos**" para cargar más resultados.


## Añadir otra edición

Si encuentras el libro que quieres, pero no la edición correcta, puedes añadir otra edición a la obra de la lista de ediciones. Haga clic en el enlace debajo de la descripción que le indica cuántas ediciones hay (por ejemplo, "**4 ediciones**"). En la parte inferior de la lista de ediciones, hay un botón para "**Añadir otra edición**".

## Añadir un libro completamente nuevo

Una vez que hayas intentado buscar tu libro, importarlo desde otro catálogo, y encontrar otras ediciones del libro, puedes añadir un nuevo libro manualmente. El enlace para añadir manualmente un libro está en la parte inferior de la página de búsqueda cuando se muestran catálogos externos. You can also navigate directly to `/create-book` on your instance.
