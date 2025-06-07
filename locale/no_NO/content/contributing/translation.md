- - -
Title: Oversettelser Date: 2021-10-20 Order: 2
- - -

## Bidra til oversettelser

Du kan bli med i BookWyrm-oversettelsesprosjektet på [translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/).

## Kjønnsnøytralt språk

Så langt det lar seg gjøre, bør Bokwyrm-oversettelser bruke et kjønnsnøytralt språk. Dette gjelder selv om et språk som standard bruker hankjønn som nøytralt kjønn, eller hvis det bruker noe lignende «han/hun». Det er også viktig at oversettelser skal være tydelige, konsise og leselig for en skjermleser, og noen ganger er disse målene i konflikt; det er ikke en perfekt løsning som passer absolutt over alt, og løsningen avhenger av språket.

Som hovedregel prøver man å verdsette inkluderende og kjønnsnøytralt språk mer enn formell korrekthet eller offisielt godkjente stilveiledninger. På engelsk, for eksempel, krever mange formelle stilguider at et singulært «she» eller «he»-pronomen brukes ved henvisning til et enkeltindivid, men i BookWyrm er det bedre å bruke det kjønnsnøytrale singulære «they» i stedenfor.

Hvis du er usikker på hva som er den beste fremgangsmåten for en oversettelse, kommenter oversettelsen eller åpne et [diskusjonstema,](https://translate.joinbookwyrm.com/project/bookwyrm/discussions) for å diskutere større spørsmål.

## Gjør maler oversettbare

BookWyrm benytter Django sin oversettelsesfunksjonalitet for å muliggjøre at sideinnholdet tilpasser seg språket brukeren har valgt. Django-dokumentasjonen [forklarer hvordan dette fungerer](https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#internationalization-in-template-code), men her en kort oppsummering:

* all maltekst bør inkludere tagger for oversettelsesmalen
* legg til `{% load i18n %}` øverst på din mal for å aktivere oversettelser
* Dersom tekstblokken er en literal tekst, kan du bruke mal-taggen `{% trans %}`
* Dersom tekstblokken inkluderer variabler, skal du bruke mal-taggparet `{% blocktrans %}` og `{% endblocktrans %}`. Hvis du inkluderer padding-mellomrom eller linjebrudd, bruk `trimmed` for å automatisk fjerne den når språkfilen blir generert: `{% blocktrans trimmed %}`

### Eksempler

```html
<p>{% trans "This list is currently empty" %}</p>

<p>
    {% blocktrans trimmed with username=item.user.display_name user_path=item.user.local_path %}
    Added by <a href="{{ user_path }}">{{ username }}</a>
    {% endblocktrans %}
</p>
```
