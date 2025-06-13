- - -
Izenburua: Kanpoko biltegia Data: 2021/06/07 Eskaera: 7
- - -

By default, BookWyrm uses local storage for static assets (favicon, default avatar, etc.), and media (user avatars, book covers, etc.), but you can use an external storage service to serve these files. BookWyrm uses `django-storages` to handle external storage, such as S3-compatible services, Apache Libcloud or SFTP.

## S3-compatible Services

### Setup

Create a bucket at your S3-compatible service of choice, along with an Access Key ID and a Secret Access Key. These can be self hosted, like [Ceph](https://ceph.io/en/) (LGPL 2.1/3.0) or [MinIO](https://min.io/) (GNU AGPL v3.0), or commercial ([Scaleway](https://www.scaleway.com/en/docs/object-storage-feature/), [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-digitalocean-space-and-api-key)…).

This guide has been tested against Scaleway Object Storage. If you use another service, please share your experience (especially if you had to take different steps) by filing an Issue on the [BookWyrm Documentation](https://github.com/bookwyrm-social/documentation) repository.

### What awaits you

If you are starting a new BookWyrm instance, the process will be:

- Set up your external storage service
- Enable external storage on BookWyrm
- Start your BookWyrm instance
- Update the instance connector

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
- `AWS_S3_REGION_NAME`: e.g. `"eu-west-1"` for AWS, `"fr-par"` for Scaleway or `"nyc3"` for Digital Ocean

If your S3-compatible service is Amazon AWS, you should be set. If not, you’ll have to uncomment the following lines:

- `AWS_S3_CUSTOM_DOMAIN`: the domain that will serve the assets, e.g. `"example-bucket-name.s3.fr-par.scw.cloud"` or `"${AWS_STORAGE_BUCKET_NAME}.${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`
- `AWS_S3_ENDPOINT_URL`: the S3 API endpoint, e.g. `"https://s3.fr-par.scw.cloud"` or `"https://${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`

### Copying local media to external storage

If your BookWyrm instance is already running and media have been uploaded (user avatars, book covers…), you will need to migrate uploaded media to your bucket.

This task is done with the command:

```bash
./bw-dev copy_media_to_s3
```

### Enabling external storage for BookWyrm

To enable the S3-compatible external storage, you will have to edit your `.env` file by changing the property value for `USE_S3` from `false` to `true`:

```
USE_S3=true
```

If your external storage is being served over HTTPS (which most are these days), you'll also need to make sure that `USE_HTTPS` is set to `true`, so images will be loaded over HTTPS:

```
USE_HTTPS=true
```

#### Static assets

Then, you will need to run the following command, to copy the static assets to your S3 bucket:

```bash
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
