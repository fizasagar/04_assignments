import requests 

#  Function to get weather details
def get_weather(city):
    api_key = "9040e12fdd89f84b68f576d3200e0bf4"  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)  #  Fetch data from API
        data = response.json()  #  Convert response to JSON format

        if data["cod"] == 200:  #  If city is found
            temp = data["main"]["temp"]  # Get temperature
            weather = data["weather"][0]["description"]  #  Get weather condition
            humidity = data["main"]["humidity"]  #  Get humidity level

            # 📌 Show the weather details
            print("\n🌍 Weather Details for", city)
            print(f"🌡️ Temperature: {temp}°C")
            print(f"☁️  Condition: {weather}")
            print(f"💧 Humidity: {humidity}%\n")

        else:  #  If city is not found
            print("\n🚫 City not found! Please enter a valid city name.\n")

    except Exception as e:
        print("\n⚠️ Error fetching data. Check your internet connection.\n")

#  Start the program
if __name__ == "__main__":
    print("\nWelcome To My Weather Program 🌤️")
    city_name = input("Enter city name: ")  #  User enters a city
    get_weather(city_name)  #  Call function to get weather
