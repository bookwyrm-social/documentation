- - -
Title: Django Debug Toolbar Date: 2022-05-16 Order: 5
- - -

BookWyrm has a branch that is configured to run [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/). This branch will never get merged into `main` and has a few tweaks that make it work with the toolbar, but unsafe to use in anything resembling a production environment. To use this branch, you will need to go through a few steps to get it running.

## Установка

- Using git, checkout out the [`debug-toolbar`](https://github.com/bookwyrm-social/bookwyrm/tree/debug-toolbar) branch
- Update the branch relative to `main` using `git merge main`. The branch is updated periodically but will likely be behind latest.
- Re-build the Docker images using `docker-compose up --build` to ensure that the Debug Toolbar library is installed from `requirements.txt`
- Access the application `web` image directly (instead of via `nginx`) using port `8000`
