""" generate html files """
from glob import glob
import os
import re

import i18n
from jinja2 import Environment, FileSystemLoader
from markdown import markdown

env = Environment(loader=FileSystemLoader("templates/"), extensions=["jinja2.ext.i18n"])

env.install_gettext_translations(i18n)


def get_site_data():
    """ this should be a file """
    dirs = glob("content/**")
    return {"categories": [re.sub(r"\d|_", " ", d) for d in dirs]}

if __name__ == "__main__":
    data = get_site_data()
    paths = [
        ["index.html", data, "content/pages/index.md"],
    ]

    # iterate through each locale
    for locale in i18n.locales_metadata:
        i18n.setLocale(locale["code"])

        LOCALIZED_SITE_PATH = "site/"
        if not locale["code"] == "en_US":
            LOCALIZED_SITE_PATH = f'site/{locale["slug"]}'

        # iterate through template types
        for (path, data, content_paths) in paths:
            print("  Generating", f"{LOCALIZED_SITE_PATH}{path}")
            with open(f"templates/{path}", "r", encoding="utf-8") as template_file:
                template_string = template_file.read()
            template = env.from_string(template_string)

            localized_dirs = f"{LOCALIZED_SITE_PATH}{path}"
            localized_dirs = localized_dirs[: localized_dirs.rfind("/")]
            if not os.path.exists(localized_dirs):
                os.makedirs(localized_dirs)

            with open(
                f"{LOCALIZED_SITE_PATH}{path}", "w+", encoding="utf-8"
            ) as render_file:
                with open(content_paths, "r", encoding="utf-8") as markdown_content:
                    data["content"] = markdown(markdown_content.read())
                render_file.write(
                    template.render(
                        locale=locale,
                        locales_metadata=i18n.locales_metadata,
                        **data,
                    )
                )
