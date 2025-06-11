- - -
Title: Developer Environment Date: 2025-05-26 Order: 5
- - -

## Pré-requisitos

Estas instruções supoem que você esteja rodando a BookWyrm utilizando o Docker. Você vai precisar [instalar o Docker](https://docs.docker.com/engine/install/) e o [docker-compose](https://docs.docker.com/compose/install/) para começar.

## Configurando o ambiente de desenvolvimento

### Get the code

1. Faça uma cópia do [código da BookWyrm no GitHub](https://github.com/bookwyrm-social/bookwyrm). Você pode [criar uma bifurcação (fork)](https://docs.github.com/en/get-started/quickstart/fork-a-repo) do repositório e então [usar `git clone` pra baixar o código](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) para seu computador.
2. Vá ao diretório onde o código foi baixado no seu computador; você trabalhará a partir dele daqui em diante.
3. Configure as variáveis do seu ambiente de trabalho copiando o arquivo de ambiente de exemplo (`.env.example`) e renomeando o arquivo para `.env`. Na linha de comando, você pode fazer assim:
``` { .sh }
cp .env.example .env
```

### Configure your environment settings

In `.env`:

4. change `DEBUG` to `true`
5. If you use a tunneling/proxy service like [ngrok](https://ngrok.com), set `DOMAIN` to to the domain name you are using (e.g. `abcd-1234.ngrok-free.app`). Otherwise, set `DOMAIN` to `localhost`
6. change `NGINX_SETUP` to `reverse_proxy` (this prevents BookWyrm trying to set up https certificates on your development machine)
7. If you need to use a particular port (e.g. if you are tunneling via ngrok), uncomment `PORT` and set it (e.g. `PORT=1333`). If using `localhost` this is optional.

If you try to register your admin account and see a message that `CSRF verification failed`, you should check these settings, as you may have set your domain or port incorrectly.

### Email (optional)

If you want to test sending emails, you will need to [set up appropriate values](/environment.html#email-configuration) in the "Email config" section. You do not need to change anything for [the separate `EMAIL` setting](/environment.html#email).

### Build and run

8. In the command line, run:

``` { .sh }
./bw-dev build            # Build the docker images
./bw-dev setup            # Initialize the database and run migrations. Note the ADMIN key at the end of this output. You'll need it to register the first admin user.
./bw-dev up               # Start the docker containers
```

9. Once the build is complete, you can access the instance at `http://localhost`, your ngrok domain, or `http://localhost:{PORT}`, depending on you domain and port configuration.
10. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

Se estiver curiosa: o comando `./bw-dev` é um shell script simples que executa várias ferramentas: no exemplo acima, você poderia pular o script e executar `docker-compose build` ou `docker-compose up` diretamente, se preferir. `./bw-dev` só junta esses comandos em um só, por conveniência. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Editando e criando Modelos (Models)

Se você quiser editar ou criar um modelo, você provavelmente vai alterar a estrutura do banco de dados. Para que essas alterações funcionem, você precisará executar o comando `makemigrations` do Django para criar um novo [arquivo de migrações do Django](https://docs.djangoproject.com/en/3.2/topics/migrations) e então `migrá-lo`:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

## Editando arquivos estáticos
Toda vez que você alterar o CSS ou o JavaScript, você precisará rodar o comando `collectstatic`do Django para que as alterações passem a funcionar:
``` { .sh }
./bw-dev collectstatic
```

Se você tiver o [yarn instalado](https://yarnpkg.com/getting-started/install), você pode executar `yarn watch:static` para executar automaticamente o script toda vez que houver alguma mudança no diretório `bookwyrm/static`.
