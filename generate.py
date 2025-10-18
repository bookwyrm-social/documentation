""" generate html files """

from glob import glob
import os
import sys

from jinja2 import Environment, FileSystemLoader
from markdown import Markdown
import yaml

import i18n

env = Environment(loader=FileSystemLoader("templates/"), extensions=["jinja2.ext.i18n"])

env.install_gettext_translations(i18n)


def get_page_metadata(locale_slug, page, version_slug=False):
    """title/order etc for a page
    this is how the markdown file is composed:

    > ---
    > Header: value
    > Another key: another value
    > ---

    and this is how crowdin sends it back as:

    > - - -
    > Header: value Another key: another value
    > - - -

    I don't know how to ask crowdin nicely not to do this, so instead I'm supporting
    both styles, which is janky.
    """
    headers = []

    with open(page, "r", encoding="utf-8") as page_markdown:
        header_block_open = False
        for line in page_markdown.readlines():
            if line.replace(" ", "").strip() == "---":
                header_block_open = not header_block_open
                continue
            if not header_block_open:
                break
            for word in line.split(" "):
                # start of a new header
                if word[-1] == ":":
                    headers.append([word])
                elif headers:
                    headers[-1].append(word)
        headers = "\n".join(" ".join(line) for line in headers)

    try:
        header_obj = yaml.safe_load(headers) or {}
    except yaml.parser.ParserError:
        header_obj = {}

    length = len(page.split("/")) - 2
    header_obj["file_path"] = (
        "/".join(page.split("/")[length:])
        if page.split("/")[-1] != "index.md"
        else page.split("/")[-1]
    )
    path_dir = page.split("/")[-1].replace(".md", ".html")
    header_obj["path"] = (
        f"/{locale_slug}{path_dir}"
        if not version_slug
        else f"/{version_slug}/{locale_slug}{path_dir}"
    )
    return header_obj


def get_site_data(locale_slug, locale_code, page, version_slug=False):
    """this should be a file"""
    category_dirs = glob("content/*/")
    categories = []
    for cat_dir in category_dirs:
        with open(f"{cat_dir}/_meta.yml", "r", encoding="utf-8") as meta_yaml:
            parsed = yaml.safe_load(meta_yaml)

        subcategories = []
        location = (
            f"locale/{locale_code}/{cat_dir}/*.md" if locale_slug else f"{cat_dir}/*.md"
        )
        for subcat in glob(location):
            subcategories.append(get_page_metadata(locale_slug, subcat, version_slug))
        subcategories.sort(key=lambda v: v.get("Order", -1))

        categories.append({**parsed, **{"subcategories": subcategories}})
    categories.sort(key=lambda v: v["order"])
    template_data = {"categories": categories}

    template_data["headers"] = get_page_metadata(locale_slug, page, version_slug)

    return template_data


def format_markdown(file_path):
    """go from markdown to html, extracting headers"""
    with open(file_path, "r", encoding="utf-8") as page_markdown:
        first_line = page_markdown.readline()
        dashed_header_format = first_line == "---\n"

    with open(file_path, "r", encoding="utf-8") as markdown_content:

        md = Markdown(
            extensions=["tables", "fenced_code", "codehilite", "toc", "sane_lists"],
            extension_configs={
                "codehilite": {"css_class": "highlight"},
                "toc": {"anchorlink": True, "anchorlink_class": "headerlink"},
            },
        )

        if dashed_header_format:
            headerless = []
            header_block_open = False
            for line in markdown_content.readlines():
                if line.replace(" ", "") == "---\n":
                    header_block_open = not header_block_open
                elif not header_block_open:
                    headerless.append(line)

            body = md.convert("".join(headerless))
            return {"body": body, "toc": md.toc_tokens}

        body = md.convert("".join(markdown_content.readlines()[3:]))
        return {"body": body, "toc": md.toc}


if __name__ == "__main__":
    # when we generate for versions we need to change the page links
    version = sys.argv[1] if (len(sys.argv) > 1 and sys.argv[1] != "main") else False
    # iterate through each locale
    for locale in i18n.locales_metadata:
        SLUG = locale["slug"]
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
            LOCALIZED_SITE_PATH = f"site/{SLUG}"

        # iterate through template types
        for path, content_paths in paths:
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
                    data = get_site_data(SLUG, locale["code"], content_path, version)
                    formatted_md = format_markdown(content_path)
                    data["content"] = formatted_md["body"]
                    data["toc"] = formatted_md["toc"]
                    data["path"] = (
                        f"/{SLUG}{output_path}"
                        if not version
                        else f"/{version}/{SLUG}{output_path}"
                    )
                    versions = ["development", "v0.7.5", "0.8.0"]
                    current_version = version if version else ""
                    render_file.write(
                        template.render(
                            versions=versions,
                            current_version=current_version,
                            locale=locale,
                            locales_metadata=i18n.locales_metadata,
                            **data,
                        )
                    )
