from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer, UserPaymentsSerializer


class UserViewSet(ModelViewSet):
    """Контроллер для работы с пользователями"""
    queryset = User.objects.all()
    default_serializer = UserSerializer
    serializers = {
        'list': UserPaymentsSerializer,
        'retrieve': UserPaymentsSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)