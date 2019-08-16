word = input("Player 1 insert a word for Player 2 to guess: ")
underscores = []
length = len(word)

for letter in word:
    underscores.append("_ ")
print ("".join(underscores))

while 


for i in range(7):
    guess = input("Guess a letter: ")
    for letter in range(len(word)):
        if guess == word[letter]:
            underscores[letter] = guess
            print ("".join(underscores))
    if 

