Telegram Bot

Bot de Telegram desarrollado en Python que utiliza diferentes APIs para obtener información y responder a los usuarios.

Funciones
/start — Muestra las opciones del bot.
/clima — Permite consultar el clima de una ciudad.
/pokemon — Busca información sobre un Pokémon.
/chiste — Obtiene un chiste aleatorio.
APIs utilizadas
Telegram Bot API — Para la comunicación con el bot.
OpenWeather API — Para consultar el clima.
PokéAPI — Para obtener información de Pokémon.
JokeAPI — Para obtener chistes.
Tecnologías
Python
Telebot
Requests
python-dotenv
Instalación

Clona el repositorio e instala las dependencias:

pip install -r requirements.txt

Crea un archivo .env con las claves necesarias:

TELEGRAM_TOKEN=tu_token
OPENWEATHER_API_KEY=tu_api_key

Después ejecuta:

python main.py
Descripción

El proyecto fue realizado como Proyecto Final para PROTECO y ademas para practicar el uso de APIs, peticiones HTTP, manejo de datos JSON y desarrollo de bots utilizando Python.
