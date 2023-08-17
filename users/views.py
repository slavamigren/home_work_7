from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import IsOwner
from users.serializers import UserSerializer, UserPaymentsSerializer, CreateUserSerializer, NotUsersProfileSerializer

#  create доступен всем желающим, иначе никто не сможет зарегистрироваться
PERMISSIONS_DICT = {
    'list': [],
    'retrieve': [],
    'update': [IsOwner],
    'partial_update': [IsOwner],
    'destroy': [IsOwner],
    'create': [AllowAny]
}


class UserViewSet(ModelViewSet):
    """Контроллер для работы с пользователями"""
    queryset = User.objects.all()
    default_serializer = UserSerializer
    serializers = {
        'list': NotUsersProfileSerializer,
        'retrieve_owners': UserPaymentsSerializer,
        'retrieve_not_owners': NotUsersProfileSerializer,
        'create': CreateUserSerializer,
    }

    def get_serializer_class(self):
        """Выбирает сериализатор для экшна"""
        if self.action == 'retrieve':
            if self.request.user == self.get_object():
                return self.serializers.get('retrieve_owners')
            else:
                return self.serializers.get('retrieve_not_owners')
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        """Выбирает permission в соответствии с методом"""
        return [permission() for permission in PERMISSIONS_DICT[self.action]]