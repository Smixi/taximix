from .base_view import TaxiServerGenericViewSet, TaxiServerView, TaxiServerViewSet
from taxii_server.serializers.api_root import ApiRootSerializer, ApiRootStatusSerializer
from rest_framework.mixins import RetrieveModelMixin
from taxii_server.models.api_root import ApiRoot
from rest_framework.response import Response

class ApiRootViewSet(RetrieveModelMixin, TaxiServerGenericViewSet):
    
    serializer_class = ApiRootSerializer
    queryset = ApiRoot.objects.all()

class ApiRootStatusViewSet(TaxiServerViewSet):

    def retrieve(self, request, pk=None, api_root_pk=None):
        api_root: ApiRoot = ApiRoot.objects.get(id=api_root_pk)
        serializer = ApiRootStatusSerializer(api_root.status, many=True)
        return Response(serializer.data)