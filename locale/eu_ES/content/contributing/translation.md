- - -
Izenburua: Itzulpenak Eguna: 2021-10-20 Ordena: 2
- - -

## Itzultzen lagundu

BookWyrm-en itzulpen proiektuarekin bat egin dezakezu hemen: [translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/).

## Genero-hizkuntza neutrala

Ahal den neurrian, BookWyrm-en itzulpenek genero neutrala duen hizkuntza erabili behar dute. Hizkuntza batek gizakia genero neutral gisa betetzen ez badu ere aplikatzen da hori, edo gizonezko eta emakumezkoen aldaera nabarmentzen badu izenordain batzuen bidez. Garrantzitsua da, halaber, itzulpenak argiak, zehatzak eta irakurgarriak izatea pantaila bidezko irakurlearentzat, eta, batzuetan, helburu horiek gatazkan daude; ez dago erantzun perfekturik eta bakarra, irtenbidea hizkuntzaren araberakoa da.

Ideia nagusi gisa, saiatu balio handiagoa jartzen hizkuntza neutral eta inklusiboari, hizkuntza formal zuzenari edo ofizialki onartutako estilo-liburuei baino. Ingelesez, adibidez, estilo-gida askok eskatzen dute "she" edo "he" izenordain berezi bat erabiltzea gizabanako bati dagokionez, baina BookWyrmen hobe da "they" izenordain berezi ez-generikoa erabiltzea haren ordez.

Itzulpen arazo bati nola heldu ez badakizu, iruzkindu itzulpena eta ireki [eztabaida gai](https://translate.joinbookwyrm.com/project/bookwyrm/discussions) bat, galdera zabalagoei erantzuteko.

## Jarri txantiloiak itzulgarriak

Bookwyrm-ek Djangoren itzulpen-funtzionalitatea erabiltzen du, orrialdearen edukia erabiltzaileak aukeratutako bistaratze-hizkuntzaren arabera alda dadin. Django dokumentazioak, garapen esparru hori [nola funtzionatzen duen azaltzen du](https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#internationalization-in-template-code), hona hemen bertsio laburra:

* txantiloiaren testu guztiek itzulpen etiketak barne izan behar dituzte
* erantsi `{% load i18n %}` txantiloiaren goiko aldean itzulpenak gaitzeko
* Testu-blokea testu literala bada, `{% trans %}` txantiloiaren etiketa erabil dezakezu
* Testu-blokeak aldagaiak baldin baditu, txantiloiaren etiketa-bikotea erabili behar duzu `{% blocktrans %}` and `{% endblocktrans %}`. Lerro-espazioak edo -jauziak sartzen badituzu, erabili `trimmed` hizkuntza-fitxategia sortzen denean automatikoki ezabatzeko: `{% blocktrans trimmed %}`

### Adibideak

```html
<p>{% trans "This list is currently empty" %}</p>

<p>
    {% blocktrans trimmed with username=item.user.display_name user_path=item.user.local_path %}
    Honek gehitua: <a href="{{ user_path }}">{{ username }}</a>
    {% endblocktrans %}
</p>
```
