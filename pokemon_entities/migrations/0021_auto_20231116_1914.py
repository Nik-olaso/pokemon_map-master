# Generated by Django 2.2.24 on 2023-11-16 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_entities", "0020_auto_20231116_1914"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 16, 19, 14, 11, 403816),
                verbose_name="Появляется",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 17, 0, 14, 11, 403816),
                verbose_name="Исчезает",
            ),
        ),
    ]
