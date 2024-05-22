from rest_framework import serializers

from users.models import User
from users.validators import URLValidator, PasswordValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        validators = [URLValidator(field='email'),
                      PasswordValidator(field='password')]
