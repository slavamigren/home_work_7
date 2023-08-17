from rest_framework import serializers

from lms.models import Course
from lms.serializers.lesson import LessonSerializer
from lms.serializers.subscription import SubscriptionSerializer


class CourseSerializer(serializers.ModelSerializer):
    """Сериализирует все поля объекта модели Course"""


    class Meta:
        model = Course
        fields = '__all__'


class CourseLessonsAmountSerializer(serializers.ModelSerializer):
    """Сериализирует все поля объекта модели Course и добавляет количество уроков в курсе
     и информацию о наличии подписки"""
    subscription = serializers.SerializerMethodField()  # подписан ли пользователь на курс True или False
    lessons_amount = serializers.IntegerField(source='lesson.all.count')
    lessons = LessonSerializer(source='lesson', many=True, read_only=True)

    def get_subscription(self, obj):
        """Проверяет, подписан ли пользователь на курс"""
        if obj.subscription.all():
            return True
        return False

    class Meta:
        model = Course
        fields = '__all__'
