import os, random, requests, re, datetime, getpass
from bs4 import BeautifulSoup

###### REGEXP ######
regexp_whitespace = re.compile(r'[\s\t\n]{2,}')
regexp_tabs = re.compile(r'\t\n+')
regexp_quotes = re.compile(r'\u2033+')

###### METHODS ######
def log(message):
	print timestamp() + '\t' + getpass.getuser() + '\t' +  str(message)

def timestamp():
	return '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())

def join(*args):
	return os.path.normpath(os.path.join(*args))

def mysql_date(date):
	date = str(date).split('/')
	( month, day, year ) = date
	year = 2000 + int(year)
	return str(year) + '-' + str(month) + '-' + str(day)

def sleep():
	return random.randint(1,30) + random.randint(1,30)/2

class RemoteLog:
	def __init__(self, app_name):
		self.name = app_name
		self.log_url = 'http://scripts.veloxwheels.com:5000/logs'
	def log(self, message):
		data = {
			'app': self.name,
			'message': message
		}
		try:
			response = requests.post(self.log_url, data=data)
		except Exception as e:
			print('Failed to push log to remote')
			print(e)

def get_stringed_soup(soup):
	stringed_soup = ""
	for string in soup.strings:
		stringed_soup = stringed_soup + string

	stringed_soup = re.sub( regexp_quotes, '', stringed_soup )
	stringed_soup = re.sub( regexp_whitespace,' ', stringed_soup)
	stringed_soup = re.sub( regexp_tabs, '', stringed_soup )
	stringed_soup = stringed_soup.strip().upper()
	return stringed_soup

def request_soup(url):
	r = requests.get( url )
	html = r.text
	soup = BeautifulSoup(html, 'html.parser')
	return soup
