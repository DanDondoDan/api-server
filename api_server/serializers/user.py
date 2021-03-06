import logging

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from api_server import models
from rest_framework.authtoken.models import Token

logger = logging.getLogger(__name__)


_MODE_USERS = {
    'MODE_EMPLOYEE': models.Person,
    'MODE_CUSTOMER': models.Customer,

}

class PasswordValidator:
    def __call__(self, value):
        if not value:
            return

        error = validate_password(value)
        if error:
            message = error
            raise serializers.ValidationError(message)


class UserPublicSerializer(serializers.ModelSerializer):
    mode = serializers.ReadOnlyField()

    class Meta:
        model = models.User
        fields = ('email', 'phone', 'birth', )

class UserPrivateSerializer(UserPublicSerializer):
    token = serializers.ReadOnlyField(source='auth_token.key')

    class Meta:
        model = models.User
        fields = UserPublicSerializer.Meta.fields + ('token',)


class UserCreateSerializer(UserPublicSerializer):
    password = serializers.CharField(validators=[PasswordValidator()], allow_blank=True)
    phone = serializers.CharField(allow_blank=True, required=False)
    birth = serializers.DateField(required=True)
    
    mode = serializers.ChoiceField(choices=models.User.MODE_USERS)

    class Meta:
        model = models.User
        write_only_fields = 'password'
        fields = UserPublicSerializer.Meta.fields + ('password', 'mode', )
        extra_kwargs = {
            'password': {'write_only': True},
            'phone': {'required': False},
        }

    def create(self, validated_data):
        mode = validated_data['mode']
        # user = models.User.objects.create(**validated_data)
        user = super().create(validated_data)
        for i in _MODE_USERS:
            _MODE_USERS[i].create(user=user)
        return user


class ResetPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(validators=[PasswordValidator()])

    class Meta:
        model = models.User
        fields = ('password',)