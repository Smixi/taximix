from rest_framework import serializers

from taxii_server.models.api_root import ApiRoot, ApiRootStatus

class ApiRootSerializer(serializers.ModelSerializer):
    
    max_content_length = serializers.SerializerMethodField()

    class Meta:
        model = ApiRoot
        fields = ['id', 'title', 'description', 'versions', 'max_content_length']

    # TODO
    def get_max_content_length(self, obj):
        return -1

class ApiRootStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiRootStatus
        fields = ['id', 'success_count', 'failure_count', 'pending_count']