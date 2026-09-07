import requests

def get_joke(category="Any"):
    url = f"https://v2.jokeapi.dev/joke/{category}?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if data.get("type") == "single":
            return data["joke"]
        elif data.get("type") == "twopart":
            return f"{data['setup']}\n\n{data['delivery']}"
        else:
            return "No se pudo obtener un chiste en este momento."
    else:
        return "Error al conectar con la API de chistes."
