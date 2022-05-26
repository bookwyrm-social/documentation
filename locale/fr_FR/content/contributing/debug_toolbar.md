BookWyrm a une branche qui est configurée pour exécuter la [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/). Cette branche ne sera jamais fusionnée dans `main` et a quelques améliorations qui la font fonctionner avec la barre d'outils, mais qui sont dangereuses à utiliser dans un environnement étant ou approchant de la production. Pour utiliser cette branche, vous devez passer par quelques étapes pour que ça marche.

## Configuration

- Avec git, basez-vous la branche [`debug-toolbar`](https://github.com/bookwyrm-social/bookwyrm/tree/debug-toolbar)
- Mettre à jour la branche relative à `main` en utilisant `git merge main`. La branche est mise à jour périodiquement, mais sera probablement en retard par rapport à la dernière version.
- Reconstruisez les images Docker en utilisant `docker-compose up --build` pour vous assurer que la lib Debug Toolbar est installée depuis `requirements.txt`
- Accédez à l'application depuis l'image `web` directement (au lieu d'y accéder via `nginx`) en utilisant le port `8000`
