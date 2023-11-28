from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserCreateSerializer

from app.utils.utils import shuffle_password
from app.tasks import send_email_task


class CustomUserCreateView(APIView):
    def post(self, request, format=None):
        User = get_user_model()
    
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data.get('username')
            phone_number = request.data.get('phone_number')
            last_name = request.data.get('last_name')
            first_name = request.data.get('first_name')
            email = to = request.data.get('email')
            role = request.data.get('role')
            
            password = request.data.get('password')
            shuffled_passwords = shuffle_password(password)
            
            
            user = User.objects.create_user(
                username=username, email=email, phone_number=phone_number,
                role=role, first_name=first_name, last_name=last_name, password=shuffled_passwords
            )
            
            data = {'shuffled_password': shuffled_passwords}
            
            try: 
                #Envoi de mail asynchrone
                send_email_task(user_to=to, data=data)
                return Response({'user_id': user.id}, status=status.HTTP_201_CREATED)

            except Exception as e:
                # user = User.objects.get(email=email)
                # user.delete()
                # user.save()
                return Response({'error': f'Une erreur de {str(e)} s\'est produite lors de l\'envoi de l\'e-mail'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)