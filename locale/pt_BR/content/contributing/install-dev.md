- - -
Title: Developer Environment Date: 2026-02-22 Order: 5
- - -

## Pré-requisitos

Estas instruções supoem que você esteja rodando a BookWyrm utilizando o Docker. Você vai precisar [instalar o Docker](https://docs.docker.com/engine/install/) e o [docker-compose](https://docs.docker.com/compose/install/) para começar.

_If you are contributing to BookWyrm in a dockerless development environment we would love for you to [help us update this guide](/documentation.html) to include instructions for setting up a dockerless development environment_.

## Configurando o ambiente de desenvolvimento

### Get the code

1. Faça uma cópia do [código da BookWyrm no GitHub](https://github.com/bookwyrm-social/bookwyrm). Você pode [criar uma bifurcação (fork)](https://docs.github.com/en/get-started/quickstart/fork-a-repo) do repositório e então [usar `git clone` pra baixar o código](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) para seu computador.
2. Vá ao diretório onde o código foi baixado no seu computador; você trabalhará a partir dele daqui em diante.
3. Development occurs on the `main` branch, so ensure that is the branch you have checked out: `git checkout main`
4. Configure as variáveis do seu ambiente de trabalho copiando o arquivo de ambiente de exemplo (`.env.example`) e renomeando o arquivo para `.env`. Na linha de comando, você pode fazer assim:

```{ .sh }
cp .env.example .env
```

### Build and run

1. In the command line, run:

```{ .sh }
./bw-dev create_secrets       # Create the secrets file with random values. You only need to do this once.
./bw-dev dev up --build       # Build and start development stack
./bw-dev rundev python manage.py admin_code       # Shows the admin-code for initial setup. You only need to do this once.
```

1. Once the build is complete, you can access the instance at `http://localhost:1333`.
2. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

Se estiver curiosa: o comando `./bw-dev` é um shell script simples que executa várias ferramentas: no exemplo acima, você poderia pular o script e executar `docker-compose build` ou `docker-compose up` diretamente, se preferir. `./bw-dev` só junta esses comandos em um só, por conveniência. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Editando e criando Modelos (Models)

Se você quiser editar ou criar um modelo, você provavelmente vai alterar a estrutura do banco de dados. Para que essas alterações funcionem, você precisará executar o comando `makemigrations` do Django para criar um novo [arquivo de migrações do Django](https://docs.djangoproject.com/en/3.2/topics/migrations) e então `migrá-lo`:

```{ .sh }
./bw-dev makemigrations
./bw-dev rundev python manage.py migrate
```

## Editando arquivos estáticos

Toda vez que você alterar o CSS ou o JavaScript, você precisará rodar o comando `collectstatic`do Django para que as alterações passem a funcionar:

```{ .sh }
./bw-dev rundev python manage.py collectstatic
```

Se você tiver o [yarn instalado](https://yarnpkg.com/getting-started/install), você pode executar `yarn watch:static` para executar automaticamente o script toda vez que houver alguma mudança no diretório `bookwyrm/static`.

## Run code-linters and formatters

Before submitting patch, you should check ruff and other formatting tools. For those to work nicely, you should make sure you have development web-container and dev-tools build.

```{ .sh}
./bw-dev dev build # This is needed only once, if you haven't run dev stack previously
./bw-dev dev build dev-tools # This is needed only once and if you change pyproject.toml or Dockerfile
```

After those commands, you can run formatters and pytest and mypy with bw-dev command:

```{ .sh}
./bw-dev formatters
./bw-dev mypy
./bw-dev pytest
```

## Run development code behind ngrok or other tunneling/proxy service

In `.env.dev`:

1. If you use a tunneling/proxy service like [ngrok](https://ngrok.com), set `DOMAIN` to to the domain name you are using (e.g. `abcd-1234.ngrok-free.app`).
2. If you need to use a particular port other than 1333, change PORT to wanted port (e.g. `PORT=1333`).

Check that you have [all the required settings configured](/environment.html#required-environment-settings) before proceeding.

If you try to register your admin account and see a message that `CSRF verification failed` you may have set your domain or port incorrectly.

## Email (optional)

If you want to test sending emails, you will need to [set up appropriate real values](/environment.html#email-configuration) in the "Email config" section. You do not need to change anything for [the separate `EMAIL` setting](/environment.html#email). These settings are in `.env` -file
