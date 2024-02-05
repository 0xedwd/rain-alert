import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from api_keys import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from config import FROM_PHONE, TO_PHONE


def send_notification(message):
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)

    message = client.messages.create(
        body=message,
        from_=FROM_PHONE,
        to=TO_PHONE
    )
    return message.status
