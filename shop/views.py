from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
# from filters import ProductFilter

from shop.serializers import GroupSerializer, UserSerializer, ProductSerializer

from .models import Product
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import ProductFilter

from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import CustomPermissions
#fur Swagger-spectacular
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample, OpenApiParameter
from rest_framework.exceptions import PermissionDenied


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [CustomPermissions]

    #filtering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']  # поиск по подстроке
    ordering_fields = ['price', 'created']  # сортировка

    #fur mark obj als double(
    @extend_schema(
        operation_id="product_markalsdoppelt",
        # parameters=[
        #     OpenApiParameter(name='all', description='Выбрать все(non-active в т.ч.) объявления, только для staff;Передай ?all=1',
        #                     required=False, type=str) ],
        description=(
                "Маркирует Product als дубль: метка 'take two' в поле 'name'. "
                "Доступно только суперпользователю."
        ),
        request=None,  # т.к. POST без тела
        responses={
            200: OpenApiResponse(
                description="Product успешно marked als doppelt",
                examples=[
                    OpenApiExample(
                        name="Success marked",
                        summary="Product success marked",
                        description="Возвращается при успешной пометке как дубль Product-obj",
                        value={"status": "Product marked als doppelt"}
                    )
                ],
            ),
            403: OpenApiResponse(description="Нет прав для marked als dopplet Product-obj"),
            404: OpenApiResponse(description="Product not find"),
        },
    )
    @action(detail=True, methods=['get'])
    def markalsdoppelt(self, request, pk=None):
        #принудительная проверка на права... castom-permissons не срабатывают корректно
        if not request.user.is_superuser:
            raise PermissionDenied("Nur superuser darf diesen Vorgang durchführen")

        obj = self.get_object()
        # Проверяем object-level permissions
        self.check_object_permissions(request, obj)
        if not obj.name.find('take two') == -1:
            return Response({"statuS":f'product {obj.name} schon marked als "take two"; cancel PATCH-operation '})
        obj.name = "take two " + obj.name
        obj.save()
        return Response({"statuS": f'marked als dopplet id {obj.id}'})
    #----------------------------------------------------------------------------------

    #----------------------------------------------------------------------------------
    #CASTOM ENdPOINTS

    #fur doublesdelete(
    @extend_schema(
        operation_id="product_doublesdelete",
        description=(
                "Удаляет дубли (это записи в названии которых присутствует маска 'take two' or 'double' "
                "(предварительно помечается скриптом product_patch_als_double(id) под суперюзеровским доступом"
                "Доступно staff-users или суперпользователю."
        ),
        request=None,  # т.к. POST без тела
        responses={
            200: OpenApiResponse(
                description="дубли Products успешно удалены",
                examples=[
                    OpenApiExample(
                        name="Успешное удаление дублей в Products",
                        summary="Products-obj deleted",
                        description="Возвращается при успешном удаление записи(-ей) дубля(-ей) ",
                        value={"status": "Дубли почищены"}
                    )
                ],
            ),
            403: OpenApiResponse(description="Нет прав для запуска endpoint -a"),
            404: OpenApiResponse(description="нет выборки для операции"),
        },
    )
    @action(detail=False, methods=['get', 'delete'])
    def doublesdelete(self, request):
        #принудительная проверка на права... castom-permissons не срабатывают корректно
        if not request.user.is_staff:
            raise PermissionDenied("Nur staff darf diesen Vorgang durchführen")

        # Получаем все объекты
        queryset = self.get_queryset()

        deleted_ids = []
        for obj in queryset:

            # Если в name есть маска дубля
            if 'take two' in obj.name or 'double' in obj.name:
                # Проверяем object-level permissions для каждого объекта
                self.check_object_permissions(request, obj)
                deleted_ids.append(f'к удалению id:{obj.id}, товар:{obj.name}')
                obj.delete()

        if deleted_ids:
            return Response({
                "status": "Deleted duplicates",
                "deleted_ids": deleted_ids
            })
        else:
            return Response({
                "status": "No duplicates found"
            })
    # @action(detail=False, methods=['delete'])
    # def doublesdelete(self, request):
    #     obj = self.get_object()
    #     # Проверяем object-level permissions
    #     self.check_object_permissions(request, obj)
    #     obj.active = True
    #     obj.save()
    #     return Response({"statuS": "activated"})
    #----------------------------------------------------------------------------------
