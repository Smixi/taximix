from rest_framework import serializers
from taxii_server.models.collection import Collection 

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['title', 'description', 'alias', 'media_types']

class CollectionsListSerializer(serializers.Serializer):
    collections = CollectionSerializer(many=True)

class CollectionRecordSerializer(serializers.Serializer):
    id = serializers.CharField(required=True)
    date_added = serializers.TimeField()
    version = serializers.CharField(required=True)
    media_type = serializers.CharField()


class CollectionManifestSerializer(serializers.Serializer):
    more = serializers.BooleanField()
    objects = CollectionRecordSerializer(many=True)