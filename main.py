import smtplib
import getpass 
from sender import auto_scheduler

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def auto_sender():
    cnts_msg = auto_scheduler.get_message()
    ctnts_list = auto_scheduler.get_contacts()

    cnts_names = []
    cnts_emails = []

    for list in ctnts_list:
        names = list[0]
        emails = list[1]
        cnts_names.append(names)
        cnts_emails.append(emails)
   
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_object.ehlo()
    smtp_object.starttls()

    email = "sadatt254@gmail.com"
    password = getpass.getpass("Password: ")

    smtp_object.login(email, password)

    for email, name in zip(cnts_emails, cnts_names):
        msg = MIMEMultipart()

        message = cnts_msg.replace('PERSON_NAME', name.title())
        sender = email
        recipient = email
        subject = "this is my awesome subject"
        message = message
        msg = "Subject: "+subject+"\n"+message

        smtp_object.sendmail(sender, recipient, msg)

if __name__ == '__main__':
    auto_sender()

