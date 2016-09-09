__author__ = 'Devin'

from Controller import DatabaseKeys
from Model.DBObject import DBObject


class StashTab(DBObject):
	#A particular tab belonging in a stash
	def __init__(self, parentStash, stashTabID, name):
		#Store the information
		self._parentStash = parentStash
		self._stashTabID = stashTabID
		self._name = name

		#All the items in this stash, keyed by item ID
		self._items = {}

	@property
	def parentStash(self):
		"""Get the parent stash to this tab"""
		return self._parentStash

	@property
	def stashID(self):
		"""Get the ID of this stash tab"""
		return self._stashTabID

	@property
	def stashName(self):
		"""Get the name of this stash"""
		return self._name

	@property
	def items(self):
		"""Gets the item dictionary for this tab"""
		return self._items

	def default(self, o):
		#Build it
		jsonDictionary = {
			DatabaseKeys.STASH_TAB_ID: self.stashID,
			DatabaseKeys.ACCOUNT_NAME: self.parentStash.parentAccount.accountName,
			DatabaseKeys.STASH_TAB_NAME: self.stashName,
			DatabaseKeys.ITEMS: self.items,
		}

		#And return it
		return jsonDictionary

	def toDatabaseDictionary(self):
		#Build the dictionary
		dictionary = {
			DatabaseKeys.STASH_TAB_ID: self.stashID,
			DatabaseKeys.STASH_TAB_NAME: self.stashName,
			DatabaseKeys.ACCOUNT_NAME: self.parentStash.parentAccount.accountName,
			DatabaseKeys.STASH_TAB_ITEMS: [],
		}

		#And return it
		return dictionary
