- - -
Title: Style Guide Date: 2021-10-20 Order: 3
- - -

## Prośby o scalenie

Jeśli chcesz udzielić się w kodzie BookWyrm, to świetnie! Jeśli istnieje otwarty problem, który chcesz naprawić, możesz zamieścić komentarz do niego, tak aby niczego nie powielać. Staraj się, aby zakres próśb o scalenie był mały i skupiony na jednym temacie. Dzięki temu łatwiej będzie ją sprawdzić i sprawniej wprowadzić zmiany.

Jeśli nie masz pewności, jak coś naprawić lub nie możesz się za to zabrać, to nic nie szkodzi i wystarczy, że zamieścisz komentarz do prośby o scalenie i wspólnie znajdziemy rozwiązanie 💖.

Pull requests have to pass all the automated checks before they can be merged - this includes style checks, global linters, a security check, and unit tests.

There are several `./bw-dev` commands you may find helpful for linting and testing prior to pushing your pull request. See [Command Line Tool](cli.html) for all the options available.

## Linting

### Global

We use [EditorConfig](https://editorconfig.org) to maintain consistent indenting and line endings.

### Python

#### Formatting and linting

BookWyrm uses [ruff](https://docs.astral.sh/ruff) for both code linting (checking for errors) and formatting (ensuring code style is consistent). All new pull requests are checked with GitHub actions, and you can automatically fix code style problems by running `./bw-dev ruff`. For linting errors, you can try `./bw-dev ruff-fix` to automatically fix errors, though this may not always be possible.

Ruff linting warnings must be addressed before pull requests are merged, but it's a judgement call if the suggestion should be used, or the warning suppressed. See [the Ruff projects's documentation on suppressing warnings](https://docs.astral.sh/ruff/linter/#comments) using code comments.

The BookWyrm project previously used `Black` for formatting and `Pylint` for linting. You may notice artefacts such as pylint suppression comments in older code. We are still refining our linting rules so if something seems confusing or not quite right, don't hesitate to ask for advice.

#### Type checking

We are gradually rolling out [static type checking](https://en.wikipedia.org/wiki/Type_system) across the BookWyrm code base. This is a long term project. Whilst it is not compulsory to formally define types in new code, it is strongly recommended. This will help to avoid some more subtle bugs that may not be identified in tests.

We currently use [mypy](https://www.mypy-lang.org) as our static type checker. Find out more about how to use mypy at [the `mypy` project documentation](https://mypy.readthedocs.io/en/stable/).

### Szablony (HTML)

Twoje prośby o scalenie zostaną również sprawdzone przez [curlylint](https://www.curlylint.org) w poszukiwaniu szablonów Django.

### CSS

Korzystamy z [stylelint](https://stylelint.io), do sprawdzania zasad CSS. Tak jak w przypadku Pylint [możesz wyłączyć stylelint](https://stylelint.io/user-guide/ignore-code) dla konkretnej zasady, ale należy mieć ku temu dobry powód.

### JavaScript

[ESLint](https://eslint.org) sprawdza wszelkie wprowadzone zmiany w JavaScript. Jeśli ESLint nie będzie współpracował z Twoim kodem JavaScript, sprawdź wiadomości narzędzia po więcej informacji.

## Inclusive Design

Celem BookWyrm jest jak największa otwartość i dostępność.

When contributing code, check the [Inclusive Web Design Checklist](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) before you file your pull request. For accessibility advice, [A11Y-101](https://www.a11y-101.com/development) is also a useful source. For information on how to make your page templates multi-lingual, see the [Translations section](/translation.html).

Niektórymi z aspektów, które współtwórcy BookWyrm uznali za przydatne do zapamiętania są:

### Formularze

* Używaj wyłącznie znaczników `input[type="checkbox"]` lub `input[type="radio"]` w znaczniku `<label>`
* Jeśli nie umieścisz pól jedno- i wielokrotnego wyboru w znaczniku `<label>`, wówczas należy go umieścić _za_ elementem, do którego się odwołuje

### Przyciski i odnośniki

* Użyj znacznika `<button>` dla czegokolwiek, co istnieje, aby wywołać instrukcję JavaScript (np. ukrywanie i pokazywanie fomrularza) lub wysyła żądanie `POST` (np. przesłanie formularza)
* Użyj znacznika `<a>` dla czegokolwiek, co wywołuje żądanie `GET`. Zazwyczaj element znacznika odnośnika (`<a>`) nie powinien być stylizowany jako przycisk (`class="button"`), ale istnieje kilka wyjątków, takich jak przyciski "Anuluj". W razie wątpliwości zapytaj o poradę w swojej prośbie o scalenie

#### Translations

BookWyrm is an international project and aims to be inclusive of as many languages as possible. All user-facing messages and templates should follow the advice on [translations and gendered language](translation.html).