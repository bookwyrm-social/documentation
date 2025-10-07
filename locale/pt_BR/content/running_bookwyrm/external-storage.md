- - -
Title: External Storage Date: 2021-06-07 Order: 8
- - -

Por padrão, a BookWyrm usa o armazenamento local para os arquivos estáticos (ícones, avatar padrão, etc.) e as mídias (avatares dos usuários, capas de livros, etc.), mas você pode usar um armazenament externo para distribuir esses arquivos. A BooKWyrm utiliza o `django-storages` para lidar com o armazenamento externo, como serviços compatíveis com S3, Apache Libcloud ou SFTP.

## Serviços compatíveis com S3

### Configuração

Crie um bucket em seu serviço compatível com S3 favorito, junto com uma Access Key ID e uma Scret Access Key. Eles podem ser auto-hospedados, como [Ceph](https://ceph.io/en/) (LGPL 2.1/3.0) ou [MinIO](https://min.io/) (GNU AGPL v3.0), ou comercial ([Scaleway](https://www.scaleway.com/en/docs/object-storage-feature/), [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-digitalocean-space-and-api-key)…).

Este guia foi testado no Scaleway Object Storage. Se você usa outro serviço, por favor nos conte sua experiência (especialmente se fez algum outro passo) criando um problema (issue) no repositório da [documentação da BookWyrm Documentation](https://github.com/bookwyrm-social/documentation).

### O que lhe espera

Se você está iniciando uma nova instância BookWyrm, o processo será:

- Configurar seu serviço de armazenamento externo
- Habilitar o armazenamento externo na BookWyrm
- Inicie sua instância BookWyrm
- Atualize o conector da instância

Se você já iniciou a instância, e imagens foram enviadas para o armazenamento local, o processo será:

- Configure seu serviço de armazenamento externo
- Copie sua mídia local para o armazenamento externo
- Habilite o armazenamento externo na BookWyrm
- Reinicie sua instância BookWyrm
- Atualize o conector da instância

### Configurações da BookWyrm

Edite seu arquivo `.env` descomentando as seguintes linhas:

- `AWS_ACCESS_KEY_ID`: sua ID de acesso
- `AWS_SECRET_ACCESS_KEY`: sua chave de acesso secreta
- `AWS_STORAGE_BUCKET_NAME`: o nome do seu bucket
- `AWS_S3_REGION_NAME`: e.g. `"eu-west-1"` for AWS, `"fr-par"` for Scaleway, `"nyc3"` for Digital Ocean or `"cluster-id"` for Linode

Se seu serviço compatível com S3 for a Amazon AWS, já está tudo pronto. Se não, você deverá descomentar as seguintes linhas:

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

### Copiando a mídia local para o armazenamento externo

Se sua instância BookWyrm já está rodando e já recebeu mídias (avatares de usuários, capas de livros…), você precisará migrar essa mídia enviada para seu bucket.

Essa tarefá é feita com o comando:

```bash
./bw-dev copy_media_to_s3
```

### Habilitando o armazenamento externo na BookWyrm

Para habilitar o armazenamento externo compatível com S3, você deverá editar seu arquivo `.env` e mudar a propriedade da variável `USE_S3` de `false` para `true`:

```
USE_S3=true
```

**Note** that after `v0.7.5` all traffic is assumed to be HTTPS, so you need to ensure that your external storage is also served over HTTPS.

#### Arquivos estáticos

Then, you will need to run the following commands to compile the themes and copy all static assets to your S3 bucket:

```bash
./bw-dev compile_themes
./bw-dev collectstatic
```

#### Configurações do CORS

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
