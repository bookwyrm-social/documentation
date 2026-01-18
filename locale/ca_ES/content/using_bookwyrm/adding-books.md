---
Title: Afegir llibres
Date: 2022-07-29
Order: 3
---

Hi ha diferents vies per tal d'afegir llibres a la teva instància de BookWyrm! Quan no trobis el llibre que estàs cercant, prova aquestes opcions per ordre -- és millor fer una importació que crear un des de zero.

## Important les dades dels teus llibres i finalitzant

Si veniu a BookWyrm des d'una altra plataforma per fer el seguiment dels llibres i la lectura, és possible que vulgueu importar els vostres llibres i les vostres dades de lectura. Actualment BookWyrm és capaç d'importar fitxers d'exportació des de les següents plataformes:

* Calibre (CSV)
* Goodreads (CSV)
* LibraryThing (TSV)
* OpenLibrary (CSV)
* Storygraph (CSV)
* OpenReads (CSV)

A 'Configuració' navegueu a 'Importa la llista de llibres', seleccioneu la font de dades que coincideixi, seleccioneu el vostre fitxer i, si és rellevant, seleccioneu si voleu importar ressenyes i quina configuració de privadesa voleu donar-los. Quan premeu «Importa», una tasca en segon pla començarà a importar les vostres dades. Se't notificarà quan hagi acabat.

És important entendre que el procés d'importació no importa dades directament de l'altre servei - en molts casos (per exemple, Goodreads) això no és possible. Quan importeu un fitxer de dades, BookWyrm cercarà la base de dades local, els servidors BookWyrm connectats i les fonts de dades públiques seleccionades per trobar una coincidència. Per aquest motiu, és possible que BookWyrm no pugui importar totes les vostres dades. Sempre estem buscant noves fonts de dades amb APIs lliures i obertes, especialment per a dades sobre llibres en idiomes diferents de l'anglès. Si teniu coneixement d'aquesta font de dades, considereu [creant una petició](https://github.com/bookwyrm-social/bookwyrm/issues),

## Carregar llibres d'altres catàlegs

Si el llibre que estàs cercant no es troba disponible a la teva instància de BookWyrm, hi ha diferents vies per tal d'afegir-lo. La millor via és important-lo des d'una font externa -- la teva instància pot carregar llibres d'altres instàncies de BookWyrm, com també d'[OpenLibrary](http://openlibrary.org/) i d'[Inventaire](http://inventaire.io/). Si no hi ha resultats per a la teva cerca, aquestes fonts seran automàticament consultades i, se't mostrarà un botó per "**Importar llibre**". Si hi han resultats locals no desitjats, pots pitjar l'enllaç "**Carregar resultats d'altres catàlegs**" per carregar més resultats.


## Afegir una altra edició

Si trobes el llibre desitjat, però no l'edició correcta, pots afegir una edició diferent des del llistat d'edicions. Pitja l'enllaç situat sota la descripció on es mostra el número d'edicions que hi ha (per exemple "**4 edicions**"). Al final de la llista d'edicions, hi trobaràs el botó "**Afegir una altra edició**".

## Afegir un llibre completament nou

Un cop has provat de cercar el llibre, importar-lo d'un altre catàleg i, comprovar altres edicions, pots afegir un nou llibre manualment. L'enllaç per a afegir manualment el llibre es troba al final de la pàgina de cerca quan es mostren catàlegs externs. També pots navegar directament a `/create-book` a la teva instància.
