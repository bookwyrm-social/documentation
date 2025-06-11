- - -
Title: Developer Environment Date: 2025-05-26 Order: 5
- - -

## Prerequisites

These instructions assume you are developing BookWyrm using Docker. You'll need to [install Docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/) to get started.

## Setting up the developer environment

### Get the code

1. Get a copy of [the BookWyrm codebase from GitHub](https://github.com/bookwyrm-social/bookwyrm). You can [create a fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) of the repository, and then [use `git clone` to download the code](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) to your computer.
2. Go to the directory which contains the code on your computer, you'll be working from there from here on out.
3. Set up your development environment variables file by copying the example environment file (`.env.example`) into a new file named `.env`. In the command line, you can do this with:
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

8. Kör på kommandoraden:

``` { .sh }
./bw-dev build            # Build the docker images
./bw-dev setup            # Initialize the database and run migrations. Note the ADMIN key at the end of this output. You'll need it to register the first admin user.
./bw-dev up               # Start the docker containers
```

9. Once the build is complete, you can access the instance at `http://localhost`, your ngrok domain, or `http://localhost:{PORT}`, depending on you domain and port configuration.
10. You can now enter your admin key and create an admin user. From here everything is the same as described in "Running BookWyrm".

If you're curious: the `./bw-dev` command is a simple shell script runs various other tools: above, you could skip it and run `docker-compose build` or `docker-compose up` directly if you like. `./bw-dev` just collects them into one common place for convenience. Run it without arguments to get a list of available commands, read the [documentation page](/cli.html) for it, or open it up and look around to see exactly what each command is doing!

## Editing or creating Models

If you change or create a model, you will probably change the database structure. For these changes to have effect you will need to run Django's `makemigrations` command to create a new [Django migrations file](https://docs.djangoproject.com/en/3.2/topics/migrations), and then `migrate` it:

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

## Editing static files
Any time you edit the CSS or JavaScript, you will need to run Django's `collectstatic` command again in order for your changes to have effect:
``` { .sh }
./bw-dev collectstatic
```

If you have [installed yarn](https://yarnpkg.com/getting-started/install), you can run `yarn watch:static` to automatically run the previous script every time a change occurs in `bookwyrm/static` directory.
