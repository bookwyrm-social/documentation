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

Used in the `production` branch's `docker-compose.yml` file as the email to send to Certbot.

### `NGINX_SETUP`

- **Type**: String
- **Default**: `https`
- **Options**: `https`, `reverse_proxy`

Indicates how to set the `nginx` configuration. `https` assumes all traffic should be handled by BookWyrm's nginx container and will attempt to set up a certbot HTTPS certificate, whereas `reverse_proxy` assumes traffic is being proxied by a web server between BookWyrm and the outside world. In development you should always set this to `reverse_proxy`.

### `PORT`

- **Type**: Integer
- **Default**: `443`, or if domain is `localhost`, `80`.

The port used to communicate with the web. Note that this is different to Django's `PORT`.

### `USE_HTTPS`

This variable is deprecated after `v0.7.5`. It is assumed that your instance is using HTTPS unless the domain is `localhost`.

## Searching

These configurations may be moved to `site.settings` in future.

### `SEARCH_TIMEOUT`

- **Type**: Integer
- **Default** `8`

The total time in seconds that the instance will spend searching connectors.

### `QUERY_TIMEOUT`

- **Type**: Integer
- **Default** `5`

Timeout for a query to an individual connector.

## Postgres configuration

The primary database for BookWyrm uses Postgres.

### `PGPORT`

- **Type**: Integer
- **Default** `5432`

The port to connect to the Postgres server. Same as Django's `PORT`.

### `POSTGRES_PASSWORD`

- **Type**: String
- **Default** `bookwyrm`

Password for the database. Set this to a strong password string between quotation marks to avoid problems with certain characters being misinterpreted.

**Do not use either of the default values from `.env` or `settings.py`** as they are publicly known.

### `POSTGRES_USER`

- **Type**: String
- **Default**: `bookwyrm`

The name of your database user. Same as Django's `USER`.

### `POSTGRES_DB`

- **Type**: String
- **Default**: `bookwyrm`

The name of your database.

### `POSTGRES_HOST`

- **Type**: String
- **Default**: `localhost`

The host server for your database. If not set or a blank string, defaults to localhost. Same as Django's `HOST`.

## Redis

Redis is used to manage both activity streams and background jobs.

### `MAX_STREAM_LENGTH`

- **Type**: Integer
- **Default**: `200`

The maximum length for Redis streams. If a stream grows longer than this, Redis will discard the oldest items in order to not exceed the `MAX_STREAM_LENGTH`.

See the [Redis `XTRIM` documentation](https://redis.io/docs/latest/commands/xtrim/) for more detail.

### `REDIS_ACTIVITY_HOST`

- **Type**: String
- **Default**: `localhost`

Redis server host. If not set, this defaults to `localhost` but if you are using Docker it should usually be set to `redis_activity` so that you are using the Redis container of that name.

### `REDIS_ACTIVITY_PORT`

- **Type**: Integer
- **Default**: `6379`

The port your Redis server uses.

### `REDIS_ACTIVITY_PASSWORD`

- **Type**: String
- **Default**: Empty string

Password for your Redis database.

### `REDIS_ACTIVITY_DB_INDEX`

- **Type**: Integer
- **Default**: not set

If you are not using the default Docker setup with a separate Redis server for activity streams, you should set the `REDIS_ACTIVITY_DB_INDEX` to indicate which Redis database is being used for BookWyrm activity streams.

### `REDIS_ACTIVITY_URL`

- **Type**: String
- **Default**: not set

If you are using an external Redis database or want to use a unix socket, you can override all the other Redis settings by explictly setting the full `REDIS_ACTIVITY_URL`.

e.g. `"redis://username:top_secret_pass@example.com:6380/0"`

### `REDIS_BROKER_HOST`

- **Type**: String
- **Default**: `localhost`

Redis Celery server host. If not set this defaults to `localhost` but if using Docker should usually be set to `redis_broker` so that you are using the Redis container of that name.

### `REDIS_BROKER_PORT`

- **Type**: Integer
- **Default**: `6379`

The port your Redis Celery server uses.

### `REDIS_BROKER_PASSWORD`

- **Type**: String
- **Default**: Empty string

Password for your Redis Celery database.

### `REDIS_BROKER_DB_INDEX`

- **Type**: Integer
- **Default**: not set

If you are not using the default Docker setup with a separate Redis server for Celery, you should set the `REDIS_ACTIVITY_DB_INDEX` to indicate which Redis database is being used for BookWyrm activity streams.

### `REDIS_BROKER_URL`

- **Type**: String
- **Default**: not set

If you are using an external Redis database or want to use a unix socket, you can override all the other Redis settings for your Celery database by explictly setting the full `REDIS_BROKER_URL`.

e.g. `"redis://username:top_secret_pass@example.com:6380/0"`

## Flower

Flower provides a web UI for monitoring Celery tasks.

### `FLOWER_PORT`

- **Type**: Integer
- **Default**: `8888`

Port for Flower site used to monitor Celery at `https://example.com/flower`.

### `FLOWER_USER`

- **required**
- **Type**: String
- **Default**: not set

The user for your Flower interface.

### `FLOWER_PASSWORD`

- **required**
- **Type**: String
- **Default**: not set

The password for your Flower monitoring interface. Flower can see all messages passing through your server so it is important that you set this to a strong, unique password and keep it secure.

## Email configuration

### `EMAIL_HOST`

- **required**
- **Type**: String
- **Default**: not set

The smtp address of your email host. e.g. `smtp.mailgun.org`. Always check the terms and conditions of your email provider before using them for sending large volumes of mail. You probably need something like Mailgun.

### `EMAIL_PORT`

- **Type**: Integer
- **Default**: `587`

The port for your email provider's smtp server.

### `EMAIL_HOST_USER`

- **Type**: String
- **Default**: not set

The username for your email provider. Usually in the form of a full email address e.g. `mail@your.domain.here`

### `EMAIL_HOST_PASSWORD`

- **Type**: String
- **Default**: not set

The password for your email provider account.

### `EMAIL_USE_TLS`

- **Type**: Boolean
- **Default**: `true`

Whether your smtp connection uses TLS. Check that you are using the correct `EMAIL_PORT` for this.

### `EMAIL_USE_SSL`

- **Type**: Boolean
- **Default**: `false`

Whether your smtp connection uses SSL. Check that you are using the correct `EMAIL_PORT` for this.

### `EMAIL_SENDER_NAME`

- **Type**: String
- **Default**: `admin`

The first part of the email address for emails sent by your BookWyrm instance. e.g. **`admin`**@example.com.

### `EMAIL_SENDER_DOMAIN`

- **Type**: String
- **Default**: Same as `DOMAIN`

The domain of the email address for emails sent by your BookWyrm instance. e.g. admin@**`example.com`**.

## S3 object storage

### `USE_S3`

- **Type**: Boolean
- **Default**: `false`

Indicates whether you are using S3 object storage for images and static files.

### `USE_S3_FOR_EXPORTS`

- **Type**: Boolean
- **Default**: `false`

Indicates whether you are using S3 object storage for user export and import files. By default `USE_S3` does not include user import and exports. It is safer to use the default local storage for these, along with the regular file deletion job running. On larger instances local storage may cause performance issues and you may prefer to set this to `true`.

### `S3_SIGNED_URL_EXPIRY`

- **Type**: Integer
- **Default**: `900`

Number of seconds before signed S3 urls expire. This is currently only used for user export files. This should only be as long as is required for a user download to complete once the user has clicked on the "download" button after the export has been processed.

### `AWS_ACCESS_KEY_ID`

- **required** if using S3 storage
- **Type**: String
- **Default**: not set

Access key for S3 storage of all types.

### `AWS_DEFAULT_ACL`

- **required** if using Backblaze storage
- **Type**: String
- **Default**: "public-read"

Backblaze (B2) does not recognise "public-read" as a default ACL setting, so Backblaze users should set this to an empty string.

### `AWS_SECRET_ACCESS_KEY`

- **required** if using S3 storage
- **Type**: String
- **Default**: not set

Secret key for S3 storage of all types.

### `AWS_STORAGE_BUCKET_NAME`

- **required** if using S3 storage
- **Type**: String
- **Default**: not set

The bucket name you are using. e.g. `"example-bucket-name"`

### `AWS_S3_REGION_NAME`

- **required** if using S3 storage
- **Type**: String
- **Default**: not set

The S3 region name. e.g. `"eu-west-1"` for AWS, `"fr-par"` for Scaleway, `"nyc3"` for Digital Ocean or `"cluster-id"` for Linode.

### `AWS_S3_CUSTOM_DOMAIN`

- **required** if using non-AWS S3 storage (e.g. Scaleway or Digital Ocean Spaces)
- **Type**: String
- **Default**: not set

The domain that will serve the assets. e.g. `"example-bucket-name.s3.fr-par.scw.cloud"`

### `AWS_S3_URL_PROTOCOL`

- **Type**: String
- **Default**: Same as `PROTOCOL` plus a colon e.g. "http:"

Protocol for your S3 storage. Defaults to `https:` in production. You do not need to set this unless you want to override the default behaviour.

### `AWS_S3_ENDPOINT_URL`

- **required** if using non-AWS S3 storage (e.g. Scaleway or Digital Ocean Spaces)
- **Type**: String
- **Default**: not set

The S3 API endpoint. e.g. `"https://s3.fr-par.scw.cloud"`

## Azure blob storage

These values are required if you are using [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-get-info).

### `USE_AZURE`

- **Type**: Boolean
- **Default**: `false`

### `AZURE_ACCOUNT_NAME`

- **required** if using Azure storage
- **Type**: String
- **Default**: not set

e.g. `"example-account-name"`

### `AZURE_ACCOUNT_KEY`

- **required** if using Azure storage
- **Type**: String
- **Default**: not set

e.g. `"Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw=="`

### `AZURE_CONTAINER`

- **required** if using Azure storage
- **Type**: String
- **Default**: not set

The unique name for your container. e.g. `"example-blob-container-name"`.

### `AZURE_CUSTOM_DOMAIN`

- **Type**: String
- **Default**: not set

You can use a [custom domain](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-custom-domain-name?tabs=azure-portal) with Azure blob storage but this is not required. e.g. `"example-account-name.blob.core.windows.net"`.

## Image generation

Some of these configuration values may be moved to site.settings in future.

### `ENABLE_THUMBNAIL_GENERATION`

- **Type**: Boolean
- **Default**: `false`

Whether to enable generation of thumbnail images for book covers. Setting this to `true` will provide a boost to performance in terms of rendering images, however it comes at the price of 4-5 times more file storage required for book covers. For this reason it is set to `false` by default.

### `ENABLE_PREVIEW_IMAGES`

- **Type**: Boolean
- **Default**: `false`

This setting allows the server to generate preview images that can be used as OpenGraph images (or Twitter card image). These previews are generated for the book (every time the title, cover or author changes, or a new public review with rating is published), the user (every time the name or avatar is changed), and the website (every time the site name, tagline or logo are changed). See [Optional Features](/optional_features.html) for more information.

### `PREVIEW_BG_COLOR`

- **Type**: String
- default: `use_dominant_color_light`

The background color for preview images. You can specify RGB tuple or RGB hex strings, or `use_dominant_color_light` / `use_dominant_color_dark`.

### `PREVIEW_TEXT_COLOR`

- **Type**: String
- **Default**: `#363636`

The text color for preview images. If `PREVIEW_BG_COLOR` is `use_dominant_color_dark`, this should be set to `#fff`.

### `PREVIEW_IMG_WIDTH`

- **Type**: Integer
- **Default**: `1200`

Width for preview images, in pixels.

### `PREVIEW_IMG_HEIGHT`

- **Type**: Integer
- **Default**: `630`

Height for preview images, in pixels.

### `PREVIEW_DEFAULT_COVER_COLOR`

- **Type**: String
- **Default**: `#002549`

If there is no cover image for a book, we create a default cover. This setting determines the color of that default book cover.

### `PREVIEW_DEFAULT_FONT`

- **Type**: String
- **Default**: `Source Han Sans`

If there is no cover image for a book, we create a default cover. This setting determines the font used on that default book cover.

## Telemetry

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