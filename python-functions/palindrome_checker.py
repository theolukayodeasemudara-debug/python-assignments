# collect number from user from the terminal
# define a function that reverses your number
# define another function that checks whethe the number you provided is a plindrome
number = int(input("enter your number: "))
def reverse_number(number):
    reversed_num = 0
    while(number != 0):
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number = number / 10
    return reversed_num

def is_palindrome(number):
    reversed = reverse_number(number)
    return number == reversed
    
if is_palindrome:
    print("number is a palindrome")    
    
print(is_palindrome(number))
