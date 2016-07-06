from datetime import datetime
import logging, os, sys

def join(*args):
	return os.path.normpath(os.path.join(*args))

LOG_DIR = os.getcwd()
class Log():
	def __init__(self, name, directory=LOG_DIR):
		self.name = name
		self.directory = directory
		self.logfile = join( self.directory, self.name + '.log')

	def action(self, message):
		self.log('ACTION', message)

	def execution(self, message):
		self.action('======= DONE ' + datetime.now().strftime("%Y-%m-%d %I:%M") + ' ========')
		self.log('EXECUTION',message)

	def error(self, message):
		self.log('ERROR',message)
		ex_type, ex, tb = sys.exc_info()
		self.action('\n======================\n'+str(ex_type)+'\n_______________________\n'+str(tb)+'\n======================\n')

	def log(self, logtype, message):
		message = str(message)
		message = logtype + '\t' + datetime.now().strftime("%Y-%m-%d %I:%M") + '\t' + message + '\n'
		print(message)
		if not os.path.isfile(self.logfile):
			with open(self.logfile,'w+') as f:
				f.write(' ')
		with open(self.logfile,'a+') as logfile:
			logfile.write(message)