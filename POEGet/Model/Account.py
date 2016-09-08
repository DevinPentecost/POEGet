__author__ = 'Devin'

from Model.Stash import Stash


class Account(object):
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
