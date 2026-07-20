- - -
Title: Style Guide Date: 2021-10-20 Order: 3
- - -

## Sol·licitud d'extracció

Així que vols contribuir al codi de BookWyrm: genial! Si hi ha alguna incidència oberta que vulgueu solucionar, poseu-hi un comentari per a evitar duplicacions de feina. Intenteu mantenir petits i enfocats a un sol tema concret l'abast dels pull requests. Aquesta manera és més fàcil de revisar i, si una part necessita canvis, no interferirà en les altres.

Si no tens clar com arreglar alguna cosa o no te'n surts, cap problema. Simplement deixa un comentari a la petició i ja ho trobarem.

Les pull requests han de passar tots els controls automàtics abans que es fusionin. Això inclou fer verificacions d'estil, linters globals, una verificació de seguretat i tests unitaris.

There are several `./bw-dev` commands you may find helpful for linting and testing prior to pushing your pull request. See [Command Line Tool](cli.html) for all the options available.

## Lint

### Global

Fem ús d'[EditorConfig](https://editorconfig.org) per mantenir sagnats i finals de línia consistents.

### Python

#### Formatting and linting

BookWyrm uses [ruff](https://docs.astral.sh/ruff) for both code linting (checking for errors) and formatting (ensuring code style is consistent). All new pull requests are checked with GitHub actions, and you can automatically fix code style problems by running `./bw-dev ruff`. For linting errors, you can try `./bw-dev ruff-fix` to automatically fix errors, though this may not always be possible.

Ruff linting warnings must be addressed before pull requests are merged, but it's a judgement call if the suggestion should be used, or the warning suppressed. See [the Ruff projects's documentation on suppressing warnings](https://docs.astral.sh/ruff/linter/#comments) using code comments.

The BookWyrm project previously used `Black` for formatting and `Pylint` for linting. You may notice artefacts such as pylint suppression comments in older code. We are still refining our linting rules so if something seems confusing or not quite right, don't hesitate to ask for advice.

#### Type checking

We are gradually rolling out [static type checking](https://en.wikipedia.org/wiki/Type_system) across the BookWyrm code base. This is a long term project. Whilst it is not compulsory to formally define types in new code, it is strongly recommended. This will help to avoid some more subtle bugs that may not be identified in tests.

We currently use [mypy](https://www.mypy-lang.org) as our static type checker. Find out more about how to use mypy at [the `mypy` project documentation](https://mypy.readthedocs.io/en/stable/).

### Plantilles (HTML)

El teu pull request també el comprovarà el linter [curlyint](https://www.curlylint.org) per plantilles Django.

### CSS

Fem servir [stylelint](https://stylelint.io) per validar totes les regles CSS. Com amb Pylint [pots deshabilitar stylelint](https://stylelint.io/user-guide/ignore-code) per a una regla en particular, però et caldrà una bona raó.

### JavaScript

L'[ESLint](https://eslint.org) comprova tots els canvis de JavaScript que facis. Si a l'ESLint no li agrada el teu JavaScript, mira el missatge linter per trobar quin és el problema exacte.

## Disseny inclusiu

BookWyrm intenta ser tan inclusiu i accessible com sigui possible.

Si contribueixes en el codi, comprova la [Llista de comprovacions per al disseny web inclusiu](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) abans de fer el teu pull request. Per a consells sobre accessibilitat, [A11Y-101](https://www.a11y-101.com/development) també pot ser una font útil. For information on how to make your page templates multi-lingual, see the [Translations section](/translation.html).

Algunes particularitats que els contribuïdors de BookWyrm han trobat útils són:

### Formularis

* Fes servir `input[type="checkbox"]` o `input[type="radio"]` només a dins de <0>&lt;label&gt;</0>
* Si no col·loques els elements checkbbox i radio dins de `<label>`, el `<label>` s'haurà de col·locar _després_ de l'element a què es refereix

### Botons i enllaços

* Use a `<button>` element for anything that exists to trigger a JavaScript action (e.g. hiding or unhiding a form) or sends a `POST` request (e.g. submitting a form)
* Use an `<a>` element for anything that triggers a `GET` request. Usually, an anchor (`<a>`) element should not be styled as a button (`class="button"`), though there are some exceptions, such as "Cancel" buttons. If in doubt, ask for advice in your pull request

#### Translations

BookWyrm is an international project and aims to be inclusive of as many languages as possible. All user-facing messages and templates should follow the advice on [translations and gendered language](translation.html).