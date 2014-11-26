class Girl:
    gender = 'female' # this is the class variable and every girl will have the gender equal to female
    def __init__(self, name):
        self.name = name # this is a instance variable, every girl will have different name

r = Girl('Rachel')
s= Girl('Stanky')

print(r.name)
print(r.gender + "\n")

print(s.name + " wala")
print(s.gender)
