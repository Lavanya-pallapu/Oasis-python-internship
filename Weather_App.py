city = input("Enter city name: ")

weather_data = {
    "Hyderabad": {"Temp": "32°C", "Condition": "Sunny"},
    "Mumbai": {"Temp": "29°C", "Condition": "Cloudy"},
    "Delhi": {"Temp": "35°C", "Condition": "Hot"}
}

if city in weather_data:
    print("Temperature:", weather_data[city]["Temp"])
    print("Condition:", weather_data[city]["Condition"])
else:
    print("City not found")