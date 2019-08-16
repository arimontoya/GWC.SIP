from random import *

computer = ["ROCK", "PAPER", "SCISSORS"]
computer_score = 0
user_score = 0
# --- Define your functions below! ---
def intro():
    user = input("Hello welcome to this virtual ROCK, PAPER, SCISSORS game! What is your name?: ")
    print ("It is nice to meet you " + user + " My name is Chatbot!")

def isvalid2(answer):
    while(True):
        response = input(answer)
        if response in computer:
            return response
        else:
            print("Please input response correctly, and in all caps.")
            loop = True

def rank(user, comp):
    global user_score
    global computer_score
    if user == "ROCK" and comp == "PAPER":
        print ("Computer wins this round!")
        computer_score = computer_score + 1
    if user == "ROCK" and comp == "SCISSORS":
        print ("User wins this round!")
        user_score = user_score + 1
    if user == "ROCK" and comp == "ROCK":
        print ("This round is a tie, play again!")
    if user == "PAPER" and comp == "SCISSORS":
        print ("Computer wins this round!")
        computer_score = computer_score + 1
    if user == "PAPER" and comp == "PAPER":
        print ("This round is a tie, play again!")
    if user == "SCISSORS" and comp == "SCISSORS":
        print ("This round is a tie, play again!")
    if user == "PAPER" and comp == "ROCK":
        print ("User wins this round!")
        user_score = user_score + 1
    if user == "SCISSORS" and comp == "ROCK":
        print ("Computer wins this round!")
        computer_score = computer_score + 1
    if user == "SCISSORS" and comp == "PAPER":
        print ("User wins this round!")
        user_score = user_score + 1
        
def rps(games):
    for rounds in range(int(games)):
        user_attempt = isvalid2("ROCK, PAPER or SCISSORS?: ")
        random_computer = randint(0, len(computer)-1)
        comp_attempt = computer[random_computer]
        print ("The computer played " + comp_attempt + ".")
        rank(user_attempt, comp_attempt)

def isvalid(question):
    while(True):
        try:
            num = float(input(question))
            return num
        except ValueError:
            print("That is not a number!")
            loop = True

# --- Put your main program below! ---
def main():
    global user_score
    global computer_score
    intro()
    while True:
        print ("For this version rounds that result in ties can not do rematches, please only input your attempts in CAPS")
        rounds = isvalid("How many rounds of ROCK, PAPER, SCISSORS do you want to play?: ")
        rps(rounds)
        if computer_score == user_score and (computer_score >= 1 or user_score >= 1):
            print ("The game of ROCK, PAPER, SCISSORS was a tie.")
        elif computer_score > user_score:
            print ("Computer won the game of ROCK, PAPER, SCISSORS.")
        elif computer_score < user_score:
            print ("User won the game of ROCK, PAPER, SCISSORS.")
        break

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
