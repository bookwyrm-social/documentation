- - -
Title: Stockage Externe Date: 2021-06-07 Order: 6
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

Une fois que les ressources statiques ont été recueillies, vous devrez configurer CORS pour votre compartiment.

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

Une absence de retour signifie que cela a fonctionné.

Si vous installez une nouvelle instance de BookWyrm, vous pouvez retourner aux instructions de configuration dès maintenant. Dans le cas contraire, continuez à lire.

### Redémarrage de votre instance

Une fois la copie des fichiers médias effectuée et les ressources statiques recueillies, vous pouvez charger la nouvelle configuration `.env` et redémarrer votre instance avec la commande :

```bash
./bw-dev up -d
```

Si tout se passe bien, votre stockage a été modifié sans arrêt du serveur. Si des polices sont manquantes (et que la console JS de votre navigateur génère des alertes à propos de CORS), quelque chose s'est mal passé [à cette étape](#cors-settings). Dans ce cas, il peut être bon de vérifier les en-têtes d'une requête HTTP pour un fichier sur votre compartiment :

```bash
curl -X OPTIONS -H 'Origin: http://MY_DOMAIN_NAME' http://BUCKET_URL/static/images/logo-small.png -H "Access-Control-Request-Method: GET"
```

Remplacez `MY_DOMAIN_NAME` par votre nom de domaine de l'instance, `BUCKET_URL` avec l'URL de votre compartiment, et le chemin du fichier par n'importe quel autre chemin valide sur votre compartiment.

Si vous voyez un message, en particulier un message commençant par `<Error><Code>CORSForbidden</Code>`, cela n'a pas fonctionné. Si vous ne voyez aucun message, cela a fonctionné.

Pour une instance en cours d'utilisation, il peut y avoir quelques fichiers qui ont été créés localement pendant l'intervalle entre la migration des fichiers vers le stockage externe, et le redémarrage de l'application. Pour s'assurer que tous les fichiers restants sont téléchargés sur le stockage externe après avoir basculé dessus, vous pouvez utiliser la commande suivante, qui copiera uniquement les fichiers qui ne sont pas déjà présents sur le stockage externe:

```bash
./bw-dev sync_media_to_s3
```

### Mise à jour du connecteur de l'instance

*Remarque : Vous pouvez sauter cette étape si vous utilisez une version à jour de BookWyrm; en septembre 2021 le "self connector" a été retiré dans [PR #1413](https://github.com/bookwyrm-social/bookwyrm/pull/1413)*

Afin que la bonne URL soit utilisée lors de l'affichage des résultats de recherche locale de livres, nous devons modifier la valeur de la racine d'URL des images de couverture.

Les données du connecteur sont accessibles via l'interface d'administration de Django, située à l'url `http://MY_DOMAIN_NAME/admin`. Le connecteur pour votre propre instance est le premier enregistrement dans la base de données, vous pouvez donc accéder au connecteur via cette URL : `https://MY_DOMAIN_NAME/admin/bookwyrm/connector/1/change/`.

Le champ _Covers url_ est défini par défaut comme `https://MY_DOMAIN_NAME/images`, vous devez le changer en `https://S3_STORAGE_URL/images`. Ensuite, cliquez sur le bouton _Enregistrer_.

Vous devrez mettre à jour la valeur de _Covers url_ chaque fois que vous changez l'URL de votre stockage.
