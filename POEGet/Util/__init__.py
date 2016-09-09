__author__ = 'Devin'

import unicodedata

DEBUG_ENABLED = True


def CLEAN_STRING(string):
	try:
		return unicodedata.normalize('NFKD', string)
	except Exception:
		return None