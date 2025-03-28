from rest_framework import serializers
from app.models import OtherSpend

class OtherSpendReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherSpend
        fields = '__all__'  # Inclut tous les champs, y compris 'custom_id' pour les requêtes GET
        depth  = 1

class OtherSpendWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherSpend
        # exclude = ['id']  # Exclut 'custom_id' pour les requêtes POST, PUT, PATCH
        fields = '__all__'
