from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email", "password", "name")
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password and returning it"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):

    """Serializer for the user authentication object"""

    email = serializers.CharField()

    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    # attrs are the atributes to validate

    def validate(self, attrs):

        """Validate and authenticate the user"""

        email = attrs.get("email")

        password = attrs.get("password")

        user = authenticate(
            # Acces the context of the request in order to authenticate the user
            request=self.context.get("request"),
            username=email,
            password=password,
        )

        if not user:

            msg = "Unable to authenticate with provided credentials"

            raise serializers.ValidationError(msg, code="authentication")

        attrs["user"] = user

        return attrs
