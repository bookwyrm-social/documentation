Por padrão, a BookWyrm usa o armazenamento local para os recursos estáticos (ícones, avatar padrão, etc.) e as mídias (avatares dos usuários, capas de livros, etc.), mas você pode usar um armazenament externo para distribuir esses arquivos. A BooKWyrm utiliza o `django-storages` para lidar com o armazenamento externo, como serviços compatíveis com S3, Apache Libcloud ou SFTP.

## Serviços compatíveis com S3

### Configuração

Crie um bucket em seu serviço compatível com S3 favorito, junto com uma Access Key ID e uma Scret Access Key. Eles podem ser auto-hospedados, como [Ceph](https://ceph.io/en/) (LGPL 2.1/3.0) ou [MinIO](https://min.io/) (GNU AGPL v3.0), ou comercial ([Scaleway](https://www.scaleway.com/en/docs/object-storage-feature/), [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-digitalocean-space-and-api-key)…).

Este guia foi testado no Scaleway Object Storage. If you use another service, please share your experience (especially if you had to take different steps) by filing an Issue on the [BookWyrm Documentation](https://github.com/bookwyrm-social/documentation) repository.

### O que lhe espera

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

If all goes well, your storage has been changed without server downtime. Se algumas fontes não aparecem (e o console JS do seu navegador alerta sobre o CORS), algo deu errado [aqui](#cors-settings). Nesse caso pode ser bom conferir os headers da solicitação HTTP em algum arquivo no seu bucket:

```bash
curl -X OPTIONS -H 'Origin: http://MEU_DOMINIO' http://ENDEREÇO_DO_BUCKET/static/images/logo-small.png -H "Access-Control-Request-Method: GET"
```

Substitua `MEU_DOMINIO` com o domínio da sua instância e `ENDEREÇO_DO_BUCKET` com o endereço de seu bucket. Você pode substituir o caminho dos arquivos para algum que seja válido em seu bucket.

Se você ver alguma mensagem, especialmente alguma que comece com `<Error><Code>CORSForbidden</Code>`, não deu certo. Se você não ver mensagem alguma, funcionou.

Em uma instância ativa pode haver vários arquivos criados localmente durante a migração para o armazenamento externo, e reiniciar a aplicação pode fazê-la utilizar o armazenamento externo. Para garantir que os arquivos restantes sejam enviados ao armazenamento externo depois de alterar, você pode usar o seguinte comando, que irá enviar apenas arquivos que ainda não estejam no armazenamento externo:

```bash
./bw-dev sync_media_to_s3
```

### Atualizando o conector da instância

*Aviso: você pode pular este passo se está utilizando uma versão atualizada da BookWyrm; em setembro de 2021, o "self connector" foi removido no [PR #1413](https://github.com/bookwyrm-social/bookwyrm/pull/1413)*

Para que o endereço correto seja utilizado ao mostrar resultados da pesquisa de livros locais, temos que alterar o valor da base do URL das imagens de capa.

Os dados do conector podem ser acessados pela interface de administração do Django presentes no endereço `http://MY_DOMAIN_NAME/admin`. O conector da sua própria instância é o primeiro registro no banco de dados, então você pode acessá-lo pelo seguinte endereço: `https://MEU_DOMINIO/admin/bookwyrm/connector/1/change/`.

O campo _URL das capas (Covers url)_ é, por padrão, `https://MEU_DOMINIO/images`, você deve mudá-lo para `https://ENDEREÇO_DO_ARMAZENAMENTO_S3/images`. Então clique o botão de _Salvar_ e voilà!

Você deverá atualizar o valor do _Covers url_ toda vez que alterar o endereço de seu armazenamento.
