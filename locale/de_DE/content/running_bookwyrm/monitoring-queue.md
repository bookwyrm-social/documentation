---
Title: Überwachungswarteschlange
Date: 2022-11-23
Order: 7
---

Es kann passieren, dass deine Instanz langsam ist. Eine Option wäre es, die Warteschlange zu inspizieren, um zu sehen, ob einige Jobs hängen. Lies weiter, um zu erfahren, wie.

## Celery

BookWyrm uses [Celery](https://docs.celeryq.dev/en/stable/) to manage background jobs.

By default this [uses gevent](https://docs.celeryq.dev/en/stable/userguide/concurrency/gevent.html) to run 1000 concurrent tasks with greenlet under a single worker. This allow for high throughput of tasks whilst restricting Celery to using a single CPU core, reducing the risk of CPU and RAM overload. If your BookWyrm instance requires more workers, you can increase this with the [`--scale`](https://docs.docker.com/reference/cli/docker/compose/up/) flag applied to the `celery_worker` service:

```sh
./bw-dev up --scale celery_worker=3
```

## Flower

Um Celery-Jobs in Echtzeit zu sehen, verwendet BookWyrm [Flower](https://flower.readthedocs.io/en/latest/).

Standardmäßig kannst du Flower-Logs unter `https://example.com/flower/` einsehen. Du wirst den Login-Namen und das Passwort aus deiner `.env`-Datei eingeben müssen. Celery kann helfen, Probleme zu beheben, die du mit deiner Aufgabenwarteschlange hast.

### Aufgaben

Wenn du wissen willst, welche Aktionen an Celery weitergegeben werden, findest du Tasks, die mit [`@app.task` annotiert wurden](https://github.com/bookwyrm-social/bookwyrm/search?q=%40app.task), im Quelltext.
