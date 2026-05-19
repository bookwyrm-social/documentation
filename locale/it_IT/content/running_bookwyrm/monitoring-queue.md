---
Title: Coda Da Monitoraggio
Date: 2022-11-23
Order: 7
---

Ci potrebbero essere eventi dove le tue istanze si comportano lentamente. One option would be to inspect the queue to see whether some jobs hang. Continua a leggere per capire come.

## Celery

BookWyrm usa [Celery](https://docs.celeryq.dev/en/stable/) per gestire le operazioni in secondo piano.

Normalmente questo [usa gevent](https://docs.celeryq.dev/en/stable/userguide/concurrency/gevent.html) per compiere 1000 operazioni conteporanee con greenlet per un singolo processore. Questo permette di gestire un alto numero di processi pur limitando Celery all'uso di un solo core CPU, riducendo il rischio di sovraccarico a CPU e RAM. Se la tua istanza BookWyrm ha bisogno di più processori, puoi aumentarli con il flag [`--scale`](https://docs.docker.com/reference/cli/docker/compose/up/) applicato al servizio `celery_worker`:

```sh
./bw-dev up --scale celery_worker=3
```

## Flower

To watch Celery jobs in real-time BookWyrm uses [Flower](https://flower.readthedocs.io/en/latest/).

By default you can view flower logs from `https://example.com/flower/`. You will need to enter the login name and password from your `.env` file. Celery can help to troubleshoot problems you may be having with your task queue.

### Compiti

If you want to know which actions are sent to celery, you can find [`@app.task` annotated](https://github.com/bookwyrm-social/bookwyrm/search?q=%40app.task) tasks in the codebase.
