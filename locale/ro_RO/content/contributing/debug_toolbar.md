BookWyrm are o ramură care este configurată să ruleze [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/). Această ramură nu va fi niciodată fuzionată cu `main` și are câteva modificări care o fac să funcționeze cu bara de instrumente, dar nesigură de utilizat în ceva asemănător unui mediu de producție. Pentru a folosi această ramură, va trebui să urmăriți câțiva pași pentru a o configura.

## Configurare

- Folosind git, deplasați-vă pe ramura [`debug-toolbar`](https://github.com/bookwyrm-social/bookwyrm/tree/debug-toolbar)
- Actualizați ramura relativ la `main` folosind `git merge main`. Ramura este actualizată periodic dar este probabil ca ea să fie în urmă.
- Reconstruiți imaginea Docker folosind `docker-compose up --build` pentru a vă asigura că biblioteca de instrumente de depanare este instalată din `requirements.txt`
- Accesați imaginea aplicației `web` direct (în loc de `nginx`) folosind portul `8000`
