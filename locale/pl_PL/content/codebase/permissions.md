- - -
Title: Uprawnienia Date: 2021-04-18 Order: 2
- - -

Dostęp użytkowników do różnych funkcji jest kontrolowany przez [wbudowany system uwierzytelniania](https://docs.djangoproject.com/en/3.2/topics/auth/default/) Django. Gdy zostaje utworzona instancja, skrypt `initdb` tworzy zestaw uprawnień, które są przypisywane do grup. Domyślnie wszyscy nowi użytkownicy zostają przypisani do grupy `edytor`, co umożliwia im edytowanie metadanych książek.

Administrator instancji powinien mieć status `superużytkownik`, co daje mu dostęp do panelu administracyjnego Django (`/admin`) oraz przyznaje mu wszystkie uprawnienia.

## Uprawnienia i grupy
Ta tabela zawiera cztery grupy (administrator, moderator, edytor oraz użytkownik) oraz uprawnienia użytkowników w tych grupach:

|                               | administrator | moderator | edytor | użytkownik |
| ----------------------------- | ------------- | --------- | ------ | ---------- |
| edytowanie ustawień instancji | ✔️            | -         | -      | -          |
| zmiana poziomu użytkownika    | ✔️            | -         | -      | -          |
| zarządzanie federacją         | ✔️            | ✔️        | -      | -          |
| wysyłanie zaproszeń           | ✔️            | ✔️        | -      | -          |
| dezaktywacja użytkowników     | ✔️            | ✔️        | -      | -          |
| usuwanie wpisów               | ✔️            | ✔️        | -      | -          |
| edytowanie książek            | ✔️            | ✔️        | ✔️     | -          |
 przesyłanie okładek            |  ✔️    |     ✔️       |   ✔️     |  ✔️
