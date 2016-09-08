__author__ = 'Devin'

DEBUG_ENABLED = True


def CLEAN_STRING(string):
	try:
		return string.encode('utf-8')
	except:
		return None