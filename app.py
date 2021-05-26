import random

print("Number guessing game")

number = random.randint(1,9)
chances = 0

print("Guess a number between 1 and 9: ")

while chances < 5:
        guess= int(input("enter yout guess"))

        if(guess== number):
                print("you won")
        elif(guess<number):
                print("your guess is too low, guess a number higher than", guess)
        else:
                print("your guess was too high, try guessing a number lower than", guess)
        chances= chances+1
if not chances < 5:
        print("you lost the number is ",number)