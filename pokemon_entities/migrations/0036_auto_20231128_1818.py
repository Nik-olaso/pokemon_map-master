# Generated by Django 2.2.24 on 2023-11-28 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_entities", "0035_auto_20231128_1816"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 28, 18, 18, 53, 4740),
                verbose_name="Появляется",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(default=None, verbose_name="Исчезает"),
        ),
    ]