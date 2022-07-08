- - -
Title: Django Debug Toolbar Date: 2022-05-16 Order: 5
- - -

BookWyrm has a branch that is configured to run [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/). This branch will never get merged into `main` and has a few tweaks that make it work with the toolbar, but unsafe to use in anything resembling a production environment. To use this branch, you will need to go through a few steps to get it running.

## Configuration

- Avec git, basez-vous la branche [`debug-toolbar`](https://github.com/bookwyrm-social/bookwyrm/tree/debug-toolbar)
- Mettre à jour la branche relative à `main` en utilisant `git merge main`. La branche est mise à jour périodiquement, mais sera probablement en retard par rapport à la dernière version.
- Reconstruisez les images Docker en utilisant `docker-compose up --build` pour vous assurer que la lib Debug Toolbar est installée depuis `requirements.txt`
- Accédez à l'application depuis l'image `web` directement (au lieu d'y accéder via `nginx`) en utilisant le port `8000`
