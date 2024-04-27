from rest_framework import viewsets

from app.utils.utils import format_valeur

from .serializers import ItemReadSerializer, ItemWriteSerializer

from app.models import Item

class ItemModelViewsets(viewsets.ModelViewSet):
    queryset            = Item.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ItemReadSerializer  # Utilise le sérialiseur pour les requêtes GET
        else:
            return ItemWriteSerializer  # Utilise le sérialiseur pour les requêtes POST, PUT, PATCH
    
    def get_queryset(self):
        return Item.objects.order_by('-id')
    
    def perform_create(self, serializer):
        # Récupérer le dernier enregistrement dans la base de données
        last = Item.objects.last()
        last_id = last.id if last else 0
        serializer.save(ref=format_valeur('A', last_id+1))
        