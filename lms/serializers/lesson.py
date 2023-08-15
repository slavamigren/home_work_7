from rest_framework import serializers

from lms.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Сериализирует все поля модели Lesson"""
    class Meta:
        model = Lesson
        fields = '__all__'
