- - -
Title: Externer Speicher Date: 2021-06-07 Order: 6
- - -

Standardmäßig verwendet BookWyrm lokalen Speicher für statische Assets (Favicon, Standard-Avatar, etc.) und Medien (Benutzer-Avatare, Buchtitelbilder usw.), aber Sie können einen externen Speicherdienst verwenden, um diese Dateien zu bereitzustellen. BookWyrm verwendet `django-storages`, um externen Speicher wie S3-kompatible Dienste, Apache Libcloud oder SFTP anzubinden.

## S3-kompatibler Speicher

### Einrichtung

Erstellen Sie einen Bucket in Ihrem S3-kompatiblen Dienst der Wahl, zusammen mit einer Zugangsschlüssel-ID und einem geheimen Zugriffsschlüssel. Diese können selbst gehostet sein, wie [Ceph](https://ceph.io/en/) (LGPL 2.1/3.0) oder [MinIO](https://min.io/) (GNU AGPL v3.0) oder kommerziell ([Scaleway](https://www.scaleway.com/en/docs/object-storage-feature/), [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-digitalocean-space-and-api-key)…).

Diese Anleitung wurde mit Scaleway Object Storage getestet. Wenn Sie einen anderen Dienst verwenden, teilen Sie bitte Ihre Erfahrungen (insbesondere wenn Sie andere Schritte unternehmen mussten), indem Sie einen Problembericht im [BookWyrm Dokumentations](https://github.com/bookwyrm-social/documentation)-Repository einreichen.

### Was erwartet Sie

Wenn Sie eine neue BookWyrm-Instanz starten, wird der Prozess sein:

- Richten Sie Ihren externen Speicherservice ein
- Aktiviere externen Speicher auf BookWyrm
- Starten Sie Ihre BookWyrm-Instanz
- Instanz Konnektor aktualisieren

Wenn Sie Ihre Instanz bereits gestartet haben und Bilder auf den lokalen Speicher hochgeladen wurden, wird der Prozess sein:

- Richten Sie Ihren externen Speicherdienst ein
- Kopieren Sie Ihre lokalen Medien auf externen Speicher
- Aktiviere externen Speicher auf BookWyrm
- Starten Sie Ihre BookWyrm-Instanz neu
- Instanz-Konnektor aktualisieren

### BookWyrm-Einstellungen

Bearbeiten Sie Ihre `.env`-Datei, indem Sie die folgenden Zeilen auskommentieren:

- `AWS_ACCESS_KEY_ID`: Ihre Zugangsschlüssel-ID
- `AWS_SECRET_ACCESS_KEY`: Ihr geheimer Zugangsschlüssel
- `AWS_STORAGE_BUCKET_NAME`: Ihr Bucket Name
- `AWS_S3_REGION_NAME`: z.B. `"eu-west-1"` für AWS, `"fr-par"` für Scaleway oder `"nyc3"` für Digital Ocean

Wenn Ihr S3-kompatibler Dienst Amazon AWS ist, sollten Sie startklar sein. Wenn nicht, müssen Sie die folgenden Zeilen wieder kommentieren:

- `AWS_S3_CUSTOM_DOMAIN`: die Domain, die die Assets bereitstellen soll, z.B. `"example-bucket-name.s3.fr-par.scw.cloud"` oder `"${AWS_STORAGE_BUCKET_NAME}.${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`
- `AWS_S3_ENDPOINT_URL`: der S3-API-Endpunkt, z.B. `"https://s3.fr-par.scw.cloud"` oder `"https://${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`

### Kopieren lokaler Medien auf externen Speicher

Wenn Ihre BookWyrm-Instanz bereits läuft und Medien hochgeladen wurden (Benutzer-Avatare, Buchtitelbilder…), müssen Sie hochgeladene Medien in Ihren Bucket migrieren.

Diese Aufgabe wird mit dem Befehl erledigt:

```bash
./bw-dev copy_media_to_s3
```

### Aktivierung des externen Speichers für BookWyrm

Um den S3-kompatiblen externen Speicher zu aktivieren, müssen Sie Ihre `.env`-Datei bearbeiten, indem der Eigenschaftswert für `USE_S3` von `false` zu `true` geändert wird:

```
USE_S3=true
```

Wenn Ihr externer Speicher über HTTPS ausgeliefert wird (was die meisten dieser Tage sind), müssen Sie auch sicherstellen, dass `USE_HTTPS` auf `true gesetzt ist`, damit Bilder über HTTPS geladen werden:

```
USE_HTTPS=true
```

#### Statische Assets

Danach müssen Sie den folgenden Befehl ausführen, um die statischen Assets in Ihren S3-Bucket zu kopieren:

```bash
./bw-dev collectstatic
```

#### CORS-Einstellungen

Sobald die statischen Assets gesammelt sind, müssen Sie CORS für Ihren Bucket einrichten.

Einige Dienste wie Digital Ocean bieten eine Schnittstelle, um es einzurichten, siehe [Digital Ocean doc: Wie man CORS konfiguriert](https://docs.digitalocean.com/products/spaces/how-to/configure-cors/).

Wenn Ihr Dienst keine Schnittstelle zur Verfügung stellt, können Sie CORS trotzdem mit der Befehlszeile einrichten.

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

Führen Sie dann den folgenden Befehl aus:

```bash
./bw-dev set_cors_to_s3 cors.json
```

Keine Ausgabe bedeutet, dass es gut sein sollte.

Wenn Sie eine neue BookWyrm-Instanz starten, können Sie sofort zu den Installationsanweisungen zurückkehren. Wenn nicht, lesen Sie weiter.

### Aktualisiere deine Instanz

Sobald die Medienmigration abgeschlossen und die statischen Assets gesammelt wurden, können Sie die neue `.env`-Konfiguration laden und Ihre Instanz neustarten mit:

```bash
./bw-dev up -d
```

Wenn alles gut geht, wurde Ihr Speicher ohne Serverausfall geändert. Wenn einige Schriftarten fehlen (und Ihre Browser-JS-Konsole mit Warnung über CORS aufwartet), schlug etwas [hier](#cors-settings) fehl. In diesem Fall kann es gut sein, die Header einer HTTP-Anfrage auf eine Datei in Ihrem Bucket zu überprüfen:

```bash
curl -X OPTIONS -H 'Origin: http://MY_DOMAIN_NAME' http://BUCKET_URL/static/images/logo-small.png -H "Access-Control-Request-Method: GET"
```

Ersetzen Sie `MY_DOMAIN_NAME` durch Ihren Domain-Namen, `BUCKET_URL` mit der URL für Ihren Bucket, Sie können den Dateipfad durch jeden anderen gültigen Pfad in Ihrem Bucket ersetzen.

Wenn Sie eine Nachricht sehen, insbesondere eine Nachricht, die mit `<Error><Code>CORSForbidden</Code>` beginnt, funktionierte sie nicht. Wenn Sie keine Nachricht sehen, funktionierte es.

Für eine aktive Instanz kann es eine Handvoll Dateien geben, die während der Zeit zwischen der Migration der Dateien auf den externen Speicher lokal erstellt wurden und ein Neustarten der App nutzt den externen Speicher. Um sicherzustellen, dass alle noch verbleibenden Dateien nach dem Umschalten auf den externen Speicher hochgeladen werden, können Sie den folgenden Befehl verwenden, der nur Dateien hochlädt, die nicht bereits im externen Speicher vorhanden sind:

```bash
./bw-dev sync_media_to_s3
```

### Instanz-Konnektor aktualisieren

*Hinweis: Sie können diesen Schritt überspringen, wenn Sie eine aktualisierte Version von BookWyrm verwenden; im September 2021 wurde der "Selbst-Steckverbinder" in [PR #1413](https://github.com/bookwyrm-social/bookwyrm/pull/1413) entfernt*

Damit die richtige URL für die Anzeige lokaler Buchsuchergebnisse verwendet wird, müssen wir den Wert für die URL-Basis der Titelbilder ändern.

Konnektor-Daten können über die Django-Admin-Schnittstelle unter der URL `http://MY_DOMAIN_NAME/admin` aufgerufen werden. Der Konnektor für Ihre eigene Instanz ist der erste Datensatz in der Datenbank, damit Sie auf den Konnektor mit dieser URL zugreifen können: `https://MY_DOMAIN_NAME/admin/bookwyrm/connector/1/change/`.

Das Feld _Covers url_ ist standardmäßig als `https://MY_DOMAIN_NAME/images`definiert, Sie müssen es auf `https://S3_STORAGE_URL/images` ändern. Klicken Sie dann auf _Speichern_ und voilà!

Sie müssen den Wert für die _Covers Url_ jedes Mal aktualisieren, wenn Sie die URL für Ihren Speicher ändern.
