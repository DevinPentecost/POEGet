__author__ = 'Devin'

from json import JSONEncoder

from Model.Stash import Stash
from Controller import DatabaseKeys


class Account(JSONEncoder):
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
