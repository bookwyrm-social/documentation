- - -
Title: Optional features Date: 2021-08-02 Order: 5
- - -

Some features of BookWyrm have to be enabled to work.

## Previzualizarea generării de imagine

By default, BookWyrm uses the instance's logo (or the default logo) as an OpenGraph preview image. As an alternative, you can enable the generation of preview images for books, users, and the website.

The preview images will be sized for large OpenGraph images (used by Twitter under the name of `summary_large_image`). Depending on the type of image, the contents will be:

- imaginea implicită a instanței va afișa logo-ul mare, împreună cu numele instanței și URL-ul său
- imaginea de utilizator va afișa avatarul său, numele său afișat, numele de utilizator (sub forma numeutilizator@instanță)
- imaginea de carte va afișa coperta sa, titlul, subtitlul (dacă este cazul), autorul și ratingul (dacă este cazul)

These images will be updated at various points:

- imaginea instanței: când numele instanței sau logo-ul mare au fost schimbate
- imaginea de utilizator: când numele afișat sau avatarul au fost schimbate
- imaginea de carte: când titlul/titlurile, autorul/autorii sau coperta au fost schimbați sau o nouă recenzie este adăugată

### Activați imaginile de previzualizare

In order to enable the feature with default settings, you have to uncomment (remove the `#` in front of) the line `ENABLE_PREVIEW_IMAGES=true` in your `.env` file. All the new updating events aforementioned will cause the generation of the corresponding image.

Examples for these images can be viewed on the [feature’s pull request’s description](https://github.com/bookwyrm-social/bookwyrm/pull/1142#pullrequest-651683886-permalink).

### Generarea imaginilor de previzualizare

If you enable this setting after your instance has been started, some images may not have been generated. A command has been added to automate the image generation. In order to prevent a ressource hog by generating **A LOT** of images, you have to pass the argument `--all` (or `-a`) to start the generation of the preview images for all users and books. Without this argument, only the site preview will be generated.

User and book preview images will be generated asynchroneously: the task will be sent to Flower. Some time may be needed before all the books and users have a working preview image. If you have a good book 📖, a kitten 🐱 or a cake 🍰, this is the perfect time to show them some attention 💖.

### Setări opționale

So you want to customize your preview images? Here are the options:

- `PREVIEW_BG_COLOR` va seta culoarea de fundal a imaginii de previzualizare. Puteți furniza o valoare de culoare, precum `#b00cc0` sau următoarele valori: `use_dominant_color_light` sau `use_dominant_color_dark`. Acestea vor extrage culoarea dominantă a coperții cărții și o vor folosi într-o temă deschisă, respectiv întunecată.
- `PREVIEW_TEXT_COLOR` va seta culoarea pentru text. Depinzând de alegerea dumneavoastră pentru culoarea de fundal, trebuie să găsiți o valoarea care are suficient contrast pentru ca imaginea să fie lizibilă. Se recomandă un raport de contrast 1:4,5.
- `PREVIEW_IMG_WIDTH` și `PREVIEW_IMG_HEIGHT` vor seta dimensiunile imaginii. În prezent, sistemul va funcționa cel mai bine cu imagini având o orientare peisaj (orizontală).
- `PREVIEW_DEFAULT_COVER_COLOR` va seta culoarea pentru cărțile fără copertă.

All the color variables accept values that can be recognized as colors by Pillow’s `ImageColor` module: [Learn more about Pillow color names](https://pillow.readthedocs.io/en/stable/reference/ImageColor.html#color-names).
