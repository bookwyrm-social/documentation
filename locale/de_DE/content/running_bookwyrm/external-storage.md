- - -
Title: Externer Speicher Date: 2021-06-07 Order: 7
- - -

Standardmäßig verwendet BookWyrm lokalen Speicher für statische Assets (Favicon, Standard-Avatar, etc.) und Medien (Benutzer-Avatare, Buchtitelbilder usw.), aber Sie können einen externen Speicherdienst verwenden, um diese Dateien zu bereitzustellen. BookWyrm verwendet `django-storages`, um externen Speicher wie S3-kompatible Dienste, Apache Libcloud oder SFTP anzubinden.

## S3-kompatibler Speicher

### Einrichtung

Erstellen Sie einen Bucket in Ihrem S3-kompatiblen Dienst der Wahl, zusammen mit einer Zugangsschlüssel-ID und einem geheimen Zugriffsschlüssel. Diese können selbst gehostet sein, wie [Ceph](https://ceph.io/en/) (LGPL 2.1/3.0) oder [MinIO](https://min.io/) (GNU AGPL v3.0) oder kommerziell ([Scaleway](https://www.scaleway.com/en/docs/object-storage-feature/), [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-digitalocean-space-and-api-key)…).

Diese Anleitung wurde mit Scaleway Object Storage getestet. Wenn Sie einen anderen Dienst verwenden, teilen Sie bitte Ihre Erfahrungen (insbesondere wenn Sie andere Schritte unternehmen mussten), indem Sie einen Problembericht im [BookWyrm Dokumentations](https://github.com/bookwyrm-social/documentation)-Repository einreichen.

### Was erwartet dich

Wenn du eine neue BookWyrm-Instanz startest, wird der Prozess sein:

- Richte deinen externen Speicherservice ein
- Aktiviere externen Speicher auf BookWyrm
- Starte deine BookWyrm-Instanz
- Instanz Konnektor aktualisieren

Wenn du deine Instanz bereits gestartet hast und Bilder auf den lokalen Speicher hochgeladen wurden, wird der Prozess sein:

- Richte den externen Speicherdienst ein
- Kopiere die lokalen Medien auf externen Speicher
- Aktiviere externen Speicher auf BookWyrm
- Starte die BookWyrm-Instanz neu
- Instanz-Konnektor aktualisieren

### BookWyrm-Einstellungen

Bearbeite die `.env`-Datei, indem du die folgenden Zeilen auskommentierst:

- `AWS_ACCESS_KEY_ID`: Ihre Zugangsschlüssel-ID
- `AWS_SECRET_ACCESS_KEY`: Ihr geheimer Zugangsschlüssel
- `AWS_STORAGE_BUCKET_NAME`: Ihr Bucket Name
- `AWS_S3_REGION_NAME`: z.B. `"eu-west-1"` für AWS, `"fr-par"` für Scaleway oder `"nyc3"` für Digital Ocean

Wenn dein S3-kompatibler Dienst Amazon AWS ist, solltest du startklar sein. Wenn nicht, musst du folgende Zeilen wieder kommentieren:

- `AWS_S3_CUSTOM_DOMAIN`: die Domain, die die Assets bereitstellen soll, z.B. `"example-bucket-name.s3.fr-par.scw.cloud"` oder `"${AWS_STORAGE_BUCKET_NAME}.${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`
- `AWS_S3_ENDPOINT_URL`: der S3-API-Endpunkt, z.B. `"https://s3.fr-par.scw.cloud"` oder `"https://${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`

### Kopieren lokaler Medien auf externen Speicher

Wenn die BookWyrm-Instanz bereits läuft und Medien hochgeladen wurden (Benutzer-Avatare, Buchtitelbilder…), musst du hochgeladene Medien in deinen Bucket migrieren.

Diese Aufgabe wird mit dem Befehl erledigt:

```bash
./bw-dev copy_media_to_s3
```

### Aktivierung des externen Speichers für BookWyrm

Um den S3-kompatiblen externen Speicher zu aktivieren, müssen Sie Ihre `.env`-Datei bearbeiten, indem der Eigenschaftswert für `USE_S3` von `false` zu `true` geändert wird:

```
USE_S3=true
```

Wenn der externe Speicher über HTTPS ausgeliefert wird (was die meisten dieser Tage sind), musst du auch sicherstellen, dass `USE_HTTPS` auf `true gesetzt ist`, damit Bilder über HTTPS geladen werden:

```
USE_HTTPS=true
```

#### Statische Assets

Danach musst du folgenden Befehl ausführen, um die statischen Assets in deinen S3-Bucket zu kopieren:

```bash
./bw-dev collectstatic
```

#### CORS-Einstellungen

Sobald die statischen Assets gesammelt sind, musst du Sie CORS für deinen Bucket einrichten.

Einige Dienste wie Digital Ocean bieten eine Schnittstelle, um es einzurichten, siehe [Digital Ocean doc: Wie man CORS konfiguriert](https://docs.digitalocean.com/products/spaces/how-to/configure-cors/).

Wenn dein Dienst keine Schnittstelle zur Verfügung stellt, kannst du CORS trotzdem mit der Befehlszeile einrichten.

Erstelle eine Datei namens `cors.json` mit folgendem Inhalt:

```json
{
  "CORSRules": [
    {
      "AllowedOrigins": ["https://MY_DOMAIN_NAME", "https://www.MY_DOMAIN_NAME"],
      "AllowedHeaders": ["*"],
      "AllowedMethods": ["GET", "HEAD", "POST", "PUT", "DELETE"],
      "MaxAgeSeconds": 3000,
      "ExposeHeaders": ["Etag"]
    }
  ]
}
```

Ersetzen Sie `MY_DOMAIN_NAME` durch den/die Domainname(n) Ihrer Instanz.

Führe dann den folgenden Befehl aus:

```bash
./bw-dev set_cors_to_s3 cors.json
```

Keine Ausgabe bedeutet, dass es gut sein sollte.

Wenn du eine neue BookWyrm-Instanz startest, kannst du sofort zu den Installationsanweisungen zurückkehren. Wenn nicht, lese weiter.

### Starte deine Instanz neu

Sobald die Medienmigration abgeschlossen und die statischen Assets gesammelt wurden, kannst du die neue `.env`-Konfiguration laden und die Instanz neustarten mit:

```bash
./bw-dev up -d
```

Wenn alles gut geht, wurde dein Speicher ohne Serverausfall geändert. Wenn einige Schriftarten fehlen (und die Browser-JS-Konsole mit Warnung über CORS aufwartet), schlug etwas [hier](#cors-settings) fehl. In diesem Fall kann es gut sein, die Header einer HTTP-Anfrage auf eine Datei in deinem Bucket zu überprüfen:

```bash
curl -X OPTIONS -H 'Origin: http://MY_DOMAIN_NAME' http://BUCKET_URL/static/images/logo-small.png -H "Access-Control-Request-Method: GET"
```

Ersetze `MY_DOMAIN_NAME` durch deinen Domain-Namen, `BUCKET_URL` mit der URL für deinen Bucket, du kannst den Dateipfad durch jeden anderen gültigen Pfad in deinem Bucket ersetzen.

Wenn du eine Nachricht siehst, insbesondere eine Nachricht, die mit `<Error><Code>CORSForbidden</Code>` beginnt, funktionierte sie nicht. Wenn du keine Nachricht siehst, funktioniert es.

Für eine aktive Instanz kann es eine Handvoll Dateien geben, die während der Zeit zwischen der Migration der Dateien auf den externen Speicher lokal erstellt wurden und ein Neustarten der App nutzt den externen Speicher. Um sicherzustellen, dass alle noch verbleibenden Dateien nach dem Umschalten auf den externen Speicher hochgeladen werden, kannst du folgenden Befehl verwenden, der nur Dateien hochlädt, die nicht bereits im externen Speicher vorhanden sind:

```bash
./bw-dev sync_media_to_s3
```

### Instanz-Konnektor aktualisieren

*Hinweis: Du kannst diesen Schritt überspringen, wenn du eine aktualisierte Version von BookWyrm verwendest; im September 2021 wurde der "Selbst-Steckverbinder" in [PR #1413](https://github.com/bookwyrm-social/bookwyrm/pull/1413) entfernt*

Damit die richtige URL für die Anzeige lokaler Buchsuchergebnisse verwendet wird, müssen wir den Wert für die URL-Basis der Titelbilder ändern.

Konnektor-Daten können über die Django-Admin-Schnittstelle unter der URL `http://MY_DOMAIN_NAME/admin` aufgerufen werden. Der Konnektor für deine eigene Instanz ist der erste Datensatz in der Datenbank, damit du auf den Konnektor mit dieser URL zugreifen kannst: `https://MY_DOMAIN_NAME/admin/bookwyrm/connector/1/change/`.

Das Feld _Covers url_ ist standardmäßig als `https://MY_DOMAIN_NAME/images`definiert, Sie müssen es auf `https://S3_STORAGE_URL/images` ändern. Klicke auf _Speichern_ und voilà!

Du musst den Wert für die _Covers Url_ jedes Mal aktualisieren, wenn du die URL für deinen Speicher änderst.
