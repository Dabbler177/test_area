# choose the range of numbers
low_num = input("What's the lowest number? ")
high_num = input("What's the highest number? ")

# generate a random integer between the lowest number and highest number
from random import randint
chosen_number = randint(low_num, high_num)

# ask for two numbers
flag = 0
while flag == 0:
    print "First Player - choose a number between ", low_num, " and ", high_num
    number1 = input()
    flag = 1
    if number1 < low_num:
       print "I said choose a number between ", low_num, " and ", high_num, " ...\n"
       flag = 0
    if number1 > high_num:
       print "I said choose a number between ", low_num, " and ", high_num, " ...\n"
       flag = 0        
flag = 0
while flag == 0:
    print "\nSecond Player - choose a number between ", low_num, " and ", high_num, " : "
    number2 = input()
    flag = 1
    if number2 < low_num:
         print "I said choose a number between ", low_num, " and ", high_num, " ...\n"
         flag = 0
    if number2 > high_num:
         print "I said choose a number between ", low_num, " and ", high_num, " ...\n"
         flag = 0

# see who was closer to the chosen number
difference_1 = abs(chosen_number - number1)
difference_2 = abs(chosen_number - number2)
print ""
print "The number was ", chosen_number
print ""
if difference_1 < difference_2:
    print "The first player is closer"
elif difference_1 == difference_2:
    print "It's a tie."
elif difference_1 > difference_2:
    print "The second player is closer."
print ""
print "Game over"
