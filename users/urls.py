from django.urls import path
from rest_framework import routers

from users.apps import UsersConfig
from users.views import UserViewSet

app_name = UsersConfig.name

urlpatterns = [

]

router = routers.SimpleRouter()
router.register('user', UserViewSet)

urlpatterns += router.urls