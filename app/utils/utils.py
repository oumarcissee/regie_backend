from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.db import models
import random



from django.db import models

class CustomPrimaryKeyField(models.CharField):
    def __init__(self, prefix='', *args, **kwargs):
        self.prefix = prefix
        kwargs['max_length'] = 10  # Assurez-vous que max_length est défini dans kwargs
        kwargs['unique'] = True    # Assurez-vous que unique est défini dans kwargs
        super().__init__(*args, **kwargs)  # Appelez l'initialisation de CharField sans max_length et unique

    def pre_save(self, model_instance, add):
        if add:
            last_object = model_instance.__class__.objects.last()
            if last_object:
                last_key = last_object.pk
                if last_key.startswith(self.prefix):
                    last_num = int(last_key[len(self.prefix):])
                    new_key = f'{self.prefix}{last_num + 1}'
                    setattr(model_instance, self.attname, new_key)
                    return new_key
        return super().pre_save(model_instance, add)

    
class CustomDate(models.Model):
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    

def send_email(subject, message, user_to):
    
    
    if not user_to or not subject or not message:
        return Response({'message': 'Tous les champs sont obligatoires'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        send_mail(subject, message, None, [user_to])  # Aucune adresse e-mail expéditeur spécifiée
        return Response({'message': 'E-mail envoyé avec succès'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': 'Une erreur s\'est produite lors de l\'envoi de l\'e-mail'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def shuffle_password(password):
    # Convertir la chaîne de mot de passe en une liste de caractères
    password_list = list(password)

    # Mélanger la liste de caractères
    random.shuffle(password_list)

    # Limiter le résultat à 10 caractères en utilisant random.sample()
    shuffled_password = ''.join(random.sample(password_list, min(len(password_list), 10)))

    return shuffled_password




