from twilio.rest import Client
import os

TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE = os.getenv('TWILIO_PHONE')

def send_sms(content, to):
  twilio = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
  twilio.messages.create(
    body=content,
    from_=TWILIO_PHONE,
    # TODO: Registrar celular do usuario pelo front
    # to=to
    to='+5521967000099')