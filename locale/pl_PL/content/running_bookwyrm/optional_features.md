- - -
Title: Dodatkowe funkcje Date: 2021-08-02 Order: 5
- - -

Niektóre z funkcji BookWyrm należy aktywować, aby były dostępne.

## Generowanie obrazów podglądu

Domyślnie BookWyrm używa logo instancji (lub domyślnego logo) jako obrazu podglądu OpenGraph. Możesz jednak włączyć generowanie obrazów podglądu dla książek, użytkowników oraz strony internetowej.

The preview images will be sized for large OpenGraph images (used by Twitter under the name of `summary_large_image`). W zależności od typu obrazu zawartością będzie:

- domyślny obraz instancji wyświetlający duże logo wraz z nazwą instancji oraz jej adresem URL
- the user image will display their avatar, display name, handle (in the form of username@instance)
- obraz książki wyświetli jej okładkę, podtytuł (jeśli dotyczy), autora oraz oceny (jeśli dotyczy)

Te obrazy będą aktualizowane w różnych momentach:

- obraz instancji: gdy nazwa instancji lub duże logo ulegną zmianie
- obraz użytkownika: gdy wyświetlana nazwa lub awatar ulegną zmianie
- obraz książki: gdy tytuł(y), autorzy lub okładka ulegnie zmianie lub zostanie dodana nowa ocena

### Aktywacja podglądów obrazów

Aby aktywować tę funkcję z domyślnymi ustawieniami, należy usunąć znacznik komentarza (usunąć `#` z przodu) wiersza `ENABLE_PREVIEW_IMAGES=true` w pliku `.env`. Wszystkie wspomniane nowe zdarzenia aktualizacji spowodują wygenerowanie odpowiedniego obrazu.

Examples for these images can be viewed on the [feature’s pull request’s description](https://github.com/bookwyrm-social/bookwyrm/pull/1142#pullrequest-651683886-permalink).

### Generowanie obrazów podglądu

Jeśli aktywujesz to ustawienie po uruchomieniu instancji, niektóre obrazy mogą nie zostać wygenerowane. Zostało dodane polecenie do automatyzacji generowania obrazów. In order to prevent a ressource hog by generating **A LOT** of images, you have to pass the argument `--all` (or `-a`) to start the generation of the preview images for all users and books. Bez tego argumentu zostanie wygenerowany tylko podgląd witryny.

User and book preview images will be generated asynchroneously: the task will be sent to Flower. Może minąć trochę czasu zanim wszystkie książki oraz użytkownicy będą mieć działające obrazy podglądu. Jeśli masz dobrą książkę 📖, zwierzątko 🐱 lub przekąskę 🍰 to jest to idealny moment na poświecenie im trochę uwagi 💖.

### Ustawienia opcjonalne

Chcesz dostosować swoje obrazy podglądu? Oto dostępne opcje:

- `PREVIEW_BG_COLOR` definiuje kolor tła dla obrazu podglądu. Możesz podać wartość koloru, taką jak `#b00cc0` lub użyć wartości `use_dominant_color_light` lub `use_dominant_color_dark`. Pozwoli to na wyodrębnienie dominującego koloru z okładki książki oraz użycie do odpowiednio w jasnym i ciemnym motywie.
- `PREVIEW_TEXT_COLOR` definiuje kolor tekstu. W zależności od wybranego koloru tła, należy znaleźć wartość o odpowiednim kontraście, aby obraz był czytelny. Zalecany kontrast wynosi 1:4.5.
- `PREVIEW_IMG_WIDTH` oraz `PREVIEW_IMG_HEIGHT` definiują wymiary obrazu. Obecnie system najlepiej współpracuje z obrazami o poziomej orientacji.
- `PREVIEW_DEFAULT_COVER_COLOR` definiuje color książek bez okładki.

All the color variables accept values that can be recognized as colors by Pillow’s `ImageColor` module: [Learn more about Pillow color names](https://pillow.readthedocs.io/en/stable/reference/ImageColor.html#color-names).
