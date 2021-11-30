import requests
city = input('City?\n')
api_url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'q':city,
    'appid':'1c5cb202c26931a604f6f1f087c949fc',
    'units':'metric'
}

res = requests.get(api_url, params=params)
print(res.headers['Content-Type'])
data = res.json()
print(f'Current temp city {city} is {data["main"]["temp"]}')
