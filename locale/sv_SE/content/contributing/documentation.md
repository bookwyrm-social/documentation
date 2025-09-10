---
Title: Dokumentation
Date: 2025-04-09
Order: 4
---

The documentation you are reading right now is maintained by the BookWyrm community. Anyone can contribute to the docs.

## Suggesting an improvement

You can report an **error**, suggest an **improvement** or request an **addition** to the documentation by [creating an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue) in [the documentation repository](https://github.com/bookwyrm-social/documentation).

## How the docs are made

The Documentation [has its own GitHub repository](https://github.com/bookwyrm-social/documentation). Documentation is written in Markdown and we use [Jinja](https://jinja.palletsprojects.com/en/stable) and a Python script to convert that into HTML. A Jinja plugin is used with Crowdin to create translations. All documentation source files should be written in English (US).

All source files are saved in the `content` directory. Each section has a directory within that, with each page being represented by a single markdown file.

## Editing or creating a documentation page

To edit or create a new page you will need to:

1. clone [the GitHub repository](https://github.com/bookwyrm-social/documentation)
2. work in the `content` directory to make your changes - either editing an existing markdown page or creating a new one
3. create a new Pull Request
4. respond to any reviews with further edits
5. enjoy seeing your updates instantly published when your pull request is approved and merged

If you have never used git or GitHub before, that may sound daunting, but let's break it down:

### Clone the repository

1. Make sure you have [a GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github).
2. Create a "clone" or "fork" of the Documentation repository:

   - From the **web interface**, click "Fork" at the top of [this page](https://github.com/bookwyrm-social/documentation)
   - If you are using **GitHub Desktop**, follow [these instructions](https://docs.github.com/en/desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop)
   - If you are using the command line, run:

   `git clone https://github.com/bookwyrm-social/documentation.git`

### Create a new branch and make your edits

För att göra ändringar:

1. [Create a new branch](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-a-branch-for-an-issue) in your fork
2. Make your edits in the `content` directory and **commit** your changes:
   - [GitHub web interface](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)
   - [GitHub Desktop](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop)
   - On the command line save your changes to the files and run `git commit`

At this point you might want to see what your changes will look like when published. See [Building docs locally](#building-docs-locally) below for instruction on how to preview your changes.

### Create a pull request

Once you have completed your changes, [make a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) to the docs repository.

Your pull request will be reviewed and one of three things will happen:

1. It will be **merged** with no changes
2. You will be asked to make **changes**
3. It will be **rejected** and closed

### Respond to reviews

If you are asked to make changes, you can make them locally and `push` your local changes to your fork/clone on GitHub. This will automatically flow through to your pull request. Let the reviewer know when you have completed your updates so they can do another review and hopefully "pull" your changes.

We welcome all contributions. It would be unusual for a contribution to the docs to be rejected immediately. This would only happen if your pull request introduces information that is wrong or misleading with no chance of being improved, or if it has been declared out of scope.

### Your changes are published

When your pull request is merged, [the documentation](https://docs.joinbookwyrm.com/) is automatically updated. You may need to refresh your browser or use "incognito mode" to see the changes in your browser.

## Nya sidor

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

### svart

This will run `black` to lint your files and avoid any issues with our automated checks. You are unlikely to need this if you are simply updating the documentation source files in `content`.
