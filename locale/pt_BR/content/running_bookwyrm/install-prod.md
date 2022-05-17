Este projeto ainda é jovem e não está, no momento, muito estável, então tenha cuidado ao rodá-lo em produção.

## Configuração do servidor
- Obtenha um domínio e configure o DNS para seu servidor. Você deverá apontar os nameservers do seu domínio no provedor de DNS ao servidor onde você hospedará a BookWyrm. Aqui estão as instruções para a [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Configure o seu servidor com firewalls adequados a uma aplicação web (estas instruções foram testadas no Ubuntu 20.04). Aqui estão as instruções para a [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Configure um serviço de email (como o [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) e as configurações corretas de SMTP/DNS. Use a documentação do serviço para configurar seu DNS
- [Instale o Docker e docker-compose](https://docs.docker.com/compose/install/)

## Instale e configure a BookWyrm

O branch `produção (production)` da BookWyrm tem uma série de ferramentas indisponíveis no branch `principal (main)` que servem para a execução em produção, como alterações no `docker-compose` para atualizar os comandos padrão, configuração de containers e alterações individuais nas configurações dos containers para ativar coisas com SSL ou backups comuns.

Instruções para rodar a BookWyrm em produção:

- Obtenha o código da aplicação: `git clone git@github.com:bookwyrm-social/bookwyrm.git`
- Mude para o branch `produção (production)`: `git checkout production`
- Crie seu arquivo de variáveis do ambiente, `cp .env.example .env`, e atualize o seguinte:
    - `SECRET_KEY` | Uma string de caracteres difíceis de descobrir
    - `DOMAIN` | Seu domínio
    - `EMAIL` | Um endereço de email para ser usado na verificação de domínio do certbot
    - `POSTGRES_PASSWORD` | Defina uma senha segura para o banco de dados
    - `REDIS_ACTIVITY_PASSWORD` | Defina uma senha segura para o subsistema Redis Activity
    - `REDIS_BROKER_PASSWORD` | Defina uma senha segura para o subsistema Redis queue broker
    - `FLOWER_USER` | Seu nome de usuário para acessar o monitor de filas Flower
    - `FLOWER_PASSWORD` | Sua senha segura para acessar o monitor de filas Flower
    - `EMAIL_HOST_USER` | O endereço do recipiente que o aplicativo usará para enviar emails
    - `EMAIL_HOST_PASSWORD` | A senha do seu serviço de email
- Configure o nginx
    - Faça uma cópia do template da configuração de produção e ative-o no ngix `cp nginx/production nginx/default.conf`
    - Atualize o `nginx/default.conf`:
        - Substitua `your-domain.com` com seu domínio em todos os lugares do arquivo (incluindo as linhas comentadas)
        - Se você não estiver utilizando o subdomínio `www`, exclua a versão do domínio www.your-domain.com do `server_name` no primeiro bloco server no `nginx/default.conf` e exclua a flag `-d www.${DOMAIN}` no fim do comando `certbot` no `docker-compose.yml`.
        - Se você estiver executando outro servidor web na sua máquina, você precisará seguir as [instruções de proxy reverso](/using-a-reverse-proxy.html)
- Rode a aplicação (e isso deve também configurar o certificado ssl do Certbot para seu domínio) com `docker-compose up --build`, e certifique-se de que todas as imagens foram construidas com sucesso
    - If you are running other services on your host machine, you may run into errors where services fail when attempting to bind to a port. See the [troubleshooting guide](#port_conflicts) for advice on resolving this.
- When docker has built successfully, stop the process with `CTRL-C`
- Set up HTTPS redirect
    - In `docker-compose.yml`, comment out the active certbot command, which installs the certificate, and uncomment the line below, which sets up automatically renewals.
    - In `nginx/default.conf`, uncomment lines 18 through 50 to enable forwarding to HTTPS. You should have two `server` blocks enabled
- Set up a `cron` job to keep your certificates up to date (Lets Encrypt certificates expire after 90 days)
    - Type `crontab -e` to edit your cron file in the host machine
    - add a line to try renewing once a day: `5 0 * * * cd /path/to/your/bookwyrm && docker-compose run --rm certbot`
- If you wish to use an external storage for static assets and media files (such as an S3-compatible service), [follow the instructions](/external-storage.html) until it tells you to come back here
- Set up the database with `./bw-dev setup`, and copy the admin code to use when you create your admin account.
    - The output of `./bw-dev setup` should conclude with your admin code. You can get your code at any time by running `./bw-dev admin_code` from the command line. Here's an example output:

``` { .sh }
*******************************************
Use this code to create your admin account:
c6c35779-af3a-4091-b330-c026610920d6
*******************************************
```

- Run docker-compose in the background with: `docker-compose up -d`
- The application should be running at your domain. When you load the domain, you should get a configuration page which confirms your instance settings, and a form to create an admin account. Use your admin code to register.

Congrats! You did it!! Configure your instance however you'd like.


## Backups

BookWyrm's db service dumps a backup copy of its database to its `/backups` directory daily at midnight UTC. Backups are named `backup__%Y-%m-%d.sql`.

The db service has an optional script for periodically pruning the backups directory so that all recent daily backups are kept, but for older backups, only weekly or monthly backups are kept. To enable this script:

- Uncomment the final line in `postgres-docker/cronfile`
- rebuild your instance `docker-compose up --build`

You can copy backups from the backups volume to your host machine with `docker cp`:

- Run `docker-compose ps` to confirm the db service's full name (it's probably `bookwyrm_db_1`.
- Run `docker cp <container_name>:/backups <host machine path>`

## Port Conflicts

BookWyrm has multiple services that run on their default ports. This means that, depending on what else you are running on your host machine, you may run into errors when building or running BookWyrm when attempts to bind to those ports fail.

If this occurs, you will need to change your configuration to run services on different ports. This may require one or more changes the following files:

- `docker-compose.yml`
- `nginx/default.conf`
- `.env` (You create this file yourself during setup)

If you are already running a web-server on your machine, you will need to set up a reverse-proxy.

## Get Connected

Because BookWyrm is a young project, we're still working towards a stable release schedule, and there are a lot of bugs and breaking changes. There is a GitHub team which can be tagged when there's something important to know about an update, which you can join by sharing your GitHub username. There are a few ways in get in touch:

 - Open an issue or pull request to add your instance to the [official list](https://github.com/bookwyrm-social/documentation/blob/main/content/using_bookwyrm/instances.md)
 - Reach out to the project on [Mastodon](https://tech.lgbt/@bookwyrm) or [email the maintainer](mailto:mousereeve@riseup.net) directly with your GitHub username
 - Join the [Matrix](https://matrix.to/#/#bookwyrm:matrix.org) chat room
