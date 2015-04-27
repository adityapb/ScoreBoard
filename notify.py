from pync import Notifier

def Notify(matchNo, data):
	Notifier.notify(str(data[matchNo-1]), title = "Match Notification")
	return