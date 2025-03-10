from rest_framework import serializers
from app.models import Discharge

class DischargeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discharge
        fields = '__all__'  # Inclut tous les champs, y compris 'custom_id' pour les requêtes GET
        depth  = 1

class DischargeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discharge
        exclude = ['ref']  # Exclut 'custom_id' pour les requêtes POST, PUT, PATCH
        # fields = '__all__'
        
