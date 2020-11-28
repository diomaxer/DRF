from rest_framework import generics, viewsets
from .serializers import CarDetailSerializer, CarListSerializer
from .models import Car
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication


class CarCreateViewSet(viewsets.ModelViewSet):
    serializer_class = CarDetailSerializer


class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAdminUser, )


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
