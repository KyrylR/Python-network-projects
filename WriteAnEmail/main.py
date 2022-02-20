import smtplib
from email import encoders
from email.mine.text import MINEText
from email.mine.base import MINEBase
from email.mine.multipart import MINEMultimart

server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

print(password)
server.login('test4edupc@gmail.com', password)


msg = MINEMultimart()
msg['From'] = 'InterNos'
msg['To'] = 'forservices.it.t@gmail.com'
msg['Subject'] = 'Just a test'

with open('msg.txt', 'r') as f:
    massage = f.read()

msg.attach(MINEText(massage, 'plain'))

filename = 'default.jpg'
attachment = open(filename, 'rb')

p = MINEBase('spplicstion', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_strig()
server.sendmail('test4edupc@gmail.com', 'forservices.it.t@gmail.com', text)
