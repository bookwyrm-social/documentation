- - -
Title: External Storage Date: 2021-06-07 Order: 8
- - -

By default, BookWyrm uses local storage for static assets (favicon, default avatar, etc.), and media (user avatars, book covers, etc.), but you can use an external storage service to serve these files. BookWyrm uses `django-storages` to handle external storage, such as S3-compatible services, Apache Libcloud or SFTP.

## S3-compatible Services

### Setup

Create a bucket at your S3-compatible service of choice, along with an Access Key ID and a Secret Access Key. These can be self hosted, like [Ceph](https://ceph.io/en/) (LGPL 2.1/3.0) or [MinIO](https://min.io/) (GNU AGPL v3.0), or commercial ([Scaleway](https://www.scaleway.com/en/docs/object-storage-feature/), [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-digitalocean-space-and-api-key)…).

This guide has been tested against Scaleway Object Storage. If you use another service, please share your experience (especially if you had to take different steps) by filing an Issue on the [BookWyrm Documentation](https://github.com/bookwyrm-social/documentation) repository.

### Co Cię czeka

Jeśli rozpoczynasz nową instancję BookWyrm, proces będzie zawierał:

- Konfigurację usługi pamięci zewnętrznej
- Aktywację pamięci zewnętrznej na BookWyrm
- Uruchomienie swojej instancji BookWyrm
- Aktualizację łącznika instancji

If you already started your instance, and images have been uploaded to local storage, the process will be:

- Set up your external storage service
- Copy your local media to external storage
- Enable external storage on BookWyrm
- Restart your BookWyrm instance
- Update the instance connector

### BookWyrm Settings

Edit your `.env` file by uncommenting the following lines:

- `AWS_ACCESS_KEY_ID`: your access key ID
- `AWS_SECRET_ACCESS_KEY`: your secret access key
- `AWS_STORAGE_BUCKET_NAME`: your bucket name
- `AWS_S3_REGION_NAME`: e.g. `"eu-west-1"` for AWS, `"fr-par"` for Scaleway, `"nyc3"` for Digital Ocean or `"cluster-id"` for Linode

If your S3-compatible service is Amazon AWS, you should be set. If not, you’ll have to uncomment the following lines:

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

### Copying local media to external storage

If your BookWyrm instance is already running and media have been uploaded (user avatars, book covers…), you will need to migrate uploaded media to your bucket.

To zadanie wykonywane jest poleceniem:

```bash
./bw-dev copy_media_to_s3
```

### Aktywowanie pamięci zewnętrznej dla BookWyrm

To enable the S3-compatible external storage, you will have to edit your `.env` file by changing the property value for `USE_S3` from `false` to `true`:

```
USE_S3=true
```

**Note** that after `v0.7.5` all traffic is assumed to be HTTPS, so you need to ensure that your external storage is also served over HTTPS.

#### Static assets

Then, you will need to run the following commands to compile the themes and copy all static assets to your S3 bucket:

```bash
./bw-dev compile_themes
./bw-dev collectstatic
```

#### CORS settings

Once the static assets are collected, you will need to set up CORS for your bucket.

Some services like Digital Ocean provide an interface to set it up, see [Digital Ocean doc: How to Configure CORS](https://docs.digitalocean.com/products/spaces/how-to/configure-cors/).

If your service doesn’t provide an interface, you can still set up CORS with the command line.

Create a file called `cors.json`, with the following content:

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

Replace `MY_DOMAIN_NAME` with the domain name(s) of your instance.

Then, run the following command:

```bash
./bw-dev set_cors_to_s3 cors.json
```

No output means it should be good.

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

If you are starting a new BookWyrm instance, you can go back to the setup instructions right now: [[Docker](install-prod.html)] [[Dockerless](install-prod-dockerless.html)]. If not, keep on reading.

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
