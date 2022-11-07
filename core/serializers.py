from rest_framework import serializers
from .models import *
from user.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "date_joined",
            "is_staff",
            "is_active",
            "is_superuser",
            "groups",
            "user_permissions",
            "last_login",
        )


class BuildingsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building_images
        fields = "__all__"


class BulidingsSerializer(serializers.ModelSerializer):
    images = BuildingsImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Building
        fields = "__all__"
        depth = 1


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class HandPickSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandPick
        fields = "__all__"
        depth = 2


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class MessagesSeriallizer(serializers.ModelSerializer):
    customer = UserSerializer()
    agent = UserSerializer()

    class Meta:
        model = Message
        fields = "__all__"


class ChatSerializer(serializers.ModelSerializer):
    chat = MessagesSeriallizer(many=True, read_only=True)
    customer = UserSerializer()

    class Meta:
        model = Chat
        fields = "__all__"
        depth = 3
