---
Title: Dokumentation
Date: 2025-04-09
Order: 4
---

Die Dokumentation, die du gerade liest, wird von der BookWyrm-Community gepflegt. Jede Person kann zur Dokumentation beitragen.

## Eine Verbesserung vorschlagen

Du kannst einen **Fehler** (engl. error) melden, eine **Verbesserung** (engl. improvement) vorschlagen oder eine **Ergänzung** (engl. addition) zur Dokumentation anfragen, indem du [einen Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue) im [Dokumentations-Repository](https://github.com/bookwyrm-social/documentation) anlegst.

## Wie die Dokumentation erstellt wird

Die Dokumentation [hat ihr eigenes GitHub-Repository](https://github.com/bookwyrm-social/documentation). Sie wird in Markdown verfasst und wir nutzen [Jinja](https://jinja.palletsprojects.com/en/stable) und ein Python-Skript, um sie in HTML umzuwandeln. Ein Jinja-Plugin wird gemeinsam mit Crowdin genutzt, um Übersetzungen zu erstellen. Alle Quelldateien der Dokumentation sollen in US-Englisch verfasst werden.

Alle Quelldatein werden im `content`-Verzeichnis abgelegt. Jeder Abschnitt hat darin ein Verzeichnis, wobei jede Seite durch eine einzelne Markdown-Datei abgebildet wird.

## Dokumentationsseiten bearbeiten oder anlegen

Um eine neue Seite anzulegen, ist Folgendes notwendig:

1. klone [das GitHub-Repository](https://github.com/bookwyrm-social/documentation)
2. arbeite im `content`-Verzeichnis, um deine Änderungen vorzunehmen – indem du entweder eine bestehende Markdown-Seite anpasst oder eine neue erstellst
3. erstelle eine neue Pull Request
4. nimm weitere Änderungen vor, wenn du Rückmeldungen erhältst
5. genieße, wie deine Änderungen sofort veröffentlicht werden, sobald deine Pull Request angenommen und gemerget wurde

Wenn du noch nie Git oder GitHub verwendet hast, mag das alles beängstigend klingen, aber lass es uns herunterbrechen:

### Klone das Repository

1. Stelle sicher, dass du [einen GitHub-Account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) hast.
2. Erstelle einen "Klon" oder "Fork" des Dokumentations-Repositorys:

   - Auf der **Web-Oberfläche** klicke "Fork" am oberen Rand [dieser Seite](https://github.com/bookwyrm-social/documentation)
   - Wenn du **GitHub Desktop** verwendest, folge [diesen Anweisungen](https://docs.github.com/en/desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop)
   - Wenn du die Kommandozeile nutzt, führe aus:

   `git clone https://github.com/bookwyrm-social/documentation.git`

### Einen neuen Branch erstellen und Änderungen vornehmen

Um Änderungen vorzunehmen:

1. [Erstelle einen neuen Branch](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-a-branch-for-an-issue) in deinem Fork
2. Nimm deine Änderungen am `content`-Verzeichnis vor und **commite** sie:
   - [GitHub-Web-Oberfläche](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)
   - [GitHub Desktop](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop)
   - In der Kommandozeile, speichere deine Änderungen an den Dateien und führe `git commit` aus

An dieser Stelle wirst du vielleicht sehen wollen, wie deine Änderungen aussehen, wenn sie veröffentlicht werden. Schau dir [Dokumentation lokal bauen](#building-docs-locally) weiter unten an, um zu erfahren, wie du eine Vorschau deiner Änderungen ansehen kannst.

### Eine Pull Request erstellen

Wenn deine Änderungen abgeschlossen sind, [erstelle eine Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) an das Dokumentations-Repository.

Deine Pull Request wird überprüft werden und eines der drei folgenden Szenarien wird eintreten:

1. Sie wird ohne Änderungen **übernommen** (engl. merged)
2. Du wirst gebeten, **Änderungen** vorzunehmen
3. Sie wird **abgelehnt** und geschlossen

### Auf Überprüfungen reagieren

Wenn du gebeten wirst, Änderungen vorzunehmen, kannst du dies lokal erledigen und deine lokalen Änderungen an deinen Fork/Klon auf Github senden (engl. `push`). Sie werden dann automatisch in deine Pull Request übernommen. Lass den\*die Reviewer\*in wissen, wenn du mit deinen Anpassungen fertig bist, damit die Person eine weitere Überprüfung starten und dann hoffentlich deine Änderungen zu sich holen (engl. `pull`) kann.

Wir heißen alle Beiträge willkommen. Es wäre ungewöhnlich, wenn ein Beitrag zur Dokumentation direkt abgelehnt würde. Das würde nur dann geschehen, wenn deine Pull Request Informationen einfügt, die falsch oder irreführend ohne Aussicht auf Besserung sind oder wenn festgestellt wird, dass sie aus dem Rahmen fällt.

### Deine Änderungen werden veröffentlicht

Wenn deine Pull Request übernommen wird, wird [die Dokumentation](https://docs.joinbookwyrm.com/) automatisch aktualisiert. Es kann sein, dass du deinen Browser neu starten oder den "Inkognito-Modus" nutzen musst, um die Änderungen in deinem Browser zu sehen.

## Neue Seiten

If you are adding a new page, you will need to add some metadata and may need to adjust other pages.

At the top of each markdown file is the "frontmatter" in `toml` format:

```toml
Title: Documentation
Date: 2025-04-09
Order: 4
```

This example shows that the page is called  "Documentation", should be the fourth page within its section (in this case, `Contributing`), and that it was last updated on 9 April 2025. If you add a page anywhere other than at the end of a section, you will need to adjust the order of every page that appears below your new page.

This section is contained within a pair of triple dashes (`---`). In markdown, triple dashes can also be used to indicate a horizontal rule, however the BookWyrm docs parser can get confused by this. If you need a horizontal rule, enter it as HTML code directly with blank lines above and below:

```html

<hr/>

```

## Building docs locally

You might want to see what your changes will look like before sending a pull request. The docs repository includes a development script like the main code repository, with the same name: `bw-dev`. You can use this to test what your changes will look like.

Unlike the main project, the documentation does not run in a Docker container. If you want to compile the documentation site locally you will need to install the dependencies, and it is recommended that you [use a virtual environment](https://docs.python.org/3/library/venv.html):

```py
python -m venv /path/to/new/virtual/environment
source <venv>/bin/activate
pip install -r requirements.txt
```

There are a number of commands available by running `./bw-dev <command>`. The ones you are likely to want to use are:

### site:compile

This will compile markdown files into html files using the `generate.py` script.

When you run `site:compile` it will generate a large number of files in the `site` directory. Do not check these in or include them in your pull request: they will be re-generated on the documentation server when your pull request is merged.

### site:serve

This runs a local web server at `http://[::1]:8080/` so you can see what the docs will look like.

### black

This will run `black` to lint your files and avoid any issues with our automated checks. You are unlikely to need this if you are simply updating the documentation source files in `content`.

## Notes for documentation maintainers

### Translations

Keep translations aligned by regularly updating from Crowdin:

1. Translations are updated in Crowdin
2. Crowdin pushes new translations to l10n_main as they are available
3. In your fork, `pull` both `main` and `l10n_main` so they are up to date in your local repository
4. Create a new fork from `main` (e.g. called `update_locales`) and check it out
5. merge `l10n_main`'s `locale` directory into your fork: `git checkout l10n_main -- locale`
6. make adjustments if necessary
7. push your local branch up to your remote and create a pull request
8. pull the PR into `main`
9. There is now a new reference file in en_US
10. Using the changes in the new reference file, translations are updated in Crowdin...

Locales for the language dropdown are listed in `i18n.py`. Generally we wait for a language to have 70% coverage in Crowdin before adding it to the list to avoid too much content remaining untranslated.

### Updating when a new version is released

When a new version of BookWyrm is released we need to create a new version of the docs:

1. Add a new branch with a name exactly matching the new version tag in BookWyrm. e.g. `v0.8.0`.

2. Add that branch name to the list of versions in `generate.py` in the `main` branch of the docs

3. Check out every other version in turn, and merge the updated generation file into it so they all have the new branch listed: `git checkout main generate.py`. Then commit this change, create a PR to merge this change into the version's branch in the docs, and merge it. This will ensure that all pages in all versions of the docs have every other version listed in the dropdown menu.

4. Merge the change in the `main` branch last - only merges into `main` trigger the GitHub action to deploy to the docs web server so if you do this first, the changes in other branches will have no effect.