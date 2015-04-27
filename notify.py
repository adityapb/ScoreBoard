from pync import Notifier
import threading
from score import score
#from chooseMatches import chooseMatches

def Notify(matchNo):
	threading.Timer(300.0, Notify).start()
	data = score()
	Notifier.notify(str(data[matchNo]), title = "Match Notification")