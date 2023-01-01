- - -
Title: ActivitatePub Date: 2021-04-20 Order: 1
- - -

BookWyrm folosește protocolul [ActivityPub](http://activitypub.rocks/) pentru a trimite și primi activitatea utilizatorului între alte instanțe BookWyrm și alte servicii care implementează ActivityPub, precum [Mastodon](https://joinmastodon.org/). Pentru a gestiona datele cărților, BookWyrm are câteva tipuri Activity extinse care nu fac parte din standard, dar înțelese de alte instanțe BookWyrm.

## Activități și obiecte

### Utilizatori și relații
Interacțiunile dintre relațiile utilizatorilor respectă specificația ActivityPub.

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
- `Review`: A review is a status in response to a book (indicated by the `inReplyToBook` field), which has a title, body, and numerical rating between 0 (not rated) and 5.
- `Comentariu`: un comentariu despre o carte menționează cartea respectivă și are un corp de mesaj.
- `Quotation`: A quote has a message body, an excerpt from a book, and mentions a book.


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
Cărțile și listele utilizatorului sunt reprezentate de [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Obiecte

- `Shelf`: o colecție de cărți a utilizatorului. În mod implicit, fiecare utilizator are un raft „`de citit`”, „`în curs de citire`” și „`citit`” pentru a urmări progresul de lectură.
- `List`: o colecție de cărți care poate avea articole contribuite de alți utilizatori.

#### Activități

- `Create`: adaugă un raft sau o listă în baza de date.
- `Delete`: înlătură un raft sau o listă.
- `Add`: adaugă o carte pe un raft sau într-o listă.
- `Remove`: înlătură o carte de pe un raft sau dintr-o listă.


## Serializare alternativă
Deoarece BookWyrm folosește propriile tipuri de obiecte (`Review`, `Comment`, `Quotation`) care nu sunt suportate de ActivityPub, stările sunt transformate în tipuri standard când sunt trimise sau vizualizate de servicii din afara BookWyrm. `Review`s sunt convertite în `Article`s, iar `Comment`s și `Quotation`s sunt convertite în `Note`s cu o legătură către cartea și imaginea de copertă atașate.
