- - -
Title: Velkommen Date: 2021-04-13
- - -

BookWyrm er et sosialt nettverk for å journalføre lesing, snakke om bøker, skrive omtaler, og finne ut hva mer du kan lese. Føderering gjør at BookWyrm-brukere i stand til å bli med i små, pålitelige samfunn som kan knytte seg til hverandre, og med andre ActivityPub-tjenester som Mastodon og Pleroma.

## Funksjoner
The features are growing every month, and there is plenty of room for suggestions and ideas. Open an [issue](https://github.com/bookwyrm-social/bookwyrm/issues) to get the conversation going, or [find a good first issue](https://github.com/bookwyrm-social/bookwyrm/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22) to make your first contribution!

- Poste om bøker
    - Skriv omtaler, med eller uten vurderinger, som samles på boksiden
    - Skriv andre typer statuser om bøker, for eksempel:
        - Kommentarer på en bok
        - Sitat eller utdrag
    - Svar på statuser
    - Vis samlede bokomtaler på tvers av tilkoblede BookWyrm-instanser
    - Differensier mellom lokale og føderte omtaler og rangeringer i din aktivitetsstrøm
- Spor leseaktivitet
    - Shelve books on default "to-read," "currently reading," "stopped reading," and "read" shelves
    - Opprett tilpassede hyller
    - Store started/stopped/finished reading dates, as well as progress updates along the way
    - Oppdater følgere om leseaktivitet (valgfritt, og med granulære personvernkontroller)
    - Opprett lister med bøker som kan åpnes for å kunne motta innsendte forslag fra hvem som helst, kurert, eller kun redigert av skaperen
    - Create groups with other BookWyrm users and collaborate with group-owned lists
- Føderering med ActivityPub
    - Kringkast og motta brukerstatuser og aktivitet
    - Del bokdata mellom instanser for å opprette en nettverksdatabase med metadata
    - Identifiser felles bøker på tvers av instanser og aggreger relatert innhold
    - Følg og samhandle med brukere på tvers av BookWyrm-instanser
    - Inter-operate with non-BookWyrm ActivityPub services like Mastodon and GoToSocial
- Granulær personvernskontroll
    - Privat, kun følgere, og offentlig personvernnivåer for poster, hyller og lister
    - Alternativ for brukere å kunne godkjenne følgere manuelt
    - Tillat blokkering og flagging for moderering

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