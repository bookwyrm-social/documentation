---
Title: Overvåkningskø
Date: 2022-11-23
Order: 6
---

Det kan forekomme tilfeller hvor instansene dine oppfører seg treigt. Et alternativ vil være å inspisere køen for å se hvirvidt noen jobber henger. Les videre for å lære hvordan.

## Celery

BookWyrm bruker [Celery](https://docs.celeryq.dev/en/stable/) til å styre bakgrunnsjobber.

## Flower

For å se på Celery-jobber i sanntid bruker BookWyrm [Flower](https://flower.readthedocs.io/en/latest/).

Om du ikke har justert [`docker-compose.yml`](https://github.com/bookwyrm-social/bookwyrm/blob/dc14670a2ca7553317528d3384146d79df1f7413/docker-compose.yml#L87-L100) finner du tjenesten på [port 8888](https://github.com/bookwyrm-social/bookwyrm/blob/dc14670a2ca7553317528d3384146d79df1f7413/.env.example#L42-L45). Det vil si: `https://MITT_DOMENENAVN:8888/`.

### Oppgaver

Du kan finne [`@app.task`-annoterte oppgaver](https://github.com/bookwyrm-social/bookwyrm/search?q=%40app.task) i kodebasen.
