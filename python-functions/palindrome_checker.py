# collect number from user from the terminal
# define a function that reverses your number
# define another function that checks whether the number you provided is a plindrome
# define a number that checks whether your number is a prime number

number = int(input("enter your number: "))
def is_palindrome(value):
    reversed_num = 0
    while value != 0:
        digit = value % 10 
        reversed_num = reversed_num * 10 + digit
        value = value/10
    return reversed_num

def is_prime_number(number):
    return ...
    
if is_palindrome(number):
    print(f"{number} is a palindrome")
else:
     print(f"{number} is not a palindrome")
     
     
        # int reversedNum = 0;
        # while(number != 0){
        #     int digit = number % 10;
        #     reversedNum = reversedNum * 10 + digit;
        #     number = number/10;
        # }
        # return reversedNum;
