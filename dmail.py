import smtplib
from email.message import EmailMessage

def sendmail(to,subject,body):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('sumapriyaperla@gmail.com','orxc kodi tdet xzry')
    msg = EmailMessage()
    msg['From']='sumapriyaperla@gmail.com'
    msg['TO'] = to
    msg['subject'] = subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()
#sendmail('sirishadasari1113@gmail.com','hi i am sumapriya','i am from narasaraopet')
#print('mailsended')