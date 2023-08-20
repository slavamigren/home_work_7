from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from lms.models import Lesson, Course
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
        if new_lesson.course:
            upd_course = Course.objects.get(pk=new_lesson.course_id)
            upd_course.update_flag = True
            upd_course.save()
        new_lesson.save()


class LessonUpdateView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]

    def perform_update(self, serializer):
        """Выставляем флаг, что урок был обновлен"""
        lesson = serializer.save()
        if lesson.course:
            upd_course = Course.objects.get(pk=lesson.course_id)
            upd_course.update_flag = True
            upd_course.save()
        lesson.save()


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