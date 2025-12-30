import smtplib
import sys
from email.message import EmailMessage

CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com",
    "googleFi": "@msg.fi.google.com"
}


class SMSHelper:
    def __init__(self, config):
        self.email = config.smsEmail
        self.password = config.smsEmailPassword
        self.alert_number = config.alertNumber
        self.alert_carrier = config.alertCarrier

    def send_message(self, message):
        recipient = self.alert_number + CARRIERS[self.alert_carrier]
        auth = (self.email, self.password)

        msg = EmailMessage()
        # subject line is required, but SMS doesn't use it
        msg['Subject'] = ""
        msg['From'] = self.email
        msg['To'] = recipient
        msg.set_content(message)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(auth[0], auth[1])
            smtp.send_message(msg)

    @staticmethod
    def is_valid_config(config):
        if (config.smsEmail and config.smsEmailPassword and config.alertNumber and config.alertCarrier):
            return True
        else:
            return False
