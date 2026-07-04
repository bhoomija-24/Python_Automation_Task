import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        current = data["current_condition"][0]

        print("\n------ Weather Report ------")
        print("City:", city.title())
        print("Temperature:", current["temp_C"], "°C")
        print("Humidity:", current["humidity"], "%")
        print("Weather:", current["weatherDesc"][0]["value"])
        print("Wind Speed:", current["windspeedKmph"], "km/h")

    else:
        print("Unable to fetch weather data.")

except Exception as e:
    print("Error:", e)