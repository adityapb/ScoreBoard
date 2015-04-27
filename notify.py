from pync import Notifier
import threading
from chooseMatches import chooseMatches

def Notify(matchNo, data):
	threading.Timer(300.0, Notify).start()
	Notifier.notify(str(data[matchNo]), title = "Match Notification")