- - -
Title: Übersetzungen Date: 2021-10-20 Order: 2
- - -

## Zu Übersetzungen beitragen

Du kannst dem BookWyrm Übersetzungsprojekt unter [translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/) beitreten.

## Geschlechtsneutrale Sprache

Wo immer möglich, sollten BookWyrm Übersetzungen geschlechtsneutrale Sprache verwenden. Dies gilt auch dann, wenn eine Sprache als neutrales Geschlecht voreingestellt ist oder wenn sie etwas Ähnliches wie "he/she" verwendet. Es ist auch wichtig, dass Übersetzungen klar, präzise und lesbar für einen Screenreader sind und manchmal stehen diese Ziele im Widerspruch zueinander; es gibt nicht die eine perfekte Lösung und diese hängt von der Sprache ab.

Als Leitfaden versuche, einen höheren Wert auf inklusive und geschlechtsneutrale Sprache zu legen als auf formale Korrektheit oder offiziell anerkannte Stilführer. Im Englischen zum Beispiel benötigen viele formale Leitfäden ein einzelnes "she"- oder "he"-Pronomen, um für eine Person verwendet zu werden, aber es wäre besser, in BookWyrm das geschlechtsneutrale singuläre "they" zu verwenden.

Wenn du nicht sicher bist, wie du am besten an ein Übersetzungsproblem herangehen kannst, kommentiere die Übersetzung oder öffne ein [-Diskussionsthema](https://translate.joinbookwyrm.com/project/bookwyrm/discussions), um weitergehende Fragen zu stellen.

## Vorlagen übersetzbar machen

Bookwyrm nutzt die Django-Übersetzungsfunktionalität, um den Seiteninhalt je nach der von den Benutzer*innen gewählten Anzeigesprache ändern zu können. Die Django-Dokumentation [bietet hilfreiche Erklärungen](https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#internationalization-in-template-code) wie das funktioniert, aber hier ist eine Kurzversion:

* alle Template-Texte sollten Übersetzungstexte enthalten
* füge `{% load i18n %}` oben an deiner Vorlage hinzu, um Übersetzungen zu aktivieren
* Wenn der Textblock wörtlicher Text ist, kannst du das Template-Tag `{% trans %}` verwenden
* Wenn der Textblock Variablen enthält, solltest du das Template-Tag-Paar `{% blocktrans %}` und `{% endblocktrans %}` verwenden. Wenn du Leerzeichen oder Zeilenumbrüche einbaust, nutze `gekürzt`, um es automatisch zu entfernen, wenn die Sprachdatei generiert wird: `{% blocktrans trimmed %}`

### Beispiele

```html
<p>{% trans "This list is currently empty" %}</p>

<p>
    {% blocktrans trimmed with username=item.user.display_name user_path=item.user.local_path %}
    hinzugefügt von <a href="{{ user_path }}">{{ username }}</a>
    {% endblocktrans %}
</p>
```
