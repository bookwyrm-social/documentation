- - -
Izenburua: ActivityPub Eguna: 2021-04-20 Ordena: 1
- - -

BookWyrm-ek [Activity Pub](http://activitypub.rocks/) protokoloa erabiltzen du erabiltzailearen jarduera bidaltzeko eta jasotzeko, BookWyrm instantzien eta ActivityPub ezarria duten beste zerbitzu baten artean, [Mastodon](https://joinmastodon.org/) bezala. Liburuko datuak erabiltzeko, BookWyrm-ek estandarrak ez diren Activity motako hainbat gehigarri erabiltzen ditu, baina BookWyrm-en beste instantziekin erabilgarriak direnak.

## Jarduerak eta Objektuak

### Erabiltzaileak eta harremanak
Erabiltzaile-harremanaren elkarrekintzek Activity Pub-en berezitasun estandarrari jarraitzen diote.

- `Jarraitu`: erabiltzaile baten egoera jasotzeko eskatzen du eta pribatutasun-aukera «jarraitzaileak soilik» aktibatuta duten egoerak erakusten ditu
- `Onartu`: `Jarraitzea` onartzen eta harremana gauzatzen du
- `Ukatu`: `Jarraitze` bati uko egiten dio
- `Blokeatu`: erabiltzaileek bestearen egoerak ikustea eragozten du eta blokeatutako erabiltzaileak aktorearen profila ikustea eragozten du
- `Eguneratu`: erabiltzaile baten profila eta konfigurazioa eguneratzen ditu
- `Ezabatu`: erabiltzaile bat desaktibatzen du
- `Desegin`: desegiten ditu `Jarraitze` bat edo `Blokeo` bat

### Egoerak
#### Objektu motak

- `Oharra`: Mastodon bezalako zerbitzuetan, `Oharra` elementuak egoera-mota nagusia dira. Barne hartzen dute mezu eremu bat, fitxategi erantsiak, erabiltzaileak aipa ditzakete eta edozein motatako estatutuen erantzunak izan daitezke. BookWyrm-en, `Oharra` elementuak zuzeneko mezu gisa soilik sor daitezke edo beste egoera batzuei emandako erantzun gisa.
- `Kritika`: Kritika bidalketa bat da, liburu bati zuzenduta (`LiburuariBuruz` eremuak adierazita). Kritika batek honako atal hauek ditu: izenburua, gorputza eta 0 (kalifikatu gabea) eta 5 arteko kalifikazioa.
- `Iruzkina`: Liburu bati buruzko iruzkin batek liburu bat aipatzen du eta mezu gorputz bat dauka.
- `Aipua`: Aipu batek du mezuaren gorpuntz bat eta liburu baten zati bat, eta liburu bat aipatzen du.


#### Jarduerak

- `Sortu`: bidalketa berri bat gordetzen du datu-basean.

   **Oharra**: BookWyrm-ek `Sortu` jarduerak baimentzen ditu baldin eta:

   - Mezu zuzenak badira (hots, `Oharra` elementuak `zuzena` pribatutasun mailarekin, tokiko erabiltzailearen aipamenarekin),
   - Liburu batekin lotuta badira ( `LiburariBuruz` eremua barne duen egoera pertsonalizatuko mota batekoa),
   - Datu-basean gordetako egoerei emandako erantzunak
- `Ezabatu`: Egoera bat ezabatzen du
- `Atsegin`: Sortzen du gogoko bat egoeretan
- `Partekatu`: Egoera sustatzen du aktorearen kronologian
- `Desegin`: Desegiten ditu `Atsegin` bat edo `Partekatu` bat

### Bildumak
[`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection) elementuari esker erabiltzaile baten liburuak eta zerrendak ager daitezke

#### Objektuak

- `Apala`: erabiltzaile baten liburu bilduma. Lehenespenez, erabiltzaile bakoitzak hainbat atal ditu irakurketaren egoeraren berri izateko: `irakurtzekoak`, `irakurtzen hasitakoak` eta `irakurriak`.
- `Zerrenda`: Zerrenda sortu zuen erabiltzaileaz besteko elementuak izan ditzakeen liburu-bilduma.

#### Jarduerak

- `Sortu`: Gehitu apal bat edo zerrenda bat datu-basean.
- `Ezabatu`: Ezabatu apal bat edo zerrenda bat.
- `Gehitu`: Liburu bat gehitzen du apal edo zerrenda batean.
- `Kendu`: Apal edo zerrenda batetik liburu bat ezabatzen du.


## Serializazio alternatiboa
BookWyrm-ek Activity Pub-ekin bateragarriak ez diren objektu pertsonalizatu motak (`Kritika`, `Iruzkina`, `Aipua`) erabiltzen dituenez, egoerak tipo estandar bihurtzen dira BookWyrm ez diren zerbitzuek bidaltzen edo ikusten dituztenean. `Kritikak`, `Artikulu` bihurtzen dira, eta `Iruzkinak` eta `Aipuak` `Ohar` bihurtzen dira, libururako esteka batekin eta erantsitako azaleko irudi batekin.
