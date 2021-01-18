from twilio.rest import Client
import smtplib

account_sid = 'account_sid'
auth_token = 'auth_token'
my_email = "my_email"
password = "password"


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, msg):
        message = self.client.messages.create(
            body=msg,
            from_='phonenumber',
            to='phonenumber'
        )
        print(message.sid)

    def send_emails(self, emails, msg, link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            for email in emails:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight\n\n{msg}\n{link}".encode('utf-8')
                )
