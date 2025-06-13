- - -
Titel: Django Debug werkbalk Datum: 2022-05-16 Order: 5
- - -

BookWyrm heeft een tak die is geconfigureerd om [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) uit te voeren. Deze tak zal nooit worden samengevoegd in `main` en heeft een paar aanpassingen waardoor het werkt met de werkbalk, maar onveilig om te gebruiken in iets dat lijkt op een productieomgeving. Om deze tak te gebruiken, moet u een paar stappen doorlopen om deze aan de praat te krijgen.

## Instellen

- Using git, checkout out the [`debug-toolbar`](https://github.com/bookwyrm-social/bookwyrm/tree/debug-toolbar) branch
- Update the branch relative to `main` using `git merge main`. The branch is updated periodically but will likely be behind latest.
- Re-build the Docker images using `docker-compose up --build` to ensure that the Debug Toolbar library is installed from `requirements.txt`
- Access the application `web` image directly (instead of via `nginx`) using port `8000`
