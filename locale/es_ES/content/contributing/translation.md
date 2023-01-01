- - -
Title: Translations Date: 2021-10-20 Order: 2
- - -

## Contribuyendo a las traducciones

Puedes unirte al proyecto de traducción en [translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/).

## Lenguaje en género neutro

Siempre que sea posible, las traducciones de BookWyrm deberían utilizar un lenguaje neutral en cuanto al género. Esto aplica incluso si un lenguaje utiliza el masculino como género neutro, o si utiliza algo similar a "él/ella". También es importante que las traducciones sean claras, concisas y legibles para un lector de pantalla, y a veces estos objetivos están en conflicto; no hay una única respuesta perfecta para esto, y la solución depende del idioma.

Como principio rector, trata de valorar más un lenguaje inclusivo y neutral para el género en lugar de la correción formal o las guías de estilo oficialmente aprobadas. En Español, por ejemplo, muchas guías de estilo formal utilizan los pronombres "ella" o "él" al referirse a un individuo, pero sería mejor en BookWyrm usar el género-neutro "elle" en su lugar.

Si tienes dudas sobre cómo abordar un problema de traducción, comenta en la traducción o abre un [tema de discusión](https://translate.joinbookwyrm.com/project/bookwyrm/discussions) para abordar preguntas más generales.

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
