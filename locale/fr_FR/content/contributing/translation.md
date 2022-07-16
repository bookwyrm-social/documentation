- - -
Title: Translations Date: 2021-10-20 Order: 2
- - -

## Contribuer aux traductions

Vous pouvez rejoindre le projet de traduction de BookWyrm à l'adresse [translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/).

## Langage non-genré / inclusif

Dans la mesure du possible, les traductions de BookWyrm doivent utiliser une langue non-genrée. Cela s'applique même si une langue désigne le masculin comme genre neutre par défaut, ou si elle utilise quelque chose de similaire à "il/elle". Il est également important que les traductions soient claires, concises et lisibles pour un lecteur d'écran, et parfois ces objectifs sont en conflit ; il n'y a pas de réponse parfaite et unique, la solution dépend de la langue.

En tant que principe directeur, essayez de donner une valeur plus élevée à un langage inclusif et neutre par rapport au langage formel correct ou aux guides de style officiellement approuvés. En anglais par exemple, de nombreux guides de style requièrent qu’un pronom singulier "she" ou "he" soit utilisé en référence à un individu, mais il est préférable dans BookWyrm d'utiliser le pronom singulier non-genré "they" à la place.

Si vous ne savez pas comment aborder un problème de traduction, commentez la traduction ou ouvrez un [sujet de discussion](https://translate.joinbookwyrm.com/project/bookwyrm/discussions) pour répondre aux questions plus larges.

## Rendre les gabarits traduisibles

Bookwyrm profite de la fonctionnalité de traduction de Django pour permettre au contenu de la page de changer en fonction de la langue d'affichage préférée du navigateur. La documentation de Django [fournit une explication utile](https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#internationalization-in-template-code) du fonctionnement, voilà la version courte :

* tous les textes du gabarit doivent inclure des balises de traduction
* ajoutez `{% load i18n %}` en haut de votre gabarit pour activer les traductions
* si le bloc de texte est du texte littéral, vous pouvez utiliser la balise `{% trans %}`
* Si le bloc de texte inclut des variables, vous devez utiliser la paire de balises `{% blocktrans %}` et `{% endblocktrans %}`. Si vous incluez des espaces ou des sauts de ligne, utilisez `trimmed` pour les supprimer automatiquement lorsque le fichier de langue est généré : `{% blocktrans trimmed %}`

### Exemples

```html
<p>{% trans "This list is currently empty" %}</p>

<p>
    {% blocktrans trimmed with username=item.user.display_name user_path=item.user.local_path %}
    Added by <a href="{{ user_path }}">{{ username }}</a>
    {% endblocktrans %}
</p>
```
