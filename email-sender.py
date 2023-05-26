from email.message import EmailMessage
import ssl
import smtplib

while True:
  email_ou_user = str(input("Digite o seu email ou usuário  '...'@gmail.com: "))
  
  if '@' in email_ou_user:
    if 'gmail.com' in email_ou_user:
      email_sender = email_ou_user
      break
    else:
      print("Somente emails do Gmail, por favor!")
  else:
    email_sender = email_ou_user + '@gmail.com'
    

email_password = str(input("Enter your password: "))
email_receiver = str(input("Receiver email: "))
subject = str(input("Subject: "))
body = str(input("Write your message:  "))

email = EmailMessage()
email['From'] = email_sender
email['To'] = email_receiver
email['Subject'] = subject
email.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver, email.as_string())

