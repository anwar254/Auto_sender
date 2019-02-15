import smtplib
import getpass 
from sender import auto_scheduler

def auto_sender():
    ctnts_list = auto_scheduler.get_contacts()

    cnts_names = []
    cnts_emails = []

    for list in ctnts_list:
        names = list[0]
        emails = list[1]
        cnts_emails.append(emails)
   
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_object.ehlo()
    smtp_object.starttls()

    email = "sadatt254@gmail.com"
    password = getpass.getpass("Password: ")

    smtp_object.login(email, password)

    for email in cnts_emails:
        sender = email
        recipient = email
        subject = "this is my awesome subject"
        message = "hello anwar"
        msg = "Subject: "+subject+"\n"+message

        smtp_object.sendmail(sender, recipient, msg)

if __name__ == '__main__':
    auto_sender()

