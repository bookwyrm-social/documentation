- - -
Title: Translations Date: 2021-10-20 Order: 2
- - -

## Contributing to translations

You can join the BookWyrm translation project at [translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/).

## Gender-neutral language

Wherever possible, BookWyrm translations should use gender-neutral language. This applies even if a language defaults to male as a neutral gender, or if it uses something similar to "he/she". It's also important for translations to be clear, concise, and legible to a screen reader, and sometimes these goals are in conflict; there isn't a perfect, one-size-fits all answer, and the solution depends on the language.

Come principio guida, cercare di posizionare un valore più alto su un linguaggio inclusivo e neutro che su una correttezza formale o guide di stile ufficialmente approvate. In inglese, per esempio, molte guide di stile formali richiedono un pronome "lei" o "he" singolare da utilizzare quando si riferisce a un individuo, ma sarebbe meglio in BookWyrm utilizzare il genere neutro singolare "loro" invece.

Se non siete sicuri di come meglio affrontare un problema di traduzione, commentate la traduzione o aprite un [argomento di discussione](https://translate.joinbookwyrm.com/project/bookwyrm/discussions) per affrontare domande su larga scala.

## Creare modelli traducibili

Bookwyrm sfrutta la funzionalità di traduzione di Django per consentire ai contenuti della pagina di cambiare a seconda della lingua di visualizzazione scelta dall'utente. The Django documentation [provides a helpful explanation](https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#internationalization-in-template-code) of how this works, but here is the short version:

* all template text should include translation template tags
* add `{% load i18n %}` at the top of your template to enable translations
* If the text block is literal text, you can use the template tag `{% trans %}`
* If the text block includes variables, you should use the template tag pair `{% blocktrans %}` and `{% endblocktrans %}`. If you are including padding whitespace or line breaks, use `trimmed` to automatically remove it when the locale file is generated: `{% blocktrans trimmed %}`

### Esempi

```html
<p>{% trans "This list is currently empty" %}</p>

<p>
    {% blocktrans trimmed with username=item.user.display_name user_path=item.user.local_path %}
    Added by <a href="{{ user_path }}">{{ username }}</a>
    {% endblocktrans %}
</p>
```
