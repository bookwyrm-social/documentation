- - -
Title: Style Guide Date: 2021-10-20 Order: 3
- - -

## Pull requests

So you want to contribute code to BookWyrm: that rules! If there's an open issue that you'd like to fix, it's helpful to comment on the issue so work doesn't get duplicated. Try to keep the scope of pull requests small and focused on a single topic. That way it's easier to review, and if one part needs changes, it won't hold up the other parts.

If you aren't sure how to fix something, or you aren't able to get around to it, that's totally okay, just leave a comment on the pull request and we'll figure it out 💖.

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

### Templates (HTML)

Your pull request will also be checked by the [curlylint](https://www.curlylint.org) linter for Django templates.

### CSS

We use [stylelint](https://stylelint.io) to check all CSS rules. As with Pylint [you can disable stylelint](https://stylelint.io/user-guide/ignore-code) for a particular rule, but you will need a good justification for doing so.

### JavaScript

[ESLint](https://eslint.org) checks any JavaScript changes you have made. If ESLint doesn't like your working JavaScript, check the linter message for the exact problem.

## Inclusive Design

Bookwyrm aims to be as inclusive and accessible as possible.

When contributing code, check the [Inclusive Web Design Checklist](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) before you file your pull request. For accessibility advice, [A11Y-101](https://www.a11y-101.com/development) is also a useful source. For information on how to make your page templates multi-lingual, see the [Translations section](/translation.html).

Some particular things that Bookwyrm contributors have found useful to remember are:

### Forms

* Only use `input[type="checkbox"]` or `input[type="radio"]` inside `<label>`
* If you do not place checkboxes and radio buttons inside the `<label>`, the `<label>` should be placed _after_ the element it relates to

### Buttons and Links

* Use a `<button>` element for anything that exists to trigger a JavaScript action (e.g. hiding or unhiding a form) or sends a `POST` request (e.g. submitting a form)
* Use an `<a>` element for anything that triggers a `GET` request. Usually, an anchor (`<a>`) element should not be styled as a button (`class="button"`), though there are some exceptions, such as "Cancel" buttons. If in doubt, ask for advice in your pull request

#### Translations

BookWyrm is an international project and aims to be inclusive of as many languages as possible. All user-facing messages and templates should follow the advice on [translations and gendered language](translation.html).