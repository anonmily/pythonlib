import sys

def is_windows():
	if sys.platform.startswith('win32'):
		return True
	else:
		return False

def is_linux():
	if sys.platform.startswith('linux') or sys.platform.startswith('freebsd'):
		return True
	else:
		return False

def is_unix():
	if sys.platform.startswith('darwin') or isLinux():
		return True
	else:
		return False

