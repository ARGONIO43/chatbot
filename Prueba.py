from OpenWeather import get_weather

def test_weather():
    city_name = "Madrid" 
    print(get_weather(city_name))

if __name__ == '__main__':
    test_weather()
