__author__ = 'Devin'


class StashTab(object):
	#A particular tab belonging in a stash
	def __init__(self, parentStash, stashTabID, name, public=True):
		#Store the information
		self._parentStash = parentStash
		self._stashTabID = stashTabID
		self._name = name
		self._public = public

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
