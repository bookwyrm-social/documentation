- - -
Títol: Funcionalitats opcionals Data: 2021-08-02 Ordre: 8
- - -

Algunes funcionalitats de BookWyrm han de ser activades per utilitzar-les.

## Generació de previsualitzacions d'imatges

Per defecte, BookWyrm fa ús del logotip de la instància (o el logotip per defecte) mitjançant una imatge de previsualització d'OpenGraph. Com a alternativa, pots habilitar la generació d'imatges de previsualització per a llibres, usuaris i la web.

Les imatges de previsualització seran redimensionades en el cas d'imatges grans d'OpenGraph (emprades per Twitter sota el nom de `summary_large_image`). Depending on the type of image, the contents will be:

- the default instance image will display the big logo, along with the name of the instance and its url
- the user image will display their avatar, display name, handle (in the form of username@instance)
- the book image will display their cover, title, subtitle (if present), author and rating (if present)

Aquestes imatges seran actualitzades en diferents punts:

- instance image: when the instance name or big logo are changed
- user image: when the display name or avatar are changed
- book image: when the title(s), author(s) or cover are changed, or when a new rating is added

### Habilitar previsualització d'imatges

In order to enable the feature with default settings, you have to uncomment (remove the `#` in front of) the line `ENABLE_PREVIEW_IMAGES=true` in your `.env` file. All the new updating events aforementioned will cause the generation of the corresponding image.

Examples for these images can be viewed on the [feature’s pull request’s description](https://github.com/bookwyrm-social/bookwyrm/pull/1142#pullrequest-651683886-permalink).

### Generant imatges previsualitzades

If you enable this setting after your instance has been started, some images may not have been generated. A command has been added to automate the image generation. In order to prevent a ressource hog by generating **A LOT** of images, you have to pass the argument `--all` (or `-a`) to start the generation of the preview images for all users and books. Without this argument, only the site preview will be generated.

User and book preview images will be generated asynchroneously: the task will be sent to Flower. Some time may be needed before all the books and users have a working preview image. Si tens un bon llibre 📖, un gat 🐱 o un pastís 🍰, aquest és el moment perfecte per mostrar-los atenció 💖.

### Paràmetres opcionals

Vols personalitzar les teves imatges de previsualització? Aquí hi ha les opcions:

- `PREVIEW_BG_COLOR` will set the color for the preview image background. You can supply a color value, like `#b00cc0`, or the following values `use_dominant_color_light` or `use_dominant_color_dark`. These will extract a dominant color from the book cover and use it, in a light or a dark theme respectively.
- `PREVIEW_TEXT_COLOR` establirà el color pel text. Depending on the choice for the background color, you should find a value that will have a sufficient contrast for the image to be accessible. A contrast ratio of 1:4.5 is recommended.
- `PREVIEW_IMG_WIDTH` and `PREVIEW_IMG_HEIGHT` will set the dimensions of the image. Currently, the system will work best on images with a landscape (horizontal) orientation.
- `PREVIEW_DEFAULT_COVER_COLOR` will set the color for books without covers.

All the color variables accept values that can be recognized as colors by Pillow’s `ImageColor` module: [Learn more about Pillow color names](https://pillow.readthedocs.io/en/stable/reference/ImageColor.html#color-names).

### Eliminar previsualització d'imatges per a usuaris remots

Prior to BookWyrm 0.5.4, preview images were generated for remote users. As it was wasteful in terms of disk space and computing power, that generation has been stopped. If you wish to delete in bulk all the images that were previously generated for remote users, a new command was added:

```sh
./bw-dev remove_remote_user_preview_images
```

That command will empty the `user.preview_image` property in the database for remote users, and delete the file in storage.
