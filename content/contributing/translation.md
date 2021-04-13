Title: Translations
Date: 2021-04-13
Order: 3

## Working with translations and locale files
Text in the html files are wrapped in translation tags (`{% trans %}` and `{% blocktrans %}`), and Django generates locale files for all the strings in which you can add translations for the text. You can find existing translations in the `locale/` directory.

The application's language is set by a request header sent by your browser to the application, so to change the language of the application, you can change the default language requested by your browser.

## Adding a locale
To start translation into a language which is currently supported, run the django-admin `makemessages` command with the language code for the language you want to add (like `de` for German, or `en-gb` for British English):
``` bash
./bw-dev makemessages -l <language code>
```

## Editing a locale
When you have a locale file, open the `django.po` in the directory for the language (for example, if you were adding German, `locale/de/LC_MESSAGES/django.po`. All the the text in the application will be shown in paired strings, with `msgid` as the original text, and `msgstr` as the translation (by default, this is set to an empty string, and will display the original text).

Add your translations to the `msgstr` strings. As the messages in the application are updated, `gettext` will sometimes add best-guess fuzzy matched options for those translations. When a message is marked as fuzzy, it will not be used in the application, so be sure to remove it when you translate that line.

When you're done, compile the locale by running:

``` bash
./bw-dev compilemessages
```

You can add the `-l <language code>` to only compile one language. When you refresh the application, you should see your translations at work.


