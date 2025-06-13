- - -
Titel: ActivityPub Dato: 2021-04-20 Rækkefølge: 1
- - -

BookWyrm bruger [ActivityPub](http://activitypub.rocks/)-protokollen til at sende og modtage brugeraktivitet mellem andre BookWyrm-servere og andre tjenester, der implementerer ActivityPub, som f. eks. [Mastodon](https://joinmastodon.org/). For at håndtere bogdata har BookWyrm en håndfuld udvidede aktivitetstyper, som ikke er en del af standarden, men er læselige for andre BookWyrm-servere.

## Aktiviteter og objekter

### Brugere og relationer
Brugerforhold og interaktioner følger standardspecifikationerne for ActivityPub.

- `Følg`: Anmodning om at modtage statusser fra en bruger og se de statusser, som kun kan ses af følgere
- `Accepter`: godkender en anmodning om at `følge` og opretter forholdet
- `Afvis`: benægter en anmodning om at `følge`
- `Blokér`: forhindrer brugere i at se hinandens statusser og forhindrer den blokerede bruger i at se profilen for brugeren, som har oprettet blokeringen
- `Opdatér`: opdaterer en brugers profil og indstillinger
- `Slet`: deaktiverer en bruger
- `Fortryd`: trækker en anmodning om at `følge` eller en `blokering` tilbage

### Statusser
#### Objekttyper

- `Note`: På tjenester som Mastodon er `Note`r den primære type status. De indeholder en beskeds brødtekst, vedhæftede filer. De kan nævne brugere og være svar på statusser af enhver type. I BookWyrm kan `Note`r kun oprettes som direkte beskeder eller som svar på andre statusser.
- `Anmeldelse`: En anmeldelse er en status som svar på en bog (angivet af `inReplyToBook`-feltet), som har en titel, brødtekst og numerisk bedømmelse på mellem 0 (ikke bedømt) og 5.
- `Kommentar`: En kommentar til en bog nævner en bog og består af en brødtekst.
- `Citat`: Et citat har en brødtekst, et uddrag fra en bog og en reference til en bog.


#### Aktiviteter

- `Opret`: gemmer en ny status i databasen.

   **Note**: BookWyrm accepterer kun `Opret`-aktiviteter, hvis de er:

   - Direkte beskeder (dvs. `Note`r med privatindstillingen `direkte`, og som nævner en lokal bruger),
   - Related to a book (of a custom status type that includes the field `inReplyToBook`),
   - Replies to existing statuses saved in the database
- `Delete`: Removes a status
- `Like`: Creates a favorite on the status
- `Announce`: Boosts the status into the actor's timeline
- `Undo`: Reverses a `Like` or `Announce`

### Collections
User's books and lists are represented by [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objects

- `Shelf`: A user's book collection. By default, every user has a `to-read`, `reading`, and `read` shelf which are used to track reading progress.
- `List`: A collection of books that may have items contributed by users other than the one who created the list.

#### Activities

- `Create`: Adds a shelf or list to the database.
- `Delete`: Removes a shelf or list.
- `Add`: Adds a book to a shelf or list.
- `Remove`: Removes a book from a shelf or list.


## Alternative Serialization
Because BookWyrm uses custom object types (`Review`, `Comment`, `Quotation`) that aren't supported by ActivityPub, statuses are transformed into standard types when sent to or viewed by non-BookWyrm services. `Review`s are converted into `Article`s, and `Comment`s and `Quotation`s are converted into `Note`s, with a link to the book and the cover image attached.
