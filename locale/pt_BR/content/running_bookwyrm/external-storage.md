- - -
Title: External Storage Date: 2021-06-07 Order: 5
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
- `AWS_S3_REGION_NAME`: p.ex. `"eu-west-1"` para a AWS, `"fr-par"` para a Scaleway ou `"nyc3"` para a Digital Ocean

Se seu serviço compatível com S3 for a Amazon AWS, já está tudo pronto. Se não, você deverá descomentar as seguintes linhas:

- `AWS_S3_CUSTOM_DOMAIN`: o domínio que irá servir os arquivos, p.ex `"example-bucket-name.s3.fr-par.scw.cloud"` ou `"${AWS_STORAGE_BUCKET_NAME}.${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`
- `AWS_S3_ENDPOINT_URL`: o endpoint da API S3, p. ex `"https://s3.fr-par.scw.cloud"` ou `"https://${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`

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

Se seu armazenamento externo está servindo via HTTPS (como a maioria hoje em dia), você também precisará se certificar de que `USE_HTTPS` seja `true` para que as imagens carreguem via HTTPS:

```
USE_HTTPS=true
```

#### Arquivos estáticos

Então, para copiar os arquivos estáticos para o seu bucket S3 você precisará executar o seguinte comando:

```bash
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

The field _Covers url_ is defined by default as `https://MY_DOMAIN_NAME/images`, you have to change it to `https://S3_STORAGE_URL/images`. Then, click the _Save_ button, and voilà!

You will have to update the value for _Covers url_ every time you change the URL for your storage.
