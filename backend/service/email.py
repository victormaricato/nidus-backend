from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Content, Email, Mail, To
import os

SENDGRID_KEY = os.getenv('SENDGRID_API_KEY')

def send_email(body, email):
  sendgrid = SendGridAPIClient(api_key=SENDGRID_KEY)
  sendgrid.from_email = Email("nidus@cauemelo.dev")
  mail = Mail(
    sendgrid.from_email, To(email), 
    'Lembrete - Nidus', 
    Content("text/plain", body))
  sendgrid.client.mail.send.post(request_body=mail.get())