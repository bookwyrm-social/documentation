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
- `Usuń`: Usuwa status
- `Polub`: Dodaje reakcję do statusu
- `Ogłoś`: Promuje status do osi czasu podmiotu
- `Cofnij`: Anuluje `Polub` lub `Ogłoś`

### Kolekcje
Listy oraz książki użytkownika są reprezentowane przez [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Obiekty

- `Półka`: Kolekcja książek użytkownika. Domyślnie, każdy użytkownik posiada półkę `do przeczytania`, `czytane` oraz `przeczytane`, które są używane do bycia na bieżąco z postępem czytania.
- `Lista`: Kolekcja książek, która może zawierać elementy od użytkowników innych niż jej autor.

#### Aktywności

- `Utwórz`: Dodaje półkę lub listę do bazy danych.
- `Usuń`: Usuwa półkę lub listę.
- `Dodaj`: Dodaje książkę na półkę lub do listy.
- `Usuń`: Usuwa książkę z półki lub listy.


## Alternatywna serializacja
BookWyrm wykorzystuje niestandardowe typy obiektów (`Recenzja`, `Komentarz`, `Cytat`), które nie są obsługiwane przez ActivityPub, dlatego statusy są zamieniane na standardowe typy, gdy są wysyłane do lub wyświetlane w usługach poza BookWyrm. `Recenzja` jest konwertowana na `Artykuł`, a `Komentarz` oraz `Cytat` są konwertowane na `Notatki` z odnośnikiem do książki oraz załączonym obrazem okładki.
