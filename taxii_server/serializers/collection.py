from rest_framework import serializers
from taxii_server.models.collection import Collection 

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['title', 'description', 'alias', 'media_types']