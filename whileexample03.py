secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input('Enter your number: '))

while number != 777:
    if number == 777:
        print('Well done, muggle! you are free now')
    else:
        print('You type ', number)
        print("haha! you're stuck in my loop")
        number = int(input('Enter new number: '))

#correct code
#user_number = int(input("Enter the number: "))

#while user_number != secret_number:
#    print("Ha ha! You're stuck in my loop!")
#    user_number = int(input("Enter the number again: "))
#print(secret_number, "Well done, muggle! You are free now.")


