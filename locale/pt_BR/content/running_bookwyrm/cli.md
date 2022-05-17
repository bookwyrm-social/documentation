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

Quando há alterações no branch `produção (production)`, você pode atualizar sua instância sem ficar fora do ar.

Este comando faz o `git pull` das últimas atualizações do branch `produção (production)`, constroi a imagem Docker, se for necessário, executa as migrações do Django, atualiza os arquivos estáticos e reinicia todos os containers do Docker.

### admin_code

Obtem o código secreto da administração para registrar o usuário administrador inicial em uma nova instância BookWyrm.

## Configurando um armazenamento compatível com S3

Por padrão, a BookWyrm usa o armazenamento local para os recursos estáticos (ícones, avatar padrão, etc.) e as mídias (avatares dos usuários, capas de livros, etc.), mas você pode usar um armazenament externo para distribuir esses arquivos. A BooKWyrm utiliza o django-storages para lidar com o armazenamento externo, como serviços compatíveis com S3, Apache Libcloud ou SFTP.

Veja [Armazenamento externo](/external-storage.html) para mais informações.

### copy_media_to_s3

Migra todas as mídias enviadas de uma instalação BookWyrm para um "bucket" compatível com S3. Utilizar para fazer o upload inicial para um "bucket" vazio.

### sync_media_to_s3

Sincroniza as mídias enviadas, novas ou alteradas, de uma instância BookWyrm para um "bucket" compatível com S3. Utilizar para garantir que todos os arquivos locais sejam enviados a um "bucket" existente.

### set_cors_to_s3 nomedoarquivo

Copia um arquivo JSON com as regras CORS para o seu bucket S3, onde `nomedoarquivo` é o nome de seu arquivo JSON (p. ex: `/bw-dev set_cors_to_s3 cors.json`)

## Desenvolvimento e teste

_Estes comandos estão disponíveis no branch `produção (production)`_.

### black

A BookWyrm usa o formatador de código [Black](https://github.com/psf/black) pra manter o código Python com um estilo consistente. Execute o `black` antes de enviar/comitar suas alterações para que a tarefa `pylint` não gere erros no seu pull request e te entristeça.

### prettier

A BookWyrm usa o [Prettier](https://prettier.io/) para manter os códigos JavaScript com um estilo consistente. Execute o `prettier` antes de enviar suas alterações nos scripts para formatar seu código automaticamente.

### stylelint

A BookWyrm usa o [Stylelint](uhttps://stylelint.io/) para manter o estilo dos arquivos CSS consistentes. Execute o `stylelintprettier` antes de enviar/comitar alterações nos scripts para formatar seu código automaticamente.

### formatters

Este comando executa todos os formatadores de estilo (`black`, `prettier`, and `stylelint`) de uma vez.

### clean

Remove todos os containers do Docker parados.

Equivalente a:

```shell
docker-compose stop
docker-compose rm -f
```

### makemessages

Cria arquivo de mensagens para todas as strings de tradução. Depois de executar `makemessages` você deve executar `compilemessages` para compilar as traduções. Veja o [makemessages do Django](https://docs.djangoproject.com/en/3.2/ref/django-admin/#makemessages).

### compilemessages

Compila os arquivos de tradução. Veja o [compilemessages do Django](https://docs.djangoproject.com/en/3.2/ref/django-admin/#compilemessages).

### pytest args

Executa testes com o `pytest`.
