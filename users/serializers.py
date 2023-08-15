from rest_framework import serializers

from lms.serializers.payment import PaymentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для пользователей"""
    class Meta:
        model = User
        fields = '__all__'


class UserPaymentsSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра одного или всех пользователей с их платежами"""
    payments = PaymentSerializer(source='payment_set', many=True)

    class Meta:
        model = User
        fields = '__all__'