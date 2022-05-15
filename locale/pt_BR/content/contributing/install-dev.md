## Pré-requisitos

Estas instruções supoem que você esteja rodando a BookWyrm utilizando o Docker. Você vai precisar [instalar o Docker](https://docs.docker.com/engine/install/) e o [docker-compose](https://docs.docker.com/compose/install/) para começar.

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

Se estiver curiosa: o comando `./bw-dev` é um shell script simples que executa várias ferramentas: no exemplo acima, você poderia pular o script e executar `docker-compose build` ou `docker-compose up` diretamente, se preferir. `./bw-dev` só junta esses comandos em um só, por conveniência. Execute-o sem argumentos para ver uma lista de comandos disponíveis, leia a [página da documentação](/command-line-tool.html) ou abra o arquivo para dar uma olhada no que cada comando faz!

### Editando e criando Modelos (Models)

If you change or create a model, you will probably change the database structure. For these changes to have effect you will need to run Django's `makemigrations` command to create a new [Django migrations file](https://docs.djangoproject.com/en/3.2/topics/migrations), and then `migrate` it:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

### Editing static files
Any time you edit the CSS or JavaScript, you will need to run Django's `collectstatic` command again in order for your changes to have effect:
``` { .sh }
./bw-dev collectstatic
```

If you have [installed yarn](https://yarnpkg.com/getting-started/install), you can run `yarn watch:static` to automatically run the previous script every time a change occurs in `bookwyrm/static` directory.
