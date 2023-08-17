from rest_framework import serializers

from lms.models import Lesson
from lms.validators import URLValidator


class LessonSerializer(serializers.ModelSerializer):
    """Сериализирует все поля модели Lesson"""
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [URLValidator(field='video_url')]
