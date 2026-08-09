- - -
Заголовок: Django Debug Toolbar Дата: 16-05-2022 Припис: 5
- - -

BookWyrm має команду переходу, яка запрограмована керувати [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/). Ця команда ніколи не об'єднається з `основною` і має кілька твікерів, які уможливлюють роботу з панеллю інструментів, але не є безпечним для використання у будь-чому схожому на виробниче середовище.  To use this branch, you will need to go through a few steps to get it running.

## Налаштування

- Використовуючи GitHub, перевірте команду переходу [`debug-toolbar`](https://github.com/bookwyrm-social/bookwyrm/tree/debug-toolbar)
- Оновіть команду відносно  `основної` використовуючи `git merge main`. Команда оновлюється періодично, але можливі затримки.
- Re-build the Docker images using `docker-compose up --build` to ensure that the Debug Toolbar library is installed from `requirements.txt`
- Access the application `web` image directly (instead of via `nginx`) using port `8000`
