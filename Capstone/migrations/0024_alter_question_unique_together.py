# Generated by Django 5.1 on 2024-10-05 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone', '0023_remove_grades_percentage'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('text', 'courseName')},
        ),
    ]