import os
from dotenv import load_dotenv
import telebot
from OpenWeather import get_weather
from PokApi import get_pokemon_info
from Jokes import get_joke  


load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    bot.reply_to(message, ("Hola soy el bot de Antonio :D. "
                           "Usa /clima para obtener el clima de una ciudad, /pokemon para obtener información sobre un Pokémon, y /joke para recibir un chiste (son en ingles :p)."))


@bot.message_handler(commands=["clima"])
def cmd_clima(message):
    msg = bot.reply_to(message, "Por favor, proporciona el nombre de la ciudad.")
    bot.register_next_step_handler(msg, ciudadprocesada)

def ciudadprocesada(message):
    city_name = message.text
    if city_name:
        weather_report = get_weather(city_name)
        bot.reply_to(message, weather_report)
    else:
        bot.reply_to(message, "No has proporcionado una ciudad. Por favor, intenta de nuevo usando /clima.")

@bot.message_handler(commands=["pokemon"])
def cmd_pokemon(message):
    msg = bot.reply_to(message, "Por favor, proporciona el nombre del Pokémon.")
    bot.register_next_step_handler(msg, pokemones)

def pokemones(message):
    pokemon_name = message.text
    if pokemon_name:
        pokemon_info, image_url = get_pokemon_info(pokemon_name)
        bot.reply_to(message, pokemon_info)
        if image_url:
            bot.send_photo(message.chat.id, image_url)
    else:
        bot.reply_to(message, "No has proporcionado un nombre de Pokémon. Por favor, intenta de nuevo usando /pokemon.")

@bot.message_handler(commands=["joke"])
def cmd_joke(message):
    msg = bot.reply_to(message, "Por favor, elige una categoría de chistes: Programming, Misc, Dark, Pun, Spooky, Christmas, o Any.")
    bot.register_next_step_handler(msg, process_joke_category)

def process_joke_category(message):
    category = message.text.capitalize()
    valid_categories = ["Programming", "Misc", "Dark", "Pun", "Spooky", "Christmas", "Any"]

    if category in valid_categories:
        joke = get_joke(category)
        bot.reply_to(message, joke)
    else:
        bot.reply_to(message, "Categoría no válida. Usa /joke e intenta de nuevo.")

@bot.message_handler(func=lambda message: True)
def handle_default(message):
    bot.reply_to(message, "Comando no reconocido. Usa /help para ver los comandos disponibles.")

if __name__ == '__main__':
    print("Bot iniciando...")
    try:
        bot.polling()
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        print("El bot ha terminado de ejecutarse.")

  