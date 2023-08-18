from rest_framework import serializers

from lms.models import Course
from lms.serializers.lesson import LessonSerializer
from lms.serializers.subscription import SubscriptionSerializer
from lms.services import get_payment_url


class CourseSerializer(serializers.ModelSerializer):
    """Сериализирует все поля объекта модели Course"""


    class Meta:
        model = Course
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
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


class CourseRetrieveSerializer(serializers.ModelSerializer):
    """Сериализирует поле объекта модели Course и добавляет количество уроков в курсе,
     информацию о наличии подписки и ссылку для оплаты"""
    subscription = serializers.SerializerMethodField()  # подписан ли пользователь на курс True или False
    payment_url = serializers.SerializerMethodField()  # ссылка для оплаты
    lessons_amount = serializers.IntegerField(source='lesson.all.count')
    lessons = LessonSerializer(source='lesson', many=True, read_only=True)

    def get_subscription(self, obj):
        """Проверяет, подписан ли пользователь на курс"""
        if obj.subscription.all():
            return True
        return False

    def get_payment_url(self, obj):
        return get_payment_url(obj.title, obj.price)

    class Meta:
        model = Course
        fields = '__all__'
