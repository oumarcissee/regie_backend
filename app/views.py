# views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail

@api_view(['POST'])
def send_email(request):
    if request.method == 'POST':
        recipient = request.data.get('email')
        subject = 'TEST'
        message = "C'est un message de test"
        
        if not recipient or not subject or not message:
            return Response({'message': 'Tous les champs sont obligatoires'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            send_mail(subject, message, None, [recipient])  # Aucune adresse e-mail expéditeur spécifiée
            return Response({'message': 'E-mail envoyé avec succès'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Une erreur s\'est produite lors de l\'envoi de l\'e-mail'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
