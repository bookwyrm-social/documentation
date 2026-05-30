- - -
Title: Style Guide Date: 2021-10-20 Order: 3
- - -

## Pull requests

Así que quieres contribuir con código a BookWyrm... ¡Genial! Si hay un problema que te gustaría solucionar, sería útil antes comentarlo para que el trabajo no se duplique. Intenta mantener las pull requests pequeñas y enfocadas a un solo tema en particular. De esa manera será más fácil revisarlo, y si algo necesita modificaciones, no afectará otras partes del código.

Si no sabes cómo arreglar algo, o no te crees capaz de solucionarlo ¡No hay problema! Solo deja un comentario en el pull request y lo trataremos 💖.

Las pull requests deben pasar todas los chequeo automatizados antes de ser fusionadas (incluyendo estilo, global linters, seguridad y testeos).

There are several `./bw-dev` commands you may find helpful for linting and testing prior to pushing your pull request. See [Command Line Tool](cli.html) for all the options available.

## Lint

### Global

Usamos [EditorConfig](https://editorconfig.org) para mantener una identación y fin de línea consistente.

### Python

#### Formatting and linting

BookWyrm uses [ruff](https://docs.astral.sh/ruff) for both code linting (checking for errors) and formatting (ensuring code style is consistent). All new pull requests are checked with GitHub actions, and you can automatically fix code style problems by running `./bw-dev ruff`. For linting errors, you can try `./bw-dev ruff-fix` to automatically fix errors, though this may not always be possible.

Ruff linting warnings must be addressed before pull requests are merged, but it's a judgement call if the suggestion should be used, or the warning suppressed. See [the Ruff projects's documentation on suppressing warnings](https://docs.astral.sh/ruff/linter/#comments) using code comments.

The BookWyrm project previously used `Black` for formatting and `Pylint` for linting. You may notice artefacts such as pylint suppression comments in older code. We are still refining our linting rules so if something seems confusing or not quite right, don't hesitate to ask for advice.

#### Type checking

We are gradually rolling out [static type checking](https://en.wikipedia.org/wiki/Type_system) across the BookWyrm code base. This is a long term project. Whilst it is not compulsory to formally define types in new code, it is strongly recommended. This will help to avoid some more subtle bugs that may not be identified in tests.

We currently use [mypy](https://www.mypy-lang.org) as our static type checker. Find out more about how to use mypy at [the `mypy` project documentation](https://mypy.readthedocs.io/en/stable/).

### Plantillas (HTML)

Tu pull request también será revisado por el linter [curlylint](https://www.curlylint.org) para plantillas de Django.

### CSS

Utilizamos [stylelint](https://stylelint.io) para verificar todas las reglas CSS. Al igual que con Pylint [puedes desactivar stylelint](https://stylelint.io/user-guide/ignore-code) para una regla en particular, aunque necesitarás una buena justificación para hacerlo.

### JavaScript

[ESLint](https://eslint.org) comprueba cualquier cambio de JavaScript que hayas realizado. Si a ESLint no le gusta tu trabajo de JavaScript, comprueba el mensaje del linter para ver el problema exacto.

## Diseño inclusivo

Bookwyrm pretende ser lo más inclusivo y accesible posible.

Cuando contribuyes con el código, chequea la [Inclusive Web Design Checklist](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) antes de presentar tu pull request. Para consejos de accesibilidad, [A11Y-101](https://www.a11y-101.com/development) es una fuente útil. For information on how to make your page templates multi-lingual, see the [Translations section](/translation.html).

Algunas cosas particulares que los colaboradores de Bookwyrm han encontrado útiles para recordar son:

### Formularios

* Solo usar `input[type="checkbox"]` o `input[type="radio"]` dentro de `<label>`
* Si no colocas checkboxes y botones de radio dentro de la `<label>`, el `<label>` debe colocarse _después_ del elemento.

### Botones y enlaces

* Usa `<button>` para activar una acción de JavaScript (por ejemplo: ocultar o desplegar un formulario); o enviar una solicitud `POST`.
* Usa `<a>` para cualquier cosa que active una solicitud `GET`. Usualmente, un ancla (`<a>`) no debe ser diseñado como un botón (`class="button"`), aunque hay algunas excepciones, como los botones de "Cancelar". Ante cualquier duda, pide ayuda en tu pull request.

#### Translations

BookWyrm is an international project and aims to be inclusive of as many languages as possible. All user-facing messages and templates should follow the advice on [translations and gendered language](translation.html).