from rest_framework import serializers
from app.models import Order

class OrderReadSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Order
        fields = '__all__'  # Inclut tous les champs, y compris 'custom_id' pour les requêtes GET
        depth  = 1

class OrderWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Order
        exclude = ['ref','id',]  # Exclut 'custom_id' pour les requêtes POST, PUT, PATCH
        # fields = '__all__'
       # depth  = 1
        
