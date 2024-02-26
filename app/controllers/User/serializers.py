from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
User = get_user_model()




class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'username',
            'matricule',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'role',
            'password',
        )
