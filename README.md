# API FINAL YATUBE
api_final_yatube - учебный проект ЯП - API к социальной сети Yatube
***
## Возможности:
* Создание постов
* Создание комменатриев к постам
* Подписка на автора поста
* Аутентификация по JWT-токену с помощью либы Simple JWT
***
## Как запустить проект:
Клонировать репозиторий и перейти в него:

```
git clone https://github.com/WeiGOooo/api_final_yatube.git && cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
URL проекта: http://127.0.0.1:8000

Документация: http://127.0.0.1:8000/redoc/
***
## Пример API
Метод создания комментария к посту:
<br>POST http://127.0.0.1:8000/api/v1/posts/14/comments/
```json
{
    "text": "тест тест",
}
```
Пример ответа:
```json
{
    "id": 4,
    "author": "anton",
    "post": 14,
    "text": "тест тест",
    "created": "2021-06-01T10:14:51.388932Z"
} 
```
