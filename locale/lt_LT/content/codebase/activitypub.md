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
- `Apžvalga`: tai yra atsako į knygą būsena (nurodyta laukelyje `Atsakas į knygą`), kurios pavadinimas, turinys ir skaitinis įvertinimas yra nuo 0 (neįvertinta) iki 5.
- `Komentaras`: knygos komentare minima knyga ir yra pranešimo tekstas.
- `Quotation`: A quote has a message body, an excerpt from a book, and mentions a book


#### Activities

- `Create`: saves a new status in the database.

   **Note**: BookWyrm only accepts `Create` activities if they are:

   - Direct messages (i.e., `Note`s with the privacy level `direct`, which mention a local user),
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
