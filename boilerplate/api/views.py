from django.contrib.auth.models import User, Group
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from rest_framework import viewsets
from api.models import Product
from api.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


