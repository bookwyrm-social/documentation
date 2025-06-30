---
Title: Cola de monitoreo
Date: 2022-11-23
Order: 6
---

Puede haber casos en los que tus instancias se ralenticen. Una opción sería inspeccionar la cola para ver si algunos trabajos se bloquean. Lee para aprender cómo.

## Celery

BookWyrm utiliza [Celery](https://docs.celeryq.dev/en/stable/) para manejar trabajos de fondo.

## Flower

Para mirar trabajos de Celery en BookWyrm en tiempo real usa [Flower](https://flower.readthedocs.io/en/latest/).

En caso de que no hayas modificado el [`docker-compose.yml`](https://github.com/bookwyrm-social/bookwyrm/blob/dc14670a2ca7553317528d3384146d79df1f7413/docker-compose.yml#L87-L100) puedes encontrar el servicio en [port 8888](https://github.com/bookwyrm-social/bookwyrm/blob/dc14670a2ca7553317528d3384146d79df1f7413/.env.example#L42-L45). Esto es: `https://MY_DOMAIN_NAME:8888/`.

### Tareas

Puedes encontrar en [`@app.task` ](https://github.com/bookwyrm-social/bookwyrm/search?q=%40app.task) tareas anotadas en el código base.
