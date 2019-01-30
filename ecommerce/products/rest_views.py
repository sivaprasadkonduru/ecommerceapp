from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Stores
from .serializers import StoreSerializer


class StoreViewAPI(ListAPIView):

    queryset = Stores.objects.all()
    serializer_class = StoreSerializer


class StoreRetrieveAPI(RetrieveAPIView):

    queryset = Stores.objects.all()
    serializer_class = StoreSerializer


class StoreViewSet(ModelViewSet):

    queryset = Stores.objects.all()
    serializer_class = StoreSerializer