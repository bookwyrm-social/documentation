- - -
Title: Fonctionnalités optionnelles Date: 2021-08-02 Order: 8
- - -

Certaines fonctionnalités de BookWyrm doivent être activées pour fonctionner.

## Prévisualisation d'images

Par défault, BookWyrm utilise le logo de l'instance (ou le logo par défault) en tant qu'image d'aperçu OpenGraph. Une autre option est d'activer la création d'aperçus pour les livres, les utilisateur-ices et le site web.

Les images d'aperçu seront dimensionnées pour les grandes images OpenGraph (utilisé par Twitter sous le nom `summary_large_image`). Selon le type d'image, son contenu sera :

- l'image par défault de l'instance va afficher le gros logo, avec le nom de l'instance et son url
- l'image de l'utilisateur-ice va afficher leur photo de profil, nom d'affichage et nom du compte (sous la forme @nom-d'utilisateur@instance)
- l'image du livre va afficher sa page courverture, titre, sous-titre (s'il y a lieu), auteur-e et "rating" (s'il y a lieu)

Ces images vont être mises à jour à plusieurs occasions :

- image de l'instance : lorsque le nom de l'instance ou le logo sont modifiés
- image de l'utilisateur-ice : lorsque le nom d'affichage ou la photo de profil sont modifiés
- image du livre : lorsque le titre, l'auteur-e ou la couverture sont modifiés, ou quand une nouvelle note est ajoutée

### Activer la prévisualisation des images

Pour activer cette fonctionnalité avec les paramètres par défaut, il faut décommenter (retirer le `#` au début de) la ligne `ENABLE_PREVIEW_IMAGES=true` dans le fichier `.env`. Tous les nouveaux événements de mise à jour précédemment mentionnés provoqueront la génération de l'image correspondante.

Des exemples pour ces images peuvent être consultés dans [la description de la pull request de cette fonctionnalité](https://github.com/bookwyrm-social/bookwyrm/pull/1142#pullrequest-651683886-permalink).

### Générer les images de prévisualisation

Si ce paramètre est activé après le démarrage de l'instance, certaines images pourraient ne pas avoir été générées. Une commande a été ajoutée pour automatiser la génération d'images. Afin d'éviter une surconsommation de ressources en générant **BEAUCOUP** d'images, il faut passer l'argument `--all` (ou `-a`) au lancement de la génération des images de prévisualisation pour toustes les utilisateur·ices et livres. Sans cet argument, seules les prévisualisations du site seront générées.

Les images de prévisualisation des utilisateur·ices et des livres seront générées de manière asynchrone : la tâche sera envoyée à Flower. Un certain temps peut être nécessaire avant que toutes les images de prévisualisation des utilisateur·ices et des livres soient disponibles. Si vous avez un bon livre 📖, un chaton 🐱 ou un gâteau 🍰, c'est le moment parfait pour leur accorder de l'attention 💖.

### Paramètres facultatifs

Alors comme ça vous voulez personnaliser vos images de prévisualisation ? Voici les possibilités :

- `PREVIEW_BG_COLOR` définit la couleur de fond de l'image de prévisualisation. Il est possible de mettre une valeur de couleur, comme `#b00cc0`, ou les valeurs suivantes : `use_dominant_color_light` ou `use_dominant_color_dark`. Cela va extraire une couleur dominante de la couverture du livre et l'utiliser, respectivement pour le thème clair ou sombre.
- `PREVIEW_TEXT_COLOR` définit la couleur du texte. En fonction du choix de la couleur de fond, vous devriez trouver une valeur qui a un contraste suffisant pour que l'image soit accessible. Un rapport de contraste de 1:4,5 est recommandé.
- `PREVIEW_IMG_WIDTH` et `PREVIEW_IMG_HEIGHT` définissent les dimensions de l'image. Actuellement, le système fonctionnera mieux avec des images au format paysage (horizontal).
- `PREVIEW_DEFAULT_COVER_COLOR` définit la couleur des livres sans couvertures.

Toutes les variables de couleur acceptent des valeurs reconnues par le module `ImageColor` de Pillow : [En apprendre plus sur les noms de couleurs dans Pillow](https://pillow.readthedocs.io/en/stable/reference/ImageColor.html#color-names).

### Supprimer les images de prévisualisation pour les comptes externes

Avant BookWyrm 0.5.4, des images de prévisualisation étaient générées pour les comptes externes. Comme c'était couteux en termes d'espace disque et de puissance de calcul, cela a été interrompu. Si vous souhaitez supprimer en masse toutes les images précédemment générées pour les comptes distants, une nouvelle commande a été ajoutée :

```sh
./bw-dev remove_remote_user_preview_images
```

Cette commande va retirer dans la base de données la valeur de la propriété `user.preview_image` pour les comptes externes et supprimer le fichier associé.
