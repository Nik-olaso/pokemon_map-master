from django.db import models
import datetime
from datetime import timedelta


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название Покемон Рус.")
    title_en = models.CharField(
        max_length=200, blank=True, verbose_name="Название Покемон Англ."
    )
    title_jp = models.CharField(
        max_length=200, blank=True, verbose_name="Название Покемон Япн."
    )
    description = models.TextField(blank=True, verbose_name="Описание Покемона")
    photo = models.ImageField(blank=True, null=True, verbose_name="Фото Покемона")
    previous_evolution = models.ForeignKey(
        "Pokemon",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Из кого эволюционирует",
        related_name="next_evolutions",
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Покемон",
        related_name="pokemons",
    )
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(verbose_name="Появляется", default=None)
    disappeared_at = models.DateTimeField(verbose_name="Исчезает", default=None)
    level = models.IntegerField(
        verbose_name="Уровень",
        blank=True,
        null=True,
    )
    health = models.IntegerField(
        verbose_name="Здоровье",
        blank=True,
        null=True,
    )
    strength = models.IntegerField(
        verbose_name="Сила",
        blank=True,
        null=True,
    )
    defence = models.IntegerField(verbose_name="Защита", blank=True, null=True)
    stamina = models.IntegerField(
        verbose_name="Выносливость",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.pokemon}:{self.latitude}-{self.longitude}"
