- - -
Títol: Barra d'eines de depuració de Django Data: 2022-05-16 Ordre: 5
- - -

BookWyrm té una branca configurada per executar la [Barra d'Eines de Depuració de Django](https://django-debug-toolbar.readthedocs.io/en/latest/). Aquesta branca no serà mai unida a `main` i té alguns retocs que li permet treballar amb la barra d'eines però, no és segur fer-ne ús en un entorn destinat a producció. To use this branch, you will need to go through a few steps to get it running.

## Set up

- Using git, checkout out the [`debug-toolbar`](https://github.com/bookwyrm-social/bookwyrm/tree/debug-toolbar) branch
- Update the branch relative to `main` using `git merge main`. The branch is updated periodically but will likely be behind latest.
- Re-build the Docker images using `docker-compose up --build` to ensure that the Debug Toolbar library is installed from `requirements.txt`
- Access the application `web` image directly (instead of via `nginx`) using port `8000`
