# Generated by Django 5.1 on 2024-08-31 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone', '0011_list_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='Address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='list',
            name='AvgCet',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='list',
            name='AvgGrade',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='list',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='list',
            name='Number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='list',
            name='Status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
