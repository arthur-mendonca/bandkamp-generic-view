from rest_framework.views import Request, Response, status
from django.shortcuts import get_object_or_404


class ListModelMixin:
    def list(self, request: Request) -> Response:
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateModelMixin:
    def create(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RetrieveModelMixin:
    def retrieve(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        lookup_field = kwargs.get(self.lookup_field)
        obj = get_object_or_404(self.get_queryset(), pk=lookup_field)
        serializer = self.serializer_class(obj)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateModelMixin:
    def update(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        lookup_field = kwargs.get(self.lookup_field)
        obj = get_object_or_404(self.get_queryset(), pk=lookup_field)
        serializer = self.serializer_class(obj, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class DestroyModelMixin:
    def destroy(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        lookup_field = kwargs.get(self.lookup_field)
        obj = get_object_or_404(self.get_queryset(), pk=lookup_field)
        obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
