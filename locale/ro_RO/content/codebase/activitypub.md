- - -
Title: ActivitatePub Date: 2021-04-20 Order: 1
- - -

BookWyrm uses the [ActivityPub](http://activitypub.rocks/) protocol to send and receive user activity between other BookWyrm instances and other services that implement ActivityPub, like [Mastodon](https://joinmastodon.org/). To handle book data, BookWyrm has a handful of extended Activity types which are not part of the standard, but are legible to other BookWyrm instances.

## Activități și obiecte

### Utilizatori și relații
User relationship interactions follow the standard ActivityPub spec.

- `Follow`: solicitați să primiți stări de la un utilizator și să le vizualizați pe cele cu confidențialitatea „numai urmăritori”
- `Accept`: aprobă o `cerere de urmărire` și finalizează relația
- `Reject`: respinge o `cerere de urmărire`
- `Block`: împiedică utilizatorii de a își vedea unul altuia stările și împiedică utilizatorul blocat de a vizualiza profilul actorului
- `Update`: actualizează profilul și setările unui utilizator
- `Delete`: dezactivează un utilizator
- `Undo`: anulează o `cerere de urmărire` sau `de blocare`

### Stări
#### Tipuri de obiecte

- `Notă`: pe servicii precum Mastodon, `Notele` sunt tipul principal de stare. Ele conțin corpul mesajului, atașamentele, pot menționa utilizatori și pot fi răspunsuri la stări de orice tip. În cadrul BookWyrm, `notele` pot fi create ca mesaje directe sau ca răspunsuri la alte stări.
- `Recenzie`: o recenzie este o stare ca răspuns unei cărți (indicat de câmpul `inReplyToBook`), care are un titlu, un corp și o evaluare numerică între 0 (fără evaluare) și 5.
- `Comentariu`: un comentariu despre o carte menționează cartea respectivă și are un corp de mesaj.
- `Citat`: un citat are un corp de mesaj, un extras dintr-o carte pe care o menționează


#### Activități

- `Create`: salvează o nouă stare în baza de date.

   **Note**: BookWyrm acceptă activități de `Create` numai dacă sunt:

   - Mesaje directe (de exemplu `Note` cu nivel de confidențialitate `direct`, care menționează un utilizator local),
   - În legătură cu o carte (de un tip de stare personalizat care include câmpul `inReplyToBook`),
   - Răspunsuri la stări existente salvate în baza de date
- `Delete`: elimină o stare
- `Like`: marchează starea ca favorit
- `Announce`: partajează starea pe fluxul actorului
- `Undo`: anulează `Like` sau `Announce`

### Colecții
User's books and lists are represented by [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Obiecte

- `Shelf`: o colecție de cărți a utilizatorului. În mod implicit, fiecare utilizator are un raft „`de citit`”, „`în curs de citire`” și „`citit`” pentru a urmări progresul de lectură.
- `List`: o colecție de cărți care poate avea articole contribuite de alți utilizatori.

#### Activități

- `Create`: adaugă un raft sau o listă în baza de date.
- `Delete`: înlătură un raft sau o listă.
- `Add`: adaugă o carte pe un raft sau într-o listă.
- `Remove`: înlătură o carte de pe un raft sau dintr-o listă.


## Serializare alternativă
Because BookWyrm uses custom object types (`Review`, `Comment`, `Quotation`) that aren't supported by ActivityPub, statuses are transformed into standard types when sent to or viewed by non-BookWyrm services. `Review`s are converted into `Article`s, and `Comment`s and `Quotation`s are converted into `Note`s, with a link to the book and the cover image attached.
