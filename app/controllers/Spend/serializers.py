from rest_framework import serializers
from app.models import Spend

class SpendReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spend
        fields = '__all__'  # Inclut tous les champs, y compris 'custom_id' pour les requêtes GET
        depth  = 1

class SpendWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spend
        exclude = ['ref','id']  # Exclut 'custom_id' pour les requêtes POST, PUT, PATCH
        # fields = '__all__'
