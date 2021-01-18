import requests
from twilio.rest import Client

account_sid = 'account_sid'
auth_token = 'auth_token'

base_url = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "api_key"

params = {
    "lat": 454.6,
    "lon": 234.533,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

will_rain = False

response = requests.get(base_url, params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_='phonenumber',
        to='phonenumber'
    )
