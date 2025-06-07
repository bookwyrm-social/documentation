- - -
Título: Almacenamiento Externo Fecha: 2021-06-02 Orden: 7
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
- `AWS_S3_REGION_NAME`: por ejemplo: `"eu-west-1"` para AWS, `"fr-par"` para Scaleway o `"nyc3"` para el Digital Ocean

Si tu servicio compatible con S3 es Amazon AWS, debe estar configurado. Si no, tendrás que descomentar las siguientes líneas:

- `AWS_S3_CUSTOM_DOMAIN`: el dominio que servirá a los assets, por ejemplo: `"example-bucket-name.s3.amazonaws.com/fr-par.scw.cloud"` o `"${AWS_STORAGE_BUCKET_NAME}.${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`
- `AWS_S3_ENDPOINT_URL`: el endpoint de la API de S3, por ejemplo: `"https:///etcfr-par.scw.cloud"` o `"https://${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`

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

Si tu almacenamiento externo está operando sobre HTTPS (la mayoría), también necesitarás asegurarte de que `USE_HTTPS` esté establecido en `true`, así las imágenes se cargarán sobre HTTPS:

```
USE_HTTPS=true
```

#### Assets estáticos

Luego, necesitarás ejecutar el siguiente comando para copiar los assets estáticos en tu "bucket" S3:

```bash
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

Si estás iniciando una nueva instancia de BookWyrm, puedes volver a las instrucciones de instalación ahora mismo. Si no es así, sigue leyendo.

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
