__author__ = 'Devin'

import sys

from Util import DEBUG_ENABLED

"""A series of print functions"""


def _CLEAN_MESSAGE(message):
	return message.encode(sys.stdout.encoding, errors='replace')

def INFOPRINT(message):
	print("-i- {}".format(_CLEAN_MESSAGE(message)))


def ERRORPRINT(message):
	print("-e- {}".format(_CLEAN_MESSAGE(message)))


def DEBUGPRINT(message):
	if DEBUG_ENABLED:
		print("-d- {}".format(_CLEAN_MESSAGE(message)))
