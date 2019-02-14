import smtplib
import os


smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
print(smtp_object.ehlo())
smtp_object.starttls()
# print(smtp_object.starttls()) 

email = "sadatt254@gmail.com"
password = os.environ.get('EMAIL_PASS')
print(password)

smtp_object.login(email, password)

print("Logged In!")

sender = email
recipient = "anwar@tunapanda.org"
subject = "this is my awesome subject"
message = "hello anwar"
msg = "Subject: "+subject+"\n"+message
print(msg)

smtp_object.sendmail(sender, recipient, msg)
