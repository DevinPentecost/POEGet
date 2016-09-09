__author__ = 'Devin'

from json import JSONEncoder

import abc

"""
This is just an interface to say that an object is capable of being put into our database
"""


class DBObject(JSONEncoder, metaclass=abc.ABCMeta):
	#There is a required function
	@abc.abstractmethod
	def toDatabaseDictionary(self):
		"""Convert this object into a dictionary our database can handle"""
		...
