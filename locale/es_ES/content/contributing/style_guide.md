- - -
Título: Style Guide Fecha: 2021-10-20 Orden: 4
- - -

## Pull requests

Así que quieres contribuir con código a BookWyrm... ¡Genial! Si hay un problema que te gustaría solucionar, sería útil antes comentarlo para que el trabajo no se duplique. Intenta mantener las pull requests pequeñas y enfocadas a un solo tema en particular. De esa manera será más fácil revisarlo, y si algo necesita modificaciones, no afectará otras partes del código.

Si no sabes cómo arreglar algo, o no te crees capaz de solucionarlo ¡No hay problema! Solo deja un comentario en el pull request y lo trataremos 💖.

Las pull requests deben pasar todas los chequeo automatizados antes de ser fusionadas (incluyendo estilo, global linters, seguridad y testeos).

## Lint

### Global

Usamos [EditorConfig](https://editorconfig.org) para mantener una identación y fin de línea consistente.

### Python

BookWyrm usa el formato de código [Black](https://github.com/psf/black) para mantener la base de Python consistente. Todas las nuevas pull requests son chequeadas con GitHub Actions. Puedes corregir problemas de estilo automáticamente ejecutando el comando `./bw-dev black`

El código también es chequeado con Pylint usando GitHub Actions. Las advertencias de Pylint deben ser abordadas antes de fusionar las pull requests, pero es una llamada si la sugerencia debe ser usada, o la advertencia suprimida. Para eliminar una advertencia, agregar un comentario al final o en la línea superior a las advertencias: `# pylint: disable=warning-name`

### Plantillas (HTML)

Tu pull request también será revisado por el linter [curlylint](https://www.curlylint.org) para plantillas de Django.

### CSS

Utilizamos [stylelint](https://stylelint.io) para verificar todas las reglas CSS. Al igual que con Pylint [puedes desactivar stylelint](https://stylelint.io/user-guide/ignore-code) para una regla en particular, aunque necesitarás una buena justificación para hacerlo.

### JavaScript

[ESLint](https://eslint.org) comprueba cualquier cambio de JavaScript que hayas realizado. Si a ESLint no le gusta tu trabajo de JavaScript, comprueba el mensaje del linter para ver el problema exacto.

## Diseño inclusivo

Bookwyrm pretende ser lo más inclusivo y accesible posible.

Cuando contribuyes con el código, chequea la [Inclusive Web Design Checklist](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) antes de presentar tu pull request. Para consejos de accesibilidad, [A11Y-101](https://www.a11y-101.com/development) es una fuente útil. Para obtener información sobre cómo hacer que tus plantillas sean plurilingüe, consulta la sección [Traducciones](/translations.html).

Algunas cosas particulares que los colaboradores de Bookwyrm han encontrado útiles para recordar son:

### Formularios

* Solo usar `input[type="checkbox"]` o `input[type="radio"]` dentro de `<label>`
* Si no colocas checkboxes y botones de radio dentro de la `<label>`, el `<label>` debe colocarse _después_ del elemento.

### Botones y enlaces

* Usa `<button>` para activar una acción de JavaScript (por ejemplo: ocultar o desplegar un formulario); o enviar una solicitud `POST`.
* Usa `<a>` para cualquier cosa que active una solicitud `GET`. Usualmente, un ancla (`<a>`) no debe ser diseñado como un botón (`class="button"`), aunque hay algunas excepciones, como los botones de "Cancelar". Ante cualquier duda, pide ayuda en tu pull request.
