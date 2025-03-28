from rest_framework import serializers
from app.models import Archives

class ArchivesReadSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Archives
        fields = '__all__'  # Inclut tous les champs, y compris 'custom_id' pour les requêtes GET
        depth  = 1

class ArchivesWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Archives
        exclude = ['nomber_of_days']  # Exclut 'custom_id' pour les requêtes POST, PUT, PATCH