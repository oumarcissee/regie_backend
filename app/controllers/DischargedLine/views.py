from rest_framework import viewsets

from app.utils.utils import format_valeur

from .serializers import DischargedLinesReadSerializer, DischargedLinesWriteSerializer

from app.models import  DischargedLines

class DischargedLinesModelViewsets(viewsets.ModelViewSet):
    queryset            = DischargedLines.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return DischargedLinesReadSerializer  # Utilise le sérialiseur pour les requêtes GET
        else:
            return DischargedLinesWriteSerializer  # Utilise le sérialiseur pour les requêtes POST, PUT, PATCH
    
    def get_queryset(self):
        # Récupérer le paramètre dans la requête
        order_param = self.request.query_params.get('order', None)
        
        if order_param is not None:
            return DischargedLines.objects.filter(order=int(order_param)).order_by('-id')
        
        return DischargedLines.objects.order_by('-id')
    
    # def perform_create(self, serializer):
    #     # Récupérer le dernier enregistrement dans la base de données
       
    #     last = serializer.save()
    #     last.ref = format_valeur("CL", last.id)
    #     last.save()