# Generated by Django 4.2.3 on 2023-07-20 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("canteen", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="food_details",
            name="food_rate",
            field=models.IntegerField(max_length=200),
        ),
    ]
