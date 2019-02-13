import datetime
import smtplib
import time
from string import Template
import json

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

cnts = {}
msg = []

class Scheduler(object):
    def __init__(self, contacts, message):
        self.contacts = contacts
        self.message =  message

    def get_contacts(self):
        cnts_data = open(self.contacts, 'r', encoding="utf-8")
        json_data = json.load(cnts_data)
        for key in json_data:
            cnts[key] = json_data[key]

    def get_message(self):
        with open(self.message, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
        msg.append(template_file_content)

def main():
    MY_ADDRESS ="anwar@tunapanda.org"
    PASSWORD = ""
    # s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    # s.starttls()
    # s.login(MY_ADDRESS, PASSWORD)

    email_scheduler = Scheduler('contacts.json', 'message.txt')
    email_scheduler.get_contacts()
    message = email_scheduler.get_message()

    print(cnts)

    send_date = datetime.datetime(2019, 2, 13, 17, 45)
    tm = datetime.datetime.now()
    print(tm.time(), send_date.time())

if __name__ == '__main__':
    main()
