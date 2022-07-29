- - -
Title: Django Debug Toolbar Date: 2022-05-16 Order: 5
- - -

BookWyrm has a branch that is configured to run [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/). This branch will never get merged into `main` and has a few tweaks that make it work with the toolbar, but unsafe to use in anything resembling a production environment. To use this branch, you will need to go through a few steps to get it running.

## Nustatyti

- Naudodami git, išsičekautinkite į šaką [`debug-toolbar`](https://github.com/bookwyrm-social/bookwyrm/tree/debug-toolbar)
- Komanda `git merge main` atnaujinkite savo šaką su `main` pakeitimais. Nors šaka periodiškai atnaujinama, gali būti, kad joje nėra naujausių pakeitimų.
- Iš naujo subildinkite „Docker“, naudodami komandą `docker-compose up --build`, kad iš failo `requirements.txt` įdiegtumėte „Debug Toolbar“ biblioteką
- Pasiekite programos `puslapį` tiesiogiai (o ne per `nginx`), naudodami portą `8000`
