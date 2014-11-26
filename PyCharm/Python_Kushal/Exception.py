__author__ = 'Kushal'

while True:
    try:
        number = int(input("what's you fav. number? \n"))
        print(" So you like " + str(18/number) + " wala")
        break
    except ValueError:
        print("Enter a number.. \n")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("Bye bye")