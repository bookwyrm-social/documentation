Desenvolvedores e administradores de instâncias Bookwyrm podem usar o script `bw-dev` para tarefas cotidianas. Isso pode tornar seus comandos mais curtos, mais fáceis de lembrar e mais difíceis de serem confundidos.

Se tiver uma instalado uma instância BookWyrm [em produção](installing-in-production.html) ou [em desenvolvimento](https://docs.joinbookwyrm.com/developer-environment.html#setting_up_the_developer_environment), você pode executar o script pela linha de comando com `./bw-dev` seguido com um subcomando para executar.

## Atalhos do Docker

### bash

Abre uma sessão `bash` interativa dentro do container `web` do Docker.

### build

Equivalente ao `docker-compose build`.

### dbshell

Abre um shell interativo do banco de dados Postgres. Espero que você saiba o que está fazendo.

### runweb args

Executa um comando arbitrário (representado acima pelo `args`) no container `web`.

Equivalente ao `docker-compose run --rm web`.

### service_ports_web args

Executa um comando arbitrário no container `web` (representado acima por `args`) com as portas expostas. Isso é útil para quando você quer executar testes `pdb` porque o `runweb` não irá expor o promp `pdb`.

Equivalente ao `docker-compose run --rm --service-ports web`.

### shell

Abre um shell interativo Django dentro do container `web` do Docker. Você pode usar isso se quiser executar comandos do shell do Django diretamente.

### up [args]

Inicia ou reinicia containers do Docker, incluindo opcionalmente quaisquer argumentos (representados acima por `args`). Equivalente ao `docker-compose up --build [args]`

## Gerenciando o banco de dados

### initdb

Inicializa um banco de dados.

### makemigrations [appname migration number]

_Este comando não está disponível no branch `produção`_.

Executa o comando `makemigrations` do Django dentro do seu container Docker. Se você alterou a estrutura do banco de dados em um branch de desenvolvimento, você precisará executar este comando para que suas alterações tenham efeito. Facultativamente, você pode especificar alguma migração para executar, p. ex. `./bw-dev makemigrations bookwyrm 0108`

### migrate

Executa o comando `migrate` do Django dentro de seu container Docker. Você sempre irá precisar executá-lo após o `makemigrations`.

### resetdb

_Este comando não está disponível no branch `produção`_.

Reinicia o banco de dados. **Este comando vai excluir todo o banco de dados da BookWyrm**, criar outro banco de dados e executar todas as migrações. Você deve deletar todos os arquivos de migração recentes que não quer rodar _antes_ de executar `resetdb`.

## Gerenciando uma instância BookWyrm

### collectstatic

Migra os recursos estáticos para um container Docker ou para um "bucket" compatível com S3, dependendo do contexto.

### generate_preview_images

Gera imagens de pré-visualização de sites, usuários e livros. Isso pode demorar algum tempo se você tiver um banco de dados grande.

### generate_thumbnails

Gera miniaturas das capas dos livros.

### populate_streams args

Preenche novamente os streams do Redis (feeds dos usuários). Você geralmente não vai precisar rodar isto a não ser que haja algum erro que apague seus feeds de usuários por algum motivo. Você pode escpecificar o stream utilizando o argumento `--stream`.

### populate_list_streams

Preenche novamente o cache de listas do Redis. Você geralmente não vai precisar executar isso a não ser que haja um erro que apaguei as listas dos usuários por algum motivo.

### populate_suggestions

Gera sugestões de usuários para todos os usuários. Você pode executar isso manualmente para atualizar as sugestões.

### restart_celery

Reinicia o container Docker do `celery_worker`.

### update

When there are changes to the `production` branch, you can update your instance without downtime.

This command `git pull`s the latest `production` branch updates, builds docker images if necessary, runs Django migrations, updates static files, and restarts all Docker containers.

### admin_code

Gets the secret admin code used to register the inital admin user on a new BookWyrm instance.

## Setting up S3 compatible storage

By default, BookWyrm uses local storage for static assets (favicon, default avatar, etc.), and media (user avatars, book covers, etc.), but you can use an external storage service to serve these files. BookWyrm uses django-storages to handle external storage, such as S3-compatible services, Apache Libcloud or SFTP.

See [External Storage](/external-storage.html) for more information.

### copy_media_to_s3

Migrate all uploaded media from an existing Bookwrym installation to an S3-compatible "bucket". Use for initial upload to an empty bucket.

### sync_media_to_s3

Sync new or changed uploaded media from an existing Bookwrym installation to an S3-compatible "bucket". Use to ensure all local files are uploaded to an existing bucket.

### set_cors_to_s3 filename

Copy a CORS rules JSON file to your S3 bucket, where `filename` is the name of your JSON file (e.g. `./bw-dev set_cors_to_s3 cors.json`)

## Development and testing

_These commands are not available on the `production` branch_.

### black

BookWyrm uses the [Black](https://github.com/psf/black) code formatter to keep the Python codebase consistent styled. Run `black` before committing your changes so the `pylint` task does not fail for your pull request and make you sad.

### prettier

BookWyrm uses [Prettier](https://prettier.io/) to keep the JavaScript codebase consistently styled. Run `prettier` before committing changes to scripts to automatically format your code.

### stylelint

BookWyrm uses [Stylelint](uhttps://stylelint.io/) to keep the CSS files consistently styled. Run `stylelintprettier` before committing changes to scripts to automatically format your code.

### formatters

This command runs all code formatters (`black`, `prettier`, and `stylelint`) in one go.

### clean

Remove all stopped Docker containers.

Equivalent to:

```shell
docker-compose stop
docker-compose rm -f
```

### makemessages

Creates message files for all translation strings. After you have run `makemessages` you need to run `compilemessages` to compile the translations. See [Django's makemessages](https://docs.djangoproject.com/en/3.2/ref/django-admin/#makemessages).

### compilemessages

Compiles translation files. See [Django's compilemessages](https://docs.djangoproject.com/en/3.2/ref/django-admin/#compilemessages).

### pytest args

Run tests with `pytest`.
