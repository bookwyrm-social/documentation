---
Title: Coda Da Monitoraggio
Date: 2022-11-23
Order: 6
---

Ci potrebbero essere eventi dove le tue istanze si comportano lentamente. Una opzione sarebbe quella di ispezionare la coda per vedere, se alcuni lavori si bloccano. Continua a leggere per capire come.

## Celery

BookWyrm sta usando [Sedery](https://docs.celeryq.dev/en/stable/) per gestire processi in background.

## Flower

Per guardare lavori di Celery in tempo reale BookWyrm utilizza [Fiore](https://flower.readthedocs.io/en/latest/).

Nel caso in cui non sia stato possibile modificare il docker-compose.yml [``](https://github.com/bookwyrm-social/bookwyrm/blob/dc14670a2ca7553317528d3384146d79df1f7413/docker-compose.yml#L87-L100) è possibile trovare il servizio su [porta 8888](https://github.com/bookwyrm-social/bookwyrm/blob/dc14670a2ca7553317528d3384146d79df1f7413/.env.example#L42-L45). Vale a dire: `https://MY_DOMAIN_NAME:8888/`.

### Compiti

Puoi trovare [`@app.task` annotati](https://github.com/bookwyrm-social/bookwyrm/search?q=%40app.task) attività nel codebase.
