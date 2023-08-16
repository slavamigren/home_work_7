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


class NotUsersProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра одного или всех пользователей не являющихся текущим без личной информации"""

    class Meta:
        model = User
        fields = ('id', 'email', 'role')


class CreateUserSerializer(serializers.ModelSerializer):
    """Сериализатор для создания нового пользователя"""
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance