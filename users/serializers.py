from datetime import datetime

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Переопределяет сериализатор для получения токена, чтобы каждый раз обновлялась
    запись в last_login"""
    def validate(self, attrs):
        # implement your logic here
        data = super().validate(attrs)
        user_obj = User.objects.filter(email=self.user.email)[0]
        if user_obj:
            user_obj.last_login = datetime.now()
            user_obj.save()
        return data