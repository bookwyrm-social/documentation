BookWyrm folosește protocolul [ActivityPub](http://activitypub.rocks/) pentru a trimite și primi activitatea utilizatorului între alte instanțe BookWyrm și alte servicii care implementează ActivityPub, precum [Mastodon](https://joinmastodon.org/). Pentru a gestiona datele cărților, BookWyrm are câteva tipuri Activity extinse care nu fac parte din standard, dar înțelese de alte instanțe BookWyrm.

## Activități și obiecte

### Utilizatori și relații
Interacțiunile dintre relațiile utilizatorilor respectă specificația ActivityPub.

- `Urmăriți`: solicitați să primiți stări de la un utilizator și să le vizualizați pe cele cu confidențialitatea „numai urmăritori”
- `Acceptați`: aprobă o `cerere de urmărire` și finalizează relația
- `Refuzați`: respinge o `cerere de urmărire`
- `Blocați`: împiedică utilizatorii de a își vedea unul altuia stările și împiedică utilizatorul blocat de a vizualiza profilul actorului
- `Actualizați`: actualizează profilul și setările unui utilizator
- `Ștergeți`: dezactivează un utilizator
- `Revocați`: anulează o `cerere de urmărire` sau `de blocare`

### Stări
#### Tipuri de obiecte

- `Notă`: pe servicii precum Mastodon, `Notele` sunt tipul principal de stare. Ele conțin corpul mesajului, atașamentele, pot menționa utilizatori și pot fi răspunsuri la stări de orice tip. În cadrul BookWyrm, `notele` pot fi create ca mesaje directe sau ca răspunsuri la alte stări.
- `Recenzie`: o recenzie este o stare ca răspuns unei cărți (indicat de câmpul `inReplyToBook`), care are un titlu, un corp și o evaluare numerică între 0 (fără evaluare) și 5.
- `Comentariu`: un comentariu despre o carte menționează cartea respectivă și are un corp de mesaj.
- `Citat`: un citat are un corp de mesaj, un extras dintr-o carte pe care o menționează


#### Activități

- `Creați`: salvează o nouă stare în baza de date.

   **Notă**: BookWyrm acceptă activități de `creare` numai dacă sunt:

   - Mesaje directe (de exemplu `Note` cu nivel de confidențialitate `direct`, care menționează un utilizator local),
   - În legătură cu o carte (de un tip de stare personalizat care include câmpul `inReplyToBook`),
   - Răspunsuri la stări existente salvate în baza de date
- `Ștergeți`: elimină o stare
- `Îmi place`: marchează starea ca favorit
- `Anunțați`: partajează starea pe fluxul actorului
- `Revocați`: anulează `îmi place` sau `anunțați`

### Colecții
Cărțile și listele utilizatorului sunt reprezentate de [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Obiecte

- `Raft`: o colecție de cărți a utilizatorului. În mod implicit, fiecare utilizator are un raft „`de citit`”, „`în curs de citire`” și „`citit`” pentru a urmări progresul de lectură.
- `Listă`: o colecție de cărți care poate avea articole contribuite de alți utilizatori.

#### Activități

- `Creați`: adaugă un raft sau o listă în baza de date.
- `Ștergeți`: înlătură un raft sau o listă.
- `Adăugați`: adaugă o carte pe un raft sau într-o listă.
- `Înlăturați`: înlătură o carte de pe un raft sau dintr-o listă.


## Serializare alternativă
Deoarece BookWyrm folosește propriile tipuri de obiecte (`Recenzie`, `Comentariu`, `Citat`) care nu sunt suportate de ActivityPub, stările sunt transformate în tipuri standard când sunt trimise sau vizualizate de servicii din afara BookWyrm. `Recenziile` sunt convertite în `Articole`, iar `Comentariile` și `Citatele` sunt convertite în `Note` cu o legătură către cartea și imaginea de copertă atașate.
