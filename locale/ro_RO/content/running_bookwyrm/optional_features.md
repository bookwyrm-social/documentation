- - -
Title: Optional features Date: 2021-08-02 Order: 8
- - -

Unele funcționalități BookWyrm trebuie să fie activate pentru a funcționa.

## Previzualizarea generării de imagine

În mod implicit, BookWyrm folosește logo-ul instanței (sau logo-ul de bază) ca imagine de previzualizare OpenGraph. Ca alternativă, puteți activa generarea de imagini de previzualizare pentru cărți, utilizatori și site-uri web.

Imaginile de previzualizare vor fi dimensionate pentru imagini OpenGraph mari (folosite de Twitter sub denumirea de `summay_large_image`). Depinzând de tipul imaginii, conținutul va fi:

- imaginea implicită a instanței va afișa logo-ul mare, împreună cu numele instanței și URL-ul său
- imaginea de utilizator va afișa avatarul său, numele său afișat, numele de utilizator (sub forma numeutilizator@instanță)
- imaginea de carte va afișa coperta sa, titlul, subtitlul (dacă este cazul), autorul și ratingul (dacă este cazul)

Aceste imagini vor fi actualizate în diferite puncte:

- imaginea instanței: când numele instanței sau logo-ul mare au fost schimbate
- imaginea de utilizator: când numele afișat sau avatarul au fost schimbate
- imaginea de carte: când titlul/titlurile, autorul/autorii sau coperta au fost schimbați sau o nouă recenzie este adăugată

### Activați imaginile de previzualizare

Pentru a activa această funcționalitate cu setările implicite, trebuie să decomentați (să înlăturați `#` din fața) liniei `ENABLE_PREVIEW_IMAGES=true` în fișierul dvs. `.env`. Toate evenimentele noi de actualizare menționate anterior vor cauza generarea imaginii corespunzătoare.

Exemple pentru aceste imaginii pot fi vizualizate pe [descrierea cererii de extragere a funcționalității](https://github.com/bookwyrm-social/bookwyrm/pull/1142#pullrequest-651683886-permalink).

### Generarea imaginilor de previzualizare

Dacă activați această setare după ce instanța dvs. a fost pornită, s-ar putea ca unele imagini să nu fi fost generate. O comandă a fost adăugată pentru a automatiza generarea de imagini. Pentru a preveni consumarea excesivă de resurse prin generarea **MULTOR** imagini, trebuie să transmiteți argumentul `--all` (sau `-a`) pentru a începe generarea imaginilor de previzualizare pentru toți utilizatorii și toate cărțile. Fără acest argument, numai previzualizarea site-ului va fi generată.

Imaginile de previzualizare pentru utilizatori și cărți vor fi generate asincron: sarcina va fi trimisă către Flower. S-ar putea să fie nevoie de ceva timp ca toate cărțile și toți utilizatorii să aibă o imagine de previzualizare funcțională. Dacă aveți o carte bună 📖, un pisoi 🐱 sau o prăjitură 🍰, acum este momentul perfect pentru a le acorda ceva atenție 💖.

### Setări opționale

Deci vreți să vă personalizați imaginile de previzualizare? Iată câteva opțiuni:

- `PREVIEW_BG_COLOR` va seta culoarea de fundal a imaginii de previzualizare. Puteți furniza o valoare de culoare, precum `#b00cc0` sau următoarele valori: `use_dominant_color_light` sau `use_dominant_color_dark`. Acestea vor extrage culoarea dominantă a coperții cărții și o vor folosi într-o temă deschisă, respectiv întunecată.
- `PREVIEW_TEXT_COLOR` va seta culoarea pentru text. Depinzând de alegerea dumneavoastră pentru culoarea de fundal, trebuie să găsiți o valoarea care are suficient contrast pentru ca imaginea să fie lizibilă. Se recomandă un raport de contrast 1:4,5.
- `PREVIEW_IMG_WIDTH` și `PREVIEW_IMG_HEIGHT` vor seta dimensiunile imaginii. În prezent, sistemul va funcționa cel mai bine cu imagini având o orientare peisaj (orizontală).
- `PREVIEW_DEFAULT_COVER_COLOR` va seta culoarea pentru cărțile fără copertă.

Toate variabilele de culoare acceptă valori care pot fi recunoscute ca atare de modulul `ImageColor` a lui Pillow: [Aflați mai multe despre numele de culori Pillow](https://pillow.readthedocs.io/en/stable/reference/ImageColor.html#color-names).

### Removing preview images for remote users

Prior to BookWyrm 0.5.4, preview images were generated for remote users. As it was wasteful in therms of disk space and computing power, that generation has been stopped. If you wish to delete in bulk all the images that were previously generated for remote users, a new command was added:

```sh
./bw-dev remove_remote_user_preview_images
```

That command will empty the `user.preview_image` property in the database for remote users, and delete the file in storage.
