# Generated by Django 2.2.24 on 2023-11-23 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_entities", "0029_auto_20231121_1819"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemon",
            name="title",
            field=models.CharField(
                max_length=200, verbose_name="Название Покемон Рус."
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 23, 18, 17, 37, 197379),
                verbose_name="Появляется",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 23, 23, 17, 37, 197379),
                verbose_name="Исчезает",
            ),
        ),
    ]