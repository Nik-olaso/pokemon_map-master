# Generated by Django 2.2.24 on 2023-11-23 16:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_entities", "0031_auto_20231123_1850"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pokemon",
            name="descendant",
        ),
        migrations.RemoveField(
            model_name="pokemon",
            name="parent",
        ),
        migrations.AddField(
            model_name="pokemon",
            name="previous_evolution",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="next_evolutions",
                to="pokemon_entities.Pokemon",
                verbose_name="Из кого эволюционирует",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 23, 19, 49, 58, 846874),
                verbose_name="Появляется",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 24, 0, 49, 58, 846874),
                verbose_name="Исчезает",
            ),
        ),
    ]
