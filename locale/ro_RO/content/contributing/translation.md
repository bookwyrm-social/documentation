- - -
Title: Translations Date: 2021-10-20 Order: 2
- - -

## Contribuiți la traducere

Puteți să vă alăturați proiectului de traducere BookWyrm la [translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/).

## Limbaj neutru de gen

Ori de câte ori este posibil, traducerile BookWyrm ar trebui să folosească limbaj de gen neutru. Asta se aplică dacă o limbă folosește în mod implicit genul masculin ca gen neutru sau dacă folosește ceva similar precum „el/ea”. Este de asemenea important ca traducerile să fie clare, concise și lizibile pentru un cititor de ecran. Uneori, aceste obiective intră în conflict. Nu există un răspuns perfect, universal valabil. Soluția depinde de limbă.

Ca directivă principală, încercați să acordați prioritate unui limbaj incluziv și neutru decât unui limbaj formal corect sau aprobat în mod oficial. În engleză, de exemplu, foarte multe recomandări de stil necesită un pronume persoana I „she” sau „he” pentru a se referi la un individ, dar ar fi mai bine ca în BookWyrm să se folosească în schimb „they”, neutru din punct de vedere al genului.

Dacă nu sunteți siguri despre cum să abordați cel mai bine o problemă de traducere, lăsați un comentariu sau deschideți [un subiect de discuție](https://translate.joinbookwyrm.com/project/bookwyrm/discussions) pentru a adresa întrebări la scară mai largă.

## Traducerea șabloanelor

BookWyrm profită de funcționalitățile de traducere Django pentru a permite conținutului paginii să se schimbe în funcție de limba de afișare aleasă de utilizator. Documentația Django [oferă o explicație utilă](https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#internationalization-in-template-code) despre cum funcționează acest proces, dar iată versiunea scurtă:

* toate șabloanele text trebuie să includă taguri de șabloane de traducere
* adăugați `{% load i18n %}` în partea de sus a șablonului dvs. pentru a activa traducerile
* Dacă blocul de text este text literal, puteți folosiți tagul șablon `{% trans %}`
* Dacă blocul de text include variabile, ar trebui să folosiți perechea de taguri șablon `{% blocktrans %}` și `{% endblocktrans %}`. Dacă includeți spațiu alb sau treceri la linie nouă, folosiți `trimmed` pentru a le înlătura automat când fișierul de localizare este generat: `{% blocktrans trimmed %}`

### Exemple

```html
<p>{% trans "This list is currently empty" %}</p>

<p>
    {% blocktrans trimmed with username=item.user.display_name user_path=item.user.local_path %}
    Added by <a href="{{ user_path }}">{{ username }}</a>
    {% endblocktrans %}
</p>
```
