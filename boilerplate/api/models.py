from django.contrib.auth.models import User, Group
from djongo import models
from djongo.models import ObjectIdField
from bson import ObjectId


class Product(models.Model):
    _id = ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=25)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name