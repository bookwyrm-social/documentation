- - -
Título: Traducciones Fecha: 2021-10-20 Orden: 2
- - -

## Contribuyendo a las traducciones

Puedes unirte al proyecto de traducción en [translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/).

## Lenguaje en género neutro

Siempre que sea posible, las traducciones de BookWyrm deberían utilizar un lenguaje neutral en cuanto al género. Esto aplica incluso si un lenguaje utiliza el masculino como género neutro, o si utiliza algo similar a "él/ella". También es importante que las traducciones sean claras, concisas y legibles para un lector de pantalla, y a veces estos objetivos están en conflicto; no hay una única respuesta perfecta para esto, y la solución depende del idioma.

Como principio rector, trata de valorar más un lenguaje inclusivo y neutral para el género en lugar de la correción formal o las guías de estilo oficialmente aprobadas. En Español, por ejemplo, muchas guías de estilo formal utilizan los pronombres "ella" o "él" al referirse a un individuo, pero sería mejor en BookWyrm usar el género-neutro "elle" en su lugar.

Si tienes dudas sobre cómo abordar un problema de traducción, comenta en la traducción o abre un [tema de discusión](https://translate.joinbookwyrm.com/project/bookwyrm/discussions) para abordar preguntas más generales.

## Volver traducibles las plantillas

BookWyrm aprovecha las funciones de traducción de Django. Permite que el contenido de la página cambie dependiendo del idioma elegido por el usuario. La documentación de Django [proporciona una útil explicación](https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#internationalization-in-template-code) de cómo funciona esto, pero aquí hay un breve resumen:

* todo el texto de la plantilla debe incluir etiquetas de traducción
* añade `{% load i18n %}` en la parte superior de la plantilla para habilitar las traducciones
* Si el bloque de texto es texto literal, puede usar la etiqueta `{% trans %}`
* Si el bloque de texto incluye variables, deberías usar el par de etiquetas `{% blocktrans %}` y `{% endblocktrans %}`. Si incluyes espacios en blanco o saltos de línea, usa `trimmed`. Para eliminarlo automáticamente cuando se genere el archivo local: `{% blocktrans trimmed %}`

### Ejemplos

```html
<p>{% trans "This list is currently empty" %}</p>

<p>
    {% blocktrans trimmed with username=item.user.display_name user_path=item.user.local_path %}
    Added by <a href="{{ user_path }}">{{ username }}</a>
    {% endblocktrans %}
</p>
```
