- - -
Title: Środowisko programistyczne Date: 2021-04-12 Order: 3
- - -

## Wymagania wstępne

Te instrukcje zakładają, że rozwijasz BookWyrm przy użyciu Docker. Aby rozpocząć, należy [zainstalować Docker](https://docs.docker.com/engine/install/) i [docker-compose](https://docs.docker.com/compose/install/).

## Konfigurowanie środowiska programistycznego

- Uzyskaj kopię [kodu BookWyrm z GitHub](https://github.com/bookwyrm-social/bookwyrm). Możesz [zduplikować](https://docs.github.com/en/get-started/quickstart/fork-a-repo) repozytorium, a następnie [użyć `git clone`, aby pobrać kod](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) na swój komputer.
- Katalog, na którym znajduje się kod na Twoim komputerze to miejsce, z którego od teraz będziesz pracować.
- Skonfiguruj plik zmiennych środowiskowych swojego środowiska programistycznego kopiując przykładowy plik (`.env.example`) do nowego pliku o nazwie `.env`. W wierszu polecenia można to zrobić następująco:
``` { .sh }
cp .env.example .env
```
- W pliku `.env` zmień `DEBUG` na `true`
- Jeśli chcesz, możesz skorzystać z usług, takich jak [ngrok](https://ngrok.com/), aby skonfigurować nazwę domeny oraz ustawić zmienną `DOMAIN` w swoim pliku `.env` dla nazwy domeny wygenerowanej przez ngrok.

- Skonfiguruj nginx w celu programowania kopiując plik konfiguracyjny nginx (`nginx/development`) do nowego pliku o nazwie `nginx/default.conf`:
``` { .sh }
cp nginx/development nginx/default.conf
```

- Uruchom aplikację. W wierszu polecenia wykonaj:
``` { .sh }
./bw-dev build            # Kompiluje obraz docker
./bw-dev setup            # Inicjuje bazę danych i uruchamia migracje
./bw-dev up               # Uruchamia kontenery docker
```
- Po zakończeniu kompilacji możesz uzyskać dostęp pod `ttp://localhost:1333` i utworzyć konto administratora.

Dla ciekawskich: polecenie `./bw-dev` to prosty skrypt uruchamiający wiele różnych narzędzi: powyżej możesz pominąć je i wykonać `docker-compose build` lub `docker-compose up` bezpośrednio, jeśli chcesz. `./bw-dev` po prostu gromadzi je wszystkie w jednym miejscu. Uruchom polecenia bez argumentów, aby uzyskać listę dostępnych poleceń, odczytać [stronę dokumentacji](/command-line-tool.html) dla niego lub otwórz ją i rozejrzyj się, aby sprawdzić, co dokładnie robi dane polecenie!

### Edytowanie lub tworzenie modeli

Zmieniając lub tworząc model prawdopodobnie ulegnie zmianie struktura bazy danych. Aby te zmiany zostały zastosowane, należy uruchomić polecenie Django `makemigrations`, aby utworzyć nowy [plik migracji Django](https://docs.djangoproject.com/en/3.2/topics/migrations), a następnie przenieść go (`migrate`):

``` { .sh }
./bw-dev makemigrations
./bw-dev migrate
```

### Edytowanie plików statycznych
Za każdym razem, gdy edytujesz CSS lub JavaScript, należy ponownie uruchomić polecenie Django `collectstatic`, aby miany zostały zastosowane:
``` { .sh }
./bw-dev collectstatic
```

Jeśli [zainstalowano yarn](https://yarnpkg.com/getting-started/install), możesz wykonać `yarn watch:static`, aby automatycznie wykonać poprzedni skrypt za każdym razem, gdy zajdzie zmiana w katalogu `bookwyrm/static`.
