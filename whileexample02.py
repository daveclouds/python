# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_number = 0

#read first number
number = int(input('Enter a number or type 0 tp stop: '))

# 0 terminates execution
while number != 0:
    #check if the number is odd
    if number % 2 == 1:
        #increase the odd_numbers counters
        odd_numbers += 1
    else:
        #increase the even_numbers counter
        even_number += 1
    #read the next number
    number =  int(input('Enter a number or type 0 tp stop: '))

print('odd numbers count:', odd_numbers)
print('even numbers count:', even_number)