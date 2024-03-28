from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import UserCreateSerializer
from django.core.mail import send_mail

from app.utils.utils import shuffle_password
from app.tasks import send_email_task, send_sms_task

User = get_user_model()


class CustomUserCreateView(APIView):
    def post(self, request, format=None):
    
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data.get('username')
            phone_number = request.data.get('phone_number')
            last_name = request.data.get('last_name')
            first_name = request.data.get('first_name')
            email = to = request.data.get('email')
                 
            shuffled_passwords =  shuffle_password(request.data.get('password'))
            
            role = "manager_a"  # Remplacez par la logique pour déterminer le rôle

            # Ajouter le rôle et le mot de passe aux données validées du serializer
            serializer.validated_data['role'] = role
            serializer.validated_data['password'] = shuffled_passwords
            
            data = {'shuffled_password': shuffled_passwords}
            
            try: 
                user = User.objects.create_user(
                    username=username, email=email, phone_number=phone_number,
                    role=role, first_name=first_name, last_name=last_name, password=shuffled_passwords
                )
                
                #Envoi de mail asynchrone
                send_email_task.delay(user_to=to, data=data)
                return Response({'user_id': user.id}, status=status.HTTP_201_CREATED)

            except Exception as e:
                # user = User.objects.get(email=email)
                # user.delete()
                # user.save()
                return Response({'error': f'Une erreur de {str(e)} s\'est produite lors de l\'envoi de l\'e-mail'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CreateUserProvider(APIView):
    def post(self, request, format=None):
    
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            username        = request.data.get('username')
            phone_number    = request.data.get('phone_number')
            last_name       = request.data.get('last_name')
            first_name      = request.data.get('first_name')
            email           = to = request.data.get('email')
            role            = 'provider' 
            
            password = request.data.get('password')
            shuffled_passwords = shuffle_password(password)          
            
            
            data = {'shuffled_password': shuffled_passwords}
            
            try: 
                #Envoi de mail asynchrone
                # send_email_task.delay(to, data)
                print (f"Mot de pass est: {data['shuffled_password']}")
                
                #Envoi des messages
                # send_sms_task.delay(phone_number,f"Bonjour {last_name}, c'est un message de test.")
                
                user = User.objects.create_user(
                    username=username, email=email, phone_number=phone_number,
                    role=role, first_name=first_name, last_name=last_name, password=shuffled_passwords
                )
                return Response({'user_id': user.id}, status=status.HTTP_201_CREATED)

            except Exception as e:
                # user = User.objects.get(email=email)
                # user.delete()
                # user.save()
                return Response({'error': f'Une erreur de {str(e)} s\'est produite lors de l\'envoi de l\'e-mail ou sms'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        

# class NewsLimitOffsetPagination(LimitOffsetPagination):
#     page_size = 3
#     page_size_query_param = 'page_size'
#     max_page_size = 1000

class GetUSerModelViewsets(viewsets.ModelViewSet):
    serializer_class    = UserCreateSerializer
    queryset            = User.objects.all()
    # lookup_field        = 'slug'

    # pagination_class = NewsLimitOffsetPagination
    
    # filter_backends = (filters.SearchFilter,)
    # search_fields   = ('title', 'content','created_at',)
    
    def get_queryset(self):
        return User.objects.order_by('-id')
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)