# Используем официальный Python-образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё содержимое проекта
COPY . .

# Создаем папку для статики
RUN [ ! -d "staticfiles" ] && mkdir staticfiles || echo "Directory staticfiles already exists"

# Собираем статику (после настройки STATIC_ROOT)
RUN python manage.py collectstatic --noinput

# Открываем порт 8000 для приложения
EXPOSE 8000

# Запуск сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
