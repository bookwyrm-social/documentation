- - -
Title: Stockage Externe Date: 2021-06-07 Order: 5
- - -

Par défaut, BookWyrm stocke localement les ressources statiques (favicon, avatar par défaut, etc.) et les médias (avatars, couvertures de livres, etc.), mais vous pouvez utiliser un service de stockage externe pour ces fichiers. BookWyrm utilise `django-storages` pour gérer le stockage externe, tel que les services compatibles S3, Apache Libcloud ou SFTP.

## Services compatibles S3

### Configuration

Créez un compartiment auprès du service compatible S3 de votre choix, ainsi qu'un ID de clé d'accès et une clé d'accès secrète. Ceux-ci peuvent être auto-hébergés, tels que [Ceph](https://ceph.io/en/) (LGPL 2.1/3.0) ou [MinIO](https://min.io/) (GNU AGPL v3.0), ou commerciaux ([Scaleway](https://www.scaleway.com/en/docs/object-storage-feature/), [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-digitalocean-space-and-api-key)...).

Ce guide a été testé avec Object Storage de Scaleway. Si vous utiliser un autre service, partagez votre expérience (en particulier si vous avez dû prendre des mesures différentes) en ouvrant un ticket sur le dépôt de la [Documentation de BookWyrm](https://github.com/bookwyrm-social/documentation).

### Ce qui vous attend

Si vous installez une nouvelle instance de BookWyrm, les étapes seront :

- Configurer votre service de stockage externe
- Activer le stockage externe sur BookWyrm
- Démarrer votre instance BookWyrm
- Mettre à jour le connecteur de l'instance

Si votre instance est déjà en place, et que des images ont été téléchargées sur le stockage local, les étapes seront :

- Configurer votre service de stockage externe
- Copier vos médias locaux sur le stockage externe
- Activer le stockage externe sur BookWyrm
- Redémarrer votre instance BookWyrm
- Mettre à jour le connecteur de l'instance

### Paramètres de BookWyrm

Modifiez votre fichier `.env` en décommentant les lignes suivantes :

- `AWS_ACCESS_KEY_ID`: votre ID de clé d'accès
- `AWS_SECRET_ACCESS_KEY`: votre clé d'accès secrète
- `AWS_STORAGE_BUCKET_NAME`: le nom de votre compartiment
- `AWS_S3_REGION_NAME`: e.g. `"eu-west-1"` pour AWS, `"fr-par"` pour Scaleway ou `"nyc3"` pour Digital Ocean

Si votre service compatible S3 est Amazon AWS, la configuration devrait être terminée. Pour les autres services, vous aurez à décommenter les lignes suivantes :

- `AWS_S3_CUSTOM_DOMAIN`: le domaine qui va mettre à disposition les fichiers, par exemple `"exemple-nom-compartiment-s3.fr-par.scw.cloud"` ou `"${AWS_STORAGE_BUCKET_NAME}.${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`
- `AWS_S3_ENDPOINT_URL`: le point de terminaison d'API S3, par exemple `"https://s3.fr-par.scw.cloud"` ou `"https://${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`

### Copie de vos médias locaux sur le stockage externe

Si votre instance BookWyrm est déjà en cours d'exécution et que des fichiers médias ont été téléchargés (avatars d'utilisateur, couvertures de livres…), vous devrez copier les médias téléchargés sur votre compartiment.

Cette tâche est effectuée avec la commande :

```bash
./bw-dev copy_media_to_s3
```

### Activation du stockage externe sur BookWyrm

Pour activer le stockage externe compatible S3, vous devrez modifier votre fichier `.env` en changeant la valeur de la propriété `USE_S3` de `false` à `true`:

```
USE_S3=true
```

Si votre stockage externe est accessible via HTTPS (la plupart le sont actuellement), vous devrez également vous assurer que `USE_HTTPS` est défini à `true`, afin que les images soient téléchargées via HTTPS :

```
USE_HTTPS=true
```

#### Ressources statiques

Vous devrez ensuite exécuter la commande suivante, afin de copier les ressources statiques vers votre compartiment S3 :

```bash
./bw-dev collectstatic
```

#### Paramètres CORS

Once the static assets are collected, you will need to set up CORS for your bucket.

Certains services tels que Digital Ocean mettent à disposition une interface pour cette étape, voir [Documentation de Digital Ocean: Comment configurer CORS](https://docs.digitalocean.com/products/spaces/how-to/configure-cors/).

Si votre service ne met pas d'interface à disposition, vous pouvez tout de même configurer CORS via la ligne de commande.

Créez un fichier nommé `cors.json` avec le contenu suivant :

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

Remplacez `MY_DOMAIN_NAME` par le(s) nom(s) de domaine de votre instance.

Exécutez alors la commande suivante :

```bash
./bw-dev set_cors_to_s3 cors.json
```

No output means it should be good.

If you are starting a new BookWyrm instance, you can go back to the setup instructions right now. If not, keep on reading.

### Restarting your instance

Once the media migration has been done and the static assets are collected, you can load the new `.env` configuration and restart your instance with:

```bash
./bw-dev up -d
```

If all goes well, your storage has been changed without server downtime. If some fonts are missing (and your browser’s JS console lights up with alerts about CORS), something went wrong [here](#cors-settings). In that case it might be good to check the headers of a HTTP request against a file on your bucket:

```bash
curl -X OPTIONS -H 'Origin: http://MY_DOMAIN_NAME' http://BUCKET_URL/static/images/logo-small.png -H "Access-Control-Request-Method: GET"
```

Replace `MY_DOMAIN_NAME` with your instance domain name, `BUCKET_URL` with the URL for your bucket, you can replace the file path with any other valid path on your bucket.

If you see any message, especially a message starting with `<Error><Code>CORSForbidden</Code>`, it didn’t work. If you see no message, it worked.

For an active instance, there may be a handful of files that were created locally during the time between migrating the files to external storage, and restarting the app so it uses the external storage. To ensure that any remaining files are uploaded to external storage after switching over, you can use the following command, which will upload only files that aren't already present in the external storage:

```bash
./bw-dev sync_media_to_s3
```

### Updating the instance connector

*Note: You can skip this step if you're running an updated version of BookWyrm; in September 2021 the "self connector" was removed in [PR #1413](https://github.com/bookwyrm-social/bookwyrm/pull/1413)*

In order for the right URL to be used when displaying local book search results, we have to modify the value for the cover images URL base.

Connector data can be accessed through the Django admin interface, located at the url `http://MY_DOMAIN_NAME/admin`. The connector for your own instance is the first record in the database, so you can access the connector with this URL: `https://MY_DOMAIN_NAME/admin/bookwyrm/connector/1/change/`.

The field _Covers url_ is defined by default as `https://MY_DOMAIN_NAME/images`, you have to change it to `https://S3_STORAGE_URL/images`. Then, click the _Save_ button, and voilà!

You will have to update the value for _Covers url_ every time you change the URL for your storage.
