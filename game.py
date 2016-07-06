import random
#greet the player, get their name, tell them to guess
print "Hello, welcome to our game!"
name = raw_input("Hello, what is your name? ")
print "Hello %s, I'm thinking of a number between 1 and 100" % (name)
print "Try to guess my number."

# get their guess, store it in a guess var, generate comp answer
guess = int(raw_input("What's your guess? "))
computer_number = random.randint(1,100)

# while guess is incorrect tell them to retry and get reguess
while guess is not computer_number:
    if guess > computer_number:
        print "Your guess is too high, try again."
        guess = int(raw_input("What's your guess? "))
    elif guess < computer_number:
        print "Your guess is too low, try again."
        guess = int(raw_input("What's your guess? "))

   
print "Congratulations! You are right."
        
    
