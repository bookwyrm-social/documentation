---
Title: Добавление Книг
Date: 2022-07-05
Order: 3
---

Есть несколько способов добавить книги на ваш сервер BookWyrm! Когда вы не можете найти книгу, которую ищете, попробуйте их по очереди — лучше импортировать книгу, чем добавлять её с нуля.

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

## Берём книги из других каталогов

If the book you're looking for isn't available on your BookWyrm instance, there are a few different ways to add it. Лучший способ — взять её извне. Ваш сервер может импортировать книги с других серверов BookWyrm, или из [OpenLibrary](http://openlibrary.org/) и [Inventaire](http://inventaire.io/). Если поиск не даст результатов, эти источники будут запрошены автоматически, и появится кнопка "**Импортировать книгу**". Если в локальных результатах поиска нет нужных книг, можно нажать на "**Загрузить результаты из других каталогов**", чтобы найти больше вариантов.


## Добавление другого издания

Если вы нашли нужную книгу, но другое издание, вы можете добавить еще одно издание в список изданий. Нажмите ссылку под описанием, в которой указано, сколько изданий имеется (например, "**4 издания**"). Под списком изданий есть кнопка "**Добавить другое издание**".

## Добавление новой книги

Если вы уже пытались найти книгу, импортировать её из другого каталога, и искали другие издания, вы можете добавить новую книгу вручную. Ссылка для добавления книги вручную находится внизу страницы поиска по внешним каталогам. You can also navigate directly to `/create-book` on your instance.
