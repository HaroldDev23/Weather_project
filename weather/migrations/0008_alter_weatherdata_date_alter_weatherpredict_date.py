# Generated by Django 4.2 on 2024-05-25 04:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "weather",
            "0007_alter_weatherdata_couverture_alter_weatherdata_date_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="weatherdata",
            name="date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="weatherpredict",
            name="date",
            field=models.DateField(auto_now_add=True),
        ),
    ]
