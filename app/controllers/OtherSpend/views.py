from rest_framework import viewsets

from app.utils.utils import format_valeur

from .serializers import OtherSpendReadSerializer, OtherSpendWriteSerializer

from app.models import OtherSpend

class OtherSpendModelViewsets(viewsets.ModelViewSet):
    queryset            = OtherSpend.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return OtherSpendReadSerializer  # Utilise le sérialiseur pour les requêtes GET
        else:
            return OtherSpendWriteSerializer  # Utilise le sérialiseur pour les requêtes POST, PUT, PATCH
    
    def get_queryset(self):
         # Récupérer le paramètre dans la requête
        discharge_param = self.request.query_params.get('discharge', None)
        
        if discharge_param is not None:
            return OtherSpend.objects.filter(discharge=int(discharge_param)).order_by('-id')
        
        return OtherSpend.objects.order_by('-id')
    
    # def perform_create(self, serializer):
    #     # Récupérer le dernier enregistrement dans la base de données
    #     last = OtherSpend.objects.last()
    #     last_id = last.id if last else 0
    #     serializer.save(ref=format_valeur('M', last_id+1))
        