Title: Developer Environment
Date: 2021-04-12
Category: Administration

## Setting up the developer environment

Set up the development environment file:

``` bash
cp .env.dev.example .env
```

Set up nginx for development `nginx/default.conf`:
``` bash
cp nginx/development nginx/default.conf
```

For most testing, you'll want to use ngrok. Remember to set the DOMAIN in `.env` to your ngrok domain.

You'll have to install the Docker and docker-compose. When you're ready, run:

```bash
docker-compose build
docker-compose run --rm web python manage.py migrate
docker-compose run --rm web python manage.py initdb
docker-compose up
```

Once the build is complete, you can access the instance at `http://localhost:1333`

### Editing static files
If you edit the CSS or JavaScript, you will need to run Django's `collectstatic` command in order for your changes to have effect. You can do this by running:
``` bash
./bw-dev collectstatic
```

If you have [installed yarn](https://yarnpkg.com/getting-started/install), you can run `yarn watch:static` to automatically run the previous script every time a change occurs in _bookwyrm/static_ directory.

### Working with translations and locale files
Text in the html files are wrapped in translation tags (`{% trans %}` and `{% blocktrans %}`), and Django generates locale files for all the strings in which you can add translations for the text. You can find existing translations in the `locale/` directory.

The application's language is set by a request header sent by your browser to the application, so to change the language of the application, you can change the default language requested by your browser.

#### Adding a locale
To start translation into a language which is currently supported, run the django-admin `makemessages` command with the language code for the language you want to add (like `de` for German, or `en-gb` for British English):
``` bash
./bw-dev makemessages -l <language code>
```

#### Editing a locale
When you have a locale file, open the `django.po` in the directory for the language (for example, if you were adding German, `locale/de/LC_MESSAGES/django.po`. All the the text in the application will be shown in paired strings, with `msgid` as the original text, and `msgstr` as the translation (by default, this is set to an empty string, and will display the original text).

Add your translations to the `msgstr` strings. As the messages in the application are updated, `gettext` will sometimes add best-guess fuzzy matched options for those translations. When a message is marked as fuzzy, it will not be used in the application, so be sure to remove it when you translate that line.

When you're done, compile the locale by running:

``` bash
./bw-dev compilemessages
```

You can add the `-l <language code>` to only compile one language. When you refresh the application, you should see your translations at work.

