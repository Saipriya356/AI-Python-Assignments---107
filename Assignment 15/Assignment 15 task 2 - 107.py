import requests
import json

API_KEY = "YOUR_API_KEY"   # Replace with your real API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Fetch weather details for a city using OpenWeather API.
    Handles:
    - Invalid URL
    - Wrong API key
    - Network timeout
    - City not found
    """

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        # API call with timeout
        response = requests.get(BASE_URL, params=params, timeout=5)

        # If API URL is wrong or API key incorrect
        if response.status_code == 401:
            print("Error: Invalid API key. Please check your key.")
            return

        if response.status_code == 404:
            print("Error: City not found. Please enter a valid city name.")
            return

        # For other unexpected HTTP codes
        if response.status_code != 200:
            print("Error: Could not connect to API. Please try again later.")
            return

        # Convert to JSON
        data = response.json()

        print("\n--- WEATHER DETAILS (JSON) ---")
        print(json.dumps(data, indent=4))

    except requests.exceptions.Timeout:
        print("Error: Connection timed out. Please check your network.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check your network connection.")

    except Exception as e:
        print("Unexpected Error:", e)


# Example call
city_name = input("Enter city name: ")
get_weather(city_name)
