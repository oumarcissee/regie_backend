from rest_framework import serializers
from app.models import  DischargedLines

class DischargedLinesReadSerializer(serializers.ModelSerializer):
    class Meta:
        model  = DischargedLines
        fields = '__all__'  # Inclut tous les champs, y compris 'custom_id' pour les requêtes GET
        depth  = 1

class DischargedLinesWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model   = DischargedLines
        # exclude = ['unites']  # Exclut 'custom_id' pour les requêtes POST, PUT, PATCH
        fields = '__all__'
       # depth  = 1
        
