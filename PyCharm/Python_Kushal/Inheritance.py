class Parent:
    def print_last_name(self):
        print("Pradhan")

class Child(Parent):
    def print_first_name(self):
        print("Kushal")
    # overriding the Parent class

    def print_last_name(self):
        print("Obama")



name = Child() # here () is necessary
name.print_first_name()
name.print_last_name()