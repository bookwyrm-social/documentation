- - -
Izenburua: Django Debug Toolbar Eguna: 2022-05-16 Ordena: 5
- - -

BookWyrm-ek adar konfiguratu bat dauka [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) exekutatzeko. Adar hori ez da inoiz `main`-ean fusionatuko eta baditu zenbait hobekuntza, tresna-barrarekin funtzionarazten dutenak, baina arriskutsuak dira produkzioan bertan edo handik gertu dagoen ingurunean erabiltzeko. Adar hori erabiltzeko, urrats batzuetatik pasa beharko zara funtzionarazteko.

## Konfigurazioa

- Git erabiliz, jarri tresna-barrako [`debug-toolbar`](https://github.com/bookwyrm-social/bookwyrm/tree/debug-toolbar) adarrean
- Adarra eguneratu `main`-etik `git merge main` erabiliz. Adarra eguneratua da aldian behin, baina azken bertsioari begira berantean izanen da ziur aski.
- Berreraiki Docker irudiak `docker-compose up --build` erabiliz Debug Toolbar lib-a instalatu dela `requirements.txt`-etik
- Aplikazion sartu `web` irudiaren bidez zuzenki (`nginx` bidez sartu ordez) `8000` ataka erabiliz
