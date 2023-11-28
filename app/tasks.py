# tasks.py

from celery import shared_task
from templates.email import CustomUserRegistrationEmail


@shared_task
def send_email_task(user_to, data):
    MailSender = CustomUserRegistrationEmail(content=data)

    MailSender.send([user_to])
