- - -
Title: Django Debug Toolbar Date: 2022-05-16 Order: 5
- - -

BookWyrm posiada gałąź skonfigurowaną do uruchamiania [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/). Ta gałąź nigdy nie zostanie złączona z `główna` i posiada kilka ulepszeń, które umożliwiają pracę z paskiem narzędzi, ale nie są bezpieczne do używania z czymkolwiek przypominającym środowisko oficjalne. To use this branch, you will need to go through a few steps to get it running.

## Set up

- Using git, checkout out the [`debug-toolbar`](https://github.com/bookwyrm-social/bookwyrm/tree/debug-toolbar) branch
- Update the branch relative to `main` using `git merge main`. The branch is updated periodically but will likely be behind latest.
- Re-build the Docker images using `docker-compose up --build` to ensure that the Debug Toolbar library is installed from `requirements.txt`
- Access the application `web` image directly (instead of via `nginx`) using port `8000`
