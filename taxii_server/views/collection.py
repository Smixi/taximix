from rest_framework.response import Response
from taxii_server.models.collection import Collection
from taxii_server.serializers.collection import CollectionManifestSerializer, CollectionSerializer, CollectionsListSerializer
from taxii_server.services.collection import get_service_manifests
from .base_view import TaxiServerGenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.decorators import action


class CollectionViewSet(RetrieveModelMixin, TaxiServerGenericViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(api_root=self.kwargs.get('api_root_pk'))

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer({'collections': queryset})
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def manifest(self, request, pk, *args, **kwargs):
        collection = self.get_object()
        manifests = get_service_manifests(collection)
        serializer = CollectionManifestSerializer(manifests)
        return Response(serializer.data)


    def get_serializer_class(self):
        if self.action == 'list':
            return CollectionsListSerializer

        return super().get_serializer_class()