ToDo List Project

Описание

Проект представляет собой веб-приложение для управления списком задач (ToDo List). Реализовано с использованием Django, PostgreSQL, Redis и Docker.

Стек технологий

Backend: Django, Django REST Framework

Database: PostgreSQL

Containerization: Docker, Docker Compose

Bot: Python-бот для автоматизации задач

Установка и запуск

1. Клонирование репозитория

git clone https://github.com/nikita-szr/ToDo_list_project/tree/feature_1
cd todo-list-project

2. Настройка окружения

Создайте .env файл и укажите переменные окружения:

.env.sample

3. Запуск через Docker

Соберите и запустите контейнеры:

docker-compose up --build

После успешного запуска приложение будет доступно по адресу: http://localhost:8000.

4. Применение миграций и создание суперпользователя

docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

5. Запуск бота

docker-compose exec bot python bot/bot.py

API

Приложение предоставляет REST API для управления задачами. Документация доступна по адресу:
http://localhost:8000/api/docs/

Основные команды

Запуск локального сервера:

docker-compose up

Остановка контейнеров:

docker-compose down

Очистка данных и пересборка:

docker-compose down -v
docker-compose up --build
