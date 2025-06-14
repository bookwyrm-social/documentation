---
Title: Ajout de livres
Date: 2022-07-29
Order: 3
---

Il y a plusieurs façons d'ajouter des livres à votre instance BookWyrm ! Quand vous ne trouvez pas le livre que vous cherchez, essayez ces options dans l'ordre -- il vaut mieux importer un livre que d'en créer un à partir de zéro.

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

## Chargement de livres à partir d'autres catalogues

If the book you're looking for isn't available on your BookWyrm instance, there are a few different ways to add it. La meilleure manière est de l'importer depuis une source externe -- votre instance peut charger des livres depuis d'autres instances BookWyrm, ainsi que d'[OpenLibrary](http://openlibrary.org/) et [Inventaire](http://inventaire.io/). S'il n'y a pas de résultats de recherche à votre requête, ces sources seront automatiquement interrogées, et les réponses s'afficheront avec un bouton « **Importer le livre** ». S'il y a des résultats de recherche locaux qui ne sont pas ceux que vous recherchez, vous pouvez cliquer sur le lien «**Charger les résultats d’autres catalogues**» pour charger plus de résultats.


## Ajout d'une nouvelle édition

Si vous avez trouvé le livre que vous cherchiez mais pas dans la bonne édition, vous pouvez ajouter une autre édition à l’œuvre à partir de la liste des éditions. Cliquez sur le lien en dessous de la description qui vous indique le nombre d'éditions (par exemple, « **4 éditions** »). En bas de la liste des éditions il y a un bouton pour « **Ajouter une nouvelle édition** ».

## Ajouter un nouveau livre

Une fois que vous avez essayé sans succès de rechercher votre livre, de l'importez depuis un autre catalogue, et de trouver d'autres éditions de ce livre, vous pouvez ajouter un nouveau livre manuellement. Le lien pour ajouter manuellement un livre se trouve au bas de la page de recherche lorsque les résultats des catalogues externes sont affichés. You can also navigate directly to `/create-book` on your instance.
