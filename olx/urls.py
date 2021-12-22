from django.urls import path
from olx.views import (
    CategoryCitySerializerListView,
    ChildListView,
    RealEstateListView,
    CarListView,
    WorkListView,
    AnimalsListView,
    HouseGardenListView,
    ElectricalEquipmentListView,
    ServicesListView,
    FashionStyleListView,
    HobbyRecreationalSportsListView,
    FreeListView,
    ExchangeListView
    )

urlpatterns = [
    path('',CategoryCitySerializerListView.as_view()),
    path('child/',ChildListView.as_view()),
    path('real-estate/',RealEstateListView.as_view()),
    path('car/',CarListView.as_view()),
    path('work/',WorkListView.as_view()),
    path('animals/',AnimalsListView.as_view()),
    path('house-garden/',HouseGardenListView.as_view()),
    path('electer/',ElectricalEquipmentListView.as_view()),
    path('service/',ServicesListView.as_view()),
    path('fashion/',FashionStyleListView.as_view()),
    path('hobby/',HobbyRecreationalSportsListView.as_view()),
    path('free/',FreeListView.as_view()),
    path('exchange/',ExchangeListView.as_view()),
]