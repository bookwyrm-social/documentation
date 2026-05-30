- - -
Title: Style Guide Date: 2021-10-20 Order: 3
- - -

## Pull requests

Então você quer contribuir com a BookWyrm? Show! Se houver algum problema aberto no repositório que você quer consertar, deixer um comentário para que o trabalho não seja feito mais de uma vez. Tente manter o escopo dos pull requests pequenos e focados em uma única questão. Assim é mais fácil revisar, e se alguma parte precisar ser alterada, isso não atrapalhará as outras partes.

Se você não sabe exatamente como consertar alguma coisa, ou se não consegue fazê-lo, está tudo bem! Só deixe um comentário no pull request e vamos descobrir 💖.

Os pull requests passam por todas as verificações automáticas antes de serem mesclados - isso inclui verificações de estilos, linters globais, uma verificação de segurança e testes unitários.

There are several `./bw-dev` commands you may find helpful for linting and testing prior to pushing your pull request. See [Command Line Tool](cli.html) for all the options available.

## Linting

### Global

Usamos o [EditorConfig](https://editorconfig.org) para manter uma identação e fins de linha consistentes.

### Python

#### Formatting and linting

BookWyrm uses [ruff](https://docs.astral.sh/ruff) for both code linting (checking for errors) and formatting (ensuring code style is consistent). All new pull requests are checked with GitHub actions, and you can automatically fix code style problems by running `./bw-dev ruff`. For linting errors, you can try `./bw-dev ruff-fix` to automatically fix errors, though this may not always be possible.

Ruff linting warnings must be addressed before pull requests are merged, but it's a judgement call if the suggestion should be used, or the warning suppressed. See [the Ruff projects's documentation on suppressing warnings](https://docs.astral.sh/ruff/linter/#comments) using code comments.

The BookWyrm project previously used `Black` for formatting and `Pylint` for linting. You may notice artefacts such as pylint suppression comments in older code. We are still refining our linting rules so if something seems confusing or not quite right, don't hesitate to ask for advice.

#### Type checking

We are gradually rolling out [static type checking](https://en.wikipedia.org/wiki/Type_system) across the BookWyrm code base. This is a long term project. Whilst it is not compulsory to formally define types in new code, it is strongly recommended. This will help to avoid some more subtle bugs that may not be identified in tests.

We currently use [mypy](https://www.mypy-lang.org) as our static type checker. Find out more about how to use mypy at [the `mypy` project documentation](https://mypy.readthedocs.io/en/stable/).

### Templates (HTML)

Suas pull requests também vão ser verificadas pelo linter [curlylint](https://www.curlylint.org) dos templates do Django.

### CSS

Usamos o [stylelint](https://stylelint.io) para conferir todas as regras de CSS. Como no Pylint, [você pode disativar o stylelint](https://stylelint.io/user-guide/ignore-code) para alguma regra particular, mas você vai precisar de uma boa justificativa para fazê-lo.

### JavaScript

[ESLint](https://eslint.org) verifica todas as modificações em JavaScript que você fizer. Se o ESLint não gostar do seu JavaScript, dê uma olhada na mensagem do linter para ver qual é o problema.

## Design inclusivo

A BookWyrm quer ser o mais inclusiva e acessível possível.

Quando for contribuir com código, dê uma olhada na [Check list de web design inclusivo](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) antes de enviar o pull request. Para sugestões de acessibilidade, o [A11Y-101](https://www.a11y-101.com/development) também é uma fonte útil. For information on how to make your page templates multi-lingual, see the [Translations section](/translation.html).

Algumas coisas que colaboradores da BookWyrm acharam boas de se lembrar:

### Formulários

* Só use `input[type="checkbox"]` ou `input[type="radio"]` dentro `<label>`
* Se você não colocar os botões de checkbox e radio dentro do `<label>`, o `<label>` deve ser colocado _depois_ do elemento ao que ele está relacionado

### Botões e links

* Use um elemento `<button>` para tudo que sirva para disparar uma ação de JavaScript (ex: esconder ou mostrar um formulário) ou enviar uma solicitação `POST` (ex: enviar um formulário)
* Use um elemento `<a>` para tudo que faça uma solicitação `GET`. Normalmente um elemento de âncora (`<a>`) não costuma ser estilizado como um botão (`class="button"`), mas há algumas exceções, como os botões de "Cancelar". Se tiver alguma dúvida, peça sugestões no seu pull request

#### Translations

BookWyrm is an international project and aims to be inclusive of as many languages as possible. All user-facing messages and templates should follow the advice on [translations and gendered language](translation.html).