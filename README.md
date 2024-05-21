coursework_7 DRF

Бэкенд-часть SPA веб-приложения "Трекер полезных привычек".

Технологии:
- python 3.12
- PostgreSQL
- Redis

Используемые библиотеки:
- celery;
- Django;
- django-celery-beat;
- djangorestframework;
- djangorestframework-simplejwt;
- drf-yasg;
- pillow;
- psycopg2-binary;
- python-crontab;
- python-dotenv;
- redis;
- requests;
- django-cors-headers.


Инструкция для развертывания проекта:
1. Клонировать проект

https://github.com/AlinaMordovina/habits.git

2. Создать виртуальное окружения

Находясь в директории проекта запустить в терминале команды:

python -m venv venv

source venv/bin/activate

3. Установить зависимости

Все зависимости указаны в файле requirements.txt

Для установки всех зависимостей из файла необходимо запустить в терминале команду:

pip install -r requirements.txt

4. Cоздать базу данных

Для создания базы данных необходимо запустить в терминале команду:

CREATE DATABASE DATABASE_NAME

5. Применить миграции 

Для создания и применения миграций необходимо запустить в терминале команды:

python3 manage.py makemigrations
python3 manage.py migrate

6. Заполнить файл .env по образцу .env.sample
7. Для создания суперпользователя необходимо применить команду "python manage.py csu"
8. Для запуска проекта использовать команду "python manage.py runserver", либо через конфигурационные настройки PyCharm.
9. Для подключения бота в Телеграм перейти по ссылке t.me/lina_habbit_bot
10. Для запуска периодических задач необходимо применить команду "celery -A config worker --beat --scheduler django --loglevel=info
"
11. Посмотреть документацию API:
- Swagger http://127.0.0.1:8000/docs/
- Redoc http://127.0.0.1:8000/redoc/







Автор проекта: Мордовина Алина