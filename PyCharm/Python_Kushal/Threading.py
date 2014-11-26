import threading

class KushalMessanger(threading.Thread):
    def run(self): # special name called run
        for _ in range(50): # we don't care about the variable so we use _
            print(threading.current_thread().getName())

x = KushalMessanger(name='send out messages')
y = KushalMessanger(name='receive messages')

x.start() # goes to the KushalMessanger Class and looks for the run method
y.start()