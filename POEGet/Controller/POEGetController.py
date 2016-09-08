__author__ = 'Devin'

import threading
import time

from Util import Printing, CLEAN_STRING
from Controller.JSONInterface import JSONInterface
from Controller import CHANGE_ID_WAIT_TIME
from Controller import JSONKeys
from Model.Account import Account
from Model.StashTab import StashTab
from Model import DEFAULT_LEAGUE
from Model.Item.Item import Item


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
			if JSONInterface.duplicateNextChangeID:
				#We want to wait and try again later
				Printing.INFOPRINT("Received duplicate NextChangeID. Waiting {} seconds".format(CHANGE_ID_WAIT_TIME))
				time.sleep(CHANGE_ID_WAIT_TIME)

		#We're out of the loop, meaning we were told to stop going.
		return

	def _updateDatabase(self, stashes):
		pass

	def _updateModel(self, stashes):
		"""Update the model with some amount of stash information"""
		Printing.INFOPRINT("Updating Model with new Payload")
		for stashTab in stashes:
			#We have a stash dictionary. Let's parse it out into relevant information
			self._handleStashTab(stashTab)
		Printing.INFOPRINT("Update Complete")

	def _handleStashTab(self, stashTab):
		"""Handle getting all the relevant information from the stash"""
		accountName = CLEAN_STRING(stashTab[JSONKeys.ACCOUNT_NAME])
		stashTabID = stashTab[JSONKeys.STASH_ID]
		items = stashTab[JSONKeys.ITEMS]
		lastCharacterName = CLEAN_STRING(stashTab[JSONKeys.LAST_CHARACTER_NAME])
		public = stashTab[JSONKeys.PUBLIC]
		stashTabName = CLEAN_STRING(stashTab[JSONKeys.STASH])
		stashTabType = stashTab[JSONKeys.STASH_TYPE]

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

		#Now we have a stash. Let's add it's items
		for item in items:
			self._handleItem(item, stashTab)

	def _handleItem(self, item, parentStashTab):
		"""Handle converting an item dictionary into an actual item object"""
		name = item[JSONKeys.ITEM_NAME]
		itemID = item[JSONKeys.ITEM_ID]
		typeLine = item[JSONKeys.TYPE_LINE]
		note = item.get(JSONKeys.NOTE, None)
		iconURL = item[JSONKeys.ICON]
		league = item.get(JSONKeys.LEAGUE, DEFAULT_LEAGUE)
		description = item.get(JSONKeys.DESCRIPTION, None)

		Printing.INFOPRINT("Received Item with ID: {}".format(itemID))

		#Does this item already exist in our stash tab?
		#TODO: Handle updating items!

		#TODO: Handle more complicated items than just nothing
		Printing.INFOPRINT("Creating new Item with ID {}".format(itemID))
		item = Item(parentStashTab, name, itemID, typeLine, note, iconURL, league, description)
		parentStashTab.items[itemID] = item

	#</editor-fold>
