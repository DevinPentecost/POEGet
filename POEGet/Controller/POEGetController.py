__author__ = 'Devin'

import threading
import time

from POEGet.Util import Printing, CLEAN_STRING
from POEGet.Controller.JSONInterface import JSONInterface
from POEGet.Controller import CHANGE_ID_WAIT_TIME, REQUEST_FAIL_WAIT_TIME
from POEGet.Controller import JSONKeys
from POEGet.Controller import DBInterface
from POEGet.Model.Account import Account
from POEGet.Model.StashTab import StashTab
from POEGet.Model import DEFAULT_LEAGUE
from POEGet.Model.Item.BaseItem import BaseItem


class POEGetController(object):
	"""This is the controller that handles getting the information, building the model, and accessing that model"""

	#Are we still talking to the interface?
	_interfacing = True

	def __init__(self):
		#We want to have a dictionary of all the items, keyed by item ID
		self._items = {}

		#We also want to have the actual model, as a dictionary of all accounts by name
		self._accounts = {}

		#Begin creating the model in another thread
		self._jsonInterfaceThread = threading.Thread(target=self.jsonInterfaceThreadWorker)
		self._jsonInterfaceThread.start()

	#<editor-fold desc="Properties">
	@property
	def items(self):
		"""Get the items dictionary"""
		return self._items

	@property
	def accounts(self):
		return self._accounts

	#</editor-fold>

	#<editor-fold desc="JSONInterface">
	def jsonInterfaceThreadWorker(self):
		"""This is the entry point for the JSONInterface thread"""

		#We want to constantly get items
		while self._interfacing:

			#Make the request
			stashes = JSONInterface.getNextPayload()

			#Now we want to build all the information from these new stashes
			self._updateModel(stashes)

			#Is there a duplicate change ID?
			if stashes is None:
				#Servers are goofed. Let's just wait.
				Printing.INFOPRINT("Unable to contact server. Waiting {} seconds".format(REQUEST_FAIL_WAIT_TIME))
				time.sleep(REQUEST_FAIL_WAIT_TIME)
			elif JSONInterface.duplicateNextChangeID:
				#We want to wait and try again later
				Printing.INFOPRINT("Received duplicate NextChangeID. Waiting {} seconds".format(CHANGE_ID_WAIT_TIME))
				time.sleep(CHANGE_ID_WAIT_TIME)

		#We're out of the loop, meaning we were told to stop going.
		return

	def _updateDatabase(self, stashes):
		pass

	def _updateModel(self, stashes):
		"""Update the model with some amount of stash information"""
		#Did we get None?
		if stashes is None:
			#We've got nothing to do
			return

		Printing.INFOPRINT("Updating Model with new Payload")
		for stashTab in stashes:
			#We have a stash dictionary. Let's parse it out into relevant information
			self._handleStashTab(stashTab)
		Printing.INFOPRINT("Update Complete")

	def _handleStashTab(self, stashTabDictionary):
		"""Handle getting all the relevant information from the stash"""
		accountName = CLEAN_STRING(stashTabDictionary[JSONKeys.ACCOUNT_NAME])
		stashTabID = stashTabDictionary[JSONKeys.STASH_ID]
		items = stashTabDictionary[JSONKeys.ITEMS]
		lastCharacterName = CLEAN_STRING(stashTabDictionary[JSONKeys.LAST_CHARACTER_NAME])
		public = stashTabDictionary[JSONKeys.PUBLIC]
		stashTabName = CLEAN_STRING(stashTabDictionary[JSONKeys.STASH])
		stashTabType = stashTabDictionary[JSONKeys.STASH_TYPE]

		Printing.INFOPRINT("Received stash tab with ID: {}".format(stashTabID))

		#Do we have an account by this name?
		account = self._accounts.get(accountName, None)
		if not account:
			Printing.INFOPRINT("Adding new Account with name: {}".format(accountName))
			account = Account(accountName, lastCharacterName)
			self._accounts[accountName] = account

		#Get the stash
		accountStash = account.stash

		#Does this tab exist in the stash?
		stashTab = accountStash.tabs.get(stashTabID, None)
		if not stashTab:
			Printing.INFOPRINT("Adding new Stash Tab with ID: {}".format(stashTabID))
			stashTab = StashTab(accountStash, stashTabID, stashTabName)

		#Check to see if the database had items in it
		previousItems = DBInterface.getAllStashItemIDs(stashTabID)

		#Now we have a stash. Let's add it's items
		remainingItems = []
		for item in items:
			remainingItems = self._handleItem(item, stashTab, previousItems)

		#We have some remaining items to remove from the stash tab
		for itemID in remainingItems:
			DBInterface.deleteItemByID(itemID)

		#And now put this stash tab into the database
		DBInterface.setStashTab(stashTab)

	def _handleItem(self, itemDictionary, parentStashTab, previousItems):
		"""Handle converting an item dictionary into an actual item object"""
		name = itemDictionary[JSONKeys.ITEM_NAME]
		itemID = itemDictionary[JSONKeys.ITEM_ID]
		typeLine = itemDictionary[JSONKeys.TYPE_LINE]
		note = itemDictionary.get(JSONKeys.NOTE, None)
		iconURL = itemDictionary[JSONKeys.ICON]
		league = itemDictionary.get(JSONKeys.LEAGUE, DEFAULT_LEAGUE)
		description = itemDictionary.get(JSONKeys.DESCRIPTION, None)

		Printing.INFOPRINT("Received Item with ID: {}".format(itemID))

		#TODO: Handle more complicated items than just nothing
		Printing.INFOPRINT("Creating new Item with ID {}".format(itemID))
		item = BaseItem(parentStashTab, name, itemID, typeLine, note, iconURL, league, description)
		parentStashTab.items[itemID] = item

		#Does this item already exist in our stash tab?
		if item.itemID in previousItems:
			#We don't need to remove it from the database
			previousItems.remove(item.itemID)

		#Add this item to the repo, and remove the old one if it is still there
		DBInterface.setItem(item)

		#And we return the list of items to remove from the stash
		return previousItems

	#</editor-fold>
