# Generated by Django 2.2.24 on 2023-11-30 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0037_auto_20231128_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='pokemon_entities.Pokemon', verbose_name='Покемон'),
        ),
    ]
