import random
print "Hello, welcome to our game!"
name = raw_input("Hello, what is your name? ")
print "Hello %s, I'm thinking of a number between 1 and 100" % (name)
print "Try to guess my number."
#greet the player, get their name, tell them to guess

def game():
    """function is a game for user to guess computer number.

    Functions starts with count 0 to count the number of guesses the user
    has to input for the correct answer. While the user guesses an integer,
    their guess will be compared with the computer's number and given hints 
    until they guess the right number. Once completed they will be congratulated
    and given their count.
    """
    count = 0
    while True:
    #if the user does not input an integer, they will get an error
        try:
            guess = int(raw_input("What's your guess? "))
            break
        except ValueError:
            print "Oops! That is not a valid number. Try again... "
    
    computer_number = random.randint(1,100)
    #generate a random number for the computer
    
    while guess is not computer_number:
    #the user will be given hints until they guess the right number
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
    #once accurate, user is congratulated and told how many guesses it took 
    new_game()
    #call the new_game function  

def new_game():
    """Plays again if user wants

    Asks the user if he/she would like to play again. If user says yes, 
    restarts the game, if user says no, says farewell. If user inputs an 
    invalid entry, the function restarts
    """

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