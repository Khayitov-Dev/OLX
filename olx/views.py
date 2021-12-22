from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import render,get_object_or_404
from rest_framework.filters import SearchFilter
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import *
from rest_framework.permissions import *
from olx.serializers import (
    CategoryCitySerializer,
    ChildSerializer,
    RealEstateSerializer,
    CarSerializer,
    WorkSerializer,
    AnimalsSerializer,
    HouseGardenSerializer,
    ElectricalEquipmentSerializer,
    ServicesSerializer,
    FashionStyleSerializer,
    HobbyRecreationalSportsSerializer,
    FreeSerializer,
    ExchangeSerializer,
)
from olx.models import(
    CategoryCity,
    Child,
    RealEstate,
    Car,
    Work,
    Animals,
    HouseGarden,
    ElectricalEquipment,
    Services,
    FashionStyle,
    HobbyRecreationalSports,
    Free,
    Exchange,
)




class CategoryCitySerializerListView(ListCreateAPIView):
    serializer_class = CategoryCitySerializer
    queryset = CategoryCity.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name']

    
    

class ChildListView(ListCreateAPIView):
    serializer_class = ChildSerializer
    queryset = Child.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title','cost']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    


class RealEstateListView(ListCreateAPIView):
    serializer_class = RealEstateSerializer
    queryset = RealEstate.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title','cost']



class CarListView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title','cost']


class WorkListView(ListCreateAPIView):
    serializer_class = WorkSerializer
    queryset = Work.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title','cost']
    


class AnimalsListView(ListCreateAPIView):
    serializer_class = AnimalsSerializer
    queryset = Animals.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title','cost']
    


class HouseGardenListView(ListCreateAPIView):
    serializer_class = HouseGardenSerializer
    queryset = HouseGarden.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title','cost']
    



class ElectricalEquipmentListView(ListCreateAPIView):
    serializer_class = ElectricalEquipmentSerializer
    queryset = ElectricalEquipment.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title','cost']



class ServicesListView(ListCreateAPIView):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title','cost']




class FashionStyleListView(ListCreateAPIView):
    serializer_class = FashionStyleSerializer
    queryset = FashionStyle.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title','cost']



class HobbyRecreationalSportsListView(ListCreateAPIView):
    serializer_class = HobbyRecreationalSportsSerializer
    queryset = HobbyRecreationalSports.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title','cost']




class FreeListView(ListCreateAPIView):
    serializer_class = FreeSerializer
    queryset = Free.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title','cost']



class ExchangeListView(ListCreateAPIView):
    serializer_class = ExchangeSerializer
    queryset = Exchange.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title','cost']