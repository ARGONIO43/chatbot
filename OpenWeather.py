import os
import requests
from dotenv import load_dotenv
import telebot

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def process_city(message):
    city_name = message.text
    if city_name:
        weather_report = get_weather(city_name)
        bot.reply_to(message, weather_report)
    else:
        bot.reply_to(message, "No has proporcionado una ciudad. Por favor, intenta de nuevo usando /clima.")

def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={OPENWEATHERMAP_API_KEY}&units=metric&lang=es"
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        print("Respuesta de la API:", data) 

        if data.get('cod') == 200:
            main = data.get('main', {})
            weather = data.get('weather', [{}])[0]
            
            temperature = main.get('temp', 'N/A')
            pressure = main.get('pressure', 'N/A')
            humidity = main.get('humidity', 'N/A')
            description = weather.get('description', 'N/A')

            weather_report = (f"Clima en {city_name}:\n"
                              f"Temperatura: {temperature}°C\n"
                              f"Presión: {pressure} hPa\n"
                              f"Humedad: {humidity}%\n"
                              f"Descripción: {description.capitalize()}")
        else:
            weather_report = f"No se pudo encontrar el clima para {city_name}. Verifica el nombre de la ciudad."
    else:
        weather_report = f"Error en la solicitud a la API de OpenWeatherMap. Código de estado: {response.status_code}"

    return weather_report