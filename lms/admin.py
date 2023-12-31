from django.contrib import admin

from lms.models import Course, Lesson, Payment, Subscription


@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'last_update_time')
    search_fields = ('title',)


@admin.register(Lesson)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    search_fields = ('title',)


@admin.register(Payment)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'date', 'paid_course', 'paid_lesson', 'amount', 'payment_type')
    search_fields = ('user',)


@admin.register(Subscription)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'course')
    search_fields = ('tuser',)