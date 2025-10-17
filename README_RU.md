# 🏠 Property API

Django REST API для управления каталогом Product.

---

## 🚀 Запуск проекта

```bash
# Клонировать репозиторий (если из архива — просто распаковать)
git clone <repo> product_api
cd product_api

# Создать и активировать виртуальное окружение
python -m venv venv
venv\Scripts\activate  # Windows
# или
source venv/bin/activate  # macOS / Linux

# Установить зависимости
pip install -r requirements.txt

# Применить миграции
python manage.py migrate (если есть файл БД "db.sqlite3" - пропустить пункт)

# Создать суперпользователя (опционально), текущий: {"login": "admin" / "psw": "admin"}
python manage.py createsuperuser (если есть файл БД "db.sqlite3" И 
	логин/пароль суперюзера - пропустить пункт)

# Запустить сервер
python manage.py runserver


📚 Документация

Swagger UI: http://127.0.0.1:8000/api/schema/swagger-ui/
OpenAPI JSON: http://127.0.0.1:8000/api/schema/
Redoc: http://127.0.0.1:8000/api/schema/redoc/

🔑 Авторизация
JWT-аутентификация через SimpleJWT
. Получение токена:

POST /api/token/
{
  "username": "admin",
  "password": "admin"
}


Использование:
Authorization: Bearer <your_access_token>

Токен живёт 60 минут.

