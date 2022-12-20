- - -
Title: ActivityPub Date: 2021-04-20 Order: 1
- - -

BookWyrm uses the [ActivityPub](http://activitypub.rocks/) protocol to send and receive user activity between other BookWyrm instances and other services that implement ActivityPub, like [Mastodon](https://joinmastodon.org/). To handle book data, BookWyrm has a handful of extended Activity types which are not part of the standard, but are legible to other BookWyrm instances.

## Activities and Objects

### Nariai ir santykiai
Narių santykių sąveika atitinka standartinę „ActivityPub“ specifikaciją.

- `Sekti`: užklausa gauti nario būsenas ir peržiūrėti tas, kurios turi tik stebėtojų privatumą
- `Patvirtinti`: patvirtina kvietimą `Sekti` ir finalizuoja santykį
- `Atmesti`: atmeta prašymą `Sekti`
- `Blokuoti`: neleisti nariams matyti vienas kito būsenų ir neleisti užblokuotam nariui matyti profilio
- `Atnaujinti`: atnaujina nario paskyrą ir nustatymus
- `Ištrinti`: išaktyvuoja narį
- `Grąžinti į pradinę būseną`: pakeičia `Sekimo` arba `Blokavimo` būseną

### Būsenos
#### Objekto tipai

- `Užrašas`: tokiose paslaugose, kaip „Mastodon“, `Užrašas` yra pirminis būsenos tipas. Juose yra žinutė, prisegtukai, galima minėti narius arba atsakyti į bet kokio tipo būsenas. „BookWyrm“ `Užrašus` galima sukurti kaip tiesiogines žinutes arba atsakymus į kitas būsenas.
- `Apžvalga`: tai yra atsako į knygą būsena (nurodyta laukelyje `inReplyToBook`), kurios pavadinimas, turinys ir skaitinis įvertinimas yra nuo 0 (neįvertinta) iki 5.
- `Komentaras`: knygos komentare minima knyga ir yra pranešimo tekstas.
- `Citavimas`: citata turi vietą žinutei, ištrauką iš knygos ir knygos pavadinimą


#### Veiklos

- `Sukurti`: išsaugo naują būseną duomenų bazėje.

   **Užrašas**: „BookWyrm“ priima tik `Sukūrimo` veiklas, jei jos:

   - Tiesioginės žinutės (pvz., `Užrašas`, kurio privatumo lygis `tiesioginis` ir minintis vietos narį);
   - Susiję su knyga (būsenos tipas, kuriame yra laukelis `inReplyToBook`);
   - Atsako į duomenų bazėje išsaugotas būsenas
- `Ištrinti`: ištrina būseną
- `Patinka`: pažymi, kad būsena patinka
- `Pranešimas`: iškelia būseną į laiko juostą
- `Grąžinti į pradinę būseną`: pakeičia `Patinka` arba `Pranešimo` būseną

### Kolekcijos
Naudotojo knygas ir sąrašus reprezentuoja [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objektai

- `Lentyna`: nario knygų kolekcija. Kiekvienas naudotojas turi lentynas `perskaityti`, `skaitoma` ir `perskaityta`, kurios padeda sekti progresą.
- `Sąrašas`: knygų rinkinys, kuriame gali būti kitų narių knygų, o ne tik sąrašą sukūrusių narių.

#### Veiklos

- `Sukurti`: prideda lentyną arba sąrašą į duomenų bazę.
- `Ištrinti`: pašalina lentyną arba sąrašą.
- `Pridėti`: prideda knygą į lentyną arba sąrašą.
- `Pašalinti`: pašalina knygą iš lentynos arba sąrašo.


## Alternatyvus serializavimas
Kadangi „BookWyrm“ naudoja pasirinktinius objektų tipus (`Apžvalga`, `Komentaras`, `Citavimas`), kurių „ActivityPub“ nepalaiko, siunčiamos būsenos transformuojamos į standartinius tipus, kai siunčia arba peržiūri ne „BookWyrm“. `Apžvalga` paverčiama `Straipsniu`, o `Komentaras` ir `Citavimas` paverčiami `Užrašu` su nuoroda į knygą ir prisegtą viršelio nuotrauką.
