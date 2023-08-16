from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from lms.models import Course
from lms.permissions import IsModerator, IsOwner
from lms.serializers.course import CourseSerializer, CourseLessonsAmountSerializer
from users.models import UserRoles

PERMISSIONS_DICT = {
    'list': [IsAuthenticated, IsModerator | IsOwner],
    'create': [IsAuthenticated, IsOwner],
    'retrieve': [IsAuthenticated, IsModerator | IsOwner],
    'update': [IsAuthenticated, IsModerator | IsOwner],
    'partial_update': [IsAuthenticated, IsModerator | IsOwner],
    'destroy': [IsAuthenticated, IsOwner]
}


class CourseViewSet(ModelViewSet):
    """Контроллер курсов"""
    queryset = Course.objects.all()
    default_serializer = CourseSerializer
    permission_classes = [IsAuthenticated]
    serializers = {
        'list': CourseLessonsAmountSerializer,
        'retrieve': CourseLessonsAmountSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        """Выбирает permission в соответствии с методом"""
        return [permission() for permission in PERMISSIONS_DICT[self.action]]

    def get_queryset(self):
        """Модераторам показывает все курсы, мемберам - только их"""
        queryset = super().get_queryset()
        if self.request.user.role == UserRoles.MODERATOR:
            return queryset
        return queryset.filter(owner=self.request.user)

