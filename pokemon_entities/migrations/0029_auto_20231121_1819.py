# Generated by Django 2.2.24 on 2023-11-21 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_entities", "0028_auto_20231117_2119"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 21, 18, 19, 52, 275535),
                verbose_name="Появляется",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="defence",
            field=models.IntegerField(
                blank=True, default=None, null=True, verbose_name="Защита"
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 21, 23, 19, 52, 275535),
                verbose_name="Исчезает",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="health",
            field=models.IntegerField(
                blank=True, default=None, null=True, verbose_name="Здоровье"
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="level",
            field=models.IntegerField(
                blank=True, default=None, null=True, verbose_name="Уровень"
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="stamina",
            field=models.IntegerField(
                blank=True, default=None, null=True, verbose_name="Выносливость"
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="strength",
            field=models.IntegerField(
                blank=True, default=None, null=True, verbose_name="Сила"
            ),
        ),
    ]
