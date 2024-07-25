#!/bin/sh

# Выполняем миграции
python manage.py migrate
python manage.py collectstatic --noinput

# Загружаем фикстуры
python manage.py loaddata fixtures/Menu.json
python manage.py loaddata fixtures/Category.json
python manage.py loaddata fixtures/MenuItem.json

# Запускаем сервер
exec python manage.py runserver 0.0.0.0:8000