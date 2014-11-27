month, name, price = ['December', 'bread glover', 14]
print(name)

# uneven names and lists
def drop_first_last(grades):
    first, *middle, last = grades # this will store the first and last element on the variable first and last and remaining on the variable list called middle
    avg = sum(middle)/len(middle)
    print(avg)
    print(middle[2])

drop_first_last([65, 76, 98, 54, 21])