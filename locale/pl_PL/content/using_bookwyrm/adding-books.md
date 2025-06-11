---
Title: Dodawanie książek
Date: 2022-07-29
Order: 3
---

Istnieje kilka sposobów na dodawanie książek do swojej instancji BookWyrm! Jeśli nie możesz znaleźć książki, której szukasz, wypróbuj te opcje w ich kolejności -- lepiej jest zaimportować książkę niż tworzyć ją od nowa.

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

## Wczytywanie książek z pozostałych katalogów

If the book you're looking for isn't available on your BookWyrm instance, there are a few different ways to add it. Najlepszym z nich jest importowanie jej z zewnętrznego źródła -- Twoja instancja może wczytać książki z pozostałych instancji BookWyrm oraz [OpenLibrary](http://openlibrary.org/) i [Inventaire](http://inventaire.io/). Jeśli nie ma wyników wyszukiwania dla Twojego zapytania, zostanie ono automatycznie przekierowane do tych źródeł i pokażą się z przyciskiem "**Importuj książkę**". Jeśli istnieją lokalne wyniki wyszukiwania, które nie są tym, czego szukasz, naciśnij na odnośnik "**Wczytaj wyniki z pozostałych katalogów**", aby wczytać więcej wyników.


## Dodawanie innego wydania

Jeśli znajdziesz właściwą książkę, ale nie odpowiednie wydanie, możesz dodać inne wydanie z listy wydań. Naciśnij na odnośnik poniżej opisu, który zawiera liczbę wydań (na przykład: "**4 wydania**"). Na dole listy wydań umieszczony jest przycisk "**Dodaj inne wydanie**".

## Dodawanie zupełnie nowej książki

Po wypróbowaniu szukania książki, importowania jej z pozostałych katalogów oraz szukania innych wydań książki, możesz dodać nową książkę ręcznie. Odnośnik do ręcznego dodania książki umieszczony jest na dole strony wyszukiwania, gdy pokazane są zewnętrzne katalogi. You can also navigate directly to `/create-book` on your instance.
