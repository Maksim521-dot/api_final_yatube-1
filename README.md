# api_final
api final
### Как запустить проект:

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
