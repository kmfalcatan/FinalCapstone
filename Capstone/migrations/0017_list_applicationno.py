# Generated by Django 5.1 on 2024-09-21 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone', '0016_alter_admin_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='ApplicationNo',
            field=models.CharField(default=0, max_length=20),
        ),
    ]