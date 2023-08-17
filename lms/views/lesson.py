from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from lms.models import Lesson
from lms.paginators import Paginator
from lms.permissions import IsModerator, IsOwner, IsStudent
from lms.serializers.lesson import LessonSerializer
from users.models import UserRoles


class LessonDeleteView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


class LessonCreateView(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonUpdateView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]


class LessonListView(ListAPIView):
    """Показывает список уроков"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = Paginator
    permission_classes = [IsModerator | IsOwner | IsStudent]

    def get_queryset(self):
        """Модераторам показывает все уроки, мемберам - только их"""
        queryset = super().get_queryset()
        if self.request.user.role == UserRoles.MODERATOR or self.request.user.role == UserRoles.STUDENT:
            return queryset
        return queryset.filter(owner=self.request.user)


class LessonDetailView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner | IsStudent]