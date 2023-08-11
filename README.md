## Описание проекта.
Сайт Foodgram, «Продуктовый помощник». Это онлайн-сервис и API для него. На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

Foodgram - проект позволяет:

- Просматривать рецепты
- Добавлять рецепты в избранное
- Добавлять рецепты в список покупок
- Создавать, удалять и редактировать собственные рецепты
- Скачивать список покупок

## Инструкции по установке
***- Клонируйте репозиторий:***
```
git clone git@github.com:hutji/foodgram-project-react.git
```

***- Установите и активируйте виртуальное окружение:***
- для MacOS
```
python3 -m venv venv
```
- для Windows
```
python -m venv venv
source venv/bin/activate
```
 
***- Установите зависимости из файла requirements.txt:***
```
pip install -r requirements.txt
```

***- Примените миграции:***
```
python manage.py migrate
```
***- В папке с файлом manage.py выполните команду для локального запуска:***
```
python manage.py runserver
```
***- Локально документация доступна по адресу:***
```
http://127.0.0.1/api/docs/
```

### Собираем контейнеры:

Из папки infra/ разверните контейнеры при помощи docker-compose:
```
docker-compose up -d --build
```
Выполните миграции:
```
docker-compose exec backend python manage.py migrate
```
Создайте суперпользователя:
```
docker-compose exec backend python manage.py createsuperuser
```
Соберите статику:
```
docker-compose exec backend python manage.py collectstatic
```
Наполните базу данных ингредиентами и тегами. Выполняйте команду из дериктории где находится файл manage.py:
```
docker-compose exec backend python manage.py load_data

```
Остановка проекта:
```
docker-compose down
```

## Примеры API эндпоинтов:
* ```/api/users/```  Get-запрос – получение списка пользователей. POST-запрос – регистрация нового пользователя. Доступно без токена.
 ``` json
{
            "username": "hutji",
            "email": "hutjicsgo@gmail.com",
            "id": 1,
            "first_name": "",
            "last_name": "",
            "is_subscribed": false
        }
    ]
}
```

* ```/api/users/set_password``` POST-запрос – изменение собственного пароля. Доступно авторизированным пользователям. 

* ```/api/tags/``` GET-запрос — получение списка всех тегов. Доступно без токена.
```json
[
    {
        "id": 3,
        "name": "Завтрак",
        "color": "green",
        "slug": "breakfast"
    },
```

* ```/api/ingredients/``` GET-запрос – получение списка всех ингредиентов. Подключён поиск по частичному вхождению в начале названия ингредиента. Доступно без токена.
```json
[
    {
        "id": 2188,
        "name": "ячневая крупа",
        "measurement_unit": "г"
    },
```
* ```/api/recipes/``` GET-запрос – получение списка всех рецептов. Возможен поиск рецептов по тегам и по id автора (доступно без токена). POST-запрос – добавление нового рецепта (доступно для авторизированных пользователей).
``` json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "tags": [],
            "author": {
                "username": "hutji",
                "email": "hutjicsgo@gmail.com",
                "id": 1,
                "first_name": "",
                "last_name": "",
                "is_subscribed": false
            },
            "ingredients": [
                {
                    "id": 2189,
                    "name": "сиртаки",
                    "measurement_unit": "уп",
                    "amount": 2
                },
                {
                    "id": 1278,
                    "name": "перец сладкий оранжевый",
                    "measurement_unit": "г",
                    "amount": 200
                },
                {
                    "id": 1342,
                    "name": "помидоры",
                    "measurement_unit": "г",
                    "amount": 300
                },
                {
                    "id": 1529,
                    "name": "салат листовой",
                    "measurement_unit": "г",
                    "amount": 300
                },
                {
                    "id": 975,
                    "name": "маслины",
                    "measurement_unit": "г",
                    "amount": 150
                }
            ],
            "is_favorited": false,
            "is_in_shopping_cart": false,
            "name": "Греческий салат",
            "image": "http://127.0.0.1:8000/media/recipes/image/recept_11881_7v20_HJQLPIy.jpg",
            "text": "Вкусный и простой салат",
            "cooking_time": 5
        }
    ]
}
```



## Технологии:
Python 3.9, 
Django 3.2, 
DRF, 
Nginx, 
Docker, 
PostgreSQL,
Github Actions.
