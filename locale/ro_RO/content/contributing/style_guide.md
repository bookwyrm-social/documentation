- - -
Title: Style Guide Date: 2021-10-20 Order: 3
- - -

## Cereri de extragere (pull requests)

Deci vreți să contribuiți la codul BookWyrm: super! Dacă există un tichet nerezolvat pe care ați vrea să-l rezolvați, este util să lăsați un comentariu pentru ca munca să nu fie duplicată. Încercați să păstrați obiectivul cererilor de extragere mic și concentrat pe o singură temă. În acest fel este mai ușor de revizuit, iar dacă o parte are nevoie de schimbări, nu le va bloca pe celelalte.

Dacă nu sunteți sigur de cum să rezolvați ceva sau nu vă descurcați, este complet în regulă. Doar lăsați un comentariu la cererea de extragere și ne vom descurca 💖.

Cererile de extragere au nevoie de a trece verificările automate înainte de a fi fuzionate. Acestea includ verificări de stil, lintere globale, o verificare de securitate și teste unitare.

There are several `./bw-dev` commands you may find helpful for linting and testing prior to pushing your pull request. See [Command Line Tool](cli.html) for all the options available.

## Linting

### Global

Folosim [EditorConfig](https://editorconfig.org) pentru a menține indentarea și finalul liniilor consecvente.

### Python

#### Formatting and linting

BookWyrm uses [ruff](https://docs.astral.sh/ruff) for both code linting (checking for errors) and formatting (ensuring code style is consistent). All new pull requests are checked with GitHub actions, and you can automatically fix code style problems by running `./bw-dev ruff`. For linting errors, you can try `./bw-dev ruff-fix` to automatically fix errors, though this may not always be possible.

Ruff linting warnings must be addressed before pull requests are merged, but it's a judgement call if the suggestion should be used, or the warning suppressed. See [the Ruff projects's documentation on suppressing warnings](https://docs.astral.sh/ruff/linter/#comments) using code comments.

The BookWyrm project previously used `Black` for formatting and `Pylint` for linting. You may notice artefacts such as pylint suppression comments in older code. We are still refining our linting rules so if something seems confusing or not quite right, don't hesitate to ask for advice.

#### Type checking

We are gradually rolling out [static type checking](https://en.wikipedia.org/wiki/Type_system) across the BookWyrm code base. This is a long term project. Whilst it is not compulsory to formally define types in new code, it is strongly recommended. This will help to avoid some more subtle bugs that may not be identified in tests.

We currently use [mypy](https://www.mypy-lang.org) as our static type checker. Find out more about how to use mypy at [the `mypy` project documentation](https://mypy.readthedocs.io/en/stable/).

### Șabloane (HTML)

Cererile dumneavoastră de extragere vor fi de asemenea verificate de linterul [curlylint](https://www.curlylint.org) pentru șabloanele Django.

### CSS

Folosim [stylelint](https://stylelint.io) pentru a verifica toate regulile CSS. Ca și în cazul lui Pylint [puteți dezactiva stylelint](https://stylelint.io/user-guide/ignore-code) pentru o regulă particulară, dar veți avea nevoie de o bună justificare pentru a face asta.

### JavaScript

[ESLint](https://eslint.org) verifică orice modificare JavaScript pe care ați făcut-o. Dacă lui ESLint nu-i place munca dvs. JavaScript, verificați mesajul linterului pentru problema exactă.

## Design inclusiv

BookWyrm dorește să fie cât mai inclusiv și accesibil posibil.

Când contribuiți la cod, verificați [lista Design Web Inclusiv](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) înainte de a depune cererea dvs. de extragere. Pentru sfaturi de accesibilitate, [A11Y-101](https://www.a11y-101.com/development) este de asemenea o resursă utilă. For information on how to make your page templates multi-lingual, see the [Translations section](/translation.html).

Câteva lucruri care li s-au părut contribuitorilor BookWyrm util de reținut sunt:

### Formulare

* Folosiți numai `input[type="checkbox"]` sau `input[type="radio"]` în interiorul `<label>`
* Dacă nu vă plac casetele de selectare sau butoanele radio în interiorul `<label>`, `<label>` ar trebui plasat _după_ elementul la care se referă

### Butoane și legături

* Folosiți `<button>` pentru orice obiect care declanșează o acțiune JavaScript (de exemplu ascunsul sau afișatul unui formular) sau trimisul unei cereri `POST` (de exemplu trimiterea unui formular)
* Folosiți`<a>` pentru orice obiect care declanșează o cerere `GET`. De obicei, un element ancoră (`<a>`) nu ar trebui stilizat ca un buton (`class="button"`), deși există unele excepții precum butoanele de "Anulați". Dacă aveți dubii, cereți sfaturi în cererile dvs. de extragere

#### Translations

BookWyrm is an international project and aims to be inclusive of as many languages as possible. All user-facing messages and templates should follow the advice on [translations and gendered language](translation.html).