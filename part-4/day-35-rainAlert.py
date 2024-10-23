import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"




weather_parameters = {
    "lat": 40.681080,
    "lon": -112.262850,
    "appid":api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"][0]["id"])

will_rain=False
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code)<700:
        will_rain=True
    if will_rain:
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'https': os.enviorn["https_proxy"]}
        client= Client(account_sid, auth_token, http_client=proxy_client)
        message=client.messages \
            .create(
                body="It's going to rain today. Remember to bring an umbrella.",
                from_="+18774466017",
                to="+14358491116",
        )
        print(message.status)

