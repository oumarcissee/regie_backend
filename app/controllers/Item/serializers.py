from rest_framework import serializers
from app.models import Item

class ItemReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'  # Inclut tous les champs, y compris 'custom_id' pour les requêtes GET

class ItemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ['ref','id']  # Exclut 'custom_id' pour les requêtes POST, PUT, PATCH
        # fields = '__all__'
        
