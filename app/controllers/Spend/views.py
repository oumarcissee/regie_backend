from rest_framework import viewsets

from app.utils.utils import format_valeur

from .serializers import SpendReadSerializer, SpendWriteSerializer

from app.models import Spend

class SpendModelViewsets(viewsets.ModelViewSet):
    queryset            = Spend.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return SpendReadSerializer  # Utilise le sérialiseur pour les requêtes GET
        else:
            return SpendWriteSerializer  # Utilise le sérialiseur pour les requêtes POST, PUT, PATCH
    
    def get_queryset(self):
        return Spend.objects.order_by('-id')
    
    def perform_create(self, serializer):
        # Récupérer le dernier enregistrement dans la base de données
        last = Spend.objects.last()
        last_id = last.id if last else 0
        serializer.save(ref=format_valeur('M', last_id+1))
        