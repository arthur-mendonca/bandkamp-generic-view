from rest_framework.views import Request, Response, APIView
from utils.mixin import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)


class GenericAPIView(APIView):
    queryset = None
    serializer_class = None
    lookup_field = "pk"


class ListAPIView(GenericAPIView, ListModelMixin):
    def get(self, request: Request) -> Response:
        return super().list(request)


class CreateAPIView(GenericAPIView, CreateModelMixin):
    def post(self, request: Request) -> Response:
        return super().create(request)


class RetrieveAPIView(GenericAPIView, RetrieveModelMixin):
    def get(self, request: Request, *args, **kwargs) -> Response:
        return super().retrieve(request, *args, **kwargs)


class UpdateAPIView(GenericAPIView, UpdateModelMixin):
    def patch(self, request: Request, *args, **kwargs) -> Response:
        return super().update(request, *args, **kwargs)


class DestroyAPIView(GenericAPIView, DestroyModelMixin):
    def delete(self, request: Request, *args, **kwargs) -> Response:
        return super().destroy(request, *args, **kwargs)


class ListCreateAPIView(ListAPIView, CreateAPIView):
    pass


class RetrieveUpdateAPIView(RetrieveAPIView, UpdateAPIView):
    pass
