from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import UserCreateSerializer,UserUpdateSerializer
from django.core.mail import send_mail
from rest_framework.decorators import action

from app.utils.utils import shuffle_password
from app.tasks import send_email_task, send_sms_task

User = get_user_model()



class UserList(APIView):
    
    # def get(self, request):
    #     objets = User.objects.filter(role='provider').order_by('-id')
    #     serializer = UserCreateSerializer(objets, many=True)
    #     return Response(serializer.data)

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
          
        """_summary_
        
        Raises:
            Http404: _description_

        Returns:
            _type_: _description_
        """
        
        
class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        objet = self.get_object(pk)
        serializer = UserCreateSerializer(objet)
        return Response(serializer.data)

    def put(self, request, pk):
        objet = self.get_object(pk)
        serializer = UserCreateSerializer(objet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        objet = self.get_object(pk)
    
        serializer = UserUpdateSerializer(objet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        objet = self.get_object(pk)
        objet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        

        """Classe de recupération

        Returns:
            _type_: _description_
        """
class UserModelViewsets(viewsets.ModelViewSet):
    serializer_class    = UserCreateSerializer
    queryset            = User.objects.all()
    
    def get_queryset(self):
        return User.objects.order_by('-id')
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        

    # @action(detail=False, methods=['get'])
    # def providers(self, request):
    #     data = User.objects.filter(role='provider').order_by('-id')
    #     print(data, "Ou rien")
    #     serializer = self.get_serializer(data, many=True)
    #     return Response(serializer.data)
    
        """get providers

        Returns:
            _type_: _description_
        """
class ProvidersModelViewsets(viewsets.ModelViewSet):
    serializer_class    = UserCreateSerializer
    queryset            = User.objects.all()
    
    def get_queryset(self):
        return User.objects.filter(role='provider').order_by('-id')
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    