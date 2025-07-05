# BookWyrm Documentation

You can view the documentation at [docs.joinbookwyrm.com](https://docs.joinbookwyrm.com).

View the main BookWyrm repository at [github.com/bookwyrm-social/bookwyrm](https://github.com/bookwyrm-social/bookwyrm)

## Contributing

More information on contributing to the docs is available [within the docs themselves]([https://docs.joinbookwyrm.com/documentation.html):

* [Editing or creating a page](https://docs.joinbookwyrm.com/documentation.html#editing-or-creating-a-documentation-page)
* [Building the docs locally to test output](https://docs.joinbookwyrm.com/documentation.html#building-docs-locally) (for testing)

## Translations

Maintainers of this repository can keep translations aligned by regularly updating from Crowdin:

1. Translations are updated in Crowdin
2. Crowdin pushes new translations to l10n_main as they are available
3. In your fork, `pull` both `main` and `l10n_main` so they are up to date in your local repository
4. Create a new fork from `main` (e.g. called `update_locales`)
5. merge `l10n_main` into your fork
6. make adjustment if necessary
7. push your local branch up to your remote and create a pull request
8. pull the PR into `main`
9. There is now a new reference file in en_US
10. Using the changes in the new reference file, translations are updated in Crowdin...
