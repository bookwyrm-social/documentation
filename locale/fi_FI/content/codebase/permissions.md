- - -
Title: Luvat Date: 2021-04-18 Order: 2
- - -

User access to different features is controlled using Django's [built-in authentication system](https://docs.djangoproject.com/en/3.2/topics/auth/default/). When an instance is created, the `initdb` script creates a set of permissions, which are assinged to groups. By default, all new users are assigned the `editor` group, which allows them to edit book metadata.

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
