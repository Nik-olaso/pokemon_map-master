# Generated by Django 2.2.24 on 2023-11-26 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_entities", "0032_auto_20231123_1949"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 26, 17, 50, 47, 959095),
                verbose_name="Появляется",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 26, 22, 50, 47, 959095),
                verbose_name="Исчезает",
            ),
        ),
    ]
