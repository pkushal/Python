class Tuna:
    def __init__(self): # this is like a constructor
        print('wala')
    def swim(self):
        print("I am swimming")
#flipper = Tuna()
#flipper.swim() # It's gonna print wala and then I am swimming

class Enemy:
    def __init__(self,x):
        self.energy = x
    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
sandy = Enemy(18)
jason.get_energy()
sandy.get_energy()