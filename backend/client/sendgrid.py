from os import environ

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Content, Email, Mail, To

API_KEY = "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"


class SendgridClient:
    def __init__(self):
        self.client = SendGridAPIClient(api_key=environ.get("SENDGRID_API_KEY", API_KEY))
        self.from_email = Email("nidusapp@protonmail.com")

    def send_email(self, to: str, subject: str, body: str):
        content = Content("text/plain", body)
        mail = Mail(self.from_email, To(to), subject, content)
        return self.client.client.mail.send.post(request_body=mail.get())

