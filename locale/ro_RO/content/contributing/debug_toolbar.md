- - -
Title: Django Debug Toolbar Date: 2022-05-16 Order: 5
- - -

BookWyrm has a branch that is configured to run [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/). This branch will never get merged into `main` and has a few tweaks that make it work with the toolbar, but unsafe to use in anything resembling a production environment. To use this branch, you will need to go through a few steps to get it running.

## Configurare

- Folosind git, deplasați-vă pe ramura [`debug-toolbar`](https://github.com/bookwyrm-social/bookwyrm/tree/debug-toolbar)
- Actualizați ramura relativ la `main` folosind `git merge main`. Ramura este actualizată periodic dar este probabil ca ea să fie în urmă.
- Reconstruiți imaginea Docker folosind `docker-compose up --build` pentru a vă asigura că biblioteca de instrumente de depanare este instalată din `requirements.txt`
- Accesați imaginea aplicației `web` direct (în loc de `nginx`) folosind portul `8000`
