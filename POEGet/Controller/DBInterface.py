__author__ = 'Devin'

import time

from pymongo import MongoClient

from Controller import DatabaseKeys, DATABASE_URI
from Util import Printing

"""This class handles interactions with the Mongo Database"""
#We want to establish our connection
_client = MongoClient(DATABASE_URI)
_database = _client[DatabaseKeys.DATABASE_NAME]
_metadata = _database[DatabaseKeys.METADATA_COLLECTION].find_one()
_items = _database[DatabaseKeys.ITEM_COLLECTION]
_tabs = _database[DatabaseKeys.STASH_TABS]


def _getMetadata():
	"""Get the metadata object from the database"""
	return _metadata


def _setMetadata(metadata):
	global _metadata
	"""Update the Metadata with the new information"""
	#Did we have an old one?
	if _metadata:
		_database[DatabaseKeys.METADATA_COLLECTION].update_one(
			{
				'_id': _metadata['_id'],
			},
			{
				'$set': metadata,
			},
		)
	else:
		#We need to instead set that value
		_database[DatabaseKeys.METADATA_COLLECTION].insert_one(metadata)
		_metadata = _database[DatabaseKeys.METADATA_COLLECTION].find_one()


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
	item = _items.find_one({DatabaseKeys.ITEM_ID: itemID})

	#Return this item dictionary
	return item


def setItem(item):
	"""Sets a particular item object, updating if needed"""
	#Let's turn the item into a database dictionary
	databaseDictionary = item.toDatabaseDictionary()

	#Next we need to see if the item is already in the database
	databaseItem = getItem(item.itemID)

	#Was it there?
	if databaseItem:
		#We update this item
		_items.update_one(
			{
				'_id': databaseItem['_id'],
			},
			{
				'$set': databaseDictionary,
			},
		)
	else:
		#We add this item
		_items.insert_one(databaseDictionary)

	#And we're done
	return


def deleteItemByID(itemID):
	"""When an item no longer exists, we want to delete it from the database"""
	deleteResult = _items.delete_one({DatabaseKeys.ITEM_ID: itemID})

	#Was something deleted?
	if deleteResult.acknowledged:
		#We should print something
		Printing.DEBUGPRINT("Deleted Item with ID: {}".format(itemID))

#<editor-fold desc="Stash Tabs">
"""Various methods for handling stash tabs"""


def getStashTab(stashTabID):
	"""Get a particular stash tab"""
	#We want to get an Item from the DB based on it's ID
	stashTab = _tabs.find_one({DatabaseKeys.STASH_TAB_ID: stashTabID})

	#Return this item dictionary
	return stashTab


def getAllStashItemIDs(stashTabID):
	"""Get all the IDs for the specified stash tab so we can see what changed"""
	#Get the stash tab
	stashTab = _tabs.find_one({DatabaseKeys.STASH_TAB_ID: stashTabID})

	#And return the list of items if there was a tab
	if stashTab:
		return stashTab[DatabaseKeys.STASH_TAB_ITEMS]
	else:
		return []


def setStashTab(stashTab):
	"""For adding/editing a stash tab"""
	#Let's turn the stashTab into a database dictionary
	stashTabDictionary = stashTab.toDatabaseDictionary()

	#Next we need to see if the stashTab is already in the database
	databaseStashTab = getStashTab(stashTab.stashID)

	#Was it there?
	if databaseStashTab:
		#We update this stashTab
		_tabs.update_one(
			{
				'_id': databaseStashTab['_id'],
			},
			{
				'$set': stashTabDictionary,
			},
		)
	else:
		#We add this stashTab
		_tabs.insert_one(stashTabDictionary)

	#And we're done
	return

#</editor-fold>
