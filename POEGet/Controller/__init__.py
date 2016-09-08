__author__ = 'Devin'

API_BASE_URL = 'http://www.pathofexile.com/api/public-stash-tabs'

#The time to wait if we get a duplicate change id in seconds
CHANGE_ID_WAIT_TIME = 5


class JSONKeys(object):
	#Top-Level
	NEXT_CHANGE_ID = "next_change_id"
	STASHES = "stashes"

	#Within the stashes
	ACCOUNT_NAME = "accountName"
	STASH_ID = "id"
	ITEMS = "items"
	LAST_CHARACTER_NAME = "lastCharacterName"
	PUBLIC = "public"
	STASH = "stash"
	STASH_TYPE = "stashType"

	#Within the items
	CORRUPTED = "corrupted"
	DESCRIPTION = "description"
	EXPLICIT_MODS = "explicitMods"
	FLAVOR_TEXT = "flavourText"
	FRAME_TYPE = "frameType"
	ICON = "icon"
	ITEM_ID = "id"
	IDENTIFIED = "identified"
	LEAGUE = "league"
	LOCKED_TO_CHARACTER = "lockedToCharacter"
	ITEM_NAME = "name"
	NOTE = "note"
	REQUIREMENTS = "requirements"
	SOCKETED_ITEMS = "socketedItems"
	SOCKETS = "sockets"
	TYPE_LINE = "typeLine"
	VERIFIED = "verified"
	HEIGHT = "h"
	WIDTH = "w"
	X_POSITION = "x"
	Y_POSITION = "y"


class DatabaseKeys(object):
	#The latest ID and when it was requested
	LATEST_NEXT_CHANGE_ID = 'latestNextChangeID'
	LATEST_NEXT_CHANGE_ID_TIMESTAMP = 'latestNextChangeIDTimestamp'

	#For an account
	ACCOUNTS = 'accounts'
	ACCOUNT_NAME = 'accountName'
	ACCOUNT_LATEST_CHARACTER_NAME = 'accountLatestCharacterName'

	#For a stash
	ACCOUNT_STASH = 'accountStash'

	#For Tabs
	STASH_TABS = 'stashTabs'
	STASH_TAB_ID = 'stashTabID'
	STASH_TAB_NAME = 'stashTabName'

	#For items
	ITEMS = 'stashTabItems'
	#<editor-fold desc="Item">
	ITEM_NAME = 'itemName'
	ITEM_ID = 'itemID'
	ITEM_TYPE_LINE = 'itemTypeLine'
	ITEM_NOTE = 'itemNote'
	ITEM_ICON_URL = 'iconURL'
	ITEM_LEAGUE = 'itemLeague'
	ITEM_DESCRIPTION = 'itemDescription'
	#</editor-fold">

	LAST_WRITE = 'lastWrite'
