from django.contrib.auth.models import User, Group

from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from rest_framework import viewsets

from api.models import Product
from api.serializers import ProductSerializer

from bson import ObjectId


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field ='_id'
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter_kwargs = {self.lookup_field: ObjectId(
            self.kwargs[self.lookup_field])}
        obj = queryset.get(**filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj