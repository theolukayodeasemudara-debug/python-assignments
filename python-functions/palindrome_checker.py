# collect number from user from the terminal
# define a function that reverses your number
# define another function that checks whether the number you provided is a plindrome
# define a method that checks whether your number is a prime number
# display is a palindrome when the requirement/condition is met
# display whether it is a prime number if the conditions is met

number = int(input("enter your number: "))
def is_palindrome(value):
    reversed_num = 0
    while value > 0:
        digit = value % 10 
        reversed_num = reversed_num * 10 + digit
        value = value//10
    return reversed_num

def is_prime_number(value):
    if value < 2:
        return False
    if value % value == 1:
        return True
    else:
        return False
    return True
    
if is_palindrome(number):
    print(f"{number} is a palindrome")
else:
     print(f"{number} is not a palindrome")
     
if is_prime_number(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
