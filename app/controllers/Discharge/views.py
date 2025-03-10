from rest_framework import viewsets

from app.utils.utils import format_valeur

from .serializers import DischargeReadSerializer, DischargeWriteSerializer

from app.models import Discharge

class DischargeModelViewsets(viewsets.ModelViewSet):
    queryset            = Discharge.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return DischargeReadSerializer  # Utilise le sérialiseur pour les requêtes GET
        else:
            return DischargeWriteSerializer  # Utilise le sérialiseur pour les requêtes POST, PUT, PATCH
    
    def get_queryset(self):
        return Discharge.objects.order_by('-id')
    
    def perform_create(self, serializer):
        # Récupérer le dernier enregistrement dans la base de données
        last = Discharge.objects.last()
        last_id = last.id if last else 0
        serializer.save(ref=format_valeur('B', last_id+1))
        