- - -
Título: Django Debug Toolbar Fecha: 2022-05-16 Orden: 5
- - -

BookWyrm tiene una rama configurada para ejecutar [Barra de Herramientas de Depuración de Django](https://django-debug-toolbar.readthedocs.io/en/latest/). Esta rama nunca se fusionará en `main` y tiene algunos ajustes que funcionan con la barra de herramientas, aunque no es segura para usar en algo parecido a un entorno de producción. Para usar esta rama, necesitarás pasar por unos pocos pasos para ponerla en marcha.

## Configuración

- Usando git, revisa la rama [`debug-toolbar`](https://github.com/bookwyrm-social/bookwyrm/tree/debug-toolbar).
- Actualiza la rama relativa a `main` usando `git merge main`. La rama se actualiza periódicamente pero probablemente esté por detrás de la última.
- Recompilar las imágenes Docker usando `docker-compose up --build` para asegurar que la biblioteca de la barra de depuración esté instalada desde `requirements.txt`.
- Acceder a la aplicación web directamente usando `web` (en lugar de `nginx`) usando el puerto `8000`.
