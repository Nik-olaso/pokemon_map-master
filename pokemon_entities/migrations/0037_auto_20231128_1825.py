# Generated by Django 2.2.24 on 2023-11-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_entities", "0036_auto_20231128_1818"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(default=None, verbose_name="Появляется"),
        ),
    ]