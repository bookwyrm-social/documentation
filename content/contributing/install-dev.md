Title: Developer Environment
Date: 2021-04-12
Order: 2

## Setting up the developer environment

Set up the development environment file:

```
:::bash linenums=False
cp .env.dev.example .env
```

Set up nginx for development `nginx/default.conf`:
```
:::bash linenums=False
cp nginx/development nginx/default.conf
```

For most testing, you'll want to use ngrok. Remember to set the DOMAIN in `.env` to your ngrok domain.

You'll have to install the Docker and docker-compose. When you're ready, run:

```
:::shell linenums=False
docker-compose build
docker-compose run --rm web python manage.py migrate
docker-compose run --rm web python manage.py initdb
docker-compose up
```

Once the build is complete, you can access the instance at `http://localhost:1333`

### Editing static files
If you edit the CSS or JavaScript, you will need to run Django's `collectstatic` command in order for your changes to have effect. You can do this by running:
```
:::shell linenums=False
./bw-dev collectstatic
```

If you have [installed yarn](https://yarnpkg.com/getting-started/install), you can run `yarn watch:static` to automatically run the previous script every time a change occurs in _bookwyrm/static_ directory.

