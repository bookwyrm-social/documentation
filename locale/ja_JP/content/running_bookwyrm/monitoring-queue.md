---
Title: Monitoring Queue
Date: 2022-11-23
Order: 6
---

There might be occurences where your instances behaves slowly. One option would be to inspect the queue to see, whether some jobs hang. Read on to learn how.

## Celery

BookWyrm is using [Celery](https://docs.celeryq.dev/en/stable/) to manage background jobs.

## Flower

To watch Celery jobs in real-time BookWyrm uses [Flower](https://flower.readthedocs.io/en/latest/).

In case you haven't tweaked the [`docker-compose.yml`](https://github.com/bookwyrm-social/bookwyrm/blob/dc14670a2ca7553317528d3384146d79df1f7413/docker-compose.yml#L87-L100) you can find the service on [port 8888](https://github.com/bookwyrm-social/bookwyrm/blob/dc14670a2ca7553317528d3384146d79df1f7413/.env.example#L42-L45). That is: `https://MY_DOMAIN_NAME:8888/`.

### Tasks

You can find [`@app.task` annotated](https://github.com/bookwyrm-social/bookwyrm/search?q=%40app.task) tasks in the codebase.
