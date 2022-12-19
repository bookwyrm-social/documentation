- - -
Titolo: Guida di stile Data: 20-10-2021 Ordine: 4
- - -

## Pull requests

Quindi vuoi contribuire al codice di BookWyrm: fantastico! Se c'è un problema aperto che si desidera risolvere, è utile commentare il problema in modo che il lavoro non venga duplicato. Cerca di mantenere piccola la portata delle richieste nel pull e focalizzati su un singolo argomento. In questo modo è più facile da rivedere, e se una parte ha bisogno di cambiamenti, non bloccherà le altre parti.

Se non sei sicuro di come risolvere qualcosa, o non sei in grado di aggirare il problema, va benissimo, basta lasciare un commento sulla pull request e lo capiremo 💖.

Le richieste di prelievo devono superare tutti i controlli automatici prima che possano essere uniti - questo include controlli di stile, linters globali, un controllo di sicurezza e test di unità.

## Linting

### Globale

Usiamo [EditorConfig](https://editorconfig.org) per mantenere costanti le terminazioni di indentazione e di linea.

### Python

BookWyrm utilizza il formattatore del codice [Black](https://github.com/psf/black) per mantenere coerente lo stile del codebase Python. Tutte le nuove richieste sono controllate con le azioni GitHub e puoi risolvere automaticamente i problemi di stile del codice eseguendo `./bw-dev black`

Il codice è anche controllato con Pylint utilizzando le azioni GitHub. Gli avvertimenti di Pylint devono essere risolti prima che le richieste di pull siano unite, ma è una chiamata di giudizio se il suggerimento deve essere utilizzato, o l'avviso soppresso. Per sopprimere un avviso, aggiungi un commento alla fine o sulla riga sopra gli avvisi: `# pylint: disable=warning-name`

### Templates (HTML)

La tua richiesta di pull sarà anche controllata dall'linter [curlylint](https://www.curlylint.org) per i modelli Django.

### CSS

Usiamo [stylelint](https://stylelint.io) per controllare tutte le regole CSS. Come con Pylint [puoi disabilitare stylelint](https://stylelint.io/user-guide/ignore-code) per una regola particolare, ma avrai bisogno di una buona motivazione per farlo.

### JavaScript

[ESLint](https://eslint.org) controlla qualsiasi modifica JavaScript che hai apportato. Se a ESLint non piace il tuo JavaScript, controlla il messaggio linter per verificare il problema esatto.

## Progettazione Inclusiva

Bookwyrm mira a essere il più completo e accessibile possibile.

Quando si contribuisce con il codice, controllare la checklist [Inclusive Web Design Checklist](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) prima di archiviare la tua richiesta pull. Per la consulenza in materia di accessibilità, [A11Y-101](https://www.a11y-101.com/development) è anche una fonte utile. Per informazioni su come rendere i modelli di pagina multilingue, vedere la [sezione Traduzioni](/translations.html).

Alcune cose particolari che i contributori di Bookwyrm hanno trovato utili per ricordare sono:

### Moduli

* Utilizza solo `input[type="checkbox"]` o `input[type="radio"]` dentro `<label>`
* Se non piazzi caselle di controllo e pulsanti radio all'interno del `<label>`, il `<label>` dovrebbe essere posizionato _dopo_ l'elemento cui si riferisce

### Tasti e collegamenti

* Usa un elemento `<button>` per qualsiasi cosa esistente per attivare un'azione JavaScript (e.. nascondere o svuotare una forma) o invia una richiesta `POST` (ad esempio inviare un modulo)
* Usa un elemento `<a>` per tutto quello che attiva una richiesta `GET`. Di solito, un elemento di ancoraggio (`<a>`) non dovrebbe essere stilato come pulsante (`class="pulsante"`), anche se ci sono alcune eccezioni, come i pulsanti "Annulla". In caso di dubbio, chieda consiglio nella tua pull request
