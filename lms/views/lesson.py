from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from lms.models import Lesson
from lms.permissions import IsModerator, IsOwner
from lms.serializers.lesson import LessonSerializer
from users.models import UserRoles


class LessonDeleteView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonCreateView(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonUpdateView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonListView(ListAPIView):
    """Показывает список уроков"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]

    def get_queryset(self):
        """Модераторам показывает все уроки, мемберам - только их"""
        queryset = super().get_queryset()
        if self.request.user.role == UserRoles.MODERATOR:
            return queryset
        return queryset.filter(owner=self.request.user)


class LessonDetailView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]