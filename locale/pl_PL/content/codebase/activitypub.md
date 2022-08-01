- - -
Title: ActivityPub Date: 2021-04-20 Order: 1
- - -

BookWyrm korzysta z protokołu [ActivityPub](http://activitypub.rocks/) do wysyłania i odbierania aktywności użytkownika pomiędzy instancjami BookWyrm oraz innymi usługami, które korzystają z ActivityPub, takimi jak [Mastodon](https://joinmastodon.org/). Do obsługi danych na temat książek BookWyrm posiada kilka rozszerzonych typów Aktywności, które nie są częścią standardu, ale są czytelne dla innych instancji BookWyrm.

## Aktywności i obiekty

### Użytkownicy i stosunki
Interakcje stosunków między użytkownikami są zgodne ze specyfikacją ActivityPub.

- `Obserwuj`: poproś o otrzymywanie statusów od użytkownika oraz przeglądanie ich statusów, które mogą wyświetlić tylko obserwujący
- `Akceptuj`: zatwierdza `Obserwowanie` i nawiązuje stosunek
- `Odmów`: odrzuca `Obserwowanie`
- `Zablokuj`: uniemożliwia użytkownikowi wzajemne wyświetlanie statusów oraz uniemożliwia wyświetlanie profilu
- `Aktualizuj`: aktualizuje profil i ustawienia użytkownika
- `Usuń`: dezaktywuje użytkownika
- `Cofnij`: anuluje `Obserwowanie` lub `Zablokowanie`

### Statusy
#### Typy obiektów

- `Notatka`: W usługach takich jak Mastodon, `Notatki` są podstawowym typem statusów. Zawierają treść wiadomości, załączniki, wzmianki o użytkownikach oraz są odpowiedziami na inne statusy dowolnego typu. Within BookWyrm, `Note`s can only be created as direct messages or as replies to other statuses.
- `Recenzja`: jest to status w odpowiedzi na książkę (wskazaną przez pole `inReplyToBook`), który zawiera tytuł, treść oraz ocenę liczbową od 0 (bez oceny) do 5.
- `Komentarz`: komentarz do książki wspomina o książce i zawiera treść.
- `Cytat`: zawiera treść, fragment książki oraz wspomina o książce


#### Aktywności

- `Tworzenie`: zapisuje nowy status w bazie danych.

   **Uwaga**: BookWyrm akceptuje aktywności `Tworzenie`, tylko jeśli:

   - Są wiadomościami bezpośrednimi (np. `Notatki` z ustawieniem `bezpośrednie`, które wspominają lokalnego użytkownika),
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
