- - -
Títol: Permisos Data: 2021-04-18 Ordre: 2
- - -

L'accés de l'usuari a les diferents funcionalitats és controlat mitjançant el [sistema d'autenticació](https://docs.djangoproject.com/en/3.2/topics/auth/default/) de Django. Quan es crea una instància, l'script `initdb` crea una sèrie de permisos, els quals són assignats a grups. Per defecte, tots els usuaris nous són assignats al grup `editor` , el qual els hi permet editar les metadades dels llibres.

La instància d'administrador ha de disposar de l'estat `superusuari` , el qual li dona accés a l'administració de Django (`/admin`) i li otorga tots els permisos a l'usuari.

## Permisos i grups
Aquesta taula mostra els quatre grups (administrador, moderador, editor i usuari) i quins permisos tenen els usuaris en aquell grup:

|                                        | administrador | moderador | editor | usuari |
| -------------------------------------- | ------------- | --------- | ------ | ------ |
| editar la configuració de la instància | ✔️            | -         | -      | -      |
| modificar el nivell de l'usuari        | ✔️            | -         | -      | -      |
| gestionar federació                    | ✔️            | ✔️        | -      | -      |
| convidar                               | ✔️            | ✔️        | -      | -      |
| desactivar usuaris                     | ✔️            | ✔️        | -      | -      |
| eliminar publicacions                  | ✔️            | ✔️        | -      | -      |
| editar llibres                         | ✔️            | ✔️        | ✔️     | -      |
 pujar portades            |  ✔️    |     ✔️       |   ✔️     |  ✔️
