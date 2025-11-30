import requests

API_KEY = "YOUR_API_KEY"   # Replace with your OpenWeather API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Fetch weather details for a given city using OpenWeather API.
    Includes:
    - Dynamic city input
    - Error handling for invalid city, network issues, wrong API key
    - User-friendly output (Temperature, Humidity, Description)
    """

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)

        # Wrong API key
        if response.status_code == 401:
            print("Error: Invalid API key. Please check your API key.")
            return

        # City not found
        if response.status_code == 404:
            print("Error: City not found. Please enter a valid city.")
            return

        # Other API error
        if response.status_code != 200:
            print("Error: Could not connect to API. Try again later.")
            return

        # Process valid data
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print("\n--- WEATHER REPORT ---")
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.capitalize()}")

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please check your internet connection.")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the network.")

    except Exception as e:
        print("Unexpected Error:", e)


# Example Dynamic Input
city_name = input("Enter a city name: ")
get_weather(city_name)
