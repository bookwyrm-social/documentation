- - -
Titel: Oversættelser Dato: 2021-10-20 Order: 2
- - -

## Sådan bidrager man til oversættelse

Du kan slutte dig til BookWyrm-oversættelsesprojektet på [translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/).

## Kønsneutralt sprog

Så vidt muligt bør BookWyrm-oversættelser anvende kønsneutralt sprog. Dette gælder også for sprog, som bruger hankøn som et neutralt køn, eller hvis det bruger noget lignende "han/hun". Det er også vigtigt, at oversættelser er klare, koncise og læselige for en skærmlæser, og nogle gange modarbejder disse mål hinanden; der er altså ikke et perfekt svar, som passer til alle, og løsningen afhænger af sproget.

Som ledende princip skal du forsøge at vægte inklusivt og kønsneutralt sprog højere end formel korrekthed eller officielt godkendte stilguider. På engelsk kræver mange formelle stilguider for eksempel, at et pronomen i ental skal være "she" eller "he", når der henvises til en person, men det ville være bedre i BookWyrm at bruge det kønsneutrale "they" i ental i stedet.

Hvis du ikke er sikker på, hvordan du bedst kan håndtere et oversættelsesproblem, kan du kommentere på oversættelsen eller åbne et [diskussionsemne](https://translate.joinbookwyrm.com/project/bookwyrm/discussions) for at påpege et mere generelt tvivlsspørgsmål.

## Sådan gøres skabeloner oversættelige

BookWyrm udnytter Djangos oversættelsesfunktionalitet til at gøre det muligt for sidens indhold at ændre sig afhængigt af brugerens valgte visningssprog. Django-dokumentationen [giver en nyttig forklaring](https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#internationalization-in-template-code) på, hvordan det virker, men her er den korte version:

* al skabelontekst bør indeholde opmærkning til oversættelsesskabeloner
* tilføj `{% load i18n %}` øverst i din skabelon for at aktivere oversættelser
* Hvis tekstblokken er ren tekst, kan du bruge skabelonmærket `{% trans %}`
* Hvis tekstblokken indeholder variabler, skal du bruge skabelonmærkeparret `{% blocktrans %}` og `{% endblocktrans %}`. Hvis du inkluderer polstring i form af blanke tegn eller linjeskift, så brug `trimmed` til automatisk at fjerne det, når oversættelsesfilen genereres: `{% blocktrans trimmed %}`

### Eksempler

```html
<p>{% trans "Denne liste er p.t. tom" %}</p>

<p>
    {% blocktrans trimmed with username=item.user.display_name user_path=item.user.local_path %}
    Tilføjet af <a href="{{ user_path }}">{{ username }}</a>
    {% endblocktrans %}
</p>
```
