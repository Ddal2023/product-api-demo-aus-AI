from rest_framework import permissions

class CustomPermissions(permissions.BasePermission):
    """
    все могут читать все
    Staff может ++ вводить новые, но НЕ редактировать и НЕ удалять
    Разрешает редактировать, удаля, вводить новый толькосуперпользователю.
    """

    # В has_object_permission можно добавить логику под кастомное действие:
    def has_object_permission(self, request, view, obj):
        print(
        f"[DEBUG] has_object_permission: {request.method} {view.action if hasattr(view, 'action') else ''} for obj={obj}")
        # # Разрешаем вообще только аутентифицированным
        # return request.user and request.user.is_authenticated

        # 🔹 Чтение разрешено всем (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # 🔹 Superuser может всё
        if request.user and request.user.is_superuser:
            return True

        # add проверки... for permissions
        #castom endpoint:
        if view.action == "doublesdelete" and request.method == "DELETE":
            # staff может запускать проверку-удаление на дубли , отмаркированные
            print(
            f"[DEBUG_doublesdelete]:has_object_permission: {request.method} {view.action if hasattr(view, 'action') else ''} for obj={obj}")
            return request.user.is_staff

        # # запреты на методы: POST метод на создание объекта срабатывает, когда объекта то еще и нет... нужно в "def has_permission("
        # if request.method == "POST" :
        #     # staff может добавлять записи Product
        #     print('разрещение на POST-request is', (request.user.is_staff or request.user.is_superuser),
        #           'разрешенные методы:', permissions.SAFE_METHODS)
        #     return (request.user.is_staff or request.user.is_superuser)

        #редактировать и удалять записи может ТОЛЬКО суперюзер!
        if (request.method == "POST" or request.method == "DELETE" or request.method == "PUT"
                or request.method == "PATCH"):
            return request.user.is_superuser

        # ❌ Все остальные — нет.. хотя, остального уж евроде и нет)
        return False

    def has_permission(self, request, view):
        print(f"[DEBUG] has_permission: {request.method} {view.action if hasattr(view, 'action') else ''}")
        # ... твоя логика
        #trasser....      return False
        # print(f"[PERM] user={request.user}, auth={request.user.is_authenticated}, method={request.method}") #...trasser
        # Разрешаем вообще только аутентифицированным
        if not (request.user and request.user.is_authenticated):
            return False    #request.user and request.user.is_authenticated

        if request.method in permissions.SAFE_METHODS:
            return True

        # 🔹 Superuser может всё
        if request.user and request.user.is_superuser:
            return True

        # 🔹 Staff может добавлять (POST)
        if request.method == "POST":
            return request.user.is_staff

        # ❌ Все остальные — нет
        return False
