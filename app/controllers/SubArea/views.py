from rest_framework import viewsets

from app.utils.utils import format_valeur

from .serializers import SubAreaReadSerializer, SubAreaWriteSerializer

from app.models import SubArea

class SubAreaModelViewsets(viewsets.ModelViewSet):
    queryset            = SubArea.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return SubAreaReadSerializer  # Utilise le sérialiseur pour les requêtes GET
        else:
            return SubAreaWriteSerializer  # Utilise le sérialiseur pour les requêtes POST, PUT, PATCH
    
    def get_queryset(self):
        return SubArea.objects.order_by('-id')
    
    def perform_create(self, serializer):
        # Récupérer le dernier enregistrement dans la base de données
        last = SubArea.objects.last()
        last_id = last.id if last else 0
        serializer.save(ref=format_valeur('SR', last_id+1))
        