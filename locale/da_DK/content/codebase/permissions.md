- - -
Titel: Tilladelser Dato: 2021-04-18 Rækkefølge: 2
- - -

Brugeradgang til forskellige funktioner styres ved hjælp af Djangos [indbyggede godkendelsessystem](https://docs.djangoproject.com/en/3.2/topics/auth/default/). Når en instans oprettes, skaber `initdb`-scriptet et sæt tilladelser, som bliver tildelt grupper. Som standard tildeles alle nye brugere `redaktør`-gruppen, som tillader dem at redigere metadata om bøger.

Administratoren for instansen skal have `superbruger`-status, hvilket giver vedkommende adgang til Django-administratorpanelet (`/admin`) og giver alle tilladelser til denne bruger.

## Tilladelser og grupper
Tabellen her viser de fire grupper (administrator, moderator, redaktør og bruger) og hvilke tilladelser, brugere i hver gruppe har:

|                                   | administrator | moderator | redaktør | bruger |
| --------------------------------- | ------------- | --------- | -------- | ------ |
| kan redigere instansindstillinger | ✔️            | -         | -        | -      |
| kan ændre brugerniveau            | ✔️            | -         | -        | -      |
| kan håndtere føderering           | ✔️            | ✔️        | -        | -      |
| kan udstede invitationer          | ✔️            | ✔️        | -        | -      |
| kan deaktivere brugere            | ✔️            | ✔️        | -        | -      |
| kan slette indlæg                 | ✔️            | ✔️        | -        | -      |
| kan redigere bøger                | ✔️            | ✔️        | ✔️       | -      |
 kan uploade omslag            |  ✔️    |     ✔️       |   ✔️     |  ✔️
