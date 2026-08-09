- - -
Заголовок: Дозволи Дата: 18-04-2021 Припис: 2
- - -

Доступ користувача до інших функцій регулюється [вбудованою системою аутентифікації](https://docs.djangoproject.com/en/3.2/topics/auth/default/) Django. When an instance is created, the `initdb` script creates a set of permissions, which are assinged to groups. By default, all new users are assigned the `editor` group, which allows them to edit book metadata.

The instance administrator should have `superuser` status, which gives them access to Django admin (`/admin`) and confers all permissions to that user.

## Дозволи та групи
Ця таблиця демонструє чотири групи користувачів (адміністратор, модератор, редактор та користувач) та дозволи якими володіє кожна окрема група:

|                        | адміністратор | модератор | редактор | користувач |
| ---------------------- | ------------- | --------- | -------- | ---------- |
| edit instance settings | ✔️            | -         | -        | -          |
| change user level      | ✔️            | -         | -        | -          |
| manage federation      | ✔️            | ✔️        | -        | -          |
| issue invites          | ✔️            | ✔️        | -        | -          |
| deactivate users       | ✔️            | ✔️        | -        | -          |
| delete posts           | ✔️            | ✔️        | -        | -          |
| редагувати книги       | ✔️            | ✔️        | ✔️       | -          |
 завантажувати обкладинки
