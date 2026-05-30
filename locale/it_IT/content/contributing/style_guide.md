- - -
Title: Style Guide Date: 2021-10-20 Order: 3
- - -

## Pull requests

Quindi vuoi contribuire al codice di BookWyrm: fantastico! Se c'è un problema aperto che si desidera risolvere, è utile commentare il problema in modo che il lavoro non venga duplicato. Cerca di mantenere piccola la portata delle richieste nel pull e focalizzati su un singolo argomento. In questo modo è più facile da rivedere, e se una parte ha bisogno di cambiamenti, non bloccherà le altre parti.

Se non sei sicuro di come risolvere qualcosa, o non sei in grado di aggirare il problema, va benissimo, basta lasciare un commento sulla pull request e lo capiremo 💖.

Le richieste di prelievo devono superare tutti i controlli automatici prima che possano essere uniti - questo include controlli di stile, linters globali, un controllo di sicurezza e test di unità.

There are several `./bw-dev` commands you may find helpful for linting and testing prior to pushing your pull request. See [Command Line Tool](cli.html) for all the options available.

## Linting

### Globale

Usiamo [EditorConfig](https://editorconfig.org) per mantenere costanti le terminazioni di indentazione e di linea.

### Python

#### Formatting and linting

BookWyrm uses [ruff](https://docs.astral.sh/ruff) for both code linting (checking for errors) and formatting (ensuring code style is consistent). All new pull requests are checked with GitHub actions, and you can automatically fix code style problems by running `./bw-dev ruff`. For linting errors, you can try `./bw-dev ruff-fix` to automatically fix errors, though this may not always be possible.

Ruff linting warnings must be addressed before pull requests are merged, but it's a judgement call if the suggestion should be used, or the warning suppressed. See [the Ruff projects's documentation on suppressing warnings](https://docs.astral.sh/ruff/linter/#comments) using code comments.

The BookWyrm project previously used `Black` for formatting and `Pylint` for linting. You may notice artefacts such as pylint suppression comments in older code. We are still refining our linting rules so if something seems confusing or not quite right, don't hesitate to ask for advice.

#### Type checking

We are gradually rolling out [static type checking](https://en.wikipedia.org/wiki/Type_system) across the BookWyrm code base. This is a long term project. Whilst it is not compulsory to formally define types in new code, it is strongly recommended. This will help to avoid some more subtle bugs that may not be identified in tests.

We currently use [mypy](https://www.mypy-lang.org) as our static type checker. Find out more about how to use mypy at [the `mypy` project documentation](https://mypy.readthedocs.io/en/stable/).

### Templates (HTML)

La tua richiesta di pull sarà anche controllata dall'linter [curlylint](https://www.curlylint.org) per i modelli Django.

### CSS

Usiamo [stylelint](https://stylelint.io) per controllare tutte le regole CSS. Come con Pylint [puoi disabilitare stylelint](https://stylelint.io/user-guide/ignore-code) per una regola particolare, ma avrai bisogno di una buona motivazione per farlo.

### JavaScript

[ESLint](https://eslint.org) controlla qualsiasi modifica JavaScript che hai apportato. Se a ESLint non piace il tuo JavaScript, controlla il messaggio linter per verificare il problema esatto.

## Progettazione Inclusiva

Bookwyrm mira a essere il più completo e accessibile possibile.

Quando si contribuisce con il codice, controllare la checklist [Inclusive Web Design Checklist](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) prima di archiviare la tua richiesta pull. Per la consulenza in materia di accessibilità, [A11Y-101](https://www.a11y-101.com/development) è anche una fonte utile. For information on how to make your page templates multi-lingual, see the [Translations section](/translation.html).

Alcune cose particolari che i contributori di Bookwyrm hanno trovato utili per ricordare sono:

### Moduli

* Utilizza solo `input[type="checkbox"]` o `input[type="radio"]` dentro `<label>`
* Se non piazzi caselle di controllo e pulsanti radio all'interno del `<label>`, il `<label>` dovrebbe essere posizionato _dopo_ l'elemento cui si riferisce

### Tasti e collegamenti

* Usa un elemento `<button>` per qualsiasi cosa esistente per attivare un'azione JavaScript (e.. nascondere o svuotare una forma) o invia una richiesta `POST` (ad esempio inviare un modulo)
* Usa un elemento `<a>` per tutto quello che attiva una richiesta `GET`. Di solito, un elemento di ancoraggio (`<a>`) non dovrebbe essere stilato come pulsante (`class="pulsante"`), anche se ci sono alcune eccezioni, come i pulsanti "Annulla". In caso di dubbio, chieda consiglio nella tua pull request

#### Translations

BookWyrm is an international project and aims to be inclusive of as many languages as possible. All user-facing messages and templates should follow the advice on [translations and gendered language](translation.html).