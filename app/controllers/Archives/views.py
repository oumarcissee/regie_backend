from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from app.utils.utils import format_valeur

from .serializers import  ArchivesReadSerializer, ArchivesWriteSerializer

from app.models import Archives

import calendar
from datetime import datetime



class ArchiveModelViewsets(viewsets.ModelViewSet):
    unique_year_month   = set()
    queryset            = Archives.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ArchivesReadSerializer  # Utilise le sérialiseur pour les requêtes GET
        else:
            return ArchivesWriteSerializer  # Utilise le sérialiseur pour les requêtes POST, PUT, PATCH
    
    def get_queryset(self):
    
        return Archives.objects.order_by('-date')
    
    def perform_create(self, serializer):
        # Obtenir le mois et l'année courants
        current_date = datetime.now()
        current_year = current_date.year
        current_month = current_date.month
        # Obtenir le nombre de jours du mois courant
        days_in_month = calendar.monthrange(current_year, current_month)[1]
        # print(f"Le nombre de jours dans le mois courant ({current_month}/{current_year}) est : {days_in_month}")
        serializer.save(nomber_of_days=days_in_month)
        
    @action(detail=False)
    def dates(self, request):
        dates = Archives.objects.all().order_by('-id')
        
        serializer = self.get_serializer(dates, many=True)
        
        return Response(data=serializer.data, status =200)

    # def format_archive(self, archive): 
    #     # date_obj = datetime.strptime(archive.date, "%Y-%m-%d %H:%M:%S.%f")
    #     print(archive.date.strftime("%Y-%m-%d %"), "Je suis dans la date")
    #     return {
    #         'id': archive.id,
    #         #'date': date_obj,  # Formater la date si nécessaire
    #         # 'number_of_days': archive.number_of_days,
    #         'discharge':   archive.discharge,
    #         'order':   archive.order,
    #     }