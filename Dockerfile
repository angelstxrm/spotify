# Используйте конкретную версию Python
FROM python:3.11-slim

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файл зависимостей и установите их
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Скопируйте весь исходный код в рабочую директорию
COPY . .

# Определите команду запуска контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]