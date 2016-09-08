__author__ = 'Devin'

import requests

from Controller import API_BASE_URL
from Controller import JSONKeys
from Util import Printing
from Controller import DBInterface


class JSONInterface(object):
	"""This interface assists in retrieving all the information from the API"""

	#The Next Change ID for getting the next payload
	try:
		nextChangeID = DBInterface.getNextChangeID()
		Printing.INFOPRINT("Retrieved NextChangeID {} from Database.".format(nextChangeID))
	except:
		nextChangeID = None
		Printing.INFOPRINT("Unable to retrieve NextChangeID from Database...")

	#Did we get a duplicate and should wait?
	duplicateNextChangeID = False

	@staticmethod
	def _buildURL():
		#Did we have a next change id?
		if JSONInterface.nextChangeID:
			#We want to include it
			targetURL = '{}?id={}'.format(API_BASE_URL, JSONInterface.nextChangeID)
		else:
			#We just want the first one
			targetURL = API_BASE_URL

		#And we have our URL
		return targetURL

	@staticmethod
	def getNextPayload():
		#We want to get the next payload of JSON information

		#Create the URL
		requestURL = JSONInterface._buildURL()

		#Get the response from the request
		Printing.INFOPRINT("Getting Next Payload.")
		Printing.DEBUGPRINT("Requesting at URL: {}".format(requestURL))
		response = requests.get(requestURL)
		Printing.INFOPRINT("Request Complete.")
		#Retrieve the JSON from it
		responseJSON = response.json()

		#Get the next change ID
		nextChangeID = responseJSON[JSONKeys.NEXT_CHANGE_ID]

		#Did it match the old one? Set the flag to be so
		duplicateNextChangeID = (nextChangeID == JSONInterface.nextChangeID)
		JSONInterface.duplicateNextChangeID = duplicateNextChangeID
		JSONInterface.nextChangeID = nextChangeID

		#Update the Database
		DBInterface.setNextChangeID(nextChangeID)

		#And return the stashes
		stashes = responseJSON[JSONKeys.STASHES]
		return stashes
