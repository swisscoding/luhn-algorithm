#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Validate identification numbers | ----\n", fg("red")))

# user interaction
number = [int(i) for i in input("Enter number to validate: ")][::-1]

# function
def validate(num):
    # lists
    to_double = []
    temporary = []

    # index variable
    index = 0

    # get all numbers to double
    for i in num:
        if index % 2 != 0:
            to_double.append(num[index])
        index += 1

    # index variable
    index = 0

    # get all numbers to stay like before
    for i in num:
        if index % 2 == 0:
            temporary.append(num[index])
        index += 1

    # double the numbers
    to_double = [i*2 for i in to_double]

    # cross sum of numbers over 9
    for i in range(len(to_double)):
        if len(str(to_double[i])) == 2:
            temp1 = int(str(to_double[i])[0])
            temp2 = int(str(to_double[i])[1])
            to_double[i] = temp1 + temp2

    # add all numbers together and check if % 10 == 0
    sum = 0
    for i in to_double:
        sum += i
    for i in temporary:
        sum += i

    if sum % 10 == 0:
        return stylize("\nThe identification number is possibly valid.\n", fg("green"))
    return stylize("\nThe identification number is not valid.\n", fg("red"))

# output
output = validate(number)
print(output)
