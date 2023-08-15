from rest_framework import serializers

from lms.models import Course
from lms.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    """Сериализирует все поля объекта модели Course"""


    class Meta:
        model = Course
        fields = '__all__'


class CourseLessonsAmountSerializer(serializers.ModelSerializer):
    """Сериализирует все поля объекта модели Course и добавляет количество уроков в курсе"""
    lessons_amount = serializers.IntegerField(source='lesson_set.all.count')
    lessons = LessonSerializer(source='lesson_set', many=True)


    class Meta:
        model = Course
        fields = '__all__'
