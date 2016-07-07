import random
#greet the player, get their name, tell them to guess
print "Hello, welcome to our game!"
name = raw_input("Hello, what is your name? ")
print "Hello %s, I'm thinking of a number between 1 and 100" % (name)
print "Try to guess my number."

# get their guess, store it in a guess var, generate comp answer
def game():
    count = 0
    while True:
        try:
            guess = int(raw_input("What's your guess? "))
            break
        except ValueError:
            print "Oops! That is not a valid number. Try again... "

    computer_number = random.randint(1,100)

    # while guess is incorrect tell them to retry and get reguess
    while guess is not computer_number:
        if guess > computer_number and guess < 100:
            print "Your guess is too high, try again."
            count += 1
            guess = int(raw_input("What's your guess? "))
        elif guess < computer_number and guess > 1:
            print "Your guess is too low, try again."
            count += 1
            guess = int(raw_input("What's your guess? "))
        elif guess > 100 or guess < 1:
            print "Please enter a number between 1 and 100"
            guess = int(raw_input("What is your new guess? "))
       
    print "Congratulations! You are right."
    print "You guessed it in %d guesses" % (count)
    new_game()

def new_game():
    play_again = raw_input("Would you like to play again? Enter 'Y' for yes or 'N' for no: ")
    play_again = play_again.upper()

    if play_again == "Y":
        print "Thanks for playing again. "
        game()
    elif play_again == "N": 
        print "Thanks for playing"
    else: 
        print "Not a valid input"
        new_game()
       
game()

        
    
