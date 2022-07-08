## Cereri de extragere (pull requests)

Deci vreți să contribuiți la codul BookWyrm: super! Dacă există un tichet nerezolvat pe care ați vrea să-l rezolvați, este util să lăsați un comentariu pentru ca munca să nu fie duplicată. Încercați să păstrați obiectivul cererilor de extragere mic și concentrat pe o singură temă. În acest fel este mai ușor de revizuit, iar dacă o parte are nevoie de schimbări, nu le va bloca pe celelalte.

Dacă nu sunteți sigur de cum să rezolvați ceva sau nu vă descurcați, este complet în regulă. Doar lăsați un comentariu la cererea de extragere și ne vom descurca 💖.

Cererile de extragere au nevoie de a trece verificările automate înainte de a fi fuzionate. Acestea includ verificări de stil, lintere globale, o verificare de securitate și teste unitare.

## Linting

### Global

Folosim [EditorConfig](https://editorconfig.org) pentru a menține indentarea și finalul liniilor consecvente.

### Python

BookWyrm folosește formatorul de cod [Black](https://github.com/psf/black) pentru a menține stilul codului consistent. Toate cererile noi de extragere sunt verificate cu acțiunile GitHub și puteți regla în modul automat problemele de stil de cod rulând `./bw-dev black`

Codul este de asemenea verificat cu Pylint folosind acțiunile GitHub. Avertismentele Pylint trebuie abordate înainte ca cererile de extragere să fie fuzionate, dar este un apel de judecată dacă sugestia ar trebui folosită sau suprimată. Pentru a șterge un avertisment, adăugați un comentariu la finalul sau deasupra avertismentului: `# pylint: disable=warning-name`

### Șabloane (HTML)

Cererile dumneavoastră de extragere vor fi de asemenea verificate de linterul [curlylint](https://www.curlylint.org) pentru șabloanele Django.

### CSS

Folosim [stylelint](https://stylelint.io) pentru a verifica toate regulile CSS. Ca și în cazul lui Pylint [puteți dezactiva stylelint](https://stylelint.io/user-guide/ignore-code) pentru o regulă particulară, dar veți avea nevoie de o bună justificare pentru a face asta.

### JavaScript

[ESLint](https://eslint.org) verifică orice modificare JavaScript pe care ați făcut-o. Dacă lui ESLint nu-i place munca dvs. JavaScript, verificați mesajul linterului pentru problema exactă.

## Design inclusiv

BookWyrm dorește să fie cât mai inclusiv și accesibil posibil.

Când contribuiți la cod, verificați [lista Design Web Inclusiv](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) înainte de a depune cererea dvs. de extragere. Pentru sfaturi de accesibilitate, [A11Y-101](https://www.a11y-101.com/development) este de asemenea o resursă utilă. Pentru informații despre cum să faceți șablonul de pagină bilingv, consultați [secțiunea de Traduceri](/translations.html).

Câteva lucruri care li s-au părut contribuitorilor BookWyrm util de reținut sunt:

### Formulare

* Folosiți numai `input[type="checkbox"]` sau `input[type="radio"]` în interiorul `<label>`
* Dacă nu vă plac casetele de selectare sau butoanele radio în interiorul `<label>`, `<label>` ar trebui plasat _după_ elementul la care se referă

### Butoane și legături

* Folosiți `<button>` pentru orice obiect care declanșează o acțiune JavaScript (de exemplu ascunsul sau afișatul unui formular) sau trimisul unei cereri `POST` (de exemplu trimiterea unui formular)
* Folosiți`<a>` pentru orice obiect care declanșează o cerere `GET`. De obicei, un element ancoră (`<a>`) nu ar trebui stilizat ca un buton (`class="button"`), deși există unele excepții precum butoanele de "Anulați". Dacă aveți dubii, cereți sfaturi în cererile dvs. de extragere
