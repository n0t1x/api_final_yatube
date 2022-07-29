### Описание проекта:
Социальная сеть Yatube, с интерфейсом API. Разработка API для проекта Yatube.

### Технологии:
Python 3.7

Django 2.2.16

DjangoRestFramework 3.12.4

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:nikontra/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов API:

#### Получить JWT-токен:

Сделать POST-запрос c "username" и "password" на эндпоинт:

```
/api/v1/jwt/create/
```

#### Получить все посты:

Сделать GET-запрос на эндпоинт:

```
/api/v1/posts/
```

### Создать пост:
Авторизоваться с помощью JWT токена и сделать POST-запрос на эндпоинт

```
/api/v1/posts/
```

при этом необходимо обязательно передать поле "text" 

### Автор
Ефимов Владислав

Контакты: 
 - Email: notix@yandex.ru
