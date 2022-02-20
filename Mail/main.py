import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = smtplib.SMTP('smtp.live.com', 587)
server.connect("smtp.live.com", 587)
server.ehlo()
server.starttls()
server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('test4edupc@hotmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'Myself'
msg['To'] = 'for.services.it.t@gmail.com'
msg['Subject'] = 'Just a test23'

with open('msg.txt', 'r') as f:
    massage = f.read()

msg.attach(MIMEText(massage, 'plain'))

filename = 'default.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()

server.sendmail('test4edupc@hotmail.com', 'for.services.it.t@gmail.com', text)
server.quit()
