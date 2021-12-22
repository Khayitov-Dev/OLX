from django.contrib import admin
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
# Register your models here.

admin.site.register(CategoryCity)
admin.site.register(Child)
admin.site.register(RealEstate)
admin.site.register(Car)
admin.site.register(Work)
admin.site.register(Animals)
admin.site.register(HouseGarden)
admin.site.register(ElectricalEquipment)
admin.site.register(Services)
admin.site.register(FashionStyle)
admin.site.register(HobbyRecreationalSports)
admin.site.register(Free)
admin.site.register(Exchange)
