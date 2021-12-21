from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from taxii_server.views.collection import CollectionViewSet
from taxii_server.views.server_discovery import ServerDiscoveryViewSet
from taxii_server.views.api_root import ApiRootStatusViewSet, ApiRootViewSet

# Create your views here.
router = DefaultRouter()
router.register(r'taxii2', ServerDiscoveryViewSet, basename="server_discovery")
router.register(r'', ApiRootViewSet, basename='api-root')

api_root_router = routers.NestedDefaultRouter(router, r'', lookup='api_root')
api_root_router.register('status', ApiRootStatusViewSet, 'status')
api_root_router.register('collections', CollectionViewSet, 'collections')

collection_router = routers.NestedDefaultRouter(api_root_router, r'collections', lookup='collection')

urlspattern = [
    path(r'', include(router.urls)),
    path(r'', include(api_root_router.urls)),
]