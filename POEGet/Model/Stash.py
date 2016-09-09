__author__ = 'Devin'

from json import JSONEncoder

from POEGet.Controller import DatabaseKeys


class Stash(JSONEncoder):
	"""A Stash is owned by an account and has any number of tabs"""

	def __init__(self, parentAccount):
		#Just store this stuff
		self._parentAccount = parentAccount

		#All of the tabs in this stash
		self._tabs = {}

	'''
	PROPERTIES
	'''

	@property
	def parentAccount(self):
		"""Get the parent account of the stash"""
		return self._parentAccount

	@property
	def tabs(self):
		"""Get the tabs in the stash"""
		return self._tabs

	def default(self, o):
		#Build the dictionary
		jsonDictionary = {
			DatabaseKeys.STASH_TABS: self.tabs,
		}

		#And return
		return jsonDictionary
