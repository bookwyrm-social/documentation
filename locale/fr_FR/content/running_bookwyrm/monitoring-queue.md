---
Title: Suivi de la file d'attente
Date: 2022-11-23
Order: 6
---

Il peut arriver que votre instance tourne au ralenti. Une solution est d'inspecter la file d'attente, afin de vérifier si des tâches sont bloquées. Lisez ce qui suit afin de savoir comment.

## Celery

BookWyrm utilise [Celery](https://docs.celeryq.dev/en/stable/) pour la gestion des tâches en arrière‑plan.

## Flower

Pour le suivi en temps réel des tâches de Celery, BookWyrm se repose sur [Flower](https://flower.readthedocs.io/en/latest/).

Si vous n'avez pas modifié [`docker-compose.yml`](https://github.com/bookwyrm-social/bookwyrm/blob/dc14670a2ca7553317528d3384146d79df1f7413/docker-compose.yml#L87-L100) jusque là, vous trouverez ce service sur le [port 8888](https://github.com/bookwyrm-social/bookwyrm/blob/dc14670a2ca7553317528d3384146d79df1f7413/.env.example#L42-L45). Pour référence : `https://MY_DOMAIN_NAME:8888/`.

### Tâches

Vous trouverez des tâches [annotées `@app.task`](https://github.com/bookwyrm-social/bookwyrm/search?q=%40app.task) dans le code source.
