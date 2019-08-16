#my list
fav_bands = ["the 1975", "twenty one pilots", "arctic monkeys", "the aces", "one direction"]

#prints length of list
print(len(fav_bands))

#boolean that prints True statement
print("the aces" in fav_bands)

#boolean that prints False statement
print("panic at the disco" in fav_bands)

#for however many items in list it will print said item
for name in fav_bands:
    print(name)

#using indices of our list it prints the names of my favorite bands sequentially
#for i in range(len(fav_bands)):
#    print(fav_bands[i])

random_list = ["steve", "robin", ["11", "dustin", "mike", "will"]]
print (random_list[2])
