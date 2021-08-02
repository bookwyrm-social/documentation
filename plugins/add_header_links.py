""" Adds permalinks to headers """
from html.parser import HTMLParser
from urllib.parse import quote as url_quote

from pelican import signals


# pylint: disable=no-self-use
class HeaderLinksHTMLParser(HTMLParser):  # pylint: disable=abstract-method
    """subclass `HTMLParser` to easily transform html.

    most of the method overrides re-construct the html and add it to self.data.
    this means that any html fed into the parser will be re-emitted,
    potentially with some transformations (adding links to headers) applied
    """

    def _is_header(self, tag):
        """check if a given tag or tag name is a header"""
        # normalize `<h2 ...>` or `h2` into just `h2`
        if tag[0] == "<":
            # second split removes trailing angle bracket on `<h2>`
            tagname = tag[1:].split()[0].split(">")[0]
        else:
            tagname = tag

        return (
            len(tagname) == 2 and tagname[0].lower() == "h" and "1" <= tagname[1] <= "6"
        )

    def _create_id_slug(self, title):
        """create a unique url-safe slug from a title"""
        slug = url_quote("_".join(title.lower().split()))
        # make sure the slug is unique
        if slug in self.slugs:
            counter = 1
            done = False
            while not done:
                if f"{slug}_{counter}" in self.slugs:
                    counter += 1
                    continue
                slug = f"{slug}_{counter}"
                done = True
        self.slugs.append(slug)
        return slug

    def __init__(self):
        self.data = []
        self.slugs = []
        # because we're going from html to html, we don't want to convert charrefs
        super().__init__(convert_charrefs=False)

    def reset(self):
        self.data = []
        self.slugs = []
        super().reset()

    def handle_starttag(self, tag, attrs):
        # `handle_data()` takes care of header start tags, so skip those
        if not self._is_header(tag):
            self.data.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        self.data.append(f"</{tag}>")

    def handle_startendtag(self, tag, attrs):
        self.data.append(self.get_starttag_text())

    def handle_data(self, data):
        """handle text nodes within a tag

        this does the heavy-lifting of checking for a header and doing
        appropriate transformations
        """
        # ensure that `data` isn't whitespace
        # the newline in '<h2>foo</h2>\n' will start a `handle-data` method call
        # where the `get_starttag_text` method still returns '<h2>' since that method
        # returns the *most recently opened* tag
        # if we don't check for whitespace here, we get stray link and header
        # openers with no closers
        if self._is_header(self.get_starttag_text()) and data.strip() != "":
            id_slug = self._create_id_slug(data)
            # use the existing tag excluding the final '>',
            # then append the id and a closing '>'
            new_tag = self.get_starttag_text()[:-1] + f' id="{id_slug}">'
            self.data.append(
                f"""{new_tag}{data}
<a href=#{id_slug} class="icon icon-chain pl-3 is-size-6">
    <span class="is-sr-only">Hyperlink to this header</span>
</a>"""
            )
        else:
            self.data.append(data)

    def handle_comment(self, data):
        self.handle_data(f"<!-- {data} -->")

    def handle_decl(self, decl):
        self.handle_data(f"<!{decl}>")

    def unknown_decl(self, data):
        self.handle_data(data)

    def handle_entityref(self, name):
        self.handle_data(f"&{name};")

    def handle_charref(self, name):
        self.handle_data(f"&#{name};")

    def __str__(self):
        return "".join(self.data)


def add_header_links(content):
    """inject header links"""
    html_parser = HeaderLinksHTMLParser()
    for index, article in enumerate(content.articles):
        html_parser.feed(article._content)
        content.articles[index]._content = str(html_parser)
        html_parser.reset()


def register():
    """this signal runs after a generator has finished rendering an article"""
    signals.article_generator_finalized.connect(add_header_links)
