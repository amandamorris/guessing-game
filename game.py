# Put your code here
from random import randint

print "Hi there!"

user_name = raw_input("What's your name? ")

print "Hi there {}, would you like to play number guessing game?".format(user_name)
print "I'll think of a number, and you can try to guess it."

user_guess = int(raw_input("Please choose a number between 1 and 100. "))

random_number = randint(1, 100)
print random_number

num_guesses = 1

while user_guess != random_number:
    if user_guess < random_number:
        print "Too low! "
    else:
        print "Too high!"
    user_guess = int(raw_input("Please choose again. "))
    num_guesses += 1

print "Congrats! You guessed it. You made {} guesses.".format(num_guesses)
