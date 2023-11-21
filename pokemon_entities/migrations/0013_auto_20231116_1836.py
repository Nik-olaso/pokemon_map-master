# Generated by Django 2.2.24 on 2023-11-16 15:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_entities", "0012_auto_20231116_1827"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pokemon",
            name="descendant",
        ),
        migrations.AddField(
            model_name="pokemon",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="pokemon_entities.Pokemon",
                verbose_name="Из кого эволюционирует",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 16, 18, 36, 12, 982383),
                verbose_name="Появляется",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 16, 23, 36, 12, 982383),
                verbose_name="Исчезает",
            ),
        ),
    ]
