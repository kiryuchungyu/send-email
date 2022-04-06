# -*- coding: UTF-8 -*-
import smtplib
from email.message import EmailMessage

class Mail:
    def __init__(self):
        self.msg = EmailMessage()
        self.msg['Subject'] = input("email subject : ")
        self.msg['From'] = input("email sender : ")
        self.msg['To'] = input("email receiver's address : ")
        self.msg.set_content(input(
        """email content : 
        """))
  
    def send_mail(self):
        email_list = {'google' : 'smtp.gmail.com',
                      'microsoft' : 'smtp.office365.com',
        }
        server = smtplib.SMTP(email_list['{}'.format(input('what is the email server, google or microsoft? : '))], 587)
        server.ehlo()
        server.starttls()
        cnt = 0
        while cnt < 3:
            cnt += 1
            try:
                server.login(input("your mail : "), input("your password : "))
                break
            except:
                print("please input the right mail address and the password!")
                if cnt == 3:
                    print("this time would be the last chance")
                    server.login(input("your mail : "), input("your password : "))
        server.send_message(self.msg)
        server.quit()
        print("your mail is sent successfully")
        print("git push test")
        print("second editor test")
        
if __name__ == '__main__':
    main = Mail()
    main.send_mail()