- - -
Title: Developer Environment Date: 2021-04-12 Order: 3
- - -

## Pré-requisitos

These instructions assume you are developing BookWyrm using Docker. You'll need to [install Docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/) to get started.

## Configurando o ambiente de desenvolvimento

- Faça uma cópia do [código da BookWyrm no GitHub](https://github.com/bookwyrm-social/bookwyrm). Você pode [criar uma bifurcação (fork)](https://docs.github.com/en/get-started/quickstart/fork-a-repo) do repositório e então [usar `git clone` pra baixar o código](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) para seu computador.
- Vá ao diretório onde o código foi baixado no seu computador; você trabalhará a partir dele daqui em diante.
- Configure as variáveis do seu ambiente de trabalho copiando o arquivo de ambiente de exemplo (`.env.example`) e renomeando o arquivo para `.env`. Na linha de comando, você pode fazer assim:
``` { .sh }
cp .env.example .env
```
- No `.env`, altere `DEBUG` para `true`
- Facultativamente, você pode usar algum serviço como o [ngrok](https://ngrok.com/) para configurar um domínio e apontar a variável `DOMAIN` do seu arquivo `.env` para o domínio gerado pelo ngrok.

- Configure o nginx para o ambiente de desenvolvimento copiando o arquivo de configuração para desenvolvimento (`nginx/development`) e renomeando o arquivo para `nginx/default.conf`:
``` { .sh }
cp nginx/development nginx/default.conf
```

- Inicie o aplicativo. In the command line, run:
``` { .sh }
./bw-dev build            # Gera a imagem docker
./bw-dev setup            # Inicializa o banco de dados e executa as migrações
./bw-dev up               # Inicia os containers do docker
```
- Uma vez completado o build, você pode acessar a instância no endereço `http://localhost:1333` e criar um usuário administrador.

If you're curious: the `./bw-dev` command is a simple shell script runs various other tools: above, you could skip it and run `docker-compose build` or `docker-compose up` directly if you like. `./bw-dev` just collects them into one common place for convenience. Run it without arguments to get a list of available commands, read the [documentation page](/command-line-tool.html) for it, or open it up and look around to see exactly what each command is doing!

### Editando e criando Modelos (Models)

If you change or create a model, you will probably change the database structure. For these changes to have effect you will need to run Django's `makemigrations` command to create a new [Django migrations file](https://docs.djangoproject.com/en/3.2/topics/migrations), and then `migrate` it:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

### Editando arquivos estáticos
Any time you edit the CSS or JavaScript, you will need to run Django's `collectstatic` command again in order for your changes to have effect:
``` { .sh }
./bw-dev collectstatic
```

If you have [installed yarn](https://yarnpkg.com/getting-started/install), you can run `yarn watch:static` to automatically run the previous script every time a change occurs in `bookwyrm/static` directory.
