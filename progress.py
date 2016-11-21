import sys
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, Percentage, ProgressBar, ReverseBar, RotatingMarker, SimpleProgress, Timer

class Progress:
	def __init__(self, max):
		self.max = max;
		self.widgets = ['Queueing', Percentage(), Bar()]
		self.index = 0
	def start(self):
		self.pbar = ProgressBar(widgets=self.widgets, maxval=self.max).start()
	def next(self):
		self.pbar.update( self.index + 1 )
	def finish(self):
		self.pbar.finish()