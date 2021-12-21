from taxii_server.serializers.service_discovery import ServiceDiscoverySerializer
from taxii_server.services.service_discovery import get_services_info
from .base_view import TaxiServerViewSet
from rest_framework.response import Response


class ServerDiscoveryViewSet(TaxiServerViewSet):

    def list(self, request):
        services_info = get_services_info()
        serializer = ServiceDiscoverySerializer(data=services_info)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)