__author__ = 'Devin'

'''
These are classes that define the multiple types of attributes an item can have
Inheritance of these will allow for complicated item types
'''

'''
Start with the simple ones - single values
'''
#<editor-fold desc="Simple Attributes">


class Identifiable(object):
	def __init__(self, identified):
		#Is it corrupted or not
		self._identified = bool(identified)

	@property
	def identified(self):
		"""Get if the item is identified"""
		return self._identified


class ItemLevel(object):
	def __init__(self, itemLevel):
		#Item Level is an int
		self._itemLevel = int(itemLevel)

	@property
	def itemLevel(self):
		"""Get the item level for this item"""
		return self._itemLevel


class Corruptible(object):
	def __init__(self, corrupted):
		#Is it corrupted or not
		self._corrupted = bool(corrupted)

	@property
	def corrupted(self):
		"""Get if the item is corrupted"""
		return self._corrupted

#</editor-fold>

'''
Now more complicated ones
'''
