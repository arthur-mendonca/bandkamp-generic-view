from rest_framework import serializers
from albums.models import Album
from albums.serializers import AlbumSerializer

from .models import Song


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ("id", "title", "duration", "album_id")
        read_only_fields = ("id",)

    def create(self, validated_data):
        album_id = self.context["view"].kwargs.get("pk")
        album = Album.objects.get(id=album_id)
        song = Song.objects.create(album=album, **validated_data)

        return song
