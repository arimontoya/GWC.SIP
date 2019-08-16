import random
 
def main():
        secret_words = ["awkward", "bagpipes", "banjo", "croquet", "cryptic",
                 "dwarves","fishhook", "gazebo", "gypsy", "haiku",
                 "hyphen", "ivory", "jazzy", "jiffy", "jinx", "jukebox",
                 "kayak", "kiosk", "klutz", "memento", "mystify", "oxygen",
                 "pajama", "phlegm", "pixel", "polka", "quad", "quip", "rhythmic",
                 "rogue", "sphinx", "squawk", "swivel", "twelfth",
                 "unzip", "waxy", "yacht", "zealous", "zombie"
                 ]
 
        chosen_word = random.choice(secret_words).lower()
        player_guess = None
        guessed_letters = []
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("_ ")
        joined_word = None
 
        hangman = (
"""
 
   O
 
 
 
 
   
""",
"""
 
   O
   +
 
 
 
   
""",
"""
 
   O
  -+
 
 
 
 
""",
"""
 
   O
  -+-
 
 
 
 
""",
"""
 
   O
  -+-
   |
 
 
 
""",
"""
 
   O
  -+-
   |
  /
 
 
""",
"""
 
   O
  -+-
   |
  / |
 
 
""")
 
 
        attempts = len(hangman)
 
 
        while (attempts != 0 and "_ " in word_guessed):
            print(("\nYou have {} attempts left").format(attempts))
            joined_word = "".join(word_guessed)
            print(joined_word)
 
            try:
                player_guess = str(input("\nGuess a letter A-Z: ")).lower()
            except:
                print("That is not valid input, try again.")
                continue                
            else:
                if not player_guess.isalpha():
                    print("Please only input letters.")
                    continue
                elif len(player_guess) > 1:
                    print("Please only input one letter.")
                    continue
                elif player_guess in guessed_letters:
                    print("You have already guessed that letter, try again.")
                    continue
                else:
                    pass
 
            guessed_letters.append(player_guess)
 
            for letter in range(len(chosen_word)):
                if player_guess == chosen_word[letter]:
                    word_guessed[letter] = player_guess
 
            if player_guess not in chosen_word:
                attempts = attempts - 1
                print(hangman[(len(hangman) - 1) - attempts])
 
        if "_ " not in word_guessed:
            print(("\nCongratulations, you guessed correctly.").format(chosen_word))
        else:
            print(("\nYou lost! The word was {}.").format(chosen_word))
 
 
 
if __name__ == "__main__":
    main()
