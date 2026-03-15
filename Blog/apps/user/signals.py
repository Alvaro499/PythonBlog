# Signals
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

#Decouple
from decouple import config

#Emails
from django.core.mail import send_mail

from apps.user.models import User


@receiver(post_save, sender=User)
def email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome t ABC Blog',
            str('Hola ' + instance.full_name + ', you have signed up satisfactory.'
                                               'It is complete pleasure that you are now part of the family'),
            config('EMAIL_HOST_USER'),
            [instance.email]
        )