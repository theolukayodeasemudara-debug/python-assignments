number = int(input("enter your number: "))
def reverse_num(value):
    reversed_num = 0
    while value > 0:
        digit = value % 10 
        reversed_num = reversed_num * 10 + digit
        value = value//10
    return reversed_num
    
print(reverse_num(number))
