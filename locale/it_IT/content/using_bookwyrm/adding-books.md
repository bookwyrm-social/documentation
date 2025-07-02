---
Title: Aggiungere libri
Date: 2022-07-29
Order: 3
---

Ci sono alcuni modi diversi per aggiungere libri alla vostra istanza BookWyrm! Quando non trovi il libro che stai cercando, provare queste opzioni in ordine -- è meglio importare un libro che crearne uno da zero.

## Importare dati sui tuoi libri e sulle tue letture

Se stai arrivando su Bookwyrm da un’altra piattaforma per tracciare libri e letture, potresti voler importare i tuoi dati su libri e letture. Attualmente Bookwyrm è in grado di importare file di esportazione dalle seguenti piattaforme:

* Calibre (CSV)
* Goodreads (CSV)
* LibraryThing (TSV)
* OpenLibrary (CSV)
* Storygraph (CSV)
* OpenReads (CSV)

Nella sezione 'Impostazioni', vai su 'Importa elenco libri', seleziona la fonte dati corrispondente, scegli il file da importare e, se pertinente, indica se importare anche le recensioni e quale livello di privacy assegnare a queste ultime. Quando premi 'Importa', verrà avviato un processo in background per importare i tuoi dati. Verrai avvisato quando avrà finito.

È importante capire che il processo di importazione non preleva i dati direttamente dal servizio esterno — in molti casi (ad esempio Goodreads) questo non è possibile. Quando importi un file di dati, Bookwyrm cercherà corrispondenze nel database locale, sui server Bookwyrm collegati e nelle fonti pubbliche selezionate. Per questo motivo, Bookwyrm potrebbe non riuscire a importare tutti i tuoi dati. Siamo sempre alla ricerca di nuove fonti di dati con API gratuite e aperte, soprattutto per informazioni su libri in lingue diverse dall’inglese. Se conosci una fonte di dati del genere, ti invitiamo a [segnalarlo creando un Issue](https://github.com/bookwyrm-social/bookwyrm/issues)

## Carica libri da altri cataloghi

Se il libro che cerchi non è presente sulla tua istanza di BookWyrm, ci sono diversi modi per aggiungerlo. Il modo migliore è quello di importarlo da una fonte esterna -- la tua istanza può importare libri da altre istanze di BookWyrm, così come [OpenLibrary](http://openlibrary.org/) e [Inventaire](http://inventaire.io/). Se non ci sono risultati per la tua ricerca, queste fonti verranno automaticamente interrogate, e verrà visualizzate con un pulsante "**Importa libro**". Se ci sono i risultati di ricerca locali che non sono quello che stai cercando, è possibile cliccare sul link "**Carica i risultati da altri cataloghi**" per caricare più risultati.


## Aggiungere un'altra versione

Se hai trovato il libro che vuoi, ma non la giusta edizione, puoi aggiungere un'altra edizione al lavoro dalla lista delle edizioni. Clicca sul link sottostante la descrizione che ti dice quante edizioni ci sono (per esempio, "4 edizioni****"). Nella parte inferiore della lista delle edizioni, c'è un pulsante per "**Aggiungere un'altra edizione**".

## Aggiunge un libro nuovo

Una volta che hai provato a cercare il tuo libro, importandolo da un altro catalogo e trovare altre edizioni del libro, puoi aggiungere un nuovo libro manualmente. Il link per aggiungere manualmente un libro è nella parte inferiore della pagina di ricerca quando vengono visualizzati cataloghi esterni. Puoi anche accedere direttamente a `/create-book` sulla tua istanza.
