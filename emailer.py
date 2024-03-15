#***************************************************************
#
#This module contains the logic to send emails.
#
#***************************************************************
#
#


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
from cryptography_utils import decrypt_message

# Carrega configurações
def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def send_email(receiver_email, subject, body):
    config = load_config()

    sender_email = decrypt_message(bytes(config["email"], 'utf-8'))
    sender_password = decrypt_message(bytes(config["password"], 'utf-8'))

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(config["smtp_server"], config["smtp_port"])
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()
