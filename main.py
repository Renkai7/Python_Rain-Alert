import requests
import smtplib
import os

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

api_key = os.environ.get("OWM_API_KEY")
API_URL = f"https://api.openweathermap.org/data/2.5/onecall?"

weather_params = {
    "lon": -76.348473,
    "lat": 39.535671,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(API_URL, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="tonystark53150@gmail.com",
            msg="Subject: Weather Report\n\nIt's going to rain today. Remember to bring an umbrella."
        )




