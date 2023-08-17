from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from lms.models import Payment
from lms.serializers.payment import PaymentSerializer


class PaymentViewSet(ListAPIView):
    """Контроллер вывода влатежей"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_type')
    ordering_fields = ('date',)
#    permission_classes = [IsAuthenticated]

