from datetime import datetime, timedelta

import requests
from django.core.mail import send_mail

from conf import settings
from conf.settings import STRIPE_AUTH, NOTIFICATION_TIME
from lms.models import Course, Lesson
from users.models import User


def get_payment_url(product, price):
    headers = {
        'Authorization': f'Bearer {STRIPE_AUTH}'
    }
    data = {
        'name': product
    }
    response = requests.request('POST', 'https://api.stripe.com/v1/products', headers=headers, data=data)
    product_id = response.json()['id']
    price *= 100  # тк там в копейках
    data = {
        'unit_amount': price,
        'currency': 'rub',
        'recurring[interval]': 'month',
        'product': product_id
    }
    response = requests.request('POST', 'https://api.stripe.com/v1/prices', headers=headers, data=data)
    price_id = response.json()['id']

    data = {
        'line_items[0][price]': price_id,
        'line_items[0][quantity]': 1,
        'mode': 'subscription',
        'success_url': 'https://example.com/success'
    }
    response = requests.request('POST', 'https://api.stripe.com/v1/checkout/sessions', headers=headers, data=data)
    return response.json()['url']

def send_update_notification():
    """Просматривает все уроки на признак обновления и истечение периода времени до рассылки"""
    current_time = datetime.now()
    notification_timedelta = timedelta(hours=NOTIFICATION_TIME)
    courses = Course.objects.all()
    for course in courses:
        if course.update_flag and current_time - course.last_update_time > notification_timedelta:
            mailing_list = [subscription.user.email for subscription in course.subscription.all()]
            send_mail(
                f'Обновление в курсе {course.title}',
                f'Обновление в курсе {course.title}',
                settings.EMAIL_HOST_USER,
                mailing_list
            )
            updated_course = Course.objects.get(pk=course.pk)
            updated_course.update_flag = False
            updated_course.save(update_fields=['update_flag'])


def check_users():
    """Проверяет last_login всех пользователей в Users, если большее 30 дней
     переводит в неактивные"""
    current_time = datetime.now()
    users = User.objects.all()
    inactive_timedelta = timedelta(days=30)
    for user in users:
        if current_time - user.last_login > inactive_timedelta:
            inactive_user = User.objects.get(pk=user.pk)
            inactive_user.is_active = True
            inactive_user.save(update_fields=['is_active'])