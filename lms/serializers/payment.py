from rest_framework import serializers

from lms.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализирует все поля объекта модели Course"""


    class Meta:
        model = Payment
        fields = '__all__'