# we will store current largest number here
largest_number = -999999999

#input first value

number = int(input('Enter a number or type -1 to stop: '))

#if the numberis not equal to -1 we will continue
while number != -1:
    #is number larger than largest number
    if number > largest_number:
        #yes, update largest_number
        largest_number = number
    # input the next number
    number = int(input('Enter a number or type -a to stop: '))

print('The largest number is: ', largest_number)