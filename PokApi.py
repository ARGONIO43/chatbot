import os
from dotenv import load_dotenv
import requests
import telebot

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
POKEAPI_BASE_URL = "https://pokeapi.co/api/v2"
bot = telebot.TeleBot(TELEGRAM_TOKEN)

def pokemones(message):
    pokemon_name = message.text
    if pokemon_name:
        pokemon_info = get_pokemon_info(pokemon_name)
        bot.reply_to(message, pokemon_info)
    else:
        bot.reply_to(message, "No has proporcionado un nombre de Pokémon. Por favor, intenta de nuevo usando /pokemon.")

def get_pokemon_info(pokemon_name):
    url = f"{POKEAPI_BASE_URL}/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        name = data['name'].capitalize()
        types = ', '.join([t['type']['name'] for t in data['types']])
        abilities = ', '.join([a['ability']['name'] for a in data['abilities']])
        stats = ', '.join([f"{stat['stat']['name'].capitalize()}: {stat['base_stat']}" for stat in data['stats']])
        image_url = data['sprites']['front_default']
        
        pokemon_info = (f"Pokémon: {name}\n"
                        f"Tipos: {types}\n"
                        f"Habilidades: {abilities}\n"
                        f"Estadísticas: {stats}")
        return pokemon_info, image_url
    else:
        pokemon_info = f"No se pudo obtener información sobre el Pokémon {pokemon_name}. Por favor, verifica el nombre."

    return pokemon_info
