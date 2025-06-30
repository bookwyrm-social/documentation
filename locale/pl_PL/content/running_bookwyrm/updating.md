- - -
Title: Aktualizowanie instancji Date: 2022-11-17 Order: 3
- - -

Gdy w gałęzi produkcyjnej są dostępne zmiany, możesz zainstalować i uruchomić je na swojej instancji używając polecenia `./bw-dev update`. Wykonuje ono kilka rzeczy:

- `git pull` wczytuje zaktualizowany kod z repozytorium git. Jeśli wystąpią konflikty, może być konieczne wykonanie `git pull` oddzielnie i rozwiązanie konfliktów przez ponownym wypróbowaniem skryptu `./bw-dev update`.
- `docker-compose build` ponownie kompiluje obrazy, co zapewnia zainstalowanie odpowiednich pakietów. Ten krok zajmuje dużo czasu i jest wymagany tylko, gdy zależności (w tym pakiety pip z `requirements.txt`) uległy zmianie, więc możesz użyć znacznika komentarza dla szybszej ścieżki aktualizacji, a znacznik możesz usunąć w razie potrzeby.
- `docker-compose run --rm web python manage.py migrate` uruchamia migracje bazy danych w Django, używając nowo skompilowanych obrazów Docker
- `docker-compose run --rm web python manage.py collectstatic --no-input` wczytuje wszelkie zaktualizowane pliki statyczne (takie jak JavaScript i CSS)
- `docker-compose down; docker-compose up -d` ponownie uruchamia wszystkie kontenery dockera i wczytuje nowo skompilowane obrazy (Uwaga: przestoje podczas ponownego uruchamiania)

## Odbudowa strumieni aktywności

Kanały każdego użytkownika są przechowywane w bazie danych Redis. Aby ponownie wypełnić strumień, użyj polecenia zarządzania:

``` { .sh }
./bw-dev populate_streams
# Lub użyj bezpośrednio docker-compose
docker-compose run --rm web python manage.py populate_streams
```

Jeśli wystąpił jakiś przerażający błąd, dane strumienia można usunąć.

``` { .sh }
docker-compose run --rm web python manage.py erase_streams
```
