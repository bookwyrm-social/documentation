- - -
Izenburua: ActivityPub Eguna: 2021-04-20 Ordena: 1
- - -

BookWyrm-ek [Activity Pub](http://activitypub.rocks/) protokoloa erabiltzen du erabiltzailearen jarduera bidaltzeko eta jasotzeko, BookWyrm instantzien eta ActivityPub ezarria duten beste zerbitzu baten artean, [Mastodon](https://joinmastodon.org/) bezala. Liburuko datuak erabiltzeko, BookWyrm-ek estandarrak ez diren Activity motako hainbat gehigarri erabiltzen ditu, baina BookWyrm-en beste instantziekin erabilgarriak direnak.

## Jarduerak eta Objektuak

### Erabiltzaileak eta harremanak
Erabiltzaile-harremanaren elkarrekintzek Activity Pub-en berezitasun estandarrari jarraitzen diote.

- `Follow`: erabiltzaile baten egoera jasotzeko eskatzen du eta pribatutasun-aukera «jarraitzaileak soilik» aktibatuta duten egoerak erakusten ditu
- `Accept`: `Follow` bat onartzen eta harremana gauzatzen du
- `Reject`: `Follow` bati uko egiten dio
- `Block`: erabiltzaileek bestearen egoerak ikustea eragozten du eta blokeatutako erabiltzaileak aktorearen profila ikustea eragozten du
- `Update`: erabiltzaile baten profila eta konfigurazioa eguneratzen ditu
- `Delete`: erabiltzaile bat desaktibatzen du
- `Undo`: desegiten ditu `Follow` bat edo `Block` bat

### Egoerak
#### Objektu motak

- `Note`: Mastodon bezalako zerbitzuetan, `Note` elementuak egoera-mota nagusia dira. Barne hartzen dute mezu eremu bat, fitxategi erantsiak, erabiltzaileak aipa ditzakete eta edozein motatako estatutuen erantzunak izan daitezke. BookWyrm-en, `Note` elementuak zuzeneko mezu gisa soilik sor daitezke edo beste egoera batzuei emandako erantzun gisa.
- `Review`: Kritika, liburu bati erantzunda ematen den egoera da (`inReplyToBook` elementuaren eremuak adierazten du), izenburu bat, gorputz bat eta 0 (sailkatu gabea) eta 5 arteko nota digital bat dauzkana.
- `Comment`: Liburu bati buruzko iruzkin batek liburu bat aipatzen du eta mezu gorputz bat dauka.
- `Quotation`: Aipamen batek mezu gorputz bat dauka, liburu baten zati bat eta liburu bat aipatzen du


#### Jarduerak

- `Create`: egoera berri bat gordetzen du datu-basean.

   **Note**: BookWyrm-ek `Create` jarduerak baimentzen ditu baldin eta:

   - Mezu zuzenak badira (hots, `Note` elementuak `direct` pribatutasun mailarekin, tokiko erabiltzailearen aipamenarekin),
   - Liburu batekin lotuta badira ( `inReplyToBook` eremua barne duen egoera pertsonalizatuko mota batekoa),
   - Datu-basean gordetako egoerei emandako erantzunak
- `Delete`: Egoera bat ezabatzen du
- `Like`: Sortzen du gogoko bat egoeretan
- `Announce`: Egoera sustatzen du aktorearen kronologian
- `Undo`: Desegiten ditu `Like` bat edo `Announce` bat

### Bildumak
[`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection) elementuari esker erabiltzaile baten liburuak eta zerrendak ager daitezke

#### Objektuak

- `Shelf`: Erabiltzaile baten liburu bilduma. Lehenespenez, erabiltzaile bakoitzak hainbat atal ditu, irakurtketaren aurrerapenari jarraitzeko: `irakurtzekoak`, `irakurtzen hasitakoak` eta `irakurriak`.
- `List`: Zerrenda sortu zuen erabiltzaileaz besteko elementuak izan ditzakeen liburu-bilduma.

#### Jarduerak

- `Create`: Gehitu apal bat edo zerrenda bat datu-basean.
- `Delete`: Ezabatu apal bat edo zerrenda bat.
- `Add`: Liburu bat gehitzen du apal edo zerrenda batean.
- `Remove`: Apal edo zerrenda batetik liburu bat ezabatzen du.


## Serializazio alternatiboa
Because BookWyrm uses custom object types (`Review`, `Comment`, `Quotation`) that aren't supported by ActivityPub, statuses are transformed into standard types when sent to or viewed by non-BookWyrm services. `Review`s are converted into `Article`s, and `Comment`s and `Quotation`s are converted into `Note`s, with a link to the book and the cover image attached.
