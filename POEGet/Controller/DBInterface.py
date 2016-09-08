__author__ = 'Devin'

import time

from pymongo import MongoClient

from Controller import DatabaseKeys

"""This class handles interactions with the Mongo Database"""
#We want to establish our connection
#TODO: Move the DB onto the network or whatever?
_client = MongoClient()
_database = _client[DatabaseKeys.DATABASE_NAME]


def _getMetadata():
	"""Get the metadata object from the database"""
	return _database[DatabaseKeys.METADATA_COLLECTION].find_one()


def _setMetadata(metadata):
	"""Update the Metadata with the new information"""
	_database[DatabaseKeys.METADATA_COLLECTION].insert_one(metadata)


def getNextChangeID():
	"""Get the NextChangeID from the DB"""
	#We want to pull it from the database
	return _getMetadata()[DatabaseKeys.NEXT_CHANGE_ID]


def getNextChangeIDTimestamp():
	"""Get the NextChangeID Timestamp from the DB"""
	#Do the same as the ID
	return _getMetadata()[DatabaseKeys.NEXT_CHANGE_ID_TIMESTAMP]


def setNextChangeID(newID):
	"""Set the NextChangeID from the DB. This also updates the timestamp"""
	#Set the new metadata
	metadata = {
		DatabaseKeys.NEXT_CHANGE_ID: newID,
		DatabaseKeys.NEXT_CHANGE_ID_TIMESTAMP: time.time(),
	}
	_setMetadata(metadata)


def getItem(itemID):
	"""Get the Item with the matching ID from the DB"""
	#We want to get an Item from the DB based on it's ID
	item = _database[DatabaseKeys.ITEM_COLLECTION].find_one({DatabaseKeys.ITEM_ID: itemID})

	#Return this item dictionary
	return item
