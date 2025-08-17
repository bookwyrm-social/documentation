""" handle internationalization """

import os
import gettext as gettextlib
import threading

localedir = os.path.join(os.path.dirname(__file__), "locale")
DOMAIN = "messages"
thread_local_data = threading.local()
thread_local_data.locale = "en_US"

locales_metadata = [
    {"code": "en_US", "name": "English (US)", "slug": ""},
    {"code": "de_DE", "name": "Deutsch", "slug": "de/"},
    {"code": "fr_FR", "name": "Français", "slug": "fr/"},
    {"code": "pl_PL", "name": "Polski", "slug": "pl/"},
    {"code": "pt_BR", "name": "Português do Brasil", "slug": "pt-br/"},
    {"code": "ro_RO", "name": "Română", "slug": "ro/"},
]

default_locale = "en_US"  # pylint: disable=invalid-name

# find out all supported locales in locale directory
locales = []
for dirpath, dirnames, filenames in os.walk(localedir):
    for dirname in dirnames:
        if os.path.exists(f"{localedir}/{dirname}/LC_MESSAGES/messages.mo"):
            locales.append(dirname)
    break

all_translations = {}
for locale_name in locales:
    all_translations[locale_name] = gettextlib.translation(
        DOMAIN, localedir, [locale_name]
    )


def gettext(message):
    """translate message based on current locale"""
    return all_translations[thread_local_data.locale].gettext(message)


# pylint: disable=invalid-name
def ngettext(singular, plural, n):
    """translation strings with plurals"""
    return all_translations[thread_local_data.locale].ngettext(singular, plural, n)


# pylint: disable=invalid-name
def setLocale(locale):
    """set thread data locale"""
    if locale in locales:
        thread_local_data.locale = locale


if __name__ == "__main__":
    # for test purpose
    for dirpath, dirnames, filenames in os.walk(localedir):
        for dirname in dirnames:
            print(dirname)
        break
