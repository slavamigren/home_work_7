from rest_framework import serializers

from lms.models import Lesson, Subscription
from lms.validators import URLValidator


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализирует все поля модели Lesson"""
    class Meta:
        model = Subscription
        fields = ('pk', 'course')
