---
Title: Überwachungswarteschlange
Date: 2022-11-23
Order: 7
---

Es kann passieren, dass deine Instanz langsam ist. Eine Option wäre es, die Warteschlange zu inspizieren, um zu sehen, ob einige Jobs hängen. Lies weiter, um zu erfahren, wie.

## Celery

BookWyrm nutzt [Celery](https://docs.celeryq.dev/en/stable/), um Hintergrundjobs zu verwalten.

Standardmäßig [nutzt es gevent](https://docs.celeryq.dev/en/stable/userguide/concurrency/gevent.html), um 1000 nebenläufige Tasks mit greenlet auf einem einzelnen Worker auszuführen. Das erlaubt einen hohen Taks-Durchsatz, während Celery auf einen einzelnen CPU-Kern beschränkt bleibt, wodurch das Risiko einer CPU- und RAM-Überlastung verringert wird. Wenn deine BookWyrm-Instanz mehr Worker braucht, kannst du die Anzahl mit der [`--scale`](https://docs.docker.com/reference/cli/docker/compose/up/)-Flag an den Befehl zum Starten des `celery_worker`-Dienstes übergeben:

```sh
./bw-dev up --scale celery_worker=3
```

## Flower

Um Celery-Jobs in Echtzeit zu sehen, verwendet BookWyrm [Flower](https://flower.readthedocs.io/en/latest/).

Standardmäßig kannst du Flower-Logs unter `https://example.com/flower/` einsehen. Du wirst den Login-Namen und das Passwort aus deiner `.env`-Datei eingeben müssen. Celery kann helfen, Probleme zu beheben, die du mit deiner Aufgabenwarteschlange hast.

### Aufgaben

Wenn du wissen willst, welche Aktionen an Celery weitergegeben werden, findest du Tasks, die mit [`@app.task` annotiert wurden](https://github.com/bookwyrm-social/bookwyrm/search?q=%40app.task), im Quelltext.
