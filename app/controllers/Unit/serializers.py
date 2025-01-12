from rest_framework import serializers
from app.models import Unit

class UnitReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'  # Inclut tous les champs, y compris 'custom_id' pour les requêtes GET
        depth  = 1

class UnitWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        exclude = ['ref','id']  # Exclut 'custom_id' pour les requêtes POST, PUT, PATCH
        # fields = '__all__'
        
