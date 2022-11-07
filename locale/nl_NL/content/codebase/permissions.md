- - -
Titel: Permissies Datum: 2021-04-18 Bestelling: 2
- - -

Gebruikerstoegang tot verschillende functies wordt gecontroleerd met behulp van Django's [ingebouwde authenticatie systeem](https://docs.djangoproject.com/en/3.2/topics/auth/default/). Wanneer een instantie is gecreëerd, maakt het `initdb` script een set van machtigingen aan, die zijn toegewezen aan groepen. Standaard krijgen alle nieuwe gebruikers de `editor` groep toegewezen waarmee ze de metadata van het boek kunnen bewerken.

The instance administrator should have `superuser` status, which gives them access to Django admin (`/admin`) and confers all permissions to that user.

## Permissions and groups
This table shows the four groups (admin, moderator, editor, and user) and what permissions users in that group have:

|                        | admin | moderator | editor | user |
| ---------------------- | ----- | --------- | ------ | ---- |
| edit instance settings | ✔️    | -         | -      | -    |
| change user level      | ✔️    | -         | -      | -    |
| manage federation      | ✔️    | ✔️        | -      | -    |
| issue invites          | ✔️    | ✔️        | -      | -    |
| deactivate users       | ✔️    | ✔️        | -      | -    |
| delete posts           | ✔️    | ✔️        | -      | -    |
| edit books             | ✔️    | ✔️        | ✔️     | -    |
 upload covers            |  ✔️    |     ✔️       |   ✔️     |  ✔️
