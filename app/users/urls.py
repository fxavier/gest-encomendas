from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)

app_name = 'users'

urlpatterns = [
    path('', include(router.urls)),
]
