#open dictionary file and make info = a variable
f = open("dictionary.txt", "r")
dictionary = f.readlines()
f.close()

print("Can you survive a dictionary attack?")

equalTo = 0

#main loop
while True:
    password = input("Enter a Password: ")
    for line in dictionary:
        x = line
        x = x.strip()
        x = x.casefold()
        if x == password:
            equalTo += 1
    if equalTo > 0:
        print("This password is not strong enough, try again!")
        equalTo = 0
    elif equalTo == 0:
        print("This password is strong, good job!")
        break
