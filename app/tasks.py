# tasks.py
from celery import shared_task
from templates.email import CustomUserRegistrationEmail

from twilio.rest import Client
from django.conf import settings

@shared_task
def send_email_task(user_to, data):
    MailSender = CustomUserRegistrationEmail(content=data)
 
    MailSender.send(to=[user_to])
    print("Après l'envoie")
    
@shared_task
def send_sms_task(to, message):
    
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    client.messages.create(
        body=message,
        from_=settings.TWILIO_PHONE_NUMBER,
        to=to
    )
       
