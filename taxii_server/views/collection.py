from taxii_server.models.collection import Collection
from taxii_server.serializers.collection import CollectionSerializer
from .base_view import TaxiServerGenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response


class CollectionViewSet(ListModelMixin, RetrieveModelMixin, TaxiServerGenericViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()