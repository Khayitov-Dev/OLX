from django.db import models
from django.db.models import fields
from rest_framework import serializers
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




class CategoryCitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CategoryCity




class ChildSerializer(serializers.ModelSerializer):
    name = CategoryCitySerializer(many=True)
    class Meta:
        fields = ['category_province','category_city','title','cost_choice','cost','body','picture','name']
        model = Child



class RealEstateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = RealEstate



class CarSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Car



class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Work



class AnimalsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Animals



class HouseGardenSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = HouseGarden



class ElectricalEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ElectricalEquipment




class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Services




class FashionStyleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = FashionStyle




class HobbyRecreationalSportsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = HobbyRecreationalSports




class FreeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Free



class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Exchange
