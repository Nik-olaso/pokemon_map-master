# Generated by Django 2.2.24 on 2023-11-16 16:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_entities", "0018_auto_20231116_1905"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemon",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="previous_evolution",
                to="pokemon_entities.Pokemon",
                verbose_name="Из кого эволюционирует",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 16, 19, 9, 58, 928241),
                verbose_name="Появляется",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 17, 0, 9, 58, 928241),
                verbose_name="Исчезает",
            ),
        ),
    ]
