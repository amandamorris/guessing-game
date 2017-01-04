# Put your code here
from random import randint

print "Hi there!"

user_name = raw_input("What's your name? ")

print "Hi there {}, would you like to play number guessing game?".format(user_name)
print "I'll think of a number, and you can try to guess it."


while True:
    try:
        USER_GUESS = int(raw_input("Please choose a number between 1 and 100. "))
        break
    except ValueError:
        print "That was not a number"

random_number = randint(1, 100)
#print random_number

num_guesses = 1

while USER_GUESS != random_number:
    if 0 < USER_GUESS and USER_GUESS < random_number:
        print "Too low! "
    elif USER_GUESS > random_number and USER_GUESS < 101:
        print "Too high!"
    else:
        print "Try again with a number that's actually between 1 and 100"
    while True:
        try:
            USER_GUESS = int(raw_input("Please choose a number between 1 and 100. "))
            break
        except ValueError:
            print "That was not a number"
    num_guesses += 1

print "Congrats! You guessed it. You made {} guesses.".format(num_guesses)
