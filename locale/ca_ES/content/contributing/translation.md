- - -
Títol: Traduccions Data: 2021-10-20 Ordre: 2
- - -

## Contribueix a les traduccions

Pots unir-te al projecte de traduccions de BookWyrm a [translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/).

## Llenguatge de gènere neutre

Sempre que sigui possible, les traduccions de BookWyrm hauran d'utilitzar llenguatge de gènere neutre. Això aplica tant si la llengua té per defecte el gènere masculí com a neutre o si utilitza quelcom similar a "ell/ella". És important per a les traduccions ser clar, concís i comprensible de cara al lector i, alguns cops aquests objectius es troben en conflicte; no hi ha una solució única o perfecta, depèn del mateix idioma.

Com a principi, intenta donar un valor alt al llenguatge inclusiu i de gènere neutre que a formes respectuoses o guies d'estil oficials. In English, for example, many formal style guides require a singular "she" or "he" pronoun to be used when referring to an individual, but it would be better in BookWyrm to use the gender-neutral singular "they" instead.

If you aren't sure how best to approach a translation problem, comment on the translation or open a [discussion topic](https://translate.joinbookwyrm.com/project/bookwyrm/discussions) to address broader-scale questions.

## Making templates translatable

Bookwyrm takes advantage of Django's translation functionality to enable page content to change depending on the user's chosen display language. The Django documentation [provides a helpful explanation](https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#internationalization-in-template-code) of how this works, but here is the short version:

* all template text should include translation template tags
* add `{% load i18n %}` at the top of your template to enable translations
* If the text block is literal text, you can use the template tag `{% trans %}`
* If the text block includes variables, you should use the template tag pair `{% blocktrans %}` and `{% endblocktrans %}`. If you are including padding whitespace or line breaks, use `trimmed` to automatically remove it when the locale file is generated: `{% blocktrans trimmed %}`

### Examples

```html
<p>{% trans "This list is currently empty" %}</p>

<p>
    {% blocktrans trimmed with username=item.user.display_name user_path=item.user.local_path %}
    Added by <a href="{{ user_path }}">{{ username }}</a>
    {% endblocktrans %}
</p>
```
