- - -
Titel: Stijlgids Datum: 2021-10-20 order: 4
- - -

## Pull-aanvragen

Dus je wilt je code bijdragen aan BookWyrm: cool! If there's an open issue that you'd like to fix, it's helpful to comment on the issue so work doesn't get duplicated. Probeer het bereik van pull-requests klein en gefocust te houden op één enkel onderwerp. That way it's easier to review, and if one part needs changes, it won't hold up the other parts.

If you aren't sure how to fix something, or you aren't able to get around to it, that's totally okay, just leave a comment on the pull request and we'll figure it out 💖.

Pull requests have to pass all the automated checks before they can be merged - this includes style checks, global linters, a security check, and unit tests.

## Linting

### Globaal

We use [EditorConfig](https://editorconfig.org) to maintain consistent indenting and line endings.

### Python

BookWyrm uses the [Black](https://github.com/psf/black) code formatter to keep the Python codebase consistent styled. All new pull requests are checked with GitHub actions, and you can automatically fix code style problems by running `./bw-dev black`

Code is also checked with Pylint using GitHub Actions. Pylint warnings must be addressed before pull requests are merged, but it's a judgement call if the suggestion should be used, or the warning suppressed. To suppress a warning, add a comment at the end of or on the line above the warnings: `# pylint: disable=warning-name`

### Sjablonen (HTML)

Your pull request will also be checked by the [curlylint](https://www.curlylint.org) linter for Django templates.

### CSS

We use [stylelint](https://stylelint.io) to check all CSS rules. As with Pylint [you can disable stylelint](https://stylelint.io/user-guide/ignore-code) for a particular rule, but you will need a good justification for doing so.

### JavaScript

[ESLint](https://eslint.org) checks any JavaScript changes you have made. If ESLint doesn't like your working JavaScript, check the linter message for the exact problem.

## Inclusief ontwerp

Bookwyrm streeft ernaar zo inclusief en toegankelijk mogelijk te zijn.

When contributing code, check the [Inclusive Web Design Checklist](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) before you file your pull request. For accessibility advice, [A11Y-101](https://www.a11y-101.com/development) is also a useful source. For information on how to make your page templates multi-lingual, see the [Translations section](/translations.html).

Some particular things that Bookwyrm contributors have found useful to remember are:

### Formulieren

* Only use `input[type="checkbox"]` or `input[type="radio"]` inside `<label>`
* If you do not place checkboxes and radio buttons inside the `<label>`, the `<label>` should be placed _after_ the element it relates to

### Knoppen en links

* Use a `<button>` element for anything that exists to trigger a JavaScript action (e.g. hiding or unhiding a form) or sends a `POST` request (e.g. submitting a form)
* Use an `<a>` element for anything that triggers a `GET` request. Usually, an anchor (`<a>`) element should not be styled as a button (`class="button"`), though there are some exceptions, such as "Cancel" buttons. If in doubt, ask for advice in your pull request
