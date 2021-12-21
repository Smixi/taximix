from rest_framework import generics, viewsets, views

class TaxiServerView(views.APIView):
    pass

class TaxiServerViewSet(viewsets.ViewSetMixin, TaxiServerView):
    pass

class TaxiServerGenericView(generics.GenericAPIView):
    pass

class TaxiServerGenericViewSet(viewsets.ViewSetMixin, TaxiServerGenericView):
    pass