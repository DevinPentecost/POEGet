__author__ = 'Devin'

from Model.Stash import Stash
from Controller import DatabaseKeys
from Model.DBObject import DBObject


class Account(DBObject):
	#A particular account that can own tabs
	def __init__(self, accountName, lastCharacterName):
		#Just store this stuff
		self._accountName = accountName
		self._lastCharacterName = lastCharacterName

		#An account has a stash as well
		self._stash = Stash(parentAccount=self)

	'''
	PROPERTIES
	'''
	#TODO: Use proper region

	@property
	def accountName(self):
		"""Get the account's name"""
		return self._accountName

	@property
	def lastCharacterName(self):
		"""Get the account's last character name"""
		return self._lastCharacterName

	@lastCharacterName.setter
	def lastCharacterName(self, newerCharacterName):
		"""Set the latest character name"""
		self._lastCharacterName = newerCharacterName

	@property
	def stash(self):
		"""Get the account's last character name"""
		return self._stash

	def default(self, o):
		#Build it
		jsonDict = {
			DatabaseKeys.ACCOUNT_NAME: self.accountName,
			DatabaseKeys.ACCOUNT_LATEST_CHARACTER_NAME: self.lastCharacterName,
			DatabaseKeys.ACCOUNT_STASH: self.stash,
		}

		#And return it
		return jsonDict

	def toDatabaseDictionary(self):
		#Build the dictionary
		dictionary = {
			DatabaseKeys.ACCOUNT_NAME: self.accountName,
			DatabaseKeys.ACCOUNT_LATEST_CHARACTER_NAME: self.lastCharacterName,
			DatabaseKeys.ACCOUNT_STASH_TABS: [stashTabID for stashTabID in self.stash.tabs],
		}

		#And return it
		return dictionary
