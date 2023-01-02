- - -
Titel: Permissies Datum: 2021-04-18 Bestelling: 2
- - -

Gebruikerstoegang tot verschillende functies wordt gecontroleerd met behulp van Django's [ingebouwde authenticatie systeem](https://docs.djangoproject.com/en/3.2/topics/auth/default/). Wanneer een instantie is gecreëerd, maakt het `initdb` script een set van machtigingen aan, die zijn toegewezen aan groepen. Standaard krijgen alle nieuwe gebruikers de `editor` groep toegewezen waarmee ze de metadata van het boek kunnen bewerken.

De instantie administrator moet de status van `supergebruiker` hebben waarmee ze toegang krijgen tot Django beheerder (`/admin`) en alle rechten toe-eigent aan die gebruiker.

## Machtigingen en groepen
Deze tabel toont de vier groepen (admin, moderator, editor en gebruiker) en welke rechten gebruikers in de betreffende groep hebben:

|                                 | beheerder | bemiddelaar | redacteur | gebruiker |
| ------------------------------- | --------- | ----------- | --------- | --------- |
| instantie instellingen bewerken | ✔️        | -           | -         | -         |
| verander gebruikersniveau       | ✔️        | -           | -         | -         |
| federatie beheren               | ✔️        | ✔️          | -         | -         |
| uitnodigingen uitgeven          | ✔️        | ✔️          | -         | -         |
| gebruikers deactiveren          | ✔️        | ✔️          | -         | -         |
| berichten verwijderen           | ✔️        | ✔️          | -         | -         |
| boeken bewerken                 | ✔️        | ✔️          | ✔️        | -         |
 boekomslagen uploaden            |  ✔️    |     ✔️       |   ✔️     |  ✔️
