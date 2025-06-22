import requests

api = "5d75e0a0e17640a8871183201252206"
city = "lagos"
url = f"http://api.weatherapi.com/v1/current.json?key={api}&q={city}"

weather = requests.get(url)
print(weather)

if weather.status_code == 200:
    data = weather.json()
    city = data['location']['name'] 
    country = data['location']['country'] 
    temp = data['current']['temp_c']
    condition = data['current']['condition']['text']

    print(f"Weather in {city}, {country}: {condition}, {temp}°C")
else:
    print("Something went wrong:", weather.status_code)