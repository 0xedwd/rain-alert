from weather_service import get_weather_data
from notification_service import send_notification


def check_weather_and_notify():
    weather_data = get_weather_data()
    weather_slice = weather_data["hourly"][:12]

    will_rain = False
    rain_msg = " 🌧️ Bring an umbrella. ☔️ ella. ☔️ ella. ☔️ eh. ☔️ eh. ☔️ eh. ☔️"

    for hour_data in weather_slice:
        condition_code = hour_data["weather"][0]["id"]
        if condition_code < 700:
            will_rain = True
            break

    if will_rain:
        status = send_notification(rain_msg)
        print(status)


if __name__ == "__main__":
    check_weather_and_notify()
