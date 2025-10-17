\# 📘 Product API — Endpoints Overview



API documentation for managing Product catalogs.  

Authorization - via \*\*JWT (SimpleJWT)\*\*.  

The full interactive Swagger is available at:  

\[http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)



---



\## 🔐 Authentication



| Method | URL | Description |

|-------|-----|-----------|

| POST | `/api/token/` | Get an access token (`access` и `refresh`) |

| POST | `/api/token/refresh/` | Refresh access token |

| POST | `/api/token/verify/` | Check the validity of the token |



---



\## 🏠 ТОвары (Products)



| Method | URL | Description | Authorization |

|-------|-----|-----------|-------------|

| GET | `/api/products/` | Recieve list of Products | ❌ |

| POST | `/api/products/` | Создать obj-Product (JWT, only staff & superuser)| ✅ |

| GET | `/api/products/{id}/` | Recieve by detail | ❌ |

| PATCH | `/api/products/{id}/` | Correct (only superuser) | ✅ |

| DELETE | `/api/products/{id}/` | Delete (only superuser) | ✅ |



---



\## ⚙️ Custom actions



| Method | URL | Description | Authorization |

|-------|-----|-----------|-------------|

| POST | `/api/products/{id}/markalsdoppelt/` | Mark als double (add mask "take two" in name-fields| ✅ (only superuser) |

| POST | `/api/products/doublesdelete/` | delete marked doubles | ✅ (superuser or staff) |



---



\## 🔎 Filtration



You can filter through query-parameters:



| Patametrs | Example | Description |

|-----------|---------|----------|

| `name` | `/api/products/?name=bear` | Find by name |

| `search` | `/api/products/?search=bear` | Filter by description and name  (in name & description)|

| `price\_min` | `/api/productss/?price\_min=100000` | Min price |

| `price\_max` | `/api/productss/?price\_max=500000` | Max price |




---



\## 🧑‍💻 Example of authorization in requests



```bash

curl -H "Authorization: Bearer <access\_token>" http://127.0.0.1:8000/api/properties/

---

## ⚙️ Custom Actions

In API additional methods (actions) are implemented, accessible from ViewSet:

| Method | URL | Descriptions | Permissions |
|-------|-----|-----------|-------|
| POST | `/api/products/{id}/markalsdoppelt/` | Marks the product as a duplicate (adds “take two” in name) | Only superuser |
| DELETE | `/api/products/doublesdelete/` | Removes all objects marked as duplicates. | Staff or superuser |

> These methods can be called from Swagger UI, part **“products” → Actions**.

