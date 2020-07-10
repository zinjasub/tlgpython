#!/usr/bin/env python3

round = 0
answer = " "


while round < 3 and answer != "Brian": # or "brian":
    round += 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ____"')
    if answer == 'Brian': # or 'brian':
        print('Correct')
        break
    elif round == 3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")
