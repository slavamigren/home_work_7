from django.contrib import admin

from lms.models import Course, Lesson


@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    search_fields = ('title',)


@admin.register(Lesson)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    search_fields = ('title',)
