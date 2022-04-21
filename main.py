import requests
from datetime import datetime

MY_LAT = 40.000397  # latitude for the location
MY_LNG = -77.631645  # longitude for the locations

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0  # converts the time to 24-hour format
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

print(sunrise)
time_now = datetime.now()
