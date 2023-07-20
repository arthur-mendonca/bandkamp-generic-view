from .serializers import SongSerializer
from .models import Song
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer

    def get_queryset(self):
        album_id = self.kwargs.get("pk")
        return Song.objects.filter(album_id=album_id)
