---
Title: Monitorant la cua
Date: 2022-11-23
Order: 6
---

Hi pot haver ocasions en què la teva instància es comporti de manera lenta. Una opció pot ser revisar la cua per veure treballs penjats. Llegeix per saber-ne més.

## Celery

BookWyrm fa ús de [Celery](https://docs.celeryq.dev/en/stable/) per gestionar treballs en cua.

## Flower

Per veure els treballs de Celery en temps real, BookWyrm fa ús de [Flower](https://flower.readthedocs.io/en/latest/).

En cas que no hagis retocat [`docker-compose.yml`](https://github.com/bookwyrm-social/bookwyrm/blob/dc14670a2ca7553317528d3384146d79df1f7413/docker-compose.yml#L87-L100) pots trobar el servei al [port 8888](https://github.com/bookwyrm-social/bookwyrm/blob/dc14670a2ca7553317528d3384146d79df1f7413/.env.example#L42-L45). Això és: `https://MY_DOMAIN_NAME:8888/`.

### Tasques

Pots trobar [`@app.task` ](https://github.com/bookwyrm-social/bookwyrm/search?q=%40app.task) les tasques anotades al codi base.
