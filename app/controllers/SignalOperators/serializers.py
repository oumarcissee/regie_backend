from rest_framework import serializers
from app.models import SignalOperators

class SignalOperatorsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignalOperators
        fields = '__all__'  # Inclut tous les champs, y compris 'custom_id' pour les requêtes GET

class SignalOperatorsWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignalOperators
        exclude = ['ref']  # Exclut 'custom_id' pour les requêtes POST, PUT, PATCH
        # fields = '__all__'
        
