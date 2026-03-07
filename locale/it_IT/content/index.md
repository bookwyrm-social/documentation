- - -
Titolo: Benvenuto Data: 13-04-2021
- - -

BookWyrm è un social network per monitorare la lettura, parlare di libri, scrivere recensioni, e scoprire cosa leggere dopo. La Federazione permette agli utenti di BookWyrm di unirsi a piccole comunità di fiducia che possono connettersi tra loro e con altri servizi ActivityPub come Mastodon e Pleroma.

## Funzionalità
Le funzionalità vengono aggiunte ogni mese, e c'è un sacco di spazio per suggerimenti e idee. Open an [issue](https://github.com/bookwyrm-social/bookwyrm/issues) to get the conversation going, or [find a good first issue](https://github.com/bookwyrm-social/bookwyrm/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22) to make your first contribution!

- Pubblicazioni sui libri
    - Componi le recensioni, con o senza valutazioni, che vengono aggregate nella pagina del libro
    - Componi altri tipi di stati sui libri, come:
        - Commenti su un libro
        - Citazioni o estratti
    - Rispondi agli stati
    - Visualizza le recensioni aggregate di un libro attraverso le istanze di BookWyrm collegate
    - Differenziare le recensioni locali e federate e la valutazione nel tuo feed di attività
- Monitorare l'attività di lettura
    - Shelve books on default "to-read," "currently reading," "stopped reading," and "read" shelves
    - Creare scaffali personalizzati
    - Store started/stopped/finished reading dates, as well as progress updates along the way
    - Aggiorna chi ti segue sull'attività di lettura (opzionalmente, e con controlli sulla privacy)
    - Crea liste di libri che possono essere aperte al contributo di chiunque, curate o modificate solo dal creatore
    - Crea gruppi con altri utenti BookWyrm e collabora con liste gestite da gruppi
- Federazione con Activitypub
    - Trasmetti e ricevi stati e attività dell'utente
    - Condividere i dati dei libri tra istanze per creare un database di metadati in rete
    - Identifica i libri condivisi tra istanze e aggrega contenuti correlati
    - Segui e interagisci con gli utenti tra le istanze di BookWyrm
    - Inter-operate with non-BookWyrm ActivityPub services like Mastodon and GoToSocial
- Controlli specifici sulla privacy
    - Livelli privati, solo follower e pubblici per la pubblicazione degli scaffali ed elenchi
    - Opzione per gli utenti di approvare manualmente i follower
    - Consenti il blocco e la segnalazione per moderazione

## Using this documentation

### Navigation

Use the menu on the left-hand side to find the section you are looking for.

* _Using BookWyrm_ explains how to use BookWyrm as an ordinary user
* You will need the _Running BookWyrm_ section if you want to administer a BookWyrm instance (server)
* _Contributing_ explains how you can get involved in the project and contribute in various ways (you don't have to know how to code)
* _Codebase_ provides more information about key aspects of BookWyrm's code
* Consult the _Reference Guides_ if you need to know what a particular environment variable or `bw-dev` command does

You can also change the language and version.

### Translations

Documentation is written in English (US) by default. When we have at least 70% coverage for a language in [BookWyrm's translation project](https://translate.joinbookwyrm.com/) it will be added to the list of available languages. If you notice some parts of a translated version are in English, you can [help us to translate them](https://translate.joinbookwyrm.com/). This can happen as we make changes and additions to the documentation.

### Versioning

Since version `0.7.5`, each BookWyrm version has a matching version in the documentation. This allows you to check the documentation as it applies to your specific BookWyrm version. If you are using a patch version with no matching documentation (e.g. `0.8.1`), this is a bugfix-only version and you should use the documentation for the preceding version (e.g. `0.8.0`).

### Page table of contents

There is also a drop-down menu on each page that displays a table of contents. You can use this to navigate directly to a particular section heading. This can be useful for very long pages like the Reference Guides. The table of contents menu does not appear on the homepage.

### Smaller screens

On smaller screens the side menu is hidden. Use the "hamburger menu" at the top right of the screen to make it visible.