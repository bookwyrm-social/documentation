---
Title: Monitoring Queue
Date: 2022-11-23
Order: 7
---

There might be occurences where your instances behaves slowly. One option would be to inspect the queue to see whether some jobs hang. Read on to learn how.

## Celery

BookWyrm uses [Celery](https://docs.celeryq.dev/en/stable/) to manage background jobs.

By default this [uses gevent](https://docs.celeryq.dev/en/stable/userguide/concurrency/gevent.html) to run 1000 concurrent tasks with greenlet under a single worker. This allow for high throughput of tasks whilst restricting Celery to using a single CPU core, reducing the risk of CPU and RAM overload. If your BookWyrm instance requires more workers, you can increase this with the [`--scale`](https://docs.docker.com/reference/cli/docker/compose/up/) flag applied to the `celery_worker` service:

```sh
./bw-dev up --scale celery_worker=3
```

## Blomma

To watch Celery jobs in real-time BookWyrm uses [Flower](https://flower.readthedocs.io/en/latest/).

By default you can view flower logs from `https://example.com/flower/`. You will need to enter the login name and password from your `.env` file. Celery can help to troubleshoot problems you may be having with your task queue.

### Uppgifter

If you want to know which actions are sent to celery, you can find [`@app.task` annotated](https://github.com/bookwyrm-social/bookwyrm/search?q=%40app.task) tasks in the codebase.
