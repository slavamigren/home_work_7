from celery import shared_task

from lms.services import send_update_notification, check_users


@shared_task
def update_notification():
    send_update_notification()


@shared_task
def check_users_activity():
    check_users()