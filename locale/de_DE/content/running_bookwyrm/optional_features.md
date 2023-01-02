- - -
Title: Optionale Funktionen Date: 2021-08-02 Order: 8
- - -

Einige Funktionen von BookWyrm müssen aktiviert werden, um zu funktionieren.

## Vorschaubilderzeugung

Standardmäßig verwendet BookWyrm das Logo der Instanz (oder das Standardlogo) als OpenGraph Vorschaubild. Alternativ können Sie die Erstellung von Vorschaubildern für Bücher, Benutzer und die Website aktivieren.

Die Vorschaubilder werden für große OpenGraph Bilder vergrößert (verwendet von Twitter unter dem Namen `summary_large_image`). Abhängig von der Art des Bildes wird der Inhalt sein:

- das Standardinstanzbild zeigt das große Logo an, zusammen mit dem Namen der Instanz und ihrer Url
- das Benutzerbild zeigt sein Avatar, den Anzeigenamen an (in Form von Benutzername@Instanz)
- das Buchbild zeigt sein Titelbild, Titel, Untertitel (falls vorhanden), Autor und Bewertung (falls vorhanden) an

Diese Bilder werden an verschiedenen Stellen aktualisiert:

- Instanzbild: wenn der Instanzname oder das große Logo geändert werden
- Benutzerbild: wenn der Anzeigename oder das Avatar geändert wird
- Buchbild: wenn der Titel, Autor oder das Cover geändert oder wenn eine neue Bewertung hinzugefügt wird

### Vorschaubilder aktivieren

Um die Funktion mit den Standardeinstellungen zu aktivieren, Sie müssen die Zeile `ENABLE_PREVIEW_IMAGES=true` in Ihrer `.env` Datei auskommentieren (entfernen Sie das Zeichen `#` am Anfang). Alle neuen Aktualisierungstermine führen zur Erzeugung des entsprechenden Bildes.

Beispiele für diese Bilder können in der [Beschreibung der Funktions-Pull-Anfrage](https://github.com/bookwyrm-social/bookwyrm/pull/1142#pullrequest-651683886-permalink) angesehen werden.

### Vorschaubilder erzeugen

Wenn Sie diese Einstellung aktivieren, nachdem Ihre Instanz gestartet wurde, wurden einige Bilder möglicherweise nicht generiert. Ein Befehl wurde hinzugefügt, um die Bildgenerierung zu automatisieren. Um eine Ressourcenüberlastung zu verhindern, wenn Sie **EINE MENGE** Bilder erzeugen, müssen Sie das Argument `--all` (oder `-a`) übergeben, um die Erzeugung der Vorschaubilder für alle Benutzer und Bücher zu starten. Ohne dieses Argument wird nur die Seitenvorschau generiert.

Benutzer- und Buchvorschaubilder werden asynchron erzeugt: Die Aufgabe wird an Flower gesendet. Etwas Zeit kann benötigt werden, bevor alle Bücher und Benutzer ein funktionierendes Vorschaubild haben. Wenn Sie ein gutes Buch haben 📖, ein Kätzchen 🐱 oder einen Kuchen 🍰, ist dies der perfekte Zeitpunkt, um ihnen Aufmerksamkeit 💖 zu schenken.

### Optionale Einstellungen

Sie möchten Ihre Vorschaubilder anpassen? Hier sind die Optionen:

- `PREVIEW_BG_COLOR` legt die Farbe für den Vorschauhintergrund fest. Sie können einen Farbwert angeben, wie `#b00cc0` oder die folgenden Werte `use_dominant_color_light` oder `use_dominant_color_dark`. Diese extrahieren eine dominante Farbe aus dem Buchcover und verwenden es in einem hellen bzw. dunklen Thema.
- `PREVIEW_TEXT_COLOR` legt die Farbe für den Text fest. Abhängig von der Auswahl für die Hintergrundfarbe sollten Sie einen Wert finden, der einen ausreichenden Kontrast hat, um das Bild zugänglich zu machen. Ein Kontrastverhältnis von 1:4.5 wird empfohlen.
- `PREVIEW_IMG_WIDTH` und `PREVIEW_IMG_HEIGHT` werden die Dimensionen des Bildes einstellen. Momentan funktioniert das System am besten mit Bildern mit horizontaler Ausrichtung.
- `PREVIEW_DEFAULT_COVER_COLOR` legt die Farbe für Bücher ohne Cover fest.

Alle Farbvariablen akzeptieren Werte, die im Modul `ImageColor` von Pillow als Farben erkannt werden können: [Erfahren Sie mehr über Farben von Pillow](https://pillow.readthedocs.io/en/stable/reference/ImageColor.html#color-names).

### Entferne Vorschaubilder für entfernte Accounts

Prior to BookWyrm 0.5.4, preview images were generated for remote users. As it was wasteful in therms of disk space and computing power, that generation has been stopped. Wenn du alle Bilder löschen möchtest, die zuvor für entfernte Accounts erstellt wurden, wurde ein neuer Befehl hinzugefügt:

```sh
./bw-dev remove_remote_user_preview_images
```

That command will empty the `user.preview_image` property in the database for remote users, and delete the file in storage.
