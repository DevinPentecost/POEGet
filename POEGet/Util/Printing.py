__author__ = 'Devin'

from Util import DEBUG_ENABLED

"""A series of print functions"""


def INFOPRINT(message):
	print("-i- {}".format(message))


def ERRORPRINT(message):
	print("-e- {}".format(message))


def DEBUGPRINT(message):
	if DEBUG_ENABLED:
		print("-d- {}".format(message))
