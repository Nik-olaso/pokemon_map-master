# Generated by Django 2.2.24 on 2023-11-17 18:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_entities", "0026_auto_20231116_1952"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 17, 21, 17, 32, 719273),
                verbose_name="Появляется",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 18, 2, 17, 32, 719273),
                verbose_name="Исчезает",
            ),
        ),
    ]