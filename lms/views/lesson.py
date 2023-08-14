from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView

from lms.models import Lesson
from lms.serializers.lesson import LessonSerializer


class LessonDeleteView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateView(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonListView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDetailView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()