# -*- coding: UTF-8 -*-
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = input("email subject : ")
msg['From'] = input("email sender : ")
msg['To'] = input("email receiver's address : ")
msg.set_content(input(
"""email content : 
"""))

email_list = {'google' : 'smtp.gmail.com',
              'microsoft' : 'smtp.office365.com',
}
server = smtplib.SMTP(email_list['{}'.format(input('what is the email server, google or microsoft? : '))], 587)
server.ehlo()
server.starttls()
server.login(input("your mail : "), input("your password : "))
server.send_message(msg)
server.quit()
print("your mail is sent successfully")
print("git push test")
