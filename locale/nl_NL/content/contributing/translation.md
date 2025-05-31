- - -
Vertalingen
- - -

## Bijdragen aan vertalingen

Je kunt deelnemen aan het BookWyrm vertaalproject op [translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/).

## Genderneutrale taal

Waar mogelijk, moeten BookWyrm vertalingen genderneutrale taal bevatten. Dit geldt zelfs als een taal standaard mannelijk is als neutraal geslacht, of als het iets gebruikt dat lijkt op "hij/zij". It's also important for translations to be clear, concise, and legible to a screen reader, and sometimes these goals are in conflict; there isn't a perfect, one-size-fits all answer, and the solution depends on the language.

As a guiding principal, try to place a higher value on inclusive and gender-neutral language than on formal correctness or officially approved style guides. In English, for example, many formal style guides require a singular "she" or "he" pronoun to be used when referring to an individual, but it would be better in BookWyrm to use the gender-neutral singular "they" instead.

If you aren't sure how best to approach a translation problem, comment on the translation or open a [discussion topic](https://translate.joinbookwyrm.com/project/bookwyrm/discussions) to address broader-scale questions.

## Sjablonen vertaalbaar maken

Bookwyrm takes advantage of Django's translation functionality to enable page content to change depending on the user's chosen display language. De Django documentatie [geeft een handige uitleg](https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#internationalization-in-template-code) over hoe dit werkt, maar hier is de korte versie:

* all template text should include translation template tags
* add `{% load i18n %}` at the top of your template to enable translations
* If the text block is literal text, you can use the template tag `{% trans %}`
* If the text block includes variables, you should use the template tag pair `{% blocktrans %}` and `{% endblocktrans %}`. If you are including padding whitespace or line breaks, use `trimmed` to automatically remove it when the locale file is generated: `{% blocktrans trimmed %}`

### Voorbeelden

```html
<p>{% trans "This list is currently empty" %}</p>

<p>
    {% blocktrans trimmed with username=item.user.display_name user_path=item.user.local_path %}
    Added by <a href="{{ user_path }}">{{ username }}</a>
    {% endblocktrans %}
</p>
```
