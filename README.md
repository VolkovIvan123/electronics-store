# Магазин электроники

Проект магазина электроники на Django с элементами дизайна в стиле Pinterest.

## Функциональность

- Главная страница с популярными товарами
- Каталог товаров
- Страница "О нас"
- Страница контактов
- Pinterest-style галерея товаров

## Технологии

- Python 3.x
- Django 5.0.2
- Bootstrap 5.3
- HTML5/CSS3

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-username/electronics-store.git
cd electronics-store
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Выполните миграции:
```bash
python manage.py migrate
```

5. Запустите сервер:
```bash
python manage.py runserver
```

Сайт будет доступен по адресу: http://127.0.0.1:8000/

## Структура проекта

- `main/` - основное приложение
  - `templates/` - шаблоны страниц
  - `static/` - статические файлы (изображения, стили)
- `electronics_store/` - настройки проекта

## Автор

Ваше имя

## Лицензия

MIT 