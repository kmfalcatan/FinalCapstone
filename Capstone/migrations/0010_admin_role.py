# Generated by Django 5.1 on 2024-08-31 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone', '0009_studentresponse_avgcet_studentresponse_avggrade'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='Role',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
