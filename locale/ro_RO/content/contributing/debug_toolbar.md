BookWyrm are o ramură care este configurată să ruleze [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/). Această ramură nu va fi niciodată fuzionată cu `main` și are câteva modificări care o fac să funcționeze cu bara de instrumente, dar nesigură de utilizat în ceva asemănător unui mediu de producție. Pentru a folosi această ramură, va trebui să urmăriți câțiva pași pentru a o configura.

## Configurare

- Folosind git, deplasați-vă pe ramura [`debug-toolbar`](https://github.com/bookwyrm-social/bookwyrm/tree/debug-toolbar)
- Update the branch relative to `main` using `git merge main`. The branch is updated periodically but will likely be behind latest.
- Re-build the Docker images using `docker-compose up --build` to ensure that the Debug Toolbar library is installed from `requirements.txt`
- Access the application `web` image directly (instead of via `nginx`) using port `8000`
