- - -
Title: Style Guide Date: 2021-10-20 Order: 3
- - -

## Pull Requests

Du möchstest also Code zu BookWyrm hinzufügen: Das ist klasse! Wenn es ein offenes Problem gibt, dass du beheben möchtest, ist es hilfreich, das Problem zu kommentieren, damit die Arbeit nicht dupliziert wird. Versuche den Umfang von Pull Requests kleinzuhalten und konzentriere dich auf ein einzelnes Thema. Auf diese Weise ist es einfacher zu überprüfen und wenn ein Teil Änderungen braucht, wird er die anderen Teile nicht aufhalten.

Wenn du nicht weißt, wie man etwas fixt oder etwas nicht schaffst: Kein Problem. Hinterlasse einen Kommentar im Pull Request und wir versuchen es, herauszufinden 💖.

Pull-Anfragen müssen alle automatisierten Prüfungen bestehen, bevor sie übernommen werden können - dazu gehören Stil-Prüfungen, globale Linter, eine Sicherheitsprüfung und Unit-Tests.

There are several `./bw-dev` commands you may find helpful for linting and testing prior to pushing your pull request. See [Command Line Tool](cli.html) for all the options available.

## Linten

### Global

Wir verwenden [EditorConfig](https://editorconfig.org), um konsistente Einrückungen und Zeilenenden zu erhalten.

### Python

#### Formatting and linting

BookWyrm uses [ruff](https://docs.astral.sh/ruff) for both code linting (checking for errors) and formatting (ensuring code style is consistent). All new pull requests are checked with GitHub actions, and you can automatically fix code style problems by running `./bw-dev ruff`. For linting errors, you can try `./bw-dev ruff-fix` to automatically fix errors, though this may not always be possible.

Ruff linting warnings must be addressed before pull requests are merged, but it's a judgement call if the suggestion should be used, or the warning suppressed. See [the Ruff projects's documentation on suppressing warnings](https://docs.astral.sh/ruff/linter/#comments) using code comments.

The BookWyrm project previously used `Black` for formatting and `Pylint` for linting. You may notice artefacts such as pylint suppression comments in older code. We are still refining our linting rules so if something seems confusing or not quite right, don't hesitate to ask for advice.

#### Type checking

We are gradually rolling out [static type checking](https://en.wikipedia.org/wiki/Type_system) across the BookWyrm code base. This is a long term project. Whilst it is not compulsory to formally define types in new code, it is strongly recommended. This will help to avoid some more subtle bugs that may not be identified in tests.

We currently use [mypy](https://www.mypy-lang.org) as our static type checker. Find out more about how to use mypy at [the `mypy` project documentation](https://mypy.readthedocs.io/en/stable/).

### Vorlagen (HTML)

Dein Pull-Request wird auch durch den [curlylint](https://www.curlylint.org)-Linter für Django-Templates überprüft.

### CSS

Wir verwenden [stylelint](https://stylelint.io), um alle CSS-Regeln zu überprüfen. Wie bei Pylint [kannst du styelint](https://stylelint.io/user-guide/ignore-code) für eine bestimmte Regel deaktivieren, aber du benötigst dafür eine gute Rechtfertigung.

### JavaScript

[ESLint](https://eslint.org) überprüft alle von Ihnen vorgenommenen JavaScript-Änderungen. Falls ESLint dein funktionierendes JavaScript nicht mag, überprüfe die Linter-Meldung auf das genaue Problem.

## Inklusives Design

Bookwyrm hat zum Ziel, so umfassend und zugänglich wie möglich zu sein.

Überprüfen Sie die [Checkliste für inklusives Web Design](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) bevor du einen Pull-Reuqest erstellst. Für Barrierefreiheit ist [A11Y-101](https://www.a11y-101.com/development) ebenfalls eine nützliche Quelle. For information on how to make your page templates multi-lingual, see the [Translations section](/translation.html).

Einige besondere Dinge, die Bookwyrm-Beitragende für nützlich erachtet haben, sind:

### Formulare

* Verwende nur `input[type="checkbox"]` oder `input[type="radio"]` in `<label>`
* Wenn du die Checkboxen und die Radiobuttons nicht innerhalb des `<label>`platzierst, sollte das `<label>` _nach_ dem Element platziert werden, auf das es sich bezieht

### Buttons und Links

* Verwende ein `<button>` Element für alles, was existiert, um eine JavaScript-Aktion auszulösen (z.B. ein Formular verstecken oder enthüllen) oder eine `POST`-Anfrage senden (z.B. ein Formular übermitteln)
* Verwende ein `<a>`-Element für alles, was eine `GET`-Anfrage auslöst. Normalerweise sollte ein Ankerelement (`<a>`) nicht als Button (`class="button"`) dargestellt werden, obwohl es einige Ausnahmen gibt, wie z. B. "Abbrechen"-Buttons. Falls Sie Zweifel haben, fragen Sie in Ihrer Pull-Anfrage um Rat

#### Translations

BookWyrm is an international project and aims to be inclusive of as many languages as possible. All user-facing messages and templates should follow the advice on [translations and gendered language](translation.html).