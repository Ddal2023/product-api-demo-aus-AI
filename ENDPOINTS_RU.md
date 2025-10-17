\# 📘 Product API — Endpoints Overview



Документация API для управления catalog of Products.  

Авторизация — через \*\*JWT (SimpleJWT)\*\*.  

Полный интерактивный Swagger доступен по адресу:  

\[http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)



---



\## 🔐 Аутентификация



| Метод | URL | Описание |

|-------|-----|-----------|

| POST | `/api/token/` | Получить токен доступа (`access` и `refresh`) |

| POST | `/api/token/refresh/` | Обновить токен доступа |

| POST | `/api/token/verify/` | Проверить валидность токена |



---



\## 🏠 ТОвары (Products)



| Метод | URL | Описание | Авторизация |

|-------|-----|-----------|-------------|

| GET | `/api/products/` | Получить список Products | ❌ |

| POST | `/api/products/` | Создать obj-Product (JWT, only staff & superuser)| ✅ |

| GET | `/api/products/{id}/` | Получить детально | ❌ |

| PATCH | `/api/products/{id}/` | Обновить (только superuser) | ✅ |

| DELETE | `/api/products/{id}/` | Удалить (only superuser) | ✅ |



---



\## ⚙️ Кастомные действия



| Метод | URL | Описание | Авторизация |

|-------|-----|-----------|-------------|

| POST | `/api/products/{id}/markalsdoppelt/` | Mark als double (add mask "take two" in name-fields| ✅ (only superuser) |

| POST | `/api/products/doublesdelete/` | delete marked doubles | ✅ (superuser or staff) |



---



\## 🔎 Фильтрация



Можно фильтровать через query-параметры:



| Параметр | Пример | Описание |

|-----------|---------|----------|

| `name` | `/api/products/?name=bear` | Поиск по названию |

| `search` | `/api/products/?search=bear` | Фильтр по описанию И названию (in name & description)|

| `price\_min` | `/api/productss/?price\_min=100000` | Минимальная цена |

| `price\_max` | `/api/productss/?price\_max=500000` | Максимальная цена |




---



\## 🧑‍💻 Пример авторизации в запросах



```bash

curl -H "Authorization: Bearer <access\_token>" http://127.0.0.1:8000/api/properties/

---

## ⚙️ Custom Actions

В API реализованы дополнительные методы (actions), доступные из ViewSet:

| Метод | URL | Описание | Права |
|-------|-----|-----------|-------|
| POST | `/api/products/{id}/markalsdoppelt/` | Помечает товар как дубль (добавляет “take two” в название) | Только superuser |
| DELETE | `/api/products/doublesdelete/` | Удаляет все помеченные как дубль объекты | Staff или superuser |

> Эти методы можно вызывать из Swagger UI, раздел **“products” → Actions**.

