""" generate html files """
from glob import glob
import os
import re

from jinja2 import Environment, FileSystemLoader
from markdown import markdown
import yaml

import i18n

env = Environment(loader=FileSystemLoader("templates/"), extensions=["jinja2.ext.i18n"])

env.install_gettext_translations(i18n)


HEADER_SLUG = r"\[comment\]: <>"


def get_page_metadata(locale_slug, page):
    """title/order etc for a page"""
    with open(page, "r", encoding="utf-8") as page_markdown:
        # extract headers
        headers = "\n".join(
            re.sub(r"[()]", r"", r)
            for r in re.findall(rf"{HEADER_SLUG} (.*)\n", page_markdown.read())
        )
    if not headers:
        return {}

    header_obj = yaml.safe_load(headers)
    path_dir = page.split("/")[-1].replace(".md", ".html")
    header_obj["path"] = f"/{locale_slug}{path_dir}"
    return header_obj


def get_site_data(locale_slug, page):
    """this should be a file"""
    category_dirs = glob("content/*/")
    categories = []
    for cat_dir in category_dirs:
        with open(f"{cat_dir}/_meta.yml", "r", encoding="utf-8") as meta_yaml:
            parsed = yaml.safe_load(meta_yaml)

        subcategories = []
        for subcat in glob(f"{cat_dir}/*.md"):
            subcategories.append(get_page_metadata(locale_slug, subcat))
        subcategories.sort(key=lambda v: v.get("Order", -1))

        categories.append({**parsed, **{"subcategories": subcategories}})
    categories.sort(key=lambda v: v["order"])
    template_data = {"categories": categories}

    template_data["headers"] = get_page_metadata(locale_slug, page)

    return template_data


def format_markdown(file_path):
    """go from markdown to html, extracting headers"""
    with open(file_path, "r", encoding="utf-8") as markdown_content:
        return markdown(markdown_content.read(), extensions=["tables", "fenced_code"])


if __name__ == "__main__":
    # iterate through each locale
    for locale in i18n.locales_metadata:
        slug = locale["slug"]
        paths = [
            ["index.html", "content/index.md"],
            ["page.html", "content/**/*.md"],
        ]

        i18n.setLocale(locale["code"])

        LOCALIZED_SITE_PATH = "site/"
        if locale["code"] != "en_US":
            paths = [
                ["index.html", f"locale/{locale['code']}/content/index.md"],
                ["page.html", f"locale/{locale['code']}/content/**/*.md"],
            ]
            LOCALIZED_SITE_PATH = f"site/{slug}"

        # iterate through template types
        for (path, content_paths) in paths:
            with open(f"templates/{path}", "r", encoding="utf-8") as template_file:
                template_string = template_file.read()
            template = env.from_string(template_string)

            localized_dirs = f"{LOCALIZED_SITE_PATH}"
            localized_dirs = localized_dirs[: localized_dirs.rfind("/")]
            if not os.path.exists(localized_dirs):
                os.makedirs(localized_dirs)

            for content_path in glob(content_paths):
                output_path = content_path.split("/")[-1].replace(".md", ".html")
                print("  Generating", f"{LOCALIZED_SITE_PATH}{output_path}")
                with open(
                    f"{LOCALIZED_SITE_PATH}{output_path}", "w+", encoding="utf-8"
                ) as render_file:
                    data = get_site_data(slug, content_path)
                    data["content"] = format_markdown(content_path)
                    data["path"] = f"/{slug}{output_path}"
                    render_file.write(
                        template.render(
                            locale=locale,
                            locales_metadata=i18n.locales_metadata,
                            **data,
                        )
                    )
