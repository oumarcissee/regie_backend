from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'role',
            'email',
            'address',
            'username',
            'is_active',
            'matricule',
            'last_name',
            'first_name',
            'phone_number',
        )
        

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'
        