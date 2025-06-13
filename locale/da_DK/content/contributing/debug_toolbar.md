- - -
Titel: Django Fejlfindingsværktøjslinje Dato: 2022-05-16 Rækkefølge: 5
- - -

BookWyrm har en gren, der er konfigureret til at køre [Django Fejlfindingsværktøjslinje](https://django-debug-toolbar.readthedocs.io/en/latest/). Denne gren vil aldrig blive flettet ind i `main` og har et par finjusteringer, der får den til at fungere med værktøjslinjen, men gør den usikker at bruge i noget, der ligner et produktionsmiljø. For at bruge denne gren bliver du nødt til at gennemgå et par trin for at få det til at køre.

## Opsætning

- Brug Git til at hente grenen [`fejlsøgningsværktøjslinje`](https://github.com/bookwyrm-social/bookwyrm/tree/debug-toolbar)
- Opdater grenen i forhold til `main` ved hjælp af `git merge main`. Grenen opdateres regelmæssigt, men vil sandsynligvis ikke være helt ajour med seneste version.
- Genopbyg Docker-billederne ved hjælp af `docker-compose up --build` for at sikre, at Fejlsøgningsværktøjslinje-biblioteket er installeret fra `requirements.txt`
- Tilgå `web`-billedet direkte (i stedet for via `nginx`) ved hjælp af port `8000`
