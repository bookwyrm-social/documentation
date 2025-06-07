- - -
Title: ActivityPub Date: 2021-04-20 Order: 1
- - -

BookWyrm bruker [ActivityPub](http://activitypub.rocks/)-protokollen for å sende og motta brukeraktivitet mellom andre BookWyrm-instanser og andre tjenester som implementerer ActivityPub, som [Mastodon](https://joinmastodon.org/). For å håndtere bokdata, har BookWyrm en håndfull utvidede aktivitetstyper som ikke er en del av standarden, men er forståelige for andre BookWyrm-instanser.

## Aktiviteter og objekter

### Brukere og relasjoner
Interaksjoner for brukerrelasjoner følger standard ActivityPub-spesifikasjon.

- `Follow`: be om å motta statuser fra en bruker, og se deres statuser som er begrenset til å sees kun av følgere
- `Accept`: godkjenner en `Follow` og fullfører forholdet
- `Reject`: nekter en `Follow`
- `Block`: forhindrer brukere fra å se hverandres statuser, og forhindrer at blokkerte brukere fra å se aktørens profil
- `Update`: oppdaterer brukerens profil og innstillinger
- `Delete`: deaktiverer en bruker
- `Undo`: reverserer en `Follow` eller `Block`

### Statuser
#### Objekttyper

- `Note`: På tjenester som Mastodon er `Note` den primære typen status. De inneholder meldingens brødtekst, vedlegg, kan nevne brukere, og kan være svar til statuser av alle typer. I BookWyrm kan `Note` bare opprettes som direktemeldinger eller som svar på andre statuser.
- `Review`: A anmeldelse er en responsstatus til en bok (indikert med `inReplyToBook`-feltet), og har en tittel, en brødtekst, og en numerisk vurdering mellom 0 (ikke vurdert) og 5.
- `Comment`: En kommentar til en bok nevner en bok og har en brødtekst.
- `Quotation`: Et sitat har en brødtekst, et utdrag fra en bok, og nevner en bok.


#### Aktiviteter

- `Create`: lagrer en ny status i databasen.

   **Merk**: BookWyrm godtar bare `Create`-aktiviteter dersom de er:

   - direktemeldinger (f.eks. `Note` med personvernsnivå `direct`, som nevner en lokal bruker),
   - svar til en bok (av en egendefinert statustype som inkluderer feltet `inReplyToBook`),
   - svar til en eksisterende status lagret i databasen
- `Delete`: Fjerner en status
- `Like`: Oppretter en favoritt på statusen
- `Announce`: Booster statusen inn i aktørens tidslinje
- `Undo`: reverserer en `Like` eller `Announce`

### Samlinger
Brukerens bøker og lister er representert av en [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objekter

- `Shelf`: En brukers boksamling. Som standard har hver bruker en `to-read`-, `reading`-, og `read`-hylle som brukes til å spore lesefremdriften.
- `List`: En samling med bøker som kan ha elementer bidratt av andre enn den som opprettet listen.

#### Aktiviteter

- `Create`: Legger til en hylle eller en liste i databasen.
- `Delete`: Fjerner en hylle eller en liste.
- `Add`: Legger til en bok til en hylle eller liste.
- `Delete`: Fjerner en bok fra en hylle eller liste.


## Alternativ serialisering
Ettersom BookWyrm bruker tilpassede objecttyper (`Review`, `Comment`, `Quotation`) som ikke er støttet av ActivityPub, vil statuser bli oversatt til standardtyper når de blir sendt til eller sett på av ikke-BookWyrm-tjenester. `Review` blir konvertert til `Article`, og `Comment` og `Quotation` blir konvertert til `Note`, med en lenke til boka med vedlagt omslagsbilde.
