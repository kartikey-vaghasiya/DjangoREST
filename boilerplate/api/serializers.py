from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Product,User,Group


class ProductSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'


# User Serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    _id = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

# Group Serializer
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    _id = serializers.CharField(read_only=True)
    class Meta:
        model = Group
        fields = ['url', 'name']
