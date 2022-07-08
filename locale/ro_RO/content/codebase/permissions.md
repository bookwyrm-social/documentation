- - -
Title: Permissions Date: 2021-04-18 Order: 2
- - -

Accesul utilizatorului la diferite funcționalități este controlat folosind [sistemul de autentificare încorporat din Django](https://docs.djangoproject.com/en/3.2/topics/auth/default/). Când o instanță este creată, scriptul `initdb` creează o serie de permisiune ce sunt asociate unor grupuri. În mod implicit, toți utilizatorilor noi li se atribuie grupul `editor` care le permite să modifica metadatele cărților.

Administratorul de rețea ar trebui să aibă statutul de `super utilizator` care îi dă acces la adminul din Django (`/admin`) și lui conferă toate permisiunile.

## Permisiuni și grupuri
Acest tabel arată cele patru grupuri (admin, moderator, editor și utilizator) și ce permisiuni au utilizatorii din fiecare grup:

|                                     | admin | moderator | editor | utilizator |
| ----------------------------------- | ----- | --------- | ------ | ---------- |
| modificarea setărilor instanței     | ✔️    | -         | -      | -          |
| schimbarea nivelului utilizatorului | ✔️    | -         | -      | -          |
| gestionarea federației              | ✔️    | ✔️        | -      | -          |
| trimiterea de invitații             | ✔️    | ✔️        | -      | -          |
| dezactivarea utilizatorilor         | ✔️    | ✔️        | -      | -          |
| ștergerea postărilor                | ✔️    | ✔️        | -      | -          |
| editarea cărților                   | ✔️    | ✔️        | ✔️     | -          |
 upload covers            |  ✔️    |     ✔️       |   ✔️     |  ✔️
