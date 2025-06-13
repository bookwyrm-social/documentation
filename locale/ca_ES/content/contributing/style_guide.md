- - -
Títol: Guia d'estil Data: 2021-10-20 Ordre: 4
- - -

## Sol·licitud d'extracció

Així que vols contribuir al codi de BookWyrm: genial! Si hi ha alguna incidència oberta que vulgueu solucionar, poseu-hi un comentari per a evitar duplicacions de feina. Intenteu mantenir petits i enfocats a un sol tema concret l'abast dels pull requests. Aquesta manera és més fàcil de revisar i, si una part necessita canvis, no interferirà en les altres.

Si no tens clar com arreglar alguna cosa o no te'n surts, cap problema. Simplement deixa un comentari a la petició i ja ho trobarem.

Les pull requests han de passar tots els controls automàtics abans que es fusionin. Això inclou fer verificacions d'estil, linters globals, una verificació de seguretat i tests unitaris.

## Lint

### Global

Fem ús d'[EditorConfig](https://editorconfig.org) per mantenir sagnats i finals de línia consistents.

### Python

BookWyrm utilitza el formatador de codi [Negre](https://github.com/psf/black) per mantenir l'estil coherent de la base de codi Python. Totes les sol·licituds d'extracció noves es comproven amb accions de GitHub i podeu solucionar automàticament els problemes d'estil de codi executant `./bw-dev black`

Code is also checked with Pylint using GitHub Actions. Pylint warnings must be addressed before pull requests are merged, but it's a judgement call if the suggestion should be used, or the warning suppressed. Per eliminar una advertència, afegeix un comentari al final o a la línia de sobre de les advertències: `# pylint: disable=warning-name`

### Plantilles (HTML)

El teu pull request també el comprovarà el linter [curlyint](https://www.curlylint.org) per plantilles Django.

### CSS

Fem servir [stylelint](https://stylelint.io) per validar totes les regles CSS. Com amb Pylint [pots deshabilitar stylelint](https://stylelint.io/user-guide/ignore-code) per a una regla en particular, però et caldrà una bona raó.

### JavaScript

L'[ESLint](https://eslint.org) comprova tots els canvis de JavaScript que facis. Si a l'ESLint no li agrada el teu JavaScript, mira el missatge linter per trobar quin és el problema exacte.

## Disseny inclusiu

BookWyrm intenta ser tan inclusiu i accessible com sigui possible.

Si contribueixes en el codi, comprova la [Llista de comprovacions per al disseny web inclusiu](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) abans de fer el teu pull request. Per a consells sobre accessibilitat, [A11Y-101](https://www.a11y-101.com/development) també pot ser una font útil. Per a informació sobre com fer que les teves plantilles siguin multilingües, ves a la [secció de traduccions](/translations.html).

Algunes particularitats que els contribuïdors de BookWyrm han trobat útils són:

### Formularis

* Fes servir `input[type="checkbox"]` o `input[type="radio"]` només a dins de <0>&lt;label&gt;</0>
* Si no col·loques els elements checkbbox i radio dins de `<label>`, el `<label>` s'haurà de col·locar _després_ de l'element a què es refereix

### Botons i enllaços

* Use a `<button>` element for anything that exists to trigger a JavaScript action (e.g. hiding or unhiding a form) or sends a `POST` request (e.g. submitting a form)
* Use an `<a>` element for anything that triggers a `GET` request. Usually, an anchor (`<a>`) element should not be styled as a button (`class="button"`), though there are some exceptions, such as "Cancel" buttons. If in doubt, ask for advice in your pull request
