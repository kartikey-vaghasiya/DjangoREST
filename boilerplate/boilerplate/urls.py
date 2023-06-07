from django.urls import include, path
from rest_framework import routers
from api.views import ProductViewSet
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework')
]
