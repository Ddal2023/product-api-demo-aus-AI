# 🏠 Property API

Django REST API для управления каталогом Product.

---

## 🚀 Project launch

```bash
# Clone the repository (if from an archive, just unzip it)
git clone <repo> product_api
cd product_api

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# или
source venv/bin/activate  # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate (If there is a database file "db.sqlite3" - skip this step)

# Create a superuser (optional), current: {"login": "admin" / "psw": "admin"}
python manage.py createsuperuser (If there is a database file "db.sqlite3" - skip this step)

# run Server
python manage.py runserver


📚 Documentation

Swagger UI: http://127.0.0.1:8000/api/schema/swagger-ui/
OpenAPI JSON: http://127.0.0.1:8000/api/schema/
Redoc: http://127.0.0.1:8000/api/schema/redoc/

🔑 Authorization
JWT-authentication via SimpleJWT
. Obtaining a token:

POST /api/token/
{
  "username": "admin",
  "password": "admin"
}


Usage:
Authorization: Bearer <your_access_token>

The token lives for 60 minutes.

