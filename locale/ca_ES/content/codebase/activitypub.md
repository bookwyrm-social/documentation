- - -
Títol: ActivityPub Data: 2021-04-20 Ordre: 1
- - -

BookWyrm utiltza el protocol [ActivityPub](http://activitypub.rocks/) per enviar i rebre activitat d'usuari entre diferents instàncies de BookWyrm i altres serveis que implementen ActivityPub, com [Mastodon](https://joinmastodon.org/). Per manegar les dades d'un llibre, BookWyrm té molts tipus d'activitats que no formen parts de l'estàndard, però que altres instàncies de BookWyrm poden llegir.

## Activitats i Objectes

### Usuaris i relacions
Les interaccions entre usuaris segueixen les especificacions estandars d'ActivityPub.

- `Segueix`: sol·licita rebre les entrades d'un usuari i veure aquelles que només són accessibles per part dels seguidors
- `Accepta`: aprova un `Segueix` i finalitza la sol·licitud
- `Refusa`: denega un `Segueix`
- `Bloqueja`: impossibilita als usuaris que es vegin mútuament les entrades i l'accés de la persona bloquejada al perfil de qui l'ha bloquejat
- `Actualitza`: actualitza el perfil i configuració de l'usuari
- `Elimina`: desactiva l'usuari
- `Desfés`: desfà un `Segueix` o `Bloqueja`

### Estats
#### Tipus d'objecte

- `Nota`: En serveis com Mastodon, les `Notes` són el tipus principal d'estat. Contenen un cos del missatge, adjunts, poden fer menció a usuaris i, ser respostes altres tipus d'estat. Dins de BookWyrm, les `Notes` només poden ser creades com a missatges directes o com a respostes a altres estats.
- `Ressenya`: Una ressenya és un estat en resposta a un llibre (indicat pel camp `inReplyToBook`), el qual conté títol, cos i, una valoració numèrica entre 0 (no valorat) i 5.
- `Comentari`: Un comentari en un llibre fa referència a un llibre i té un cos del missatge.
- `Cita`: Una cita té un cos del missatge, un extracte d'un llibre i, menciona un llibre.


#### Activitats

- `Crear`: guarda un nou estat a la base de dades.

   **Nota**: BookWyrm nomès accepta activitats de `Crear` si són:

   - Missatges directes (per exemple `Notes` amb el nivell de privacitat `directe`, el qual menciona a un usuari local),
   - Relacionat amb un llibre (amb un estat personalitzat que inclogui el camp `inReplyToBook`),
   - Respostes a estats ja existents guardats a la base de dades
- `Eliminar`: Elimina un estat
- `M'agrada`: Crea un favorit a l'estat
- `Anunci`: Destaca l'estat a la línia de temps de l'actor
- `Desfer`: Desfà un `M'agrada` o un `Anunci`

### Col·leccions
Els llibres i llistats de l'usuari son representats per [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objectes

- `Prestatge`: Una col·lecció de llibres d'un usuari. Per defecte, tots els usuaris tenen un prestatge `per-llegir`, `llegint` i `llegit` els quals són emprats per fer un seguiment de la seva activitat de lectura.
- `Llista`: Una col·lecció de llibres que pot contenir contribucions realitzades per altres usuaris a més a més de qui ha creat la llista.

#### Activitats

- `Create`: Afegeix un prestatge o llista a la base de dades.
- `Delete`: Elimina un prestatge o llista.
- `Add`: Afegeix un llibre al prestatge o llista.
- `Remove`: Elimina un llibre del prestatge o llista.


## Serialitzacions alternatives
Degut a que BookWyrm fa ús de tipus d'objectes personalitzats (`Ressenya`, `Comentari`, `Cita`) que no són reconeguts per l'ActiityPub, els estats són transformats a tipus estàndard quan s'envien o són llegits per serveis que no són BookWyrm. `Ressenyes` són convertides en `Article`s i, `Comentari`s i `Cites` són transformats en `Notes`, amb un enllaç al llibre i a la imatge de portada adjunta.
