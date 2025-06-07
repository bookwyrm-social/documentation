- - -
Título: Actualizando tu instancia Fecha: 2022-11-17 Orden: 3
- - -

Cuando hay actualizaciones disponibles en la rama de producción, puedes instalarla y correrla en tu instancia usando el comando `./bw-dev update`. Esto produce una serie de cosas:

- `git pull` toma el código actualizado del repositorio git. Si hay problemas, puedes correr `git pull` por separado y resolver los conflictos intentando `./bw-dev update` nuevamente.
- `docker-compose build` reconstruye las imágenes, lo que asegura que sean instalados los paquetes correctos. Este paso puede tomar un tiempo y solo es necesario cuando las dependencias (incluyendo los paquetes de pip `requirements.txt`) han cambiado, así que puedes comentar si quieres una actualización más rápida y no importa descomentar si es necesario.
- `docker-compose run --rm web python manage.py migrate` corre las migraciones de la base de datos en Django usando las imágenes Docker recién construidas.
- `docker-compose run --rm web python manage.py collectstatic --no-input` carga cualquier archivo estático actualizado (como JavaScript y CSS).
- `docker-compose down; docker-compose up -d` reiniciará todos los contenedores docker y usará las imágenes recién construidas (Atención: tiempo de inactividad durante el reinicio).

## Reconstruir streams de actividad

Las fuentes de cada usuario se almacena en Redis. Para rellenar un stream, utilice el comando de gestión:

``` { .sh }
./bw-dev populate_streams
# O usa docker-compose directamente
docker-compose run --rm web python manage.py populate_streams
```

Si algo ocurrió mal, los datos pueden ser eliminados.

``` { .sh }
docker-compose run --rm web python manage.py erase_streams
```
