from django.urls import path, include
from rest_framework import routers

from .views import index
from .serializers import CategoryViewSet, ClubViewSet, ProductViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'clubs', ClubViewSet)
router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]