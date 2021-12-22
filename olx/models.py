from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


MONEY = (
    ('EURO','EURO'),
    ('SOM','SOM'),
    ('USD','USD'),
)




Province = (
    ('Andijon viloyati','Andijon viloyati'),
    ('Buxoro viloyati','Buxoro viloyati'),
    ('Fargʻona viloyati','Fargʻona viloyati'),
    ('Jizzax viloyati','Jizzax viloyati'),
    ('Xorazm viloyati','Xorazm viloyati'),
    ('Namangan viloyati','Namangan viloyati'),
    ('Navoiy viloyati','Navoiy viloyati'),
    ('Qashqadaryo viloyati','Qashqadaryo viloyati'),
    ('Qoraqalpogʻiston Respublikasi','Qoraqalpogʻiston Respublikasi'),
    ('Samarqand viloyati','Samarqand viloyati'),
    ('Sirdaryo viloyati','Sirdaryo viloyati'),
    ('Toshkent viloyati','Toshkent viloyati'),
)




class CategoryCity(models.Model):
    province = models.CharField(max_length=255,choices=Province)
    name = models.CharField(max_length=255,null=True)


    class Meta:
        verbose_name_plural = 'Tumanlar'
        

    def __str__(self):
        return self.name




class Base(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category_province = models.CharField(max_length=255,choices=Province)
    category_city = models.ForeignKey(CategoryCity,on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True)
    cost_choice = models.CharField(max_length=255,choices=MONEY)
    cost = models.IntegerField()
    body =  models.TextField()
    picture = models.ImageField(upload_to='images/')



    class Meta:
        abstract=True 

    def __str__(self):
        return self.title







class Child(Base):
    class Meta:
        verbose_name_plural = 'Bolalar Dunyosi'




class RealEstate(Base):
    class Meta:
        verbose_name_plural = "Ko'chmas  Mulk"



class Car(Base):
    class Meta:
        verbose_name_plural = "Transport"



class Work(Base):
    class Meta:
        verbose_name_plural = "Ish"



class Animals(Base):
    class Meta:
        verbose_name_plural = "Hayvonlar"



class HouseGarden(Base):
    class Meta:
        verbose_name_plural = "Uy va bog'"


    

class ElectricalEquipment(Base):
    class Meta:
        verbose_name_plural = "Elektr Jihozlar"



class Services(Base):
    class Meta:
        verbose_name_plural = "Xizmatlar"



class FashionStyle(Base):
    class Meta:
        verbose_name_plural = "Moda va Stil"




class HobbyRecreationalSports(Base):
    class Meta:
        verbose_name_plural = "Hobbi Dam Olish Sport"




class Free(Base):
    class Meta:
        verbose_name_plural = "Tekinga beraman"



class Exchange(Base):
    class Meta:
        verbose_name_plural = "Ayirboshlash"

