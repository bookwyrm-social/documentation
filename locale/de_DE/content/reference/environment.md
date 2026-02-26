---
Title: Umgebungsvariablen
Date: 2025-04-28
Order: 1
---

BookWyrm-Server benötigen gewisse Umgebungsvariablen (engl. "environment", kurz `ENV`), um korrekt zu funktionieren. Diese werden in einer Datei namens `.env` gesetzt, die in dem Verzeichnis liegt, aus dem heraus du BookWyrm ausführst. Du wirst die meisten dieser Variablen in der Datei `.env.example` beschrieben finden, die im Hauptcoderepository liegt. Kopiere diese Datei und nutze sie als Basis für deine Datei `.env`.

**BookWyrm-Instanzadministrator\*innen** sollten aufmerksam die Veröffentlichungshinweise jeder Version auf Änderungen oder Erweiterungen der Umgebungsvariablen prüfen.

Wo immer dies möglich ist, sollten **BookWyrm-Entwickler\*innen** `site.settings` gegenüber `ENV`-Werten bevorzugen, wenn sie neue Konfigurationsoptionen einführen.

## Notwendige Einstellungen

Die Datei `.env.example` beinhaltet Standardwerte für die Kerneinstellungen. Diese sind als sichere Standardwerte für Produktivumgebungen ausgelegt, abgesehen von den Standardpasswörtern. Nutzer\*innen von Docker können `./bw-dev create_secrets` ausführen, um sichere und einzigartige Geheimnisse für folgende Variablen zu generieren:

- `SECRET_KEY`
- `POSTGRES_PASSWORD`
- `REDIS_ACTIVITY_PASSWORD`
- `REDIS_BROKER_PASSWORD`
- `FLOWER_PASSWORD`

Du _musst_ jeder dieser Einstellungen in deiner `.env`-Datei angemessene Werte zuweisen:

- `SECRET_KEY`
- `DOMAIN`
- Flower:
  - `FLOWER_USER`
  - `FLOWER_PASSWORD`
  - `FLOWER_PORT`
- E-Mail (dürfen in Entwicklungsumgebung leere Zeichenketten beinhalten, aber diese müssen nichtsdestotrotz gesetzt werden):
  - `EMAIL_HOST`
  - `EMAIL_PORT`
  - `EMAIL_HOST_USER`
  - `EMAIL_HOST_PASSWORD`
  - `EMAIL_USE_TLS`
  - `EMAIL_USE_SSL`
  - `EMAIL_SENDER_NAME`
- Postgres:
  - `POSTGRES_USER`
  - `POSTGRES_DB`
  - `POSTGRES_HOST`
  - `POSTGRES_PASSWORD`
- Redis:
  - `REDIS_BROKER_HOST`
  - `REDIS_BROKER_PORT`
  - `REDIS_ACTIVITY_HOST`
  - `REDIS_ACTIVITY_PORT`
  - `REDIS_ACTIVITY_PASSWORD`
  - `REDIS_BROKER_PASSWORD`

Wenn BookWyrm in einer **Entwicklungsumgebung** betrieben wird:

- `NGINX_SETUP` **muss** `reverse_proxy` zugewiesen werden
- `DEBUG` _sollte_ `true` zugewiesen werden
- `DOMAIN` darf `localhost` zugewiesen werden

Wenn BookWyrm in einer **Produktivumgebung** betrieben wird:

- `DEBUG` **muss** `false` zugewiesen werden
- `DOMAIN` **darf nicht** `localhost` zugewiesen werden
- E-Mail-Einstellungen **müssen** real sein und einen E-Mail-Provider für den Massenversand wie zum Beispiel mailgun verwenden

## Django-Einstellungen

Lerne mehr über alle diese Einstellungen in [der Django-Referenz](https://docs.djangoproject.com/en/4.2/ref/settings).

### `ALLOWED_HOSTS`

- **Typ**: Zeichenkette kommaseparierter Werte
- **Default**: alle

Eine Liste von Zeichenketten, die die Hosts und Domain-Namen representieren, unter denen diese Seite ausgeliefert werden darf. Dies ist eine Sicherheitsmaßnahme, um HTTP-Host-Header-Angriffe zu verhindern, die selbst bei vielen scheinbar sicheren Web-Server-Konfigurationen möglich sind.

Der Standard ist es, alle Hosts zuzulassen, aber du solltest dies ändern. Beispiel: `"localhost,bookwyrm.example.com"`

### `MEDIA_ROOT`

- **Typ**: Zeichenkette
- **Default**: `images`

Absoluter Dateipfad zu dem Verzeichnis, das von Nutzer\*innen hochgeladene Dateien enthält. Wenn Docker zum Einsatz kommt, denke daran, dass dieses Verzeichnis innerhalb deines Containers liegt, nicht auf der Host-Maschine.

### `SECRET_KEY`

- notwendig
- **Typ**: Zeichenkette
- **Default**: `"7(2w1sedok=aznpq)ta1mc4i%4h=xx@hxwx*o57ctsuml0x%fr"`

Ein geheimer Schlüssel für die jeweilige BookWyrm-Instanz. Er wird genutzt, um kryptographische Signaturen bereitzustellen, und sollte auf eine einzigartige, nicht vorhersagbare, lange Zeichenkette festgelegt werden.

Wenn du den `SECRET_KEY` in `.env.example` nicht änderst, wird BookWyrm eine Fehlermeldung zeigen und sich weigern, zu starten.

### `STATIC_ROOT`

- **Typ**: Zeichenkette
- **Default**: `static`

Der absolute Pfad zu dem Verzeichnis, in dem `collectstatic` alle statischen Dateien zur Auslieferung aufsammelt. Wenn Docker zum Einsatz kommt, denke daran, dass dieses Verzeichnis innerhalb deines Containers liegt, nicht auf der Host-Maschine.

### `DEBUG`

- **Typ**: Boolean
- **Default**: `false`

`DEBUG` stellt in der Weboberfläche nützliche Fehlerinformationen bereit, die zum Debuggen des Entwicklungsservers genutzt werden können.

In Produktivsystemen sollte `false` zugewiesen werden. **Stelle niemals eine Seite öffentlich zur Verfügung, bei der `DEBUG` auf `true` gesetzt wurde.**

**Hinweis:** Bis einschließlich Version 0.7.5 war der Standardwert für `DEBUG` `true`.

### `LANGUAGE_CODE`

- **Typ**: Zeichenkette
- **Default**: `"en-us"`

Eine Zeichenkette, die die Standardsprache für diese Installation repräsentiert.

### `SESSION_COOKIE_AGE`

- **Typ**: Integer
- **Default**: `2592000`

Die Zeit, bis man abgemeldet wird (in Sekunden). Der Standardwert entspricht 30 Tagen. Zukünftig wird dieser Wert [voraussichtlich auf ein Jahr geändert](https://github.com/bookwyrm-social/bookwyrm/issues/3082).

### `DATA_UPLOAD_MAX_MEMORY_MiB`

- **Typ**: Integer
- **Default**: `100`

Maximal erlaubter Speicher für Dateiuploads. Du kannst dies erhöhen, wenn Nutzer\*innen Probleme beim Upload von BookWyrm-Exportdateien feststellen. Die eigentliche Django-Einstellung ist `DATA_UPLOAD_MAX_MEMORY_SIZE`, allerdings nutzen wir in der `.env`-Datei diese Variable, um Instanz-Administrator\*innen zu erlauben, den Wert [in Mebibytes](https://en.wikipedia.org/wiki/Byte#Multiple-byte_units) anstelle von Bytes anzugeben.

## Grundlegende BookWyrm-Seiteneinstellungen

### `DEFAULT_LANGUAGE`

- **Typ**: Zeichenkette
- **Default**: `English`

Bücher werden in Suchergebnissen priorisiert, wenn eine ihrer Sprachen (im Feld `language`) diesem Wert entspricht.

### `DOMAIN`

- **notwendig**
- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Der Fully Qualified Domain Name deiner Website. Gib kein Protokoll und keinen Port an. Beispiel: `example.com` oder `subdomain.example.com`.

### `EMAIL`

- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Die Adresse wird in der `docker-compose.yml`-Datei des `production`-Branches an Certbot weitergereicht.

### `NGINX_SETUP`

- **Typ**: Zeichenkette
- **Default**: `https`
- **Optionen**: `https`, `reverse_proxy`

Signalisiert die `nginx`-Konfiguration. `https` nimmt an, dass der gesamte Datenverkehr durch BookWyrms `nginx`-Container gehandhabt wird. In dieser Konfiguration wird versucht, mit Certbot ein HTTPS-Zertifikat zu erstellen. `reverse_proxy` dagegen nimmt an, dass der Datenverkehr von einem vorgeschalteten Webserver zwischen BookWyrm und der Außenwelt gehandhabt wird. In der Entwicklungsumgebung sollte immer `reverse_proxy` gesetzt werden.

### `PORT`

- **Typ**: Integer
- **Default**: `443`, oder `80`, wenn die Domain `localhost` entspricht.

Der Port, der für die Kommunikation im Web genutzt wird. Beachte, dass diese Einstellung sich von Djangos `PORT` unterscheidet.

### `USE_HTTPS`

Diese Variable wurde nach Version `v0.7.5` obsolet. Es wird angenommen, dass deine Instanz HTTPS verwendet, sofern die Domain nicht `localhost` ist.

## Suchen

Diese Konfiguration kann künftig zu `site.settings` verschoben werden.

### `SEARCH_TIMEOUT`

- **Typ**: Integer
- **Default**: `8`

Die Höchstdauer in Sekunden, die die Instanz nutzen wird, um über Konnektoren Inhalte zu suchen.

### `QUERY_TIMEOUT`

- **Typ**: Integer
- **Default**: `5`

Zeitbeschränkung für eine Anfrage an einen einzelnen Konnektor.

## Postgres-Konfiguration

Die Hauptdatenbank für BookWyrm nutzt Postgres.

### `PGPORT`

- **Typ**: Integer
- **Default**: `5432`

Der Port, um sich mit dem Postgres-Server zu verbinden. Entspricht Djangos `PORT`.

### `POSTGRES_PASSWORD`

- **Typ**: Zeichenkette
- **Default**: `bookwyrm`

Passwort für die Datenbank. Lege hier ein starkes Passwort fest. Setze es in Anführungszeichen, um Probleme mit der Fehlinterpretation gewisser Zeichen zu vermeiden.

**Nutze weder die Standardwerte aus `.env` noch aus `setings.py`**, da diese öffentlich bekannt sind.

### `POSTGRES_USER`

- **Typ**: Zeichenkette
- **Default**: `bookwyrm`

Der Name deines Datenbankbenutzers. Entspricht Djangos `USER`.

### `POSTGRES_DB`

- **Typ**: Zeichenkette
- **Default**: `bookwyrm`

Der Name deiner Datenbank.

### `POSTGRES_HOST`

- **Typ**: Zeichenkette
- **Default**: `localhost`

Der Host-Server deiner Datenbank. Wird dieser Wert nicht gesetzt oder leer gelassen, wird `localhost` angenommen. Entspricht Djangos `HOST`.

## Redis

Redis wird verwendet, um sowohl Aktivitätsströme als auch Hintergrundaufgaben zu verwalten.

### `MAX_STREAM_LENGTH`

- **Typ**: Integer
- **Default**: `200`

Die Maximallänge für Redis-Streams. Wird ein Stream größer, wird Redis die ältesten Elemente verwerfen, um die `MAX_STREAM_LENGTH` nicht zu überschreiten.

Siehe [Redis-`XTRIM`-Dokumentation](https://redis.io/docs/latest/commands/xtrim/) für weitere Details.

### `REDIS_ACTIVITY_HOST`

- **Typ**: Zeichenkette
- **Default**: `localhost`

Der Redis-Server-Host. Wird als `localhost` angenommen, sofern nichts anderes angegeben wird. Wenn du Docker verwendest, sollte der Wert üblicherweise `redis_activity` sein, damit du den gleichnamigen Redis-Container verwendest.

### `REDIS_ACTIVITY_PORT`

- **Typ**: Integer
- **Default**: `6379`

Der Port, den dein Redis-Server verwendet.

### `REDIS_ACTIVITY_PASSWORD`

- **Typ**: Zeichenkette
- **Default**: leer

Das Passwort für deine Redis-Datenbank.

### `REDIS_ACTIVITY_DB_INDEX`

- **Typ**: Integer
- **Default**: nicht gesetzt

Wenn du nicht das Standard-Docker-Setup mit separatem Redis-Server für Aktivitäts-Streams verwendest, solltest du `REDIS_ACTIVITY_DB_INDEX` setzen, um zu signalisieren, welche Redis-Datenbank für BookWyrms Aktivitätsströme verwendet wird.

### `REDIS_ACTIVITY_URL`

- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Wenn du eine externe Redis-Datenbank oder einen Unix-Socket verwendest, kannst du alle anderen Redis-Einstellungen überschreiben, indem du die volle `REDIS_ACTIVITY_URL` setzt.

Beispiel: `"redis://username:top_secret_pass@example.com:6380/0"`

### `REDIS_BROKER_HOST`

- **Typ**: Zeichenkette
- **Default**: `localhost`

Der Redis-Celery-Server-Host. Wird als `localhost` angenommen, sofern nichts anderes angegeben wird. Wenn du Docker verwendest, sollte der Wert üblicherweise `redis_broker` sein, damit du den gleichnamigen Redis-Container verwendest.

### `REDIS_BROKER_PORT`

- **Typ**: Integer
- **Default**: `6379`

Der Port, den dein Redis-Celery-Server verwendet.

### `REDIS_BROKER_PASSWORD`

- **Typ**: Zeichenkette
- **Default**: leer

Das Passwort für deine Redis-Celery-Datenbank.

### `REDIS_BROKER_DB_INDEX`

- **Typ**: Integer
- **Default**: nicht gesetzt

Wenn du nicht das Standard-Docker-Setup mit separatem Redis-Server für Celery verwendest, solltest du `REDIS_ACTIVITY_DB_INDEX` setzen, um zu signalisieren, welche Redis-Datenbank für BookWyrms Aktivitätsströme verwendet wird.

### `REDIS_BROKER_URL`

- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Wenn du eine externe Redis-Datenbank oder einen Unix-Socket verwendest, kannst du alle anderen Redis-Einstellungen für deine Celery-Datenbank überschreiben, indem du die volle `REDIS_BROKER_URL` setzt.

Beispiel: `"redis://username:top_secret_pass@example.com:6380/0"`

## Flower

Flower stellt eine Weboberfläche zur Verfügung, um Celery-Tasks zu überwachen.

### `FLOWER_PORT`

- **Typ**: Integer
- **Default**: `8888`

Der Port für die Flower-Seite, um Celery unter `https://example.com/flower` zu überwachen.

### `FLOWER_USER`

- **notwendig**
- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Der Nutzer deiner Flower-Instanz.

### `FLOWER_PASSWORD`

- **notwendig**
- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Das Passwort für deine Flower-Überwachungsoberfläche. Flower kann alle Nachrichten sehen, die deinen Server erreichen, daher ist es wichtig, dass du ein starkes, einzigartiges Passwort setzt und dieses sicher verwahrst.

## E-Mail-Konfiguration

### `EMAIL_HOST`

- **notwendig**
- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Die SMTP-Adresse deines E-Mail-Hosts. Beispiel: `smtp.mailgun.org`. Prüfe stets die Nutzungsbedingungen deines E-Mail-Anbieters, bevor du deinen Account nutzt, um große Mengen E-Mails zu versenden. Du wirst vermutlich einen Dienst wie Mailgun benötigen.

### `EMAIL_PORT`

- **Typ**: Integer
- **Default**: `587`

Der SMTP-Server-Port deines E-Mail-Anbieters.

### `EMAIL_HOST_USER`

- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Der Nutzername deines E-Mail-Anbieters. Normalerweise eine volle E-Mail-Adresse wie `mail@your.domain.here`.

### `EMAIL_HOST_PASSWORD`

- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Das Passwort für den Account bei deinem E-Mail-Anbieter.

### `EMAIL_USE_TLS`

- **Typ**: Boolean
- **Default**: `true`

Ob deine SMTP-Verbidung TLS nutzt. Prüfem hierfür, ob du den richtigen `EMAIL_PORT` verwendest.

### `EMAIL_USE_SSL`

- **Typ**: Boolean
- **Default**: `false`

Ob deine SMTP-Verbidung SSL nutzt. Prüfem hierfür, ob du den richtigen `EMAIL_PORT` verwendest.

### `EMAIL_SENDER_NAME`

- **Typ**: Zeichenkette
- **Default**: `admin`

Der erste Teil der E-Mail-Adresse für Nachrichten, die deine BookWyrm-Instanz versendet. Beispiel: **`admin`**@example.com.

### `EMAIL_SENDER_DOMAIN`

- **Typ**: Zeichenkette
- **Default**: wie `DOMAIN`

Die Domain der E-Mail-Adresse für Nachrichten, die deine BookWyrm-Instanz versendet. Beispiel: admin@**`example.com`**.

## S3-Object-Storage

### `USE_S3`

- **Typ**: Boolean
- **Default**: `false`

Zeigt an, ob du S3-Object-Storage für Bilder und statische Dateien nutzt.

### `USE_S3_FOR_EXPORTS`

- **Typ**: Boolean
- **Default**: `false`

Zeigt an, ob du S3-Object-Storage für Dateien bei Kontoexporten und -importen nutzt. Standardmäßig beinhaltet `USE_S3` Kontoimporte und -exporte nicht. Es ist sicherer, hierfür den lokalen Speicher zu verwenden und den normalen Dateilöschvorgang regelmäßig auszuführen. Auf größeren Instanzen kann der lokale Speicher Performanzprobleme hervorrufen und es kann sich anbieten, diesen Wert auf `true` zu setzen.

### `S3_SIGNED_URL_EXPIRY`

- **Typ**: Integer
- **Default**: `900`

Die Anzahl an Sekunden, bevor signierte S3-URLs ablaufen. Dies wird aktuell nur für Konto-Exportdateien verwendet. Der Wert sollte nur so groß sein, wie es notwendig ist, um als Nutzer\*in einen Download abzuschließen, nachdem man bei Abschluss eines Exports auf "Herunterladen" geklickt hat.

### `AWS_ACCESS_KEY_ID`

- **notwendig**, wenn S3-Speicher zum Einsatz kommt
- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Zugriffsschlüssel für S3-Speicher aller Art.

### `AWS_DEFAULT_ACL`

- **notwendig**, wenn Backblaze-Speicher zum Einsatz kommt
- **Typ**: Zeichenkette
- **Default**: "public-read"

Backblaze (B2) erkennt "public-read" nicht als eine Standard-ACL-Einstellung an. Backblaze-Nutzer\*innen sollten daher eine leere Zeichenkette angeben.

### `AWS_SECRET_ACCESS_KEY`

- **notwendig**, wenn S3-Speicher zum Einsatz kommt
- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Geheimer Schlüssel für S3-Speicher aller Art.

### `AWS_STORAGE_BUCKET_NAME`

- **notwendig**, wenn S3-Speicher zum Einsatz kommt
- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Der Bucket-Name, den du nutzt. Beispiel: `"example-bucket-name"`

### `AWS_S3_REGION_NAME`

- **notwendig**, wenn S3-Speicher zum Einsatz kommt
- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Der S3-Regionenname. Beispiel: `"eu-west-1"` für AWS, `"fr-par"` für Scaleway, `"nyc3"` für Digital Ocean oder `"cluster-id"` für Linode.

### `AWS_S3_CUSTOM_DOMAIN`

- **notwendig**, wenn S3-Storage zum Einsatz kommt, der nicht von AWS betrieben wird (z. B. Scaleway oder Digital Ocean Spaces)
- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Die Domain, unter der Assets ausgeliefert werden. Beispiel: `"example-bucket-name.s3.fr-par.scw.cloud"`

### `AWS_S3_URL_PROTOCOL`

- **Typ**: Zeichenkette
- **Default**: wie `PROTOCOL` mit Doppelpunkt, also etwa "http:"

Protokoll für den S3-Speicher. Wird in der Produktivumgebung standardmäßig als `https:` angenommen. Du musst dies nicht setzen, sofern du das Standardverhalten nicht überschreiben möchtest.

### `AWS_S3_ENDPOINT_URL`

- **notwendig**, wenn S3-Storage zum Einsatz kommt, der nicht von AWS betrieben wird (z. B. Scaleway oder Digital Ocean Spaces)
- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Der S3-API-Endpunkt. Beispiel: `"https://s3.fr-par.scw.cloud"`

## Azure-Blob-Storage

Diese Werte werden benötigt, wenn [Azure-Blob-Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-get-info) zum Einsatz kommt.

### `USE_AZURE`

- **Typ**: Boolean
- **Default**: `false`

### `AZURE_ACCOUNT_NAME`

- **notwendig**, wenn Azure-Speicher zum Einsatz kommt
- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Beispiel: `"example-account-name"`

### `AZURE_ACCOUNT_KEY`

- **notwendig**, wenn Azure-Speicher zum Einsatz kommt
- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Beispiel: `"Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw=="`

### `AZURE_CONTAINER`

- **notwendig**, wenn Azure-Speicher zum Einsatz kommt
- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Der einzigartige Name deines Containers. Beispiel: `"example-blob-container-name"`.

### `AZURE_CUSTOM_DOMAIN`

- **Typ**: Zeichenkette
- **Default**: nicht gesetzt

Du kannst eine [eigene Domain](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-custom-domain-name?tabs=azure-portal) für den Azure-Blob-Storage nutzen, aber dies ist nicht notwendig. Beispiel: `"example-account-name.blob.core.windows.net"`.

## Bildgenerierung

Teile dieser Konfiguration könnten künftig zu `site.settings` verschoben werden.

### `ENABLE_THUMBNAIL_GENERATION`

- **Typ**: Boolean
- **Default**: `false`

Ob die Generierung von Vorschaubildern für Buch-Titelbilder aktiviert werden soll. Wenn du dies auf `true` setzt, wird die Performanz beim Rendern der Bilder verbessert. Allerdings wird für das Speichern der Titelbilder 4- bis 5-mal soviel Speicher benötigt. Aus diesem Grund ist der Standardwert `false`.

### `ENABLE_PREVIEW_IMAGES`

- **Typ**: Boolean
- **Default**: `false`

Diese Einstellung erlaubt es dem Server, Vorschaubilder zu generieren, die als OpenGraph-Bilder (auch als Twitter-Card-Bilder bekannt) genutzt werden. Diese Vorschaubilder werden für Bücher (jedes Mal, wenn sich der Titel, das Vorschaubild oder der\*die Autor\*in ändern oder wenn eine neue öffentliche Bewertung veröffentlicht wird), Konten (jedes Mal, wenn sich der Name oder Avatar ändert) und die Website (jedes Mal, wenn sich der Seitenname, die Beschreibung oder das Logo ändert) generiert. Siehe [Optionale Features](/optional_features.html) für weitere Informationen.

### `PREVIEW_BG_COLOR`

- **Typ**: Zeichenkette
- **Default**: `use_dominant_color_light`

Die Hintergrundfarbe für Vorschaubilder. Du kannst ein RGB-Tupel oder RGB-Hex-Werte angeben oder `use_dominant_color_light`/`use_dominant_color_dark` angeben.

### `PREVIEW_TEXT_COLOR`

- **Typ**: Zeichenkette
- **Default**: `#363636`

Die Textfarbe für Vorschaubilder. Wenn die `PREVIEW_BG_COLOR` auf `use_dominant_color_dark` gesetzt ist, sollte dies `#fff` sein.

### `PREVIEW_IMG_WIDTH`

- **Typ**: Integer
- **Default**: `1200`

Breite für Vorschaubilder in Pixeln.

### `PREVIEW_IMG_HEIGHT`

- **Typ**: Integer
- **Default**: `630`

Höhe für Vorschaubilder in Pixeln.

### `PREVIEW_DEFAULT_COVER_COLOR`

- **Typ**: Zeichenkette
- **Default**: `#002549`

Wenn es zu einem Buch kein Titelbild gibt, erstellen wir ein neues Titelbild. Diese Einstellung bestimmt die Farbe dieses neuen Titelbilds.

### `PREVIEW_DEFAULT_FONT`

- **Typ**: Zeichenkette
- **Default**: `Source Han Sans`

Wenn es zu einem Buch kein Titelbild gibt, erstellen wir ein neues Titelbild. Diese Einstellung bestimmt die Schriftart dieses neuen Titelbilds.

## Telemetrie

Use these settings to enable automatically sending telemetry to an OTLP-compatible service. Many of the main monitoring apps have OLTP collectors, including NewRelic, DataDog, and Honeycomb.io - consult their documentation for setup instructions.

### `OTEL_EXPORTER_OTLP_ENDPOINT`

- **Type**: String
- **Default**: not set

API endpoint for your provider.

### `OTEL_EXPORTER_OTLP_HEADERS`

- **Type**: String
- **Default**: not set

Any headers required, usually authentication information.

### `OTEL_SERVICE_NAME`

- **Type**: String
- **Default**: not set

Service name is an arbitrary tag that is attached to any data sent, used to distinguish different sources. It can be useful for sending prod and dev metrics to the same place and keeping them separate, for instance.

## HTTP headers

### `HTTP_X_FORWARDED_PROTO`

- **Type**: Boolean
- **Default**: `false`

Setting this to `true` can compromise your site’s security. Ensure you fully understand your setup before changing it.

Only use it if your proxy is "swallowing" whether the original request was made via https. Please [refer to the Django Documentation](https://docs.djangoproject.com/en/4.2/ref/settings/#secure-proxy-ssl-header) and assess the risks for your instance.

### `CSP_ADDITIONAL_HOSTS`

- **Type**: String
- **Default**: not set

Additional hosts to allow in the `Content-Security-Policy`, "self" (should be `DOMAIN` with optionally ":" + `PORT`) and `AWS_S3_CUSTOM_DOMAIN` (if used) are added by default.  Value should be a comma-separated list of host names.

## Multifactor (TOTP) authentication

Some of these configuration values may be moved to site.settings in future.

### `TWO_FACTOR_LOGIN_VALIDITY_WINDOW`

- **Type**: Integer
- **Default**: `2`

Sets the number of codes either side of which will be accepted. This should be a low number but you can increase it if your users are experiencing high network latency and their codes are expiring before they can complete the login process. With the default settings for this and `TWO_FACTOR_LOGIN_MAX_SECONDS`, users have up to 180 seconds to use a given login code and can use a valid code up to two before the current one.

### `TWO_FACTOR_LOGIN_MAX_SECONDS`

- **Type**: Integer
- **Default**: `60`

Time in seconds for which a user login code is valid.