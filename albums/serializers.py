from rest_framework import serializers
from .models import Album
from users.serializers import UserSerializer


class AlbumSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ("id", "name", "year", "user")
        read_only_fields = ("id",)

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        return Album.objects.create(**validated_data)

    def update(self, instance: Album, validated_data: dict) -> Album:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
