__author__ = 'Devin'

from json import JSONEncoder

from Model import DEFAULT_LEAGUE
from Controller import DatabaseKeys


class Item(JSONEncoder):
	#This is just the base class for an item
	def __init__(self, parentStashTab, name, itemID, typeLine, note, iconURL, league=DEFAULT_LEAGUE, description=None):
		#Let's get all that information stored
		self._parentStashTab = parentStashTab
		self._name = str(name)
		self._itemID = str(itemID)
		self._typeLine = str(typeLine)
		self._note = str(note) if note else note
		self._iconURL = str(iconURL)
		self._league = str(league)
		self._description = str(description) if description else description

	#All other Attributes will be inherited and such

	#<editor-fold desc="Properties">
	@property
	def parentStashTab(self):
		"""The parentStashTab of this item"""
		return self._parentStashTab

	@property
	def name(self):
		"""The name of this item"""
		return self._name

	@property
	def itemID(self):
		"""The ID of this item"""
		return self._itemID

	@property
	def typeLine(self):
		"""The type of this item"""
		return self._typeLine

	@property
	def note(self):
		"""The note of this item"""
		return self._note

	@property
	def iconURL(self):
		"""The icon URL of this item"""
		return self._iconURL

	@property
	def league(self):
		"""The league of this item"""
		return self._league

	@property
	def description(self):
		"""The description of this item"""
		return self._description

	#</editor-fold>

	def default(self, o):
		#Build the dictionary
		jsonDictionary = {
			DatabaseKeys.ITEM_NAME: self.name,
			DatabaseKeys.ITEM_ID: self.itemID,
			DatabaseKeys.ITEM_TYPE_LINE: self.typeLine,
			DatabaseKeys.ITEM_NOTE: self.note,
			DatabaseKeys.ITEM_ICON_URL: self.iconURL,
			DatabaseKeys.ITEM_LEAGUE: self.league,
			DatabaseKeys.ITEM_DESCRIPTION: self.description,
		}

		#And return it
		return jsonDictionary
