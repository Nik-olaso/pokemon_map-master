import folium
import json
from django.utils import timezone
from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity
from django.shortcuts import get_object_or_404

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision"
    "/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832"
    "&fill=transparent"
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    time = timezone.localtime()
    pokemon_entities = PokemonEntity.objects.filter(
        appeared_at__lte=time, disappeared_at__gte=time
    )
    pokemons = Pokemon.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        img_url = request.build_absolute_uri(pokemon_entity.pokemon.photo.url)
        add_pokemon(
            folium_map, pokemon_entity.latitude, pokemon_entity.longitude, img_url
        )

    pokemons_on_page = []
    for pokemon in pokemons:
        img_url = request.build_absolute_uri(pokemon.photo.url)
        pokemons_on_page.append(
            {
                "pokemon_id": pokemon.pk,
                "img_url": img_url,
                "title_ru": pokemon.title,
            }
        )
        print(pokemons_on_page)

    return render(
        request,
        "mainpage.html",
        context={
            "map": folium_map._repr_html_(),
            "pokemons": pokemons_on_page,
        },
    )


def show_pokemon(request, pokemon_id):
    pokemons = get_object_or_404(Pokemon, pk=pokemon_id)
    if pokemons.pk == int(pokemon_id):
        pokemon_entities = PokemonEntity.objects.filter(pokemon=pokemons)
    previous_evolutions_info = {}
    next_evolutions_info = {}
    previous_evolutions = pokemons.previous_evolution
    next_evolutions = pokemons.next_evolutions.first()
    if previous_evolutions:
        previous_evolutions_info = {
            "title_ru": previous_evolutions.title,
            "pokemon_id": previous_evolutions.pk,
            "img_url": request.build_absolute_uri(previous_evolutions.photo.url),
        }

    if next_evolutions:
        next_evolutions_info = {
            "title_ru": next_evolutions.title,
            "pokemon_id": next_evolutions.pk,
            "img_url": request.build_absolute_uri(next_evolutions.photo.url),
        }
    pokemon_identity = {
        "title_ru": pokemons.title,
        "title_en": pokemons.title_en,
        "title_jp": pokemons.title_jp,
        "description": pokemons.description,
        "img_url": request.build_absolute_uri(pokemons.photo.url),
        "next_evolution": next_evolutions_info,
        "previous_evolution": previous_evolutions_info,
    }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.latitude,
            pokemon_entity.longitude,
            request.build_absolute_uri(pokemons.photo.url),
        )

    return render(
        request,
        "pokemon.html",
        context={"map": folium_map._repr_html_(), "pokemon": pokemon_identity},
    )
