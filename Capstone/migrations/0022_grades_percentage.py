# Generated by Django 5.1 on 2024-10-05 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone', '0021_question_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='grades',
            name='Percentage',
            field=models.IntegerField(default=0),
        ),
    ]
