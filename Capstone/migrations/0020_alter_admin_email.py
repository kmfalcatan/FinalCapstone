# Generated by Django 5.1 on 2024-09-21 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone', '0019_alter_admin_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='Email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
