from rest_framework.viewsets import ModelViewSet

from lms.models import Course
from lms.serializers.course import CourseSerializer, CourseLessonsAmountSerializer


class CourseViewSet(ModelViewSet):
    """Контроллер курсов"""
    queryset = Course.objects.all()
    default_serializer = CourseSerializer
    serializers = {
        'list': CourseLessonsAmountSerializer,
        'retrieve': CourseLessonsAmountSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)


