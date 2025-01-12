from rest_framework import viewsets

from app.utils.utils import format_valeur

from .serializers import UnitReadSerializer, UnitWriteSerializer

from app.models import Unit

class UnitModelViewsets(viewsets.ModelViewSet):
    queryset            = Unit.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return UnitReadSerializer  # Utilise le sérialiseur pour les requêtes GET
        else:
            return UnitWriteSerializer  # Utilise le sérialiseur pour les requêtes POST, PUT, PATCH
    
    def get_queryset(self):
        return Unit.objects.order_by('-id')
    
    def perform_create(self, serializer):
        # Récupérer le dernier enregistrement dans la base de données
        last = Unit.objects.last()
        last_id = last.id if last else 0
        serializer.save(ref=format_valeur('U', last_id+1))
        