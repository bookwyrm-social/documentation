- - -
Title: Tillatelser Date: 2021-04-18 Order: 2
- - -

Brukertilgang til ulike funksjoner kontrolleres ved hjelp av Django sitt [innebygde autentiseringssystem](https://docs.djangoproject.com/en/3.2/topics/auth/default/). Når en instans er opprettet, vil `initdb`-skriptet opprette et sett med tillatelser, som tildeles grupper. Som standard tildeles alle nye brukere `editoren` -gruppen, hvilket tillater dem å redigere bokmetadata.

Instansadministratoren bør ha `superuser` status, som gir dem tilgang til Django admin (`/admin`), og gir alle tillatelser til den brukeren.

## Tillatelser og grupper
Denne tabellen viser de fire gruppene (admin, moderator, redaktør og bruker) og hvilke tillatelser brukere i den gruppa har:

|                              | admin | moderator | redaktører | bruker |
| ---------------------------- | ----- | --------- | ---------- | ------ |
| rediger instansinnstillinger | ✔️    | -         | -          | -      |
| endre brukernivå             | ✔️    | -         | -          | -      |
| administrere føderering      | ✔️    | ✔️        | -          | -      |
| tildele invitasjoner         | ✔️    | ✔️        | -          | -      |
| deaktivere brukere           | ✔️    | ✔️        | -          | -      |
| slette innlegg               | ✔️    | ✔️        | -          | -      |
| redigere bøker               | ✔️    | ✔️        | ✔️         | -      |
 last opp bokomslag           |  ✔️    |     ✔️       |   ✔️     |  ✔️
