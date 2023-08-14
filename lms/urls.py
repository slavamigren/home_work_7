from django.urls import path
from rest_framework import routers

from lms.apps import LmsConfig
from lms.views.course import CourseViewSet
from lms.views.lesson import LessonListView, LessonCreateView, LessonDetailView, LessonUpdateView, LessonDeleteView

app_name = LmsConfig.name

urlpatterns = [
    path('', LessonListView.as_view(), name='lesson_list'),
    path('create/', LessonCreateView.as_view(), name='lesson_create'),
    path('delete/<int:pk>/', LessonDeleteView.as_view(), name='lesson_destroy'),
    path('detail/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('update/<int:pk>/', LessonUpdateView.as_view(), name='lesson_update')
]

router = routers.SimpleRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns += router.urls
