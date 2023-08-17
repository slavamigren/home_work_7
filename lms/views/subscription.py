from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from lms.models import Subscription
from lms.permissions import IsStudent, IsOwner, IsStudentOwner
from lms.serializers.subscription import SubscriptionSerializer


class SubscriptionDeleteView(DestroyAPIView):
    """Удаляет подписку на курс, но разрешено только владельцу"""
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsStudentOwner]


class SubscriptionCreateView(CreateAPIView):
    """Создаёт подписку на курс, разрешено только студенту"""
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsStudent]

    def perform_create(self, serializer):
        new_subscription = serializer.save()
        new_subscription.user = self.request.user
        new_subscription.save()


class SubscriptionListView(ListAPIView):
    """Показывает список подписок для пользователя"""
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsOwner]

    def get_queryset(self):
        """Модераторам показывает все уроки, мемберам - только их"""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
