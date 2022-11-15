---
Title: Monitoring Queue
Date: 2022-11-23
Order: 6
---

Es kann passieren, dass Ihre Instanz langsam ist. Eine Option wäre die Warteschlange zu inspizieren, um zu sehen, ob einige Jobs hängen. Lesen Sie weiter, um zu erfahren, wie.

## Celery

BookWyrm verwendet [Celery](https://docs.celeryq.dev/en/stable/) um Hintergrundjobs zu verwalten.

## Flower

Um Celery-Jobs in Echtzeit zu sehen, verwendet BookWyrm [Flower](https://flower.readthedocs.io/en/latest/).

Falls Sie das [`Docker-compose.yml nicht geändert haben`](https://github.com/bookwyrm-social/bookwyrm/blob/dc14670a2ca7553317528d3384146d79df1f7413/docker-compose.yml#L87-L100) finden Sie den Service auf [Port 8888](https://github.com/bookwyrm-social/bookwyrm/blob/dc14670a2ca7553317528d3384146d79df1f7413/.env.example#L42-L45). Das ist: `https://MY_DOMAIN_NAME:8888/`.

### Aufgaben

Sie finden unter [`@app.task` kommentiert](https://github.com/bookwyrm-social/bookwyrm/search?q=%40app.task) Aufgaben in der Codebase.
