---
Title: Boeken toevoegen
Date: 2022-07-29
Order: 3
---

Er zijn een aantal verschillende manieren om boeken toe te voegen aan je BookWyrm instantie! Wanneer je het boek waar je naar op zoek bent niet kunt vinden probeer de opties in genoemde volgorde -- het is beter om een boek te importeren dan er eentje vanuit het niets te maken.

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

## Boeken uit andere catalogi laden

If the book you're looking for isn't available on your BookWyrm instance, there are a few different ways to add it. De beste manier is om deze te importeren uit een externe bron -- je instantie kan boeken laden uit andere BookWyrm instanties, evenals vanuit [OpenLibrary](http://openlibrary.org/) en [Inventaire](http://inventaire.io/). Als er geen zoekresultaten zijn voor uw zoekopdracht, zullen deze bronnen automatisch worden bevraagd, en verschijnt er een "**Importeer boek**" knop. Als er lokale zoekresultaten niet zijn wat je zoekt, klik dan op de "**Laad resultaten van andere catalogi**" koppeling om meer resultaten te laden.


## Een editie toevoegen

Als je het boek dat je wilt vinden, maar deze niet de juiste editie is, kun je nog een editie toevoegen aan het werk vanuit de lijst met edities. Klik op de koppeling onder de beschrijving die je vertelt hoeveel edities er zijn (bijvoorbeeld "**4 edities**"). Onder aan de lijst met edities, is er een knop om "**Een andere editie** " toe te voegen.

## Een geheel nieuw boek toevoegen

Nadat je hebt geprobeerd om naar je boek te zoeken, importeer deze vanuit een andere catalogus en zoek naar andere edities van het boek, deze kan je handmatig een nieuw boek toevoegen. De koppeling om handmatig een boek toe te voegen staat onderaan de zoekpagina als externe catalogi worden weergegeven. You can also navigate directly to `/create-book` on your instance.
