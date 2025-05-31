- - -
Título: Funciones opcionales Fecha: 2021-08-02 Orden: 8
- - -

Algunas características de BookWyrm tienen que estar habilitadas para funcionar.

## Previsualización de imágenes

Por defecto, BookWyrm utiliza el logo de la instancia como una imagen de vista previa de OpenGraph. Como alternativa, puedes habilitar la generación de imágenes de vista previa para libros, usuarios y el sitio web.

Las imágenes de vista previa grandes serán redimensionadas para las imágenes de OpenGraph (utilizadas por Twitter con el nombre de `Resumy_large_image`). Dependiendo del tipo de imagen, el contenido será:

- la imagen por defecto de la instancia mostrará el logo grande junto con el nombre de la instancia y su url
- la imagen del usuario mostrará su avatar, nombre, e identificador (en forma de nombre de usuario@instancia)
- la imagen del libro mostrará su portada, título, subtítulo (si está presente), autore y valoración (si está presente)

Estas imágenes se actualizarán en varios puntos:

- imagen de la instancia: cuando se cambia el nombre de la instancia o el logotipo grande
- imagen de usuario: cuando se cambia el nombre o avatar
- imagen de libro: cuando el título, le autore o la portada son cambiados, o cuando se añade una nueva valoración

### Habilitar imágenes de vista previa

Para activar la característica con la configuración predeterminada, tienes que descomentar (eliminar la `#`) la línea `ENABLE_PREVIEW_IMAGES=true` en tu archivo `.env`. Todas las nuevas actualizaciones de eventos causarán la generación de la imagen correspondiente.

Ejemplos de estas imágenes se pueden ver en la descripción de la [solicitud de extracción](https://github.com/bookwyrm-social/bookwyrm/pull/1142#pullrequest-651683886-permalink) de la función.

### Generando vista previa

Si activas esta configuración después de que la instancia haya sido iniciada, es posible que algunas imágenes no hayan sido generadas. Se ha añadido un comando para automatizar la generación de imágenes. Con el fin de prevenir un bloqueo de recursos generando **UN MONTÓN** de imágenes, tienes que pasar el argumento `--all` (o `-a`) para iniciar la generación de imágenes de vista previa para todos los usuarios y libros. Sin este argumento, solo se generará la vista previa del sitio.

Las imágenes de vista previa del usuario y del libro se generarán de forma asincrónica: la tarea se enviará a Flower. Puede ser necesario algún tiempo antes de que todos los libros y usuarios tengan una imagen de vista previa funcional. Si tienes un buen libro 📖, un gatito 🐱 o un pastel 🍰, este es el momento perfecto para brindarles algo de atención 💖.

### Configuraciones opcionales

¿Así que quieres personalizar tus imágenes de vista previa? Aquí hay algunas opciones:

- `PREVIEW_BG_COLOR` establecerá el color del fondo de la imagen de vista previa. Puedes proporcionar un valor del color, como `#b00cc0`, o los siguientes valores: `use_dominant_color_light`, o `use_dominant_color_dark`. Estos extraerán un color dominante de la portada del libro y la utilizarán en un tema claro o oscuro, respectivamente.
- `PREVIEW_TEXT_COLOR` establecerá el color del texto. Dependiendo de la elección del color de fondo, debes encontrar un valor que tenga un contraste suficiente para que la imagen sea accesible. Se recomienda una relación de contraste de 1:4.5
- `PREVIEW_IMG_WIDTH` y `PREVIEW_IMG_HEIGHT` establecerán las dimensiones de la imagen. Actualmente, el sistema funciona mejor en imágenes con una orientación horizontal.
- `PREVIEW_DEFAULT_COVER_COLOR` establecerá el color para libros sin portadas.

Todas las variables de color aceptan valores que pueden ser reconocidos como colores por el módulo `ImageColor` de Pillow: [Aprende más sobre los nombres de colores de Pillow](https://pillow.readthedocs.io/en/stable/reference/ImageColor.html#color-names).

### Eliminar imágenes de vista previa generadas por usuarios remotos

Antes de BookWyrm 0.5.4, las imágenes de vista previa eran generadas por usuarios remotos. Al ser excesivo en términos de espacio en disco y potencia informática, esa generación se ha detenido. Si deseas eliminar todas las imágenes que se generaron previamente por usuarios remotos, se añadió un nuevo comando:

```sh
./bw-dev remove_remote_user_preview_images
```

Ese comando vaciará la propiedad `user.preview_image` en la base de datos para usuarios remotos, y eliminará el archivo en almacenamiento.
