- - -
Titolo: Caratteristiche opzionali Data: 2021-08-02 Ordine: 8
- - -

Alcune caratteristiche di BookWyrm devono essere abilitate per funzionare.

## Generazione immagine anteprima

Per impostazione predefinita, BookWyrm utilizza il logo dell'istanza (o il logo predefinito) come immagine di anteprima OpenGraph. In alternativa, è possibile attivare la generazione di immagini di anteprima per libri, utenti e il sito web.

Le immagini di anteprima saranno dimensionate per grandi immagini OpenGraph (usate da Twitter con il nome di `summary_large_image`). A seconda del tipo di immagine, il contenuto sarà:

- l'immagine di istanza predefinita mostrerà il grande logo, insieme al nome dell'istanza e al suo url
- l'immagine utente mostrerà il suo avatar, il nome del display, la maniglia (nella forma di username@instance)
- l'immagine del libro mostrerà la copertina, il titolo, il sottotitolo (se presente), l'autore e la valutazione (se presente)

Queste immagini saranno aggiornate in vari punti:

- immagine di istanza: quando il nome dell'istanza o il grande logo sono cambiati
- immagine utente: quando il nome del display o l'avatar sono cambiati
- immagine del libro: quando il titolo, l'autore o la copertina sono cambiati, o quando viene aggiunta una nuova valutazione

### Abilitare le immagini di anteprima

Per abilitare la funzione con le impostazioni predefinite, devi scommentare (rimuovi la `#` di fronte alla) la riga `ENABLE_PREVIEW_IMAGES=true` nella tua `. file nv`. Tutti i nuovi eventi di aggiornamento di cui sopra provocheranno la generazione dell'immagine corrispondente.

Esempi per queste immagini possono essere visualizzati sulla descrizione [della richiesta di pull della funzione](https://github.com/bookwyrm-social/bookwyrm/pull/1142#pullrequest-651683886-permalink).

### Generazione immagini di anteprima

Se abiliti questa impostazione dopo che l'istanza è stata avviata, alcune immagini potrebbero non essere state generate. È stato aggiunto un comando per automatizzare la generazione di immagini. Al fine di evitare un hog di ressource generando **A LOT** di immagini, devi passare l'argomento `--all` (o `-a`) per avviare la generazione delle immagini di anteprima per tutti gli utenti e i libri. Senza questo argomento, verrà generata solo l'anteprima del sito.

Le immagini di anteprima dell'utente e del libro verranno generate in modo asincrono: l'attività verrà inviata a Flower. Potrebbe essere necessario un certo tempo prima che tutti i libri e gli utenti abbiano un'immagine di anteprima di lavoro. Se hai un buon libro 📖, un gattino 🐱 o una torta 🍰, questo è il momento perfetto per mostrare loro una certa attenzione 💖.

### Impostazioni facoltative

Così si desidera personalizzare le immagini di anteprima? Ecco le opzioni:

- `PREVIEW_BG_COLOR` imposterà il colore per lo sfondo dell'immagine di anteprima. È possibile fornire un valore di colore, come `#b00cc0`o i seguenti valori `use_dominant_color_light` o `use_dominant_color_dark`. Questi estraggono un colore dominante dalla copertina del libro e la usano, rispettivamente in una luce o in un tema scuro.
- `PREVIEW_TEXT_COLOR` imposterà il colore per il testo. A seconda della scelta del colore di sfondo, si dovrebbe trovare un valore che avrà un contrasto sufficiente perché l'immagine sia accessibile. Si raccomanda un rapporto di contrasto 1:4,5.
- `PREVIEW_IMG_WIDTH` e `PREVIEW_IMG_HEIGHT` imposteranno le dimensioni dell'immagine. Attualmente, il sistema funzionerà meglio su immagini con un orientamento orizzontale (orizzontale).
- `PREVIEW_DEFAULT_COVER_COLOR` imposterà il colore per i libri senza copertine.

Tutte le variabili di colore accettano valori che possono essere riconosciuti come colori dal modulo `ImageColor` di Cuscino: [Scopri di più sui nomi di colore Cuscino](https://pillow.readthedocs.io/en/stable/reference/ImageColor.html#color-names).

### Rimozione delle immagini di anteprima per gli utenti remoti

Prima di BookWyrm 0.5.4, le immagini di anteprima sono state generate per gli utenti remoti. Poiché era uno spreco in termini di spazio su disco e di energia di calcolo, questa generazione è stata interrotta. Se si desidera eliminare in massa tutte le immagini precedentemente generate per gli utenti remoti, è stato aggiunto un nuovo comando:

```sh
./bw-dev remove_remote_user_preview_images
```

Questo comando svuoterà la proprietà `user.preview_image` nel database per gli utenti remoti ed eliminerà il file nell'archivio.
