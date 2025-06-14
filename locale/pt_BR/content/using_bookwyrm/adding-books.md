---
Title: Adicionar livros
Date: 2022-07-29
Order: 3
---

Há várias formas de adicionar os livros à sua instância de BookWyrm! Quando você não puder encontrar o livro que procura, tente estas opções em ordem -- é melhor importar um livro do que criar um do zero.

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

## Carregue livros de outros catálogos

If the book you're looking for isn't available on your BookWyrm instance, there are a few different ways to add it. A melhor maneira é importá-lo de uma fonte externa -- sua instância pode carregar livros de outras de BookWyrm, como também de  [OpenLibrary](http://openlibrary.org/) e [Inventaire](http://inventaire.io/). Se não houver resultados de busca para sua consulta, estas fontes serão automaticamente consultadas e aparecerá com um botão para "**Importar livro**". Se houver resultados de pesquisa local que não sejam os que você está procurando, você pode clicar no link "**Carregar resultados de outros catálogos**" para carregar mais resultados.


## Adicionar outra edição

Se você encontrar o livro que você queria, mas não a edição correta, você pode adicionar outra edição ao catálogo a partir da lista de edições. Clique no link abaixo da descrição que diz quantas edições existem (por exemplo, "**4 edições**"). No botão da lista de edições há um botão para "**Adicionar outra edição**".

## Adicione um livro completamente novo

Uma vez que você tentou procurar o seu livro, importando-o de outro catálogo, e encontrar outras edições do livro, você pode adicionar um livro novo manualmente. O link para adicionar manualmente um livro novo está na parte inferior da página de busca quando os catálogos externos são mostrados. You can also navigate directly to `/create-book` on your instance.
