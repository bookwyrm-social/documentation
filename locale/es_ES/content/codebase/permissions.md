- - -
Título: Permisos Fecha: 18-04-2021 Pedido: 2
- - -

El acceso del usuario a diferentes características se controla usando el [sistema de autenticación integrado](https://docs.djangoproject.com/en/3.2/topics/auth/default/) de Django. Cuando se crea una instancia, el script `initdb` crea un conjunto de permisos, que son asignados a grupos. De manera predeterminada, a les nueves usuaries se les asigna el grupo `editore`, lo que les permite editar los metadatos de los libros.

Le administradore de la instancia debe tener el estatus de `superusuarie`, lo que le da acceso a la administración (`/admin`) y le otorga todos los permisos.

## Permisos y grupos
La siguiente tabla muestra los cuatro grupos (administradore, moderadore, editore y usuarie):

|                                   | administradore | moderadore | editore | usuarie |
| --------------------------------- | -------------- | ---------- | ------- | ------- |
| editar configuración de instancia | ✔️             | -          | -       | -       |
| cambiar nivel de usuarie          | ✔️             | -          | -       | -       |
| administrar federación            | ✔️             | ✔️         | -       | -       |
| enviar invitaciones               | ✔️             | ✔️         | -       | -       |
| desactivar usuaries               | ✔️             | ✔️         | -       | -       |
| eliminar publicaciones            | ✔️             | ✔️         | -       | -       |
| editar libros                     | ✔️             | ✔️         | ✔️      | -       |
 subir portadas            |  ✔️    |     ✔️       |   ✔️     |  ✔️
