- - -
Títol: Barra d'eines de depuració de Django Data: 2022-05-16 Ordre: 5
- - -

BookWyrm té una branca configurada per executar la [Barra d'Eines de Depuració de Django](https://django-debug-toolbar.readthedocs.io/en/latest/). Aquesta branca no serà mai unida a `main` i té alguns retocs que li permet treballar amb la barra d'eines però, no és segur fer-ne ús en un entorn destinat a producció. Per a fer servir aquesta branca, necessitaràs fer algunes accions per fer-la funcionar.

## Configuració

- Utilitzant git, busca la branca [`debug-toolbar`](https://github.com/bookwyrm-social/bookwyrm/tree/debug-toolbar)
- Actualitza la branca relativa a `main` fent ús de `git merge main`. La branca s'actualitza periòdicament però anirà per darrere de l'última.
- Reconstrueix les imatges de Docker mitjançant `docker-compose up --build` per assegurar-te que la llibreria de la Barra d'eines de Depuració s'instal·la des de `requirements.txt`
- Accedeix directament a la imatge de l'aplicació `web` (en comptes de via `nginx`) fent ús del port `8000`
