from rest_framework import viewsets

from app.utils.utils import format_valeur

from .serializers import OrderLineReadSerializer, OrderLineWriteSerializer

from app.models import  OrderLine

class OrderLineModelViewsets(viewsets.ModelViewSet):
    queryset            = OrderLine.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return OrderLineReadSerializer  # Utilise le sérialiseur pour les requêtes GET
        else:
            return OrderLineWriteSerializer  # Utilise le sérialiseur pour les requêtes POST, PUT, PATCH
    
    def get_queryset(self):
        return OrderLine.objects.order_by('-id')
    
    def perform_create(self, serializer):
        # Récupérer le dernier enregistrement dans la base de données
        last = OrderLine.objects.last()
        last_id = last.id if last else 0
        serializer.save(ref=format_valeur('CL', last_id+1))
        
        #Gestion de la ligne des commandes
        