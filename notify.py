from pync import Notifier
import threading

def Notify(matchNo, data):
	threading.Timer(300.0, Notify).start()
	Notifier.notify(str(data[matchNo-1]), title = "Match Notification")