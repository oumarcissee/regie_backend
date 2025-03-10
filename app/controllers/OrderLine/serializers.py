from rest_framework import serializers
from app.models import  OrderLine

class OrderLineReadSerializer(serializers.ModelSerializer):
    class Meta:
        model  = OrderLine
        fields = '__all__'  # Inclut tous les champs, y compris 'custom_id' pour les requêtes GET
        depth  = 1

class OrderLineWriteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model   = OrderLine
        # exclude = ['ref']  # Exclut 'custom_id' pour les requêtes POST, PUT, PATCH
       # depth  = 1
        
