from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

smtp_username = os.environ['EMAIL_ID']
smtp_password = os.environ['PASSWORD']
receiver_email = os.environ['DEFAULT_USER']

def send_mail(text:str,sender:str):

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587 
    sender_email = smtp_username
    subject = 'You got a message from {}'.format(sender)

    msgRoot = MIMEMultipart('related')
    msgRoot['From'] = sender_email
    msgRoot['To'] = receiver_email
    msgRoot['Subject'] = subject

    text = """you got a message from {}\n{}""".format(sender,text)

    message=MIMEText(text,"plain")

    msgRoot.attach(message)
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls() 
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email,receiver_email,msgRoot.as_string())
            print(f'Email sent successfully to : {receiver_email}')
    except Exception as err:
        print(f"There is an error when we trying to send email to {receiver_email}")
    