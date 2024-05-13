from rest_framework import viewsets

from app.utils.utils import format_valeur

from .serializers import OrderReadSerializer, OrderWriteSerializer

from app.models import Order

class OrderModelViewsets(viewsets.ModelViewSet):
    queryset            = Order.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return OrderReadSerializer  # Utilise le sérialiseur pour les requêtes GET
        else:
            return OrderWriteSerializer  # Utilise le sérialiseur pour les requêtes POST, PUT, PATCH
    
    def get_queryset(self):
        return Order.objects.order_by('-id')
    
    def perform_create(self, serializer):
        # Récupérer le dernier enregistrement dans la base de données
        last = Order.objects.last()
        last_id = last.id if last else 0
        serializer.save(ref=format_valeur('C', last_id+1))
        