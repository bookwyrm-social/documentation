## Contribuiți la traducere

Puteți să vă alăturați proiectului de traducere BookWyrm la [translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/).

## Limbaj neutru de gen

Ori de câte ori este posibil, traducerile BookWyrm ar trebui să folosească limbaj de gen neutru. Asta se aplică dacă o limbă folosește în mod implicit genul masculin ca gen neutru sau dacă folosește ceva similar precum „el/ea”. Este de asemenea important ca traducerile să fie clare, concise și lizibile pentru un cititor de ecran. Uneori, aceste obiective intră în conflict. Nu există un răspuns perfect, universal valabil. Soluția depinde de limbă.

As a guiding principal, try to place a higher value on inclusive and gender-neutral language than on formal correctness or officially approved style guides. In English, for example, many formal style guides require a singular "she" or "he" pronoun to be used when referring to an individual, but it would be better in BookWyrm to use the gender-neutral singular "they" instead.

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
