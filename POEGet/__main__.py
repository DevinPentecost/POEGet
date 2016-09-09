__author__ = 'Devin'

import time

from POEGet.Util import Printing


#Launch an instance for now
from POEGet.Controller.POEGetController import POEGetController

Printing.INFOPRINT("Creating Controller.")

controller = POEGetController()

Printing.INFOPRINT("Controller created. Waiting for KeyboardInterrupt.")

#Wait for a keyboard interrupt
try:
	while True:
		time.sleep(0)
except KeyboardInterrupt:
	Printing.INFOPRINT("Received KeyboardInterrupt. Stopping!")
	controller.shutdown()
