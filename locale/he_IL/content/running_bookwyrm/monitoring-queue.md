---
Title: תור ניטור
Date: 23-11-2022
Order: 6
---

ייתכנו מקרים בהם המופעים שלך יתנהגו באיטיות יותר. אפשרות אחת תהיה לבדוק את התור כדי לראות אם חלק מהעבודות תקועות. יש לקרוא כדי ללמוד איך.

## Celery

BookWyrm משתמש ב-[Celery](https://docs.celeryq.dev/en/stable/) כדי לנהל את העבודות ברקע.

## Flower

To watch Celery jobs in real-time BookWyrm uses [Flower](https://flower.readthedocs.io/en/latest/).

In case you haven't tweaked the [`docker-compose.yml`](https://github.com/bookwyrm-social/bookwyrm/blob/dc14670a2ca7553317528d3384146d79df1f7413/docker-compose.yml#L87-L100) you can find the service on [port 8888](https://github.com/bookwyrm-social/bookwyrm/blob/dc14670a2ca7553317528d3384146d79df1f7413/.env.example#L42-L45). That is: `https://MY_DOMAIN_NAME:8888/`.

### Tasks

You can find [`@app.task` annotated](https://github.com/bookwyrm-social/bookwyrm/search?q=%40app.task) tasks in the codebase.
