import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Name' # Change name 
email['to'] = 'ChangeMe' # Send to Address
email['subject'] = 'TestTestTest'

email.set_content(html.substitute({'name': 'AnyName'}), 'html') 

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('EmailLogin', 'EmailPassword') # For use with Gmail, Make sure 'Less Secure App Access is turned On in google settings'
	smtp.send_message(email)
	print('Email Sent')
