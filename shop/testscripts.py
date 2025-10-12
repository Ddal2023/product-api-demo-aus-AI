import requests, json

# def user_post():
#     auth = ("admin", 'admin')  # - normaler User
#     data = {
#         "username": "Ustas", "password": "ford2007"}
#     data = {
#         # "username": "Alex", "password": "ford2007", "staffstatus": True, "email": "alex@shop.com"}
#         "staffstatus": True, "email": "alex@shops.com"}
#     url = f"http://127.0.0.1:8000/users/3/"
#     resp = requests.patch(url, auth=auth, data = data)
#     print('response-code fur POST-request:', resp.status_code)
#     print(resp.json())
#
# user_post()

#add new Product
def product_post(data = {}, auth=()):
    # data = {
    #     "name": "Хрін Верес білий гострий 130г",
    #     "description": "Класичний хрін, дрібно натертий та швидко законсервований, аби не втратити важливої гостроти. "
    #         "Саме такий соус готує «Верес», щоб господарки могли ставити його на стіл у якості доповнення до м׳ясних страв.",
    #     "price": "25.25",}  #грн

    # auth = ("admin", 'admin')  # - normaler User
    # auth = ("Ustas", 'ford2007')  # - normaler User

    # resp = requests.delete(url, auth=auth)
    # id = 5
    url = f"http://127.0.0.1:8000/products/"
    resp = requests.post(url, auth=auth, data = data)
    print('response-code fur POST-request:', resp.status_code)
    # try:
    print(resp.json())
    # except:
    #     print(resp.text)

def product_get():
    auth = ("admin", 'admin')  # - normaler User
    auth = ("Ustas", 'ford2007')  # - normaler User
    # resp = requests.delete(url, auth=auth)
    url = f"http://127.0.0.1:8000/products/"
    resp = requests.get(url, auth=auth)
    print('response-code fur POST-request:', resp.status_code)
    # try:
    print(resp.json())
    # except:
    #     print(resp.text)

def product_patch_als_double(id = 0):
    auth = ("admin", 'admin')  # - normaler User
    auth = ("Ustas", 'ford2007')  # - normaler User
    # resp = requests.delete(url, auth=auth)

    url = f"http://127.0.0.1:8000/products/{id}/"
    resp = requests.get(url, auth=auth)
    if resp.status_code >= 400:
        print(f'not finded product wih id {id} ; cancel PATCH-operation ')
        return

    r = resp.json()
    print('response-code fur GET/id/-request:', resp.status_code)
    print('recieved product:', r)

    if not r['name'].find('take two')==-1:
        print(f'product {r['name']} schon marked als "take two"; cancel PATCH-operation ')
        return

    #marked produkt als double
    data = {
        "name": "take two " + r['name'], "description": "take two " + r['description'], 'price': float(r['price'])*2 }
    resp = requests.patch(url, auth=auth, data=data)
    print('response-code fur PATCH-request:', resp.status_code)
    # try:
    print('korrekted product is:', resp.json())
    # except:
    #     print(resp.text)

def product_delete(id = 0, auth = ("Ustas", 'ford2007') ):
    auth = ("admin", 'admin')  # - normaler User
    auth = ("Ustas", 'ford2007')  # - normaler User

    url = f"http://127.0.0.1:8000/products/{id}/"
    resp = requests.get(url, auth=auth)
    if resp.status_code >= 400:
        print(f'not finded product wih id {id} ; cancel DELETE-operation.... status_code {resp.status_code} ')
        return
    resp = requests.delete(url, auth=auth)
    r = resp.json()
    print('response-code fur DELETE/id/-request:', resp.status_code)
    # print('DELETED product:', r, 'user:', requests.user)
    try:
        print('DELETED product:', r, 'user:', requests.user)
    except:
        print('DELETED product:', r)


def recieve_jwt(auth=(None, None)):
    AUTH_URL = "http://127.0.0.1:8000/api/token/"
    data = {"username": "admin", "password": "admin"}
    data = {"username": auth[0], "password": auth[1]}
    # получаем токен
    resp = requests.post(AUTH_URL, data=data)
    tokens = resp.json()
    if not resp.ok:
        print(f'неудачная попытка получения токена доступа! причина {resp.reason} ')
        return {'status_code': resp.status_code, 'token': None}
    access_token = tokens['access']  # if resp.ok==False: resp.reason
    print(f'token ist {access_token}')
    return {'status_code': resp.status_code, 'token': access_token}

def product_jwt_get():
    auth = ("admin", 'admin')  # - normaler User
    auth = ("Ustas", 'ford2007')  # - normaler User
    # resp = requests.delete(url, auth=auth)

    daten_jwt = recieve_jwt(auth)
    if daten_jwt['token']==None:
        print('token nicht available, daten export nicht machen')
        return

    # заголовки с токеном
    HEADERS = {"Authorization": f"Bearer {daten_jwt['token']}"}
    API_URL = f"http://127.0.0.1:8000/products/"
    API_URL = f"http://127.0.0.1:8000/products/?price_min=100"
    # GET запрос с токеном
    resp = requests.get(f"{API_URL}", headers=HEADERS)

    # url = f"http://127.0.0.1:8000/products/"
    # resp = requests.get(url, auth=auth)
    print('response-code fur GET-request:', resp.status_code)
    try:
        print(resp.json())
    except:
        print(resp.text)


# product_post()
# product_get()
#product_patch_als_double(2)
# product_delete(13)
#
data = {
    "name": "Хрін Верес білий гострий 130г",
    "description": "Класичний хрін, дрібно натертий та швидко законсервований, аби не втратити важливої гостроти. "
        "Саме такий соус готує «Верес», щоб господарки могли ставити його на стіл у якості доповнення до м׳ясних страв.",
    "price": "25.25",}  #грн
auth = ("Ustas", 'ford2007')  # - normaler User
auth = ("admin", 'admin')  # - normaler User

# product_post(data, auth)
# product_delete(16, auth)
product_jwt_get()


