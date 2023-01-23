- - -
Title: Style Guide Date: 2021-10-20 Order: 4
- - -

## Pull requests

Vous voulez contribuer au code de BookWyrm, c’est génial ! S'il y a un problème ouvert que vous souhaitez corriger, il est préférable de laisser un commentaire dans la conversation pour que le travail ne soit pas dupliqué. Essayez de limiter la portée des pull requests et de concentrer votre attention sur un seul sujet. Comme ça elle est plus facile à relire, et si une partie a besoin de changements elle ne retardera pas les autres parties.

Si vous ne savez pas comment régler un problème, ou que vous n'êtes plus disponible pour le faire, ne vous en faites pas. Laissez simplement un commentaire sur la pull request et nous allons prendre le relais 💖.

Les pull requests doivent valider tous les tests automatiques avant d'être fusionnées, ça inclut des vérifications de style, des linters globaux, un test de sécurité et des tests unitaires.

## Lint

### Global

Nous utilisons [EditorConfig](https://editorconfig.org) pour maintenir la cohérence de l’indentation et des fins de lignes.

### Python

BookWyrm utilise le formateur de code [Black](https://github.com/psf/black) pour maintenir la cohérence de la base de code Python. Toutes les nouvelles pull requests sont vérifiées avec des actions GitHub, et vous pouvez corriger automatiquement les problèmes de style de code en exécutant `./bw-dev black`

Le code est également vérifié avec Pylint via une action GitHub. Les avertissements de Pylint doivent être traités avant que les pull requests soient fusionnées, mais c'est une question de jugement si la suggestion doit être utilisée, ou l'avertissement supprimé. Pour supprimer un avertissement, ajoutez un commentaire à la fin ou sur la ligne précédant les avertissements : `# pylint: disable=nom-de-la-regle`

### Gabarits (HTML)

Votre pull request sera également vérifiée par le linter [curlylint](https://www.curlylint.org) pour les gabarits Django.

### CSS

Nous utilisons [stylelint](https://stylelint.io) pour vérifier toutes les règles CSS. Comme pour Pylint [vous pouvez désactiver le stylelint](https://stylelint.io/user-guide/ignore-code) pour une règle particulière, mais vous aurez besoin d'une bonne justification pour le faire.

### JavaScript

[ESLint](https://eslint.org) vérifie toute modification effectuée en JavaScript. Si ESLint n'aime pas votre JavaScript (même fonctionnel), vérifiez le message linter pour le problème exact.

## Design inclusif

BookWyrm aspire à être aussi inclusif et accessible que possible.

Lorsque vous contribuez du code, vérifiez la [checklist Inclusive Web Design](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) avant de proposer votre pull request. Pour des conseils sur l'accessibilité, [A11Y-101](https://www.a11y-101.com/development) est également une ressource utile. Pour plus d'informations sur la manière de rendre vos gabarits de page multilingues, voir [la section Traductions](/translation.html).

Quelques particularités à garder en tête pour la contribution au code de BookWyrm :

### Formulaires

* N'utiliser `input[type="checkbox"]` ou `input[type="radio"]` qu’à l'intérieur de `<label>`
* Si vous ne placez pas les cases à cocher et les boutons radio à l'intérieur du `<label>`, le `<label>` doit être placé _après_ l'élément auquel il se rapporte

### Boutons et Liens

* Utilisez un élément `<button>` pour tout ce qui a pour but de déclencher une action JavaScript (par ex. cacher ou révéler un formulaire) ou envoyer une requête `POST` (par ex. soumettre un formulaire)
* Utilisez un élément `<a>` pour tout ce qui déclenche une requête `GET`. Habituellement, un lien (`<a>`) ne doit pas avoir l’apparence d’un bouton (`class="button"`), bien qu'il y ait quelques exceptions comme les boutons "Annuler". En cas de doute, demandez conseil dans votre pull request
