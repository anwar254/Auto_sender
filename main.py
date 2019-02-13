import datetime
import smtplib
import time

cnts = []

class Scheduler(object):
    def __init__(self, contacts, message):
        self.contacts = contacts
        self.message =  message

    def get_contacts(self):
        file = open(self.contacts, 'r')
        for contact in file:
            cnts.append(contact)

    def get_message(self):
        with open(self.message, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
        return Template(template_file_content)

def main():
    email_scheduler = Scheduler('contacts.txt', 'message.txt')
    email_scheduler.get_contacts()

    print(email_scheduler.get_message())

    send_date = datetime.datetime(2019, 2, 13, 17, 45)
    tm = datetime.datetime.now()
    print(tm.time(), send_date.time())
    if tm.time() == send_date.time():
        print("time")

if __name__ == '__main__':
    main()
