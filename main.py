import datetime
import smtplib
import time
from string import Template
import json

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

cnts_names = []
cnts_emails = []
msg = []

class Scheduler(object):
    def __init__(self, contacts, message):
        self.contacts = contacts
        self.message =  message

    def get_contacts(self):
        cnts_data = open(self.contacts, 'r', encoding="utf-8")
        json_data = json.load(cnts_data)
        for key in json_data:
            names = key
            email = json_data[key]
            cnts_names.append(names)
            cnts_emails.append(email)

    def get_message(self):
        with open(self.message, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
        msg.append(template_file_content)

def main():
    MY_ADDRESS ="zack@tunapanda.org"
    PASSWORD = "flakkathadon"
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(MY_ADDRESS, PASSWORD)

    email_scheduler = Scheduler('contacts.json', 'message.txt')
    email_scheduler.get_contacts()
    nme = email_scheduler.get_message()

    for name, email in zip(cnts_names, cnts_emails):
        msg = MIMEMultipart()

        message = nme.substitute(PERSON_NAME=name.title())

        print(message)

        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is TEST"

        msg.attach(MIMEText(message, 'plain'))

        s.send_message(msg)
        del msg

        s.quit()

    send_date = datetime.datetime(2019, 2, 13, 17, 45)
    tm = datetime.datetime.now()
    print(tm.time(), send_date.time())

if __name__ == '__main__':
    main()
