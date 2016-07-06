import os, sys, yaml, traceback, cgitb, shutil

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Message:
	def __init__(self,config):
		self.config = config
		assert 'sender' in config
		assert 'senderpassword' in config

	def send_html(self, config):
		assert 'subject' in config
		assert 'html' in config
		assert 'text' in config
		assert 'from' in config
		assert 'to' in config
	
		html = "<!DOCTYPE html><html><head></head><body>" + config['html'] + "</body></html>"
		
		textpart = MIMEText(text,'plain')
		htmlpart = MIMEText(html,'html')
		
		message = MIMEMultipart('alternative')
		message['Subject'] = config['subject']
		message['From'] = config['sender']
		message['To'] = config['to']
		message.attach(textpart)
		message.attach(htmlpart)
		
		self.send_email(to=config['to'], message=message.as_string() )
	
	def send(self, to, message, type='email'):
		# Credentials (if needed)
		username = self.config['sender']
		password = self.config['senderpassword']
		
		sender = username
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(username,password)
		server.sendmail(sender, to, message)
		server.quit()
	
	def send_email(self, to, message):
		self.send( to, message, type="email")
	
	def send_text(self, to, message):
		message = MIMEText(message)
		self.send( to, message.as_string(), type="text")
	
	def notify_error(self):
		ex_type, ex, tb = sys.exc_info()
		self.send_html({ 
			'subject': 'Fatal Error',
			'html': cgitb.html(sys.exc_info()),
			'text': cgitb.text(sys.exc_info())
		})
	
