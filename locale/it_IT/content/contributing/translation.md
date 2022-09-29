- - -
Title: Translations Date: 2021-10-20 Order: 2
- - -

## Contributing to translations

You can join the BookWyrm translation project at [translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/).

## Gender-neutral language

Wherever possible, BookWyrm translations should use gender-neutral language. This applies even if a language defaults to male as a neutral gender, or if it uses something similar to "he/she". È anche importante che le traduzioni siano chiare, concise e leggibili per un lettore a schermo e a volte questi obiettivi sono in conflitto; non c'è una risposta perfetta, unica e adatta a tutti, e la soluzione dipende dalla lingua.

Come principio guida, cercare di posizionare un valore più alto su un linguaggio inclusivo e neutro che su una correttezza formale o guide di stile ufficialmente approvate. In inglese, per esempio, molte guide di stile formali richiedono un pronome "lei" o "he" singolare da utilizzare quando si riferisce a un individuo, ma sarebbe meglio in BookWyrm utilizzare il genere neutro singolare "loro" invece.

Se non siete sicuri di come meglio affrontare un problema di traduzione, commentate la traduzione o aprite un [argomento di discussione](https://translate.joinbookwyrm.com/project/bookwyrm/discussions) per affrontare domande su larga scala.

## Creare modelli traducibili

Bookwyrm sfrutta la funzionalità di traduzione di Django per consentire ai contenuti della pagina di cambiare a seconda della lingua di visualizzazione scelta dall'utente. La documentazione Django [fornisce un'utile spiegazione](https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#internationalization-in-template-code) di come funziona, ma ecco una versione breve:

* tutto il testo del modello dovrebbe includere i tag del modello di traduzione
* aggiungi `{% load i18n %}` nella parte superiore del tuo modello per abilitare le traduzioni
* Se il blocco di testo è un testo letterale, puoi usare il tag modello `{% trans %}`
* Se il blocco di testo include variabili, dovresti usare la coppia di tag modello `{% blocktrans %}` e `{% endblocktrans %}`. Se stai includendo spazio bianco di riempimento o interruzioni di linea, usa `trimmed` per rimuoverlo automaticamente quando il file locale viene generato: `{% blocktrans trimmed %}`

### Esempi

```html
<p>{% trans "This list is currently empty" %}</p>

<p>
    {% blocktrans trimmed with username=item.user.display_name user_path=item.user.local_path %}
    Added by <a href="{{ user_path }}">{{ username }}</a>
    {% endblocktrans %}
</p>
```
