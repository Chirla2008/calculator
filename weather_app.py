
import requests
from datetime import datetime

API_KEY = "YOUR_API_KEY"

CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            CURRENT_URL, params=params, timeout=10
        )
        response.raise_for_status()
        data = response.json()

        print("\n===== CURRENT WEATHER =====")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels like:", data["main"]["feels_like"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Condition:", data["weather"][0]["description"].title())
        print("Wind speed:", data["wind"]["speed"], "m/s")

    except requests.exceptions.HTTPError:
        print("Could not get weather. Check city name or API key.")
        return
    except requests.exceptions.RequestException as error:
        print("Network error:", error)
        return
    except (KeyError, ValueError):
        print("Unexpected response from the weather service.")
        return

    get_forecast(city)


def get_forecast(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            FORECAST_URL, params=params, timeout=10
        )
        response.raise_for_status()
        data = response.json()

        print("\n===== FIVE-DAY FORECAST =====")

        # API returns forecasts at 3-hour intervals.
        # Select one forecast per date.
        seen_dates = set()

        for item in data["list"]:
            forecast_date = item["dt_txt"].split(" ")[0]

            if forecast_date not in seen_dates:
                seen_dates.add(forecast_date)

                formatted_date = datetime.strptime(
                    forecast_date, "%Y-%m-%d"
                ).strftime("%d-%m-%Y")

                print("\nDate:", formatted_date)
                print("Temperature:", item["main"]["temp"], "°C")
                print("Humidity:", item["main"]["humidity"], "%")
                print(
                    "Condition:",
                    item["weather"][0]["description"].title()
                )

                if len(seen_dates) == 5:
                    break

    except requests.exceptions.RequestException as error:
        print("Forecast unavailable:", error)
    except (KeyError, ValueError):
        print("Could not process forecast data.")


def main():
    if API_KEY == "YOUR_API_KEY":
        print("Please add your OpenWeather API key first.")
        return

    print("===== WEATHER APP =====")

    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()

        if city.lower() == "exit":
            print("Thank you for using Weather App!")
            break

        if not city:
            print("Please enter a city name.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()
