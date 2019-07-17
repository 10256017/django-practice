from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'last_name',
            'first_name',
            'email',
            'is_superuser',
            'is_staff',
            'is_active',
        ]

    # 客製化組合欄位
    def get_name(self, user):
        return f'{user.first_name} {user.last_name}'.strip()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
