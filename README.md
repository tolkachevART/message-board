# message-board

Этот проект представляет собой приложение для сайта с объявлениями. Он позволяет пользователям выкладывать свои объявления,а так же видеть отзывы к ним.

### Функционал приложения:
Авторизация и аутентификация пользователей.

Распределение ролей между пользователями (пользователь и админ).

Восстановление пароля через электронную почту.

CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).

Под каждым объявлением пользователи могут оставлять отзывы.

В заголовке сайта можно осуществлять поиск объявлений по названию.



## Установка

### Клонирование репозитория
````
https://github.com/tolkachevART/message-board.git
````
### Создание зависимостей
Установить зависимости из файла pyproject.toml
````
poetry install
````
### Настройка окружения
Скопируйте файл .env.sample в .env и заполните необходимые переменные своими данными.

## Запуск проекта

Для запуска проекта выполните следующую команду в терминале:
````
python manage.py runserver
````

### Docker
Для запуска файла в Docker:
````
docker-compose up -d --build
````
