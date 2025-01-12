from rest_framework import viewsets

from app.utils.utils import format_valeur

from .serializers import SignalOperatorsReadSerializer, SignalOperatorsWriteSerializer

from app.models import SignalOperators

class SignalOperatorsModelViewsets(viewsets.ModelViewSet):
    queryset            = SignalOperators.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return SignalOperatorsReadSerializer  # Utilise le sérialiseur pour les requêtes GET
        else:
            return SignalOperatorsWriteSerializer  # Utilise le sérialiseur pour les requêtes POST, PUT, PATCH
    
    def get_queryset(self):
        return SignalOperators.objects.order_by('-id')
    
    def perform_create(self, serializer):
        # Récupérer le dernier enregistrement dans la base de données
        last = SignalOperators.objects.last()
        last_id = last.id if last else 0
        serializer.save(ref=format_valeur('SO', last_id+1))
        