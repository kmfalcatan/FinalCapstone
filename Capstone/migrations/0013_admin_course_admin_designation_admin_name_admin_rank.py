# Generated by Django 5.1 on 2024-09-01 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone', '0012_alter_list_address_alter_list_avgcet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='Course',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AddField(
            model_name='admin',
            name='Designation',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AddField(
            model_name='admin',
            name='Name',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AddField(
            model_name='admin',
            name='Rank',
            field=models.CharField(default='null', max_length=255),
        ),
    ]