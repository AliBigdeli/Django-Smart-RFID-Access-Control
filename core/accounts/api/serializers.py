from rest_framework import serializers
from accounts.models import User, Profile
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import ugettext_lazy as _

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        max_length=128,
        write_only=True,
    )

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password,
            )
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code="authorization")
        data["user"] = user
        return data

class RegisterSerializer(serializers.ModelSerializer):
    """Registration serializer with password checkup"""

    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True
    )
    password1 = serializers.CharField(
        max_length=68, min_length=6, write_only=True
    )

    class Meta:
        model = User
        fields = ["email", "password", "password1"]

    def validate(self, data):
        if data["password"] != data["password1"]:
            raise serializers.ValidationError(
                {"details": "Passwords does not match"}
            )
        return data

    def create(self, validated_data):
        validated_data.pop("password1")
        return User.objects.create_user(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    """Profile serializer to manage extra user info"""

    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
        ]
