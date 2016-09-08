__author__ = 'Devin'


class Stash(object):
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
