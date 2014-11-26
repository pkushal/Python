class Mario:
    def move(self):
        print("I am moving...")
class Shroom:
    def eat_shroom(self):
        print("Now I am big")

class BigMario(Mario, Shroom):
    pass # when you have nothing to write but you have to write something to avoid syntax error

bm = BigMario()
bm.eat_shroom()
bm.move()