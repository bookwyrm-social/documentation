- - -
Títol: Traduccions Data: 2021-10-20 Ordre: 2
- - -

## Contribueix a les traduccions

Pots unir-te al projecte de traduccions de BookWyrm a [translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/).

## Llenguatge de gènere neutre

Sempre que sigui possible, les traduccions de BookWyrm hauran d'utilitzar llenguatge de gènere neutre. Això aplica tant si la llengua té per defecte el gènere masculí com a neutre o si utilitza quelcom similar a "ell/ella". És important per a les traduccions ser clar, concís i comprensible de cara al lector i, alguns cops aquests objectius es troben en conflicte; no hi ha una solució única o perfecta, depèn del mateix idioma.

Com a principi, intenta donar un valor alt al llenguatge inclusiu i de gènere neutre que a formes respectuoses o guies d'estil oficials. En anglès, per exemple, moltes guies d'estil formals requereixen que s'utilitzi un pronom singular "ella" o "ell" quan es refereixi a un individu, però seria millor a BookWyrm utilitzar el singular "ells" de gènere neutre.

Si no esteu segur de com abordar millor un problema de traducció, comenteu la traducció o obriu un [tema de discussió](https://translate.joinbookwyrm.com/project/bookwyrm/discussions) per abordar preguntes d'escala més àmplia.

## Fer plantilles traduïbles

Bookwyrm aprofita la funcionalitat de traducció de Django per permetre que el contingut de la pàgina canviï en funció de l'idioma de visualització escollit per l'usuari. La documentació de Django [ofereix una explicació útil](https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#internationalization-in-template-code) de com funciona això, però aquí teniu la versió curta:

* tot el text de la plantilla ha d'incloure etiquetes de plantilla de traducció
* afegeix `{% load i18n %}` a la part superior de la plantilla per habilitar les traduccions
* Si el bloc de text és text literal, podeu utilitzar l'etiqueta de plantilla `{% trans %}`
* Si el bloc de text inclou variables, hauríeu d'utilitzar la parella d'etiquetes de plantilla `{% blocktrans %}` i `{% endblocktrans %}`. Si incloeu espais en blanc de farciment o salts de línia, utilitzeu `trimmed` per eliminar-lo automàticament quan es generi el fitxer de configuració regional: `{% blocktrans trimmed %}`

### Exemples

```html
<p>{% trans "This list is currently empty" %}</p>

<p>
    {% blocktrans trimmed with username=item.user.display_name user_path=item.user.local_path %}
    Added by <a href="{{ user_path }}">{{ username }}</a>
    {% endblocktrans %}
</p>
```
