- - -
Title: Traducións Date: 2021-10-20 Order: 2
- - -

## Axuda a traducir

Podes unirte ao proxecto de tradución de BookWyrm en [translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/).

## Linguaxe de xénero neutro

Sempre que sexa posible, as traducións de BookWyrm deberán utilizar unha linguaxe de xénero neutro. Isto é de aplicación incluso se o idioma adopta a forma masculina como xénero neutro, ou se utiliza algo semellante a "el/ela". É importante tamén que as traducións sexan concisas e claras, lexibles para lectores de pantalla, polo que hai veces que estos obxectivos entran en conflito; nada é perfecto, non hai unha solución que contente a todo o mundo, e esta solución depende do idioma en cuestión.

Como criterio superior, intenta poñer máis énfase nunha linguaxe de xénero neutro e inclusivo que na corrección formal ou as guías de estilo oficialmente establecidas. En inglés, por exemplo, as guías de estilo indican a forma singular do pronome "she" ou "he" para referirse a un individuo, pero en BookWyrm avogamos polo uso da forma de xénero neutro singular "they".

Se non tes certeza sobre como afrontar este problema de tradución, fai un comentario na tradución ou abre un [tema de discusión](https://translate.joinbookwyrm.com/project/bookwyrm/discussions) para afrontar o problema nunha instancia superior.

## Facer os modelos traducibles

BookWyrm aproveita as vantaxes da funcionabilidade das traducións de Django para permitir que o contido da páxina varíe en función do idioma elexido. A documentación de Django [proporciona axuda](https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#internationalization-in-template-code) sobre como funciona, pero aquí tes unha versión reducida:

* todos os modelos do texto deben incluír etiquetas do modelo da tradución
* engade `{% load i18n %}` na parte superior do modelo para activar as traducións
* Se o bloque de texto é texto literal, podes usar o modelo de etiqueta `{% trans %}`
* Se o bloque inclúe variables, debes usar o par de modelos de etiqueta `{% blocktrans %}` e `{% endblocktrans %}`. Se estás incluíndo espazos en branco ou saltos de liña, usa `trimmed` para eliminalos automáticamente cando se crea o ficheiro coa tradución: `{% blocktrans trimmed %}`

### Exemplos

```html
<p>{% trans "This list is currently empty" %}</p>

<p>
    {% blocktrans trimmed with username=item.user.display_name user_path=item.user.local_path %}
    Engadido por <a href="{{ user_path }}">{{ username }}</a>
    {% endblocktrans %}
</p>
```
