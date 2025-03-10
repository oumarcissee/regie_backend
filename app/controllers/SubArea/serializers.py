from rest_framework import serializers
from app.models import SubArea

class SubAreaReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubArea
        fields = '__all__'  # Inclut tous les champs, y compris 'custom_id' pour les requêtes GET
        depth  = 1

class SubAreaWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubArea
        exclude = ['ref','id',]  # Exclut 'custom_id' pour les requêtes POST, PUT, PATCH
        # fields = '__all__'
        
