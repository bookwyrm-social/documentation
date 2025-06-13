- - -
Izenburua: Baimenak Eguna: 2021-04-18 Ordena: 2
- - -

Erabiltzailearen hainbat ezaugarritarako sarbidea Djangoko [autentifikazio-sistema integratuaren](https://docs.djangoproject.com/en/3.2/topics/auth/default/) bidez kontrolatzen da. Instantzia bat sortzen denean, `initdb` sriptak taldeei esleitutako baimen sorta bat sortzen du. Lehenespenez, erabiltzaile berri guztiak `editor` taldeari esleitzen dira eta horrela liburuaren metadatuak aldatzeko eskubidea dute.

Administrazio instantziak `superuser` estatusa izan behar du. Horrek Djangoren administraziorako sarbidea (`/admin`) ematen dio eta erabiltzaile horri baimen guztiak ematen dizkio.

## Baimenak eta taldeak
Taula honek lau taldeak erakusten ditu (administratzailea, moderatzailea, editorea eta erabiltzailea) eta talde horien erabiltzaileei dagozkien baimenak:

|                                   | administratzailea | moderatzailea | editorea | erabiltzailea |
| --------------------------------- | ----------------- | ------------- | -------- | ------------- |
| instantziaren ezarpenak aldatzea  | ✔️                | -             | -        | -             |
| erabiltzaile baten maila aldatzea | ✔️                | -             | -        | -             |
| federazioa kudeatzea              | ✔️                | ✔️            | -        | -             |
| gonbidapenak sortzea              | ✔️                | ✔️            | -        | -             |
| erabiltzaileak deskaktibatzea     | ✔️                | ✔️            | -        | -             |
| mezuak ezabatzea                  | ✔️                | ✔️            | -        | -             |
| liburuak editatzea                | ✔️                | ✔️            | ✔️       | -             |
 azalak linean ezartzea            |  ✔️    |     ✔️       |   ✔️     |  ✔️
