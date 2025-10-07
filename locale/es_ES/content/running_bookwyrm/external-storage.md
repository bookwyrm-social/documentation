- - -
Title: External Storage Date: 2021-06-07 Order: 8
- - -

Por defecto, BookWyrm utiliza almacenamiento local para assets estáticos (favicon, avatar por defecto, etc.), y multimedia (avatares de usuarios, portadas de libros, etc.), pero puede utilizar un servicio de almacenamiento externo para proporcionar estos archivos. BookWyrm utiliza `django-storages` para manejar el almacenamiento externo, como también servicios compatibles con S3, Apache Libcloud o SFTP.

## Servicios compatibles con S3

### Configuración

Cree un "bucket" en el servicio de su elección compatible con S3, junto con un ID de clave de acceso y una clave de acceso secreta. Estos pueden ser autoalojados, como [Ceph](https://ceph.io/en/) (LGPL 2.1/3.0) o [MinIO](https://min.io/) (GNU AGPL v3. ), o comercial ([Scaleway](https://www.scaleway.com/en/docs/object-storage-feature/), [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-digitalocean-space-and-api-key)…).

Esta guía ha sido probada sobre el almacenamiento de objetos de Scaleway. Si utilizas otro servicio, por favor comparte tu experiencia (especialmente si tomaste pasos diferentes) presentando un asunto en el repositorio [BookWyrm Documentation](https://github.com/bookwyrm-social/documentation).

### Lo que te espera

Si estás empezando una nueva instancia de BookWyrm, el proceso será:

- Configura tu servicio de almacenamiento externo
- Habilita el almacenamiento externo en BookWyrm
- Inicia tu instancia de BookWyrm
- Actualiza el conector de la instancia

Si ya has iniciado tu instancia, y las imágenes se han subido al almacenamiento local, el proceso será:

- Configura tu servicio de almacenamiento externo
- Copia tu multimedia local a almacenamiento externo
- Habilita el almacenamiento externo en BookWyrm
- Reinicia tu instancia de BookWyrm
- Actualiza el conector de la instancia

### Ajustes de BookWyrm

Edita tu archivo `.env` descomentando las siguientes líneas:

- `AWS_ACCESS_KEY_ID`: tu ID de clave de acceso
- `AWS_SECRET_ACCESS_KEY`: tu clave de acceso secreta
- `AWS_STORAGE_BUCKET_NAME`: tu nombre de "bucket"
- `AWS_S3_REGION_NAME`: e.g. `"eu-west-1"` for AWS, `"fr-par"` for Scaleway, `"nyc3"` for Digital Ocean or `"cluster-id"` for Linode

Si tu servicio compatible con S3 es Amazon AWS, debe estar configurado. Si no, tendrás que descomentar las siguientes líneas:

- `AWS_S3_CUSTOM_DOMAIN`: the domain that will serve the assets:
  - for Scaleway, e.g. `"example-bucket-name.s3.fr-par.scw.cloud"`
  - for Digital Ocean, e.g. `"${AWS_STORAGE_BUCKET_NAME}.${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`
  - for Linode Object Storage, this should be set to the cluster domain, e.g. `"eu-central-1.linodeobjects.com"`
- `AWS_S3_ENDPOINT_URL`: the S3 API endpoint:
  - for Scaleway, e.g. `"https://s3.fr-par.scw.cloud"`
  - for Digital Ocean, e.g. `"https://${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`
  - For Linode Object Storage, set this to the cluster domain, e.g. `"https://eu-central-1.linodeobjects.com"`

For many S3 compatible services, the default `ACL` is `"public-read"`, and this is what BookWyrm defaults to. If you are using Backblaze (B2) you need to explicitly set the default ACL to be empty in your `.env` file:

```
AWS_DEFAULT_ACL=""
```

### Copia tu multimedia local a almacenamiento externo

Si su instancia de BookWyrm ya se está ejecutando y los archivos se han subido (avatares de usuario, portadas de libros…), necesitarás migrarlos a tu "bucket".

Esta tarea se realiza con el comando:

```bash
./bw-dev copy_media_to_s3
```

### Habilita el almacenamiento externo en BookWyrm

Para habilitar el almacenamiento externo compatible con S3, tendrás que editar tu archivo `.env` cambiando el valor de la propiedad para `USE_S3` de `false` a `true`:

```
USE_S3=true
```

**Note** that after `v0.7.5` all traffic is assumed to be HTTPS, so you need to ensure that your external storage is also served over HTTPS.

#### Assets estáticos

Then, you will need to run the following commands to compile the themes and copy all static assets to your S3 bucket:

```bash
./bw-dev compile_themes
./bw-dev collectstatic
```

#### Configuración CORS

Una vez que los assets estáticos sean recogidos, necesitarás configurar CORS para tu "bucket".

Algunos servicios, como Digital Ocean, proporcionan una interfaz para configurarlo, mira [Digital Ocean doc: Cómo configurar CORS](https://docs.digitalocean.com/products/spaces/how-to/configure-cors/).

Si tu servicio no proporciona una interfaz, puedes configurar CORS con la línea de comandos.

Crea un archivo llamado `cors.json`con el siguiente código:

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

Reemplaza `MY_DOMAIN_NAME` con el nombre de dominio de tu instancia.

Ejecuta el siguiente comando:

```bash
./bw-dev set_cors_to_s3 cors.json
```

Ningún output significa que debería ser buena.

### Additional Step for Linode Object Storage Users

For Linode, you now need to make an alteration to the `.env` to ensure that the generated links to your storage objects are correct. If you miss this step, all the links to images and static files (like css) will be broken. To fix this, you need to now insert the bucket-name into the `AWS_S3_CUSTOM_DOMAIN`, for example if your `AWS_STORAGE_BUCKET_NAME` is `"my-bookwyrm-bucket"`, then set it to:

```
AWS_S3_CUSTOM_DOMAIN=my-bookwyrm-bucket.cluster-id.linodeobjects.com
```

*Note*: From this point on, any bw-dev copy or sync commands will place objects into an incorrect location in your object store, so if you need to use them, revert to the previous setting, run and re-enable.

### User export and import files

After `v0.7.5`, user export and import files are saved to local storage even if `USE_S3` is set to `true`. Generally it is safer to use local storage for these files, and keep your used storage under control by setting up the task to periodically delete old export and import files.

If you are running a large instance you may prefer to use S3 for these files as well. If so, you will need to set the environment variable `USE_S3_FOR_EXPORTS` to `true`.

### New Instance

If you are starting a new BookWyrm instance, you can go back to the setup instructions right now: [[Docker](install-prod.html)] [[Dockerless](install-prod-dockerless.html)]. Si no es así, sigue leyendo.

### Reiniciando tu instancia

Una vez que se haya realizado la migración de archivos y se recopilen los assets estáticos, puedes cargar el nuevo `.env` y reinicia la instancia con:

```bash
./bw-dev up -d
```

Si todo va bien, tu almacenamiento habrá sido cambiado sin tiempo de inactividad del servidor. Si faltan algunas fuentes (y la consola JS de tu navegador alerta sobre CORS), algo salió mal [aquí](#cors-settings). En ese caso podría ser bueno comprobar las cabeceras de petición HTTP en un archivo en tu "bucket":

```bash
curl -X OPTIONS -H 'Origin: http://MY_DOMAIN_NAME' http://BUCKET_URL/static/images/logo-small.png -H "Access-Control-Request-Method: GET"
```

Reemplaza `MY_DOMAIN_NAME` con el nombre de dominio de tu instancia y `BUCKET_URL` con la URL de tu cubeta; puedes reemplazar la ruta del archivo por cualquier otra ruta válida en tu "bucket".

Si ves cualquier mensaje, especialmente un mensaje que comienza con `<Error><Code>CORSForbidden</Code>`, no funcionó. Si no ves ningún mensaje, funcionó.

Para una instancia activa, puede haber un puñado de archivos que fueron creados localmente durante el tiempo entre migrar los archivos al almacenamiento externo y reiniciar la aplicación para que utilice el almacenamiento externo. Para asegurarte que cualquier archivo restante se suba al almacenamiento externo luego, puedes usar el siguiente comando, el cual subirá solo archivos que no estén ya presentes en el almacenamiento externo:

```bash
./bw-dev sync_media_to_s3
```

### Actualiza el conector de la instancia

*Nota: Puedes omitir este paso si estás ejecutando una versión actualizada de BookWyrm; en septiembre de 2021 se eliminó el "autoconector" en [PR #1413](https://github.com/bookwyrm-social/bookwyrm/pull/1413)*

Para utilizar la URL correcta al mostrar los resultados de la búsqueda de libros locales, tenemos que modificar el valor para la base de URL de las imágenes de portada.

Se puede acceder a los datos del conector a través de la interfaz de administración de Django, ubicada en la url `http://MY_DOMAIN_NAME/admin`. El conector para su propia instancia es el primer registro en la base de datos. Puedes acceder al conector con esta URL: `https://MY_DOMAIN_NAME/admin/bookwyrm/connector/1/change/`.

El campo _Covers url_ se define por defecto como `https://MY_DOMAIN_NAME/images`. Tienes que cambiarlo a `https://S3_STORAGE_URL/images`. Luego, haz clic en el botón _Save_ y voilà!

Tendrás que actualizar el valor de _Covers url_ cada vez que cambies la URL de tu almacenamiento.
