Title: Style Guide
Date: 2021-07-12
Order: 4

## Pull requests

So you want to contribute code to BookWyrm: that rules! If there's an open issue that you'd like to fix, it's helpful to comment on the issue so work doesn't get duplicated. Try to keep the scope of pull requests small and focused on a single topic. That way it's easier to review, and if one part needs changes, it won't hold up the other parts.

If you aren't sure how to fix something, or you aren't able to get around to it, that's totally okay, just leave a comment on the pull request and we'll figure it out 💖.

## Code style

BookWyrm uses the [Black](https://github.com/psf/black) code formatter to keep the Python codebase consistent styled. All new pull requests are checked with GitHub actions, and you can automatically fix code style problems by running `./bw-dev black`

## Linting

Code is also checked with Pylint using GitHub Actions. Pylint warnings must be addressed before pull requests are merged, but it's a judgement call if the suggestion should be used, or the warning suppressed. To suppress a warning, add a comment at the end of or on the line above the warnings: `# pylint: disable=warning-name`
