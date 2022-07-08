- - -
Title: Style Guide Date: 2021-10-20 Order: 4
- - -

## Pull requests

So you want to contribute code to BookWyrm: that rules! If there's an open issue that you'd like to fix, it's helpful to comment on the issue so work doesn't get duplicated. Try to keep the scope of pull requests small and focused on a single topic. That way it's easier to review, and if one part needs changes, it won't hold up the other parts.

If you aren't sure how to fix something, or you aren't able to get around to it, that's totally okay, just leave a comment on the pull request and we'll figure it out 💖.

Pull requests have to pass all the automated checks before they can be merged - this includes style checks, global linters, a security check, and unit tests.

## Linting

### Global

We use [EditorConfig](https://editorconfig.org) to maintain consistent indenting and line endings.

### Python

BookWyrm uses the [Black](https://github.com/psf/black) code formatter to keep the Python codebase consistent styled. All new pull requests are checked with GitHub actions, and you can automatically fix code style problems by running `./bw-dev black`

Code is also checked with Pylint using GitHub Actions. Pylint warnings must be addressed before pull requests are merged, but it's a judgement call if the suggestion should be used, or the warning suppressed. To suppress a warning, add a comment at the end of or on the line above the warnings: `# pylint: disable=warning-name`

### Templates (HTML)

Your pull request will also be checked by the [curlylint](https://www.curlylint.org) linter for Django templates.

### CSS

We use [stylelint](https://stylelint.io) to check all CSS rules. As with Pylint [you can disable stylelint](https://stylelint.io/user-guide/ignore-code) for a particular rule, but you will need a good justification for doing so.

### JavaScript

[ESLint](https://eslint.org) checks any JavaScript changes you have made. If ESLint doesn't like your working JavaScript, check the linter message for the exact problem.

## Design inclusivo

Bookwyrm aims to be as inclusive and accessible as possible.

When contributing code, check the [Inclusive Web Design Checklist](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) before you file your pull request. For accessibility advice, [A11Y-101](https://www.a11y-101.com/development) is also a useful source. For information on how to make your page templates multi-lingual, see the [Translations section](/translations.html).

Some particular things that Bookwyrm contributors have found useful to remember are:

### Formulários

* Só use `input[type="checkbox"]` ou `input[type="radio"]` dentro `<label>`
* Se você não colocar os botões de checkbox e radio dentro do `<label>`, o `<label>` deve ser colocado _depois_ do elemento ao que ele está relacionado

### Botões e links

* Use um elemento `<button>` para tudo que sirva para disparar uma ação de JavaScript (ex: esconder ou mostrar um formulário) ou enviar uma solicitação `POST` (ex: enviar um formulário)
* Use um elemento `<a>` para tudo que faça uma solicitação `GET`. Normalmente um elemento de âncora (`<a>`) não costuma ser estilizado como um botão (`class="button"`), mas há algumas exceções, como os botões de "Cancelar". Se tiver alguma dúvida, peça sugestões no seu pull request
