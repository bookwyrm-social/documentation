- - -
Titel: ActivityPub Datum: 2021-04-20 Volgorde: 1
- - -

BookWyrm maakt gebruik van het [ActivityPub](http://activitypub.rocks/) protocol voor het verzenden en ontvangen van gebruikersactiviteit tussen andere BookWyrm instanties en andere diensten die ActivityPub implementeren zoals [Mastodon](https://joinmastodon.org/). Om gegevens van boeken te verwerken heeft BookWyrm een handvol uitgebreide activiteitstypen die niet deel zijn van de standaard, maar leesbaar zijn voor andere BookWyrm instanties.

## Activiteiten en Objecten

### Gebruikers en relaties
Gebruikersrelatie interacties volgen de standaard ActivityPub specificatie.

- `Follow`: verzoek om statussen van een gebruiker te ontvangen en hun statussen met alleen volgers-only privacy te bekijken
- `Accept`: keurt een `Follow` goed en voltooit de relatie
- `Reject`: weigert een `Follow`
- `Block`: voorkomen dat gebruikers elkaars statussen zien, en voorkomt dat de geblokkeerde gebruiker het profiel van de speler bekijkt
- `Update`: updates het profiel en instellingen van een gebruiker
- `Delete`: deactiveert een gebruiker
- `Undo`: draait een `Follow` of `Block` terug

### Statussen
#### Objecttypes

- `Note`: Voor diensten zoals Mastodon, `Note`s zijn het primaire status type. Ze bevatten een bericht, bijlagen, kunnen gebruikers vermelden en zijn antwoorden op statussen van elk type. Binnen BookWyrm kan `Note`s alleen worden gemaakt als directe berichten of als antwoord op andere statussen.
- `Review`: Een recensie is een status in reactie op een boek (aangegeven door het `inReplyToBook` veld) die een titel, lichaam en numerieke beoordeling tussen 0 (niet beoordeeld) en 5 heeft.
- `Comment`: Een reactie op een boek vermeldt een boek en bevat een bericht.
- `Quotation`: Een citaat heeft een bericht, een extract uit een boek en vermeldt een boek.


#### Activiteiten

- `Create`: slaat een nieuwe status op in de database.

   **Let op**: BookWyrm accepteert alleen `Create` activiteiten als ze zijn:

   - Directe berichten (d.w.z. `Note`met het privacyniveau `direct`, die een lokale gebruiker vermeldt),
   - Gerelateerd aan een boek (van een aangepast statustype dat het veld `inReplyToBook` bevat),
   - Antwoorden op bestaande statussen opgeslagen in de database
- `Delete`: Verwijdert een status
- `Like`: Maakt een favoriet aan op de status
- `Announce`: Vergroot de status in de tijdlijn van de speler
- `Undo`: draait een `Like` of `Announce` terug

### Verzamelingen
De boeken en lijsten van gebruikers worden vertegenwoordigd door [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objecten

- `Shelf`: Een boekverzameling van gebruikers. Standaard heeft elke gebruiker een `om te lezen`, `lezen`, en `gelezen` plank die gebruikt worden om de leesvoortgang bij te houden.
- `List`: Een verzameling boeken waarbij items kunnen worden bijgedragen door andere gebruikers dan degene die de lijst hebben gemaakt.

#### Activiteiten

- `Aanmaken`: Voegt een plank of een lijst toe aan de database.
- `Delete`: Verwijdert een plank of lijst.
- `Add`: Voegt een boek toe aan een plank of lijst.
- `Remove`: Verwijdert een boek van een plank of lijst.


## Alternatieve serialisatie
Omdat BookWyrm gebruikmaakt van aangepaste objecttypes (`Review`, `Comment`, `Quotation`) die niet worden ondersteund door ActivityPub, worden statussen omgezet in standaard types wanneer ze worden verzonden naar of bekeken door niet-BookWyrm diensten. `Review`s worden omgezet in `Article`s, en `Comment`s en `Quotation`s worden omgezet in `Note`s, met een koppeling naar het boek en de bijgevoegde omslagafbeelding.
