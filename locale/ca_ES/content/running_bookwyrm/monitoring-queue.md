---
Title: Monitorant la cua
Date: 2022-11-23
Order: 7
---

Hi pot haver ocasions en què la teva instància es comporti de manera lenta. One option would be to inspect the queue to see whether some jobs hang. Llegeix per saber-ne més.

## Celery

BookWyrm is using [Celery](https://docs.celeryq.dev/en/stable/) to manage background jobs.

## Flower

To watch Celery jobs in real-time BookWyrm uses [Flower](https://flower.readthedocs.io/en/latest/).

By default you can view flower logs from `https://example.com/flower/`. You will need to enter the login name and password from your `.env` file. Celery can help to troubleshoot problems you may be having with your task queue.

### Tasques

If you want to know which actions are sent to celery, you can find [`@app.task` annotated](https://github.com/bookwyrm-social/bookwyrm/search?q=%40app.task) tasks in the codebase.
