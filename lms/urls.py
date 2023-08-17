from django.urls import path
from rest_framework import routers

from lms.apps import LmsConfig
from lms.views.course import CourseViewSet
from lms.views.lesson import LessonListView, LessonCreateView, LessonDetailView, LessonUpdateView, LessonDeleteView
from lms.views.payment import PaymentViewSet
from lms.views.subscription import SubscriptionDeleteView, SubscriptionCreateView, SubscriptionListView

app_name = LmsConfig.name

urlpatterns = [
    path('lesson/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lesson/delete/<int:pk>/', LessonDeleteView.as_view(), name='lesson_delete'),
    path('lesson/detail/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>/', LessonUpdateView.as_view(), name='lesson_update'),

    path('payment/', PaymentViewSet.as_view(), name='payment_list'),

    path('subscription/delete/<int:pk>/', SubscriptionDeleteView.as_view(), name='subscription_delete'),
    path('subscription/create/', SubscriptionCreateView.as_view(), name='subscription_create'),
    path('subscription/', SubscriptionListView.as_view(), name='subscription_list'),
]

router = routers.SimpleRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns += router.urls


