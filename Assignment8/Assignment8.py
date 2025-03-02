import requests

def get_weather_data(city, api_key):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    url = f"{base_url}appid={api_key}&q={city}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:  
        return response.json() 
    else:
        print("Error:", response.status_code, response.json().get('message'))
        return None

def display_weather_info(weather_data):
    if weather_data:
        city_name = weather_data.get('name')
        country = weather_data.get('sys', {}).get('country')
        temperature = weather_data.get('main', {}).get('temp')
        wind_speed = weather_data.get('wind', {}).get('speed')
        description = weather_data.get('weather', [{}])[0].get('description')
        
        print(f"Weather in {city_name}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description}")
    else:
        print("No weather data to display.")

# Create an account on "https://openweathermap.org/" and enter your own api key.
def main():
    api_key = '1c8b5e9ee02a4d3e8662d6c137515f0e' 
    city = input("Enter the city: ")  # Get city name from user
    weather_data = get_weather_data(city, api_key)  # Fetch weather data
    display_weather_info(weather_data)  # Display weather info


if __name__ == "__main__":  
    main()
