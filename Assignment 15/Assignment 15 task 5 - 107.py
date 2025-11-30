import requests
import json
import os

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeather API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
RESULT_FILE = "results.json"


def get_weather(city):
    """
    Fetch weather details for a given city using OpenWeather API.
    Includes:
    - API error handling
    - Friendly output formatting
    - JSON formatted response
    - Appending results to a local JSON file
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

        # Extract valid data
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        # Prepare weather JSON object
        weather_result = {
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "weather": description
        }

        # ---- Display User-Friendly Output ----
        print("\n--- WEATHER REPORT ---")
        print(json.dumps(weather_result, indent=4))

        # ---- Save to Local File (Append Mode) ----
        if os.path.exists(RESULT_FILE):
            with open(RESULT_FILE, "r") as f:
                existing_data = json.load(f)
        else:
            existing_data = []

        # Append new result
        existing_data.append(weather_result)

        # Write back to JSON file
        with open(RESULT_FILE, "w") as f:
            json.dump(existing_data, f, indent=4)

        print(f"\n✔ Weather data saved to {RESULT_FILE}")

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please check your internet connection.")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the network.")

    except Exception as e:
        print("Unexpected Error:", e)


# ---- Example Run ----
if __name__ == "__main__":
    city_name = input("Enter a city name: ")
    get_weather(city_name)
