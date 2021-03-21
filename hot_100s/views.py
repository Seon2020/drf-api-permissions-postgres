from hot_100s.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from .serializer import HitsSerializer
from .models import Hits

class HitsList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Hits.objects.all()
    serializer_class = HitsSerializer

class HitsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Hits.objects.all()
    serializer_class = HitsSerializer
    