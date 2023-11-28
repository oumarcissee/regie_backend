from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail

import random


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



