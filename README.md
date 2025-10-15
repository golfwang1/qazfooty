# QazFooty — Django-проект

## Установка
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Зайдите на http://127.0.0.1:8000/ — увидите главную.
Админка: http://127.0.0.1:8000/admin/

## Добавление клубов (Кайрат, Актобе)
1) В админке создайте клубы: "Кайрат", "Актобе"
2) Заполните титулы и логотипы
3) Добавьте игроков через связанную модель Player

## Замена фонового изображения
Положите свой файл в `static/img/bg.jpg` и в нужном CSS укажите:
```css
body { background: url('/static/img/bg.jpg') center/cover no-repeat fixed; }
```
Либо замените inline-стили в шаблоне `base.html` на ваш путь через `{% static 'img/ВАШ_ФАЙЛ' %}`.

## Деплой на Render
1) Commit & push в GitHub
2) На Render создайте Web Service, укажите:
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start Command: `gunicorn qazfooty.wsgi:application`
3) Переменные окружения: `DEBUG=False`, `ALLOWED_HOSTS=ваш_домен,ваш-сабдомен.onrender.com`
4) Подключите домен (например, `qazfooty.kz`)

## API (простая заготовка)
Вы можете быстро сделать endpoints через Django REST Framework, но это за пределами стартера.
