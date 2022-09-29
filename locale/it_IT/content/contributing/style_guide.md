- - -
Titolo: Guida di stile Data: 20-10-2021 Ordine: 4
- - -

## Pull requests

Quindi vuoi contribuire al codice di BookWyrm: fantastico! Se c'è un problema aperto che si desidera risolvere, è utile commentare il problema in modo che il lavoro non venga duplicato. Cerca di mantenere piccola la portata delle richieste nel pull e focalizzati su un singolo argomento. In questo modo è più facile da rivedere, e se una parte ha bisogno di cambiamenti, non bloccherà le altre parti.

Se non sei sicuro di come risolvere qualcosa, o non sei in grado di aggirare il problema, va benissimo, basta lasciare un commento sulla pull request e lo capiremo 💖.

Pull requests have to pass all the automated checks before they can be merged - this includes style checks, global linters, a security check, and unit tests.

## Linting

### Globale

Usiamo [EditorConfig](https://editorconfig.org) per mantenere costanti le terminazioni di indentazione e di linea.

### Python

BookWyrm utilizza il formattatore del codice [Black](https://github.com/psf/black) per mantenere coerente lo stile del codebase Python. Tutte le nuove richieste sono controllate con le azioni GitHub e puoi risolvere automaticamente i problemi di stile del codice eseguendo `./bw-dev black`

Il codice è anche controllato con Pylint utilizzando le azioni GitHub. Pylint warnings must be addressed before pull requests are merged, but it's a judgement call if the suggestion should be used, or the warning suppressed. To suppress a warning, add a comment at the end of or on the line above the warnings: `# pylint: disable=warning-name`

### Templates (HTML)

Your pull request will also be checked by the [curlylint](https://www.curlylint.org) linter for Django templates.

### CSS

We use [stylelint](https://stylelint.io) to check all CSS rules. As with Pylint [you can disable stylelint](https://stylelint.io/user-guide/ignore-code) for a particular rule, but you will need a good justification for doing so.

### JavaScript

[ESLint](https://eslint.org) checks any JavaScript changes you have made. If ESLint doesn't like your working JavaScript, check the linter message for the exact problem.

## Inclusive Design

Bookwyrm aims to be as inclusive and accessible as possible.

When contributing code, check the [Inclusive Web Design Checklist](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) before you file your pull request. For accessibility advice, [A11Y-101](https://www.a11y-101.com/development) is also a useful source. For information on how to make your page templates multi-lingual, see the [Translations section](/translations.html).

Some particular things that Bookwyrm contributors have found useful to remember are:

### Forms

* Only use `input[type="checkbox"]` or `input[type="radio"]` inside `<label>`
* If you do not place checkboxes and radio buttons inside the `<label>`, the `<label>` should be placed _after_ the element it relates to

### Pulsanti e collegamenti

* Use a `<button>` element for anything that exists to trigger a JavaScript action (e.g. hiding or unhiding a form) or sends a `POST` request (e.g. submitting a form)
* Use an `<a>` element for anything that triggers a `GET` request. Usually, an anchor (`<a>`) element should not be styled as a button (`class="button"`), though there are some exceptions, such as "Cancel" buttons. If in doubt, ask for advice in your pull request
