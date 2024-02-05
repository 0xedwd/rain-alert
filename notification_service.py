from twilio.rest import Client
from api_keys import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from config import FROM_PHONE, TO_PHONE


def send_notification(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message,
        from_=FROM_PHONE,
        to=TO_PHONE
    )
    return message.status
