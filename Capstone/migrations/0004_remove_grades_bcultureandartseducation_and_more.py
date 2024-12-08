# Generated by Django 5.1 on 2024-08-12 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grades',
            name='BCultureandArtsEducation',
        ),
        migrations.RemoveField(
            model_name='grades',
            name='BSAgriculturalandBiosystemsEngineering',
        ),
        migrations.RemoveField(
            model_name='grades',
            name='BSExerciseandSportScience',
        ),
        migrations.RemoveField(
            model_name='grades',
            name='BSNutritionandDietetics',
        ),
        migrations.RemoveField(
            model_name='grades',
            name='BSPhysicalEducatio',
        ),
        migrations.RemoveField(
            model_name='grades',
            name='BSPsycology',
        ),
        migrations.AddField(
            model_name='grades',
            name='BSPhysicalEducation',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='grades',
            name='BSPsychology',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='AComputerTechnology',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='AvgCet',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='AvgGrade',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BAEnglish',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BAHistory',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BAMCBroadcasting',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BAMCJournalism',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BAPoliticalScience',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BEarlyChildhoodEducation',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BElementaryEducation',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSAccountancy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSAgribusiness',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSAgriculture',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSAgricultureTechnology',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSAgroforestry',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSArchitecture',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSCivilEngineering',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSCommunityDevelopment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSComputerEngineering',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSComputerScience',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSEconomics',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSElectricalEngineering',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSElectronicsEngineering',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSEnvironmentScience',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSEnvironmentalEngineering',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSFoodTechnology',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSForestry',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSGeodeticEngineering',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSHomeEconomics',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSIndustrialEngineering',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSInformationTechnology',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSLaws',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSMechanicalEngineering',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSNursing',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSPublicAdministration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSSanitaryEngineering',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSSocialWork',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSecondaryEducation',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='BSpecialNeedsEducation',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='TotalScore',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='grades',
            name='BCultureAndArtsEducation',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='grades',
            name='BSAgriculturalAndBiosystemsEngineering',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='grades',
            name='BSExerciseAndSportScience',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='grades',
            name='BSNutritionAndDietetics',
            field=models.IntegerField(default=0),
        ),
    ]
