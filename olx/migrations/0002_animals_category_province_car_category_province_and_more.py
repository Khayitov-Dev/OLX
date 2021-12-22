# Generated by Django 4.0 on 2021-12-14 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animals',
            name='category_province',
            field=models.CharField(choices=[('Andijon viloyati', 'Andijon viloyati'), ('Buxoro viloyati', 'Buxoro viloyati'), ('Fargʻona viloyati', 'Fargʻona viloyati'), ('Jizzax viloyati', 'Jizzax viloyati'), ('Xorazm viloyati', 'Xorazm viloyati'), ('Namangan viloyati', 'Namangan viloyati'), ('Navoiy viloyati', 'Navoiy viloyati'), ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'), ('Qoraqalpogʻiston Respublikasi', 'Qoraqalpogʻiston Respublikasi'), ('Samarqand viloyati', 'Samarqand viloyati'), ('Sirdaryo viloyati', 'Sirdaryo viloyati'), ('Toshkent viloyati', 'Toshkent viloyati')], default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='category_province',
            field=models.CharField(choices=[('Andijon viloyati', 'Andijon viloyati'), ('Buxoro viloyati', 'Buxoro viloyati'), ('Fargʻona viloyati', 'Fargʻona viloyati'), ('Jizzax viloyati', 'Jizzax viloyati'), ('Xorazm viloyati', 'Xorazm viloyati'), ('Namangan viloyati', 'Namangan viloyati'), ('Navoiy viloyati', 'Navoiy viloyati'), ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'), ('Qoraqalpogʻiston Respublikasi', 'Qoraqalpogʻiston Respublikasi'), ('Samarqand viloyati', 'Samarqand viloyati'), ('Sirdaryo viloyati', 'Sirdaryo viloyati'), ('Toshkent viloyati', 'Toshkent viloyati')], default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='child',
            name='category_province',
            field=models.CharField(choices=[('Andijon viloyati', 'Andijon viloyati'), ('Buxoro viloyati', 'Buxoro viloyati'), ('Fargʻona viloyati', 'Fargʻona viloyati'), ('Jizzax viloyati', 'Jizzax viloyati'), ('Xorazm viloyati', 'Xorazm viloyati'), ('Namangan viloyati', 'Namangan viloyati'), ('Navoiy viloyati', 'Navoiy viloyati'), ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'), ('Qoraqalpogʻiston Respublikasi', 'Qoraqalpogʻiston Respublikasi'), ('Samarqand viloyati', 'Samarqand viloyati'), ('Sirdaryo viloyati', 'Sirdaryo viloyati'), ('Toshkent viloyati', 'Toshkent viloyati')], default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electricalequipment',
            name='category_province',
            field=models.CharField(choices=[('Andijon viloyati', 'Andijon viloyati'), ('Buxoro viloyati', 'Buxoro viloyati'), ('Fargʻona viloyati', 'Fargʻona viloyati'), ('Jizzax viloyati', 'Jizzax viloyati'), ('Xorazm viloyati', 'Xorazm viloyati'), ('Namangan viloyati', 'Namangan viloyati'), ('Navoiy viloyati', 'Navoiy viloyati'), ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'), ('Qoraqalpogʻiston Respublikasi', 'Qoraqalpogʻiston Respublikasi'), ('Samarqand viloyati', 'Samarqand viloyati'), ('Sirdaryo viloyati', 'Sirdaryo viloyati'), ('Toshkent viloyati', 'Toshkent viloyati')], default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exchange',
            name='category_province',
            field=models.CharField(choices=[('Andijon viloyati', 'Andijon viloyati'), ('Buxoro viloyati', 'Buxoro viloyati'), ('Fargʻona viloyati', 'Fargʻona viloyati'), ('Jizzax viloyati', 'Jizzax viloyati'), ('Xorazm viloyati', 'Xorazm viloyati'), ('Namangan viloyati', 'Namangan viloyati'), ('Navoiy viloyati', 'Navoiy viloyati'), ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'), ('Qoraqalpogʻiston Respublikasi', 'Qoraqalpogʻiston Respublikasi'), ('Samarqand viloyati', 'Samarqand viloyati'), ('Sirdaryo viloyati', 'Sirdaryo viloyati'), ('Toshkent viloyati', 'Toshkent viloyati')], default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fashionstyle',
            name='category_province',
            field=models.CharField(choices=[('Andijon viloyati', 'Andijon viloyati'), ('Buxoro viloyati', 'Buxoro viloyati'), ('Fargʻona viloyati', 'Fargʻona viloyati'), ('Jizzax viloyati', 'Jizzax viloyati'), ('Xorazm viloyati', 'Xorazm viloyati'), ('Namangan viloyati', 'Namangan viloyati'), ('Navoiy viloyati', 'Navoiy viloyati'), ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'), ('Qoraqalpogʻiston Respublikasi', 'Qoraqalpogʻiston Respublikasi'), ('Samarqand viloyati', 'Samarqand viloyati'), ('Sirdaryo viloyati', 'Sirdaryo viloyati'), ('Toshkent viloyati', 'Toshkent viloyati')], default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='free',
            name='category_province',
            field=models.CharField(choices=[('Andijon viloyati', 'Andijon viloyati'), ('Buxoro viloyati', 'Buxoro viloyati'), ('Fargʻona viloyati', 'Fargʻona viloyati'), ('Jizzax viloyati', 'Jizzax viloyati'), ('Xorazm viloyati', 'Xorazm viloyati'), ('Namangan viloyati', 'Namangan viloyati'), ('Navoiy viloyati', 'Navoiy viloyati'), ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'), ('Qoraqalpogʻiston Respublikasi', 'Qoraqalpogʻiston Respublikasi'), ('Samarqand viloyati', 'Samarqand viloyati'), ('Sirdaryo viloyati', 'Sirdaryo viloyati'), ('Toshkent viloyati', 'Toshkent viloyati')], default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hobbyrecreationalsports',
            name='category_province',
            field=models.CharField(choices=[('Andijon viloyati', 'Andijon viloyati'), ('Buxoro viloyati', 'Buxoro viloyati'), ('Fargʻona viloyati', 'Fargʻona viloyati'), ('Jizzax viloyati', 'Jizzax viloyati'), ('Xorazm viloyati', 'Xorazm viloyati'), ('Namangan viloyati', 'Namangan viloyati'), ('Navoiy viloyati', 'Navoiy viloyati'), ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'), ('Qoraqalpogʻiston Respublikasi', 'Qoraqalpogʻiston Respublikasi'), ('Samarqand viloyati', 'Samarqand viloyati'), ('Sirdaryo viloyati', 'Sirdaryo viloyati'), ('Toshkent viloyati', 'Toshkent viloyati')], default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='housegarden',
            name='category_province',
            field=models.CharField(choices=[('Andijon viloyati', 'Andijon viloyati'), ('Buxoro viloyati', 'Buxoro viloyati'), ('Fargʻona viloyati', 'Fargʻona viloyati'), ('Jizzax viloyati', 'Jizzax viloyati'), ('Xorazm viloyati', 'Xorazm viloyati'), ('Namangan viloyati', 'Namangan viloyati'), ('Navoiy viloyati', 'Navoiy viloyati'), ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'), ('Qoraqalpogʻiston Respublikasi', 'Qoraqalpogʻiston Respublikasi'), ('Samarqand viloyati', 'Samarqand viloyati'), ('Sirdaryo viloyati', 'Sirdaryo viloyati'), ('Toshkent viloyati', 'Toshkent viloyati')], default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='realestate',
            name='category_province',
            field=models.CharField(choices=[('Andijon viloyati', 'Andijon viloyati'), ('Buxoro viloyati', 'Buxoro viloyati'), ('Fargʻona viloyati', 'Fargʻona viloyati'), ('Jizzax viloyati', 'Jizzax viloyati'), ('Xorazm viloyati', 'Xorazm viloyati'), ('Namangan viloyati', 'Namangan viloyati'), ('Navoiy viloyati', 'Navoiy viloyati'), ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'), ('Qoraqalpogʻiston Respublikasi', 'Qoraqalpogʻiston Respublikasi'), ('Samarqand viloyati', 'Samarqand viloyati'), ('Sirdaryo viloyati', 'Sirdaryo viloyati'), ('Toshkent viloyati', 'Toshkent viloyati')], default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='category_province',
            field=models.CharField(choices=[('Andijon viloyati', 'Andijon viloyati'), ('Buxoro viloyati', 'Buxoro viloyati'), ('Fargʻona viloyati', 'Fargʻona viloyati'), ('Jizzax viloyati', 'Jizzax viloyati'), ('Xorazm viloyati', 'Xorazm viloyati'), ('Namangan viloyati', 'Namangan viloyati'), ('Navoiy viloyati', 'Navoiy viloyati'), ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'), ('Qoraqalpogʻiston Respublikasi', 'Qoraqalpogʻiston Respublikasi'), ('Samarqand viloyati', 'Samarqand viloyati'), ('Sirdaryo viloyati', 'Sirdaryo viloyati'), ('Toshkent viloyati', 'Toshkent viloyati')], default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='category_province',
            field=models.CharField(choices=[('Andijon viloyati', 'Andijon viloyati'), ('Buxoro viloyati', 'Buxoro viloyati'), ('Fargʻona viloyati', 'Fargʻona viloyati'), ('Jizzax viloyati', 'Jizzax viloyati'), ('Xorazm viloyati', 'Xorazm viloyati'), ('Namangan viloyati', 'Namangan viloyati'), ('Navoiy viloyati', 'Navoiy viloyati'), ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'), ('Qoraqalpogʻiston Respublikasi', 'Qoraqalpogʻiston Respublikasi'), ('Samarqand viloyati', 'Samarqand viloyati'), ('Sirdaryo viloyati', 'Sirdaryo viloyati'), ('Toshkent viloyati', 'Toshkent viloyati')], default=True, max_length=255),
            preserve_default=False,
        ),
    ]