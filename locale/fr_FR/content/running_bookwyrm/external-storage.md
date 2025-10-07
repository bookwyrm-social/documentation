- - -
Title: External Storage Date: 2021-06-07 Order: 8
- - -

Par défaut, BookWyrm stocke localement les ressources statiques (favicon, avatar par défaut, etc.) et les médias (avatars, couvertures de livres, etc.), mais vous pouvez utiliser un service de stockage externe pour ces fichiers. BookWyrm utilise `django-storages` pour gérer le stockage externe, tel que les services compatibles S3, Apache Libcloud ou SFTP.

## Services compatibles S3

### Configuration

Créez un compartiment auprès du service compatible S3 de votre choix, ainsi qu'un ID de clé d'accès et une clé d'accès secrète. Ceux-ci peuvent être auto-hébergés, tels que [Ceph](https://ceph.io/en/) (LGPL 2.1/3.0) ou [MinIO](https://min.io/) (GNU AGPL v3.0), ou commerciaux ([Scaleway](https://www.scaleway.com/en/docs/object-storage-feature/), [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-digitalocean-space-and-api-key)...).

Ce guide a été testé avec Object Storage de Scaleway. Si vous utiliser un autre service, partagez votre expérience (en particulier si vous avez dû prendre des mesures différentes) en ouvrant un ticket sur le dépôt de la [Documentation de BookWyrm](https://github.com/bookwyrm-social/documentation).

### Ce qui vous attend

Si vous installez une nouvelle instance de BookWyrm, les étapes seront :

- Configurer votre service de stockage externe
- Activer le stockage externe sur BookWyrm
- Démarrer votre instance BookWyrm
- Mettre à jour le connecteur de l'instance

Si votre instance est déjà en place, et que des images ont été téléchargées sur le stockage local, les étapes seront :

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
- `AWS_S3_REGION_NAME`: e.g. `"eu-west-1"` for AWS, `"fr-par"` for Scaleway, `"nyc3"` for Digital Ocean or `"cluster-id"` for Linode

Si votre service compatible S3 est Amazon AWS, la configuration devrait être terminée. Pour les autres services, vous aurez à décommenter les lignes suivantes :

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

### Copie de vos médias locaux sur le stockage externe

Si votre instance BookWyrm est déjà en cours d'exécution et que des fichiers médias ont été téléchargés (avatars d'utilisateur, couvertures de livres…), vous devrez copier les médias téléchargés sur votre compartiment.

Cette tâche est effectuée avec la commande :

```bash
./bw-dev copy_media_to_s3
```

### Activation du stockage externe sur BookWyrm

Pour activer le stockage externe compatible S3, vous devrez modifier votre fichier `.env` en changeant la valeur de la propriété `USE_S3` de `false` à `true`:

```
USE_S3=true
```

**Note** that after `v0.7.5` all traffic is assumed to be HTTPS, so you need to ensure that your external storage is also served over HTTPS.

#### Ressources statiques

Then, you will need to run the following commands to compile the themes and copy all static assets to your S3 bucket:

```bash
./bw-dev compile_themes
./bw-dev collectstatic
```

#### Paramètres CORS

Une fois que les ressources statiques ont été recueillies, vous devrez configurer CORS pour votre compartiment.

Certains services tels que Digital Ocean mettent à disposition une interface pour cette étape, voir [Documentation de Digital Ocean: Comment configurer CORS](https://docs.digitalocean.com/products/spaces/how-to/configure-cors/).

Si votre service ne met pas d'interface à disposition, vous pouvez tout de même configurer CORS via la ligne de commande.

Créez un fichier nommé `cors.json` avec le contenu suivant :

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

Exécutez alors la commande suivante :

```bash
./bw-dev set_cors_to_s3 cors.json
```

Une absence de retour signifie que cela a fonctionné.

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

If you are starting a new BookWyrm instance, you can go back to the setup instructions right now: [[Docker](install-prod.html)] [[Dockerless](install-prod-dockerless.html)]. Dans le cas contraire, continuez à lire.

### Redémarrage de votre instance

Une fois la copie des fichiers médias effectuée et les ressources statiques recueillies, vous pouvez charger la nouvelle configuration `.env` et redémarrer votre instance avec la commande :

```bash
./bw-dev up -d
```

Si tout se passe bien, votre stockage a été modifié sans arrêt du serveur. Si des polices sont manquantes (et que la console JS de votre navigateur génère des alertes à propos de CORS), quelque chose s'est mal passé [à cette étape](#cors-settings). Dans ce cas, il peut être bon de vérifier les en-têtes d'une requête HTTP pour un fichier sur votre compartiment :

```bash
curl -X OPTIONS -H 'Origin: http://MY_DOMAIN_NAME' http://BUCKET_URL/static/images/logo-small.png -H "Access-Control-Request-Method: GET"
```

Remplacez `MY_DOMAIN_NAME` par votre nom de domaine de l'instance, `BUCKET_URL` avec l'URL de votre compartiment, et le chemin du fichier par n'importe quel autre chemin valide sur votre compartiment.

Si vous voyez un message, en particulier un message commençant par `<Error><Code>CORSForbidden</Code>`, cela n'a pas fonctionné. Si vous ne voyez aucun message, cela a fonctionné.

Pour une instance en cours d'utilisation, il peut y avoir quelques fichiers qui ont été créés localement pendant l'intervalle entre la migration des fichiers vers le stockage externe et le redémarrage de l'application. Pour s'assurer que tous les fichiers restants sont téléchargés sur le stockage externe une fois basculé dessus, vous pouvez utiliser la commande suivante, qui copiera uniquement les fichiers qui ne sont pas déjà présents sur le stockage externe :

```bash
./bw-dev sync_media_to_s3
```

### Mise à jour du connecteur de l'instance

*Remarque : Vous pouvez sauter cette étape si vous utilisez une version à jour de BookWyrm; en septembre 2021 le « self connector » a été retiré dans [PR #1413](https://github.com/bookwyrm-social/bookwyrm/pull/1413)*

Afin que la bonne URL soit utilisée lors de l'affichage des résultats de recherche locale de livres, nous devons modifier la valeur de la racine d'URL des images de couverture.

Les données du connecteur sont accessibles via l'interface d'administration de Django, située à l'url `http://MY_DOMAIN_NAME/admin`. Le connecteur pour votre propre instance est le premier enregistrement dans la base de données, vous pouvez donc accéder au connecteur via cette URL : `https://MY_DOMAIN_NAME/admin/bookwyrm/connector/1/change/`.

Le champ _Covers url_ est défini par défaut comme `https://MY_DOMAIN_NAME/images`, vous devez le changer en `https://S3_STORAGE_URL/images`. Ensuite, cliquez sur le bouton _Enregistrer_.

Vous devrez mettre à jour la valeur de _Covers url_ chaque fois que vous changez l'URL de votre stockage.
