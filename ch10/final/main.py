from WeatherAPI import WeatherAPI
from NewsAPI import NewsAPI
from LocationAPI import LocationAPI

def main():
    weather_api_key = "ee97496a792dc438e2cdaa5b0c2a8480"
    news_api_key = "99bbe9cd55284890be56ba839652fd45"
    location_api_key = "dc5fa6d70c124f4286932e3d0995587e"

    city = input("What city would you like: ")

    location_api = LocationAPI(location_api_key)
    weather_api = WeatherAPI(weather_api_key)
    news_api = NewsAPI(news_api_key)
    
    location_data = location_api.get(city)
    weather_data = weather_api.get(city)
    news_data = news_api.get(city)
    
    lat, lng = location_data['lat'], location_data['lng']
    temp = round(weather_data['main']['temp'] - 273.15, 2)
    description = weather_data['weather'][0]['description'].capitalize()

    news_headlines = [article['title'] for article in news_data['articles']]
    
    print(f"\nLocation data for {city}:")
    print(f"Latitude: {lat}, Longitude: {lng}")
    print(f"\nCurrent weather in {city}: {temp}°C and {description}")
    print("Top news headlines:")
    for headline in news_headlines:
        print("- " + headline)

main()