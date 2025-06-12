- - -
Title: Tłumaczenia Date: 2021-10-20 Order: 2
- - -

## Udzielanie się w tłumaczeniach

Możesz dołączyć do projektu tłumaczenia BookWyrm na [translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/).

## Język neutralny płciowo

Tam, gdzie to możliwe, tłumaczenia BookWyrm powinny zawierać neutralne płciowo wyrazy. Ma to zastosowanie również, gdy rodzaj męski jest traktowany jako neutralny lub istnieje coś podobnego do "on/ona". Równie ważne jest, aby przetłumaczone treści były jasne, zwięzłe i czytelne dla użytkownika, a czasami te wartości nie idą w parze; nie ma jednej odpowiedzi na wszystkie aspekty, więc należy wykorzystać wszelkie zasoby języka.

Poświęć więcej uwagi na integrację oraz neutralny płciowo język niż na poprawność lub oficjalne formy stylizacji. Na przykład w języku angielskim wiele formalnych zwrotów wymaga użycia zaimka "ona" lub "on", gdy odnosimy się do osoby, ale lepiej będzie, jeśli na BookWyrm zastosujemy neutralne płciowo "ono/oni".

Jeśli nie masz pewności, jak najlepiej podejść do problemu z tłumaczeniem, dodaj komentarz do tłumaczenia lub utwórz [dyskusję](https://translate.joinbookwyrm.com/project/bookwyrm/discussions), aby uzyskać odpowiedź na bardziej zawiłe pytania.

## Umożliwianie tłumaczenia szablonów

BookWyrm korzysta z funkcji tłumaczenia Django, aby umożliwić zmienianie treści strony w zależności od języka wybranego przez użytkownika. Dokumentacja Django [zawiera pomocne objaśnienia](https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#internationalization-in-template-code), jak to działa, a tutaj krótkie jej podsumowanie:

* cały tekst szablonu powinien zawierać znaczniki tłumaczenia szablonu
* dodaj `{% load i18n %}` na górze szablonu, aby umożliwić tłumaczenia
* Jeśli blok tekstu jest tekstem dosłownym, możesz skorzystać z znacznika szablonu `{% trans %}`
* Jeśli blok tekstu zawiera zmienne, należy użyć pary znaczników `{% blocktrans %}` oraz `{% endblocktrans %}`. If you are including padding whitespace or line breaks, use `trimmed` to automatically remove it when the locale file is generated: `{% blocktrans trimmed %}`

### Przykłady

```html
<p>{% trans "This list is currently empty" %}</p>

<p>
    {% blocktrans trimmed with username=item.user.display_name user_path=item.user.local_path %}
    Dodane przez <a href="{{ user_path }}">{{ username }}</a>
    {% endblocktrans %}
</p>
```
