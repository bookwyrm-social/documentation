- - -
Title: Style Guide Date: 2021-10-20 Order: 3
- - -

## Pull requests

Vous voulez contribuer au code de BookWyrm, c’est génial ! S'il y a un problème ouvert que vous souhaitez corriger, il est préférable de laisser un commentaire dans la conversation pour que le travail ne soit pas dupliqué. Essayez de limiter la portée des pull requests et de concentrer votre attention sur un seul sujet. Comme ça elle est plus facile à relire, et si une partie a besoin de changements elle ne retardera pas les autres parties.

Si vous ne savez pas comment régler un problème, ou que vous n'êtes plus disponible pour le faire, ne vous en faites pas. Laissez simplement un commentaire sur la pull request et nous allons prendre le relais 💖.

Les pull requests doivent valider tous les tests automatiques avant d'être fusionnées, ça inclut des vérifications de style, des linters globaux, un test de sécurité et des tests unitaires.

There are several `./bw-dev` commands you may find helpful for linting and testing prior to pushing your pull request. See [Command Line Tool](cli.html) for all the options available.

## Lint

### Global

Nous utilisons [EditorConfig](https://editorconfig.org) pour maintenir la cohérence de l’indentation et des fins de lignes.

### Python

#### Formatting and linting

BookWyrm uses [ruff](https://docs.astral.sh/ruff) for both code linting (checking for errors) and formatting (ensuring code style is consistent). All new pull requests are checked with GitHub actions, and you can automatically fix code style problems by running `./bw-dev ruff`. For linting errors, you can try `./bw-dev ruff-fix` to automatically fix errors, though this may not always be possible.

Ruff linting warnings must be addressed before pull requests are merged, but it's a judgement call if the suggestion should be used, or the warning suppressed. See [the Ruff projects's documentation on suppressing warnings](https://docs.astral.sh/ruff/linter/#comments) using code comments.

The BookWyrm project previously used `Black` for formatting and `Pylint` for linting. You may notice artefacts such as pylint suppression comments in older code. We are still refining our linting rules so if something seems confusing or not quite right, don't hesitate to ask for advice.

#### Type checking

We are gradually rolling out [static type checking](https://en.wikipedia.org/wiki/Type_system) across the BookWyrm code base. This is a long term project. Whilst it is not compulsory to formally define types in new code, it is strongly recommended. This will help to avoid some more subtle bugs that may not be identified in tests.

We currently use [mypy](https://www.mypy-lang.org) as our static type checker. Find out more about how to use mypy at [the `mypy` project documentation](https://mypy.readthedocs.io/en/stable/).

### Gabarits (HTML)

Votre pull request sera également vérifiée par le linter [curlylint](https://www.curlylint.org) pour les gabarits Django.

### CSS

Nous utilisons [stylelint](https://stylelint.io) pour vérifier toutes les règles CSS. Comme pour Pylint [vous pouvez désactiver le stylelint](https://stylelint.io/user-guide/ignore-code) pour une règle particulière, mais vous aurez besoin d'une bonne justification pour le faire.

### JavaScript

[ESLint](https://eslint.org) vérifie toute modification effectuée en JavaScript. Si ESLint n'aime pas votre JavaScript (même fonctionnel), vérifiez le message linter pour le problème exact.

## Design inclusif

BookWyrm aspire à être aussi inclusif et accessible que possible.

Lorsque vous contribuez du code, vérifiez la [checklist Inclusive Web Design](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) avant de proposer votre pull request. Pour des conseils sur l'accessibilité, [A11Y-101](https://www.a11y-101.com/development) est également une ressource utile. For information on how to make your page templates multi-lingual, see the [Translations section](/translation.html).

Quelques particularités à garder en tête pour la contribution au code de BookWyrm :

### Formulaires

* N'utiliser `input[type="checkbox"]` ou `input[type="radio"]` qu’à l'intérieur de `<label>`
* Si vous ne placez pas les cases à cocher et les boutons radio à l'intérieur du `<label>`, le `<label>` doit être placé _après_ l'élément auquel il se rapporte

### Boutons et Liens

* Utilisez un élément `<button>` pour tout ce qui a pour but de déclencher une action JavaScript (par ex. cacher ou révéler un formulaire) ou envoyer une requête `POST` (par ex. soumettre un formulaire)
* Utilisez un élément `<a>` pour tout ce qui déclenche une requête `GET`. Habituellement, un lien (`<a>`) ne doit pas avoir l’apparence d’un bouton (`class="button"`), bien qu'il y ait quelques exceptions comme les boutons "Annuler". En cas de doute, demandez conseil dans votre pull request

#### Translations

BookWyrm is an international project and aims to be inclusive of as many languages as possible. All user-facing messages and templates should follow the advice on [translations and gendered language](translation.html).