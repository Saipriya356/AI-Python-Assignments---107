import requests

API_KEY = "YOUR_API_KEY"   # Replace with your actual API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Fetch weather details for a city using OpenWeather API.
    Extracts:
    - temperature
    - humidity
    - weather description
    Handles errors gracefully.
    """

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)

        # Validation
        if response.status_code == 401:
            print("Error: Invalid API key.")
            return
        
        if response.status_code == 404:
            print("Error: City not found.")
            return

        if response.status_code != 200:
            print("Error: Could not connect to API.")
            return

        data = response.json()

        # Extracting specific values
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        # Display output
        print("\n--- WEATHER REPORT ---")
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.capitalize()}")

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to network.")

    except Exception as e:
        print("Unexpected Error:", e)


# Example call
city_name = input("Enter city name: ")
get_weather(city_name)
