# Generated by Django 5.1 on 2024-10-22 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone', '0026_course_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Logo',
            field=models.CharField(default='img/png-clipart-computer-icons-error-information-error-angle-triangle-thumbnail-removebg-preview copy.png', max_length=255),
        ),
    ]
