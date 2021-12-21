from rest_framework import serializers

class ServiceDiscoverySerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    contact = serializers.CharField(required=False)
    default = serializers.CharField(required=False)
    api_roots = serializers.ListField(child=serializers.CharField(), required=False)